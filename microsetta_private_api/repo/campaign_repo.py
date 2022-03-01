import psycopg2
import json

from microsetta_private_api.client.fundrazr import FundrazrClient
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.campaign import Campaign, payment_from_db
from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.repo.interested_user_repo import InterestedUserRepo
from microsetta_private_api.tasks import send_email
from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.localization import EN_US


class UnknownItem(psycopg2.errors.ForeignKeyViolation):
    pass


class UnknownTransaction(ValueError):
    pass


class CampaignRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    @staticmethod
    def _campaign_to_row(c):
        return (c.campaign_id, c.title, c.instructions, c.header_image,
                c.permitted_countries, c.language_key,
                c.accepting_participants, '',
                c.language_key_alt, c.title_alt, c.instructions_alt)

    def _row_to_campaign(self, r):
        associated_projects = ", ".join(self._get_projects(r['campaign_id']))
        return Campaign(r['campaign_id'], r['title'], r['instructions'],
                        r['header_image'], r['permitted_countries'],
                        r['language_key'], r['accepting_participants'],
                        associated_projects, r['language_key_alt'],
                        r['title_alt'], r['instructions_alt'])

    def _get_projects(self, campaign_id):
        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT barcodes.project.project "
                "FROM campaign.campaigns "
                "INNER JOIN campaign.campaigns_projects "
                "ON "
                "campaign.campaigns.campaign_id = "
                "campaign.campaigns_projects.campaign_id "
                "LEFT JOIN barcodes.project "
                "ON "
                "campaign.campaigns_projects.project_id = "
                "barcodes.project.project_id "
                "WHERE "
                "campaign.campaigns.campaign_id = %s",
                (campaign_id,)
            )

            project_rows = cur.fetchall()
            campaign_projects = [project[0] for project in project_rows]
            return campaign_projects

    def get_all_campaigns(self):
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT campaign_id, title, instructions, header_image, "
                "permitted_countries, language_key, accepting_participants, "
                "language_key_alt, title_alt, "
                "instructions_alt "
                "FROM campaign.campaigns ORDER BY title"
            )
            rows = cur.fetchall()
            return [self._row_to_campaign(r) for r in rows]

    def create_campaign(self, **kwargs):
        # required parameters to create a campaign
        title = kwargs['title']
        associated_projects = kwargs['associated_projects']

        # optional parameters when creating a campaign
        instructions = kwargs.get('instructions')
        permitted_countries = kwargs.get('permitted_countries')
        language_key = kwargs.get('language_key')
        accepting_participants = kwargs.get('accepting_participants')
        language_key_alt = kwargs.get('language_key_alt')
        title_alt = kwargs.get('title_alt')
        instructions_alt = kwargs.get('instructions_alt')
        extension = kwargs.get('extension')

        with self._transaction.cursor() as cur:
            cur.execute(
                "INSERT INTO campaign.campaigns (title, instructions, "
                "permitted_countries, language_key, accepting_participants, "
                "language_key_alt, title_alt, "
                "instructions_alt) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s) "
                "RETURNING campaign_id",
                (title, instructions, permitted_countries, language_key,
                 accepting_participants, language_key_alt, title_alt,
                 instructions_alt)
            )
            campaign_id = cur.fetchone()[0]

            if campaign_id is None:
                raise RepoException("Error inserting campaign into database")
            else:
                cur.executemany(
                    "INSERT INTO campaign.campaigns_projects ("
                    "campaign_id,project_id"
                    ") VALUES (%s, %s) ",
                    [(campaign_id, pid) for pid in associated_projects]
                )

                self.update_header_image(campaign_id, extension)
                return self.get_campaign_by_id(campaign_id)

    def update_campaign(self, **kwargs):
        # required parameters to update a campaign
        campaign_id = kwargs['campaign_id']
        title = kwargs['title']

        # not permitted to update associated projects
        if 'associated_projects' in kwargs:
            raise RepoException("Modifying associated projects not allowed")

        # optional parameters to update a campaign
        instructions = kwargs.get('instructions')
        permitted_countries = kwargs.get('permitted_countries')
        language_key = kwargs.get('language_key')
        accepting_participants = kwargs.get('accepting_participants')
        language_key_alt = kwargs.get('language_key_alt')
        title_alt = kwargs.get('title_alt')
        instructions_alt = kwargs.get('instructions_alt')
        extension = kwargs.get('extension')

        with self._transaction.cursor() as cur:
            cur.execute(
                "UPDATE campaign.campaigns SET title = %s, instructions = %s, "
                "permitted_countries = %s, language_key = %s, "
                "accepting_participants = %s, language_key_alt = %s, "
                "title_alt = %s, instructions_alt = %s "
                "WHERE campaign_id = %s",
                (title, instructions, permitted_countries, language_key,
                 accepting_participants, language_key_alt, title_alt,
                 instructions_alt, campaign_id)
            )

            self.update_header_image(campaign_id, extension)

        return self.get_campaign_by_id(campaign_id)

    def get_campaign_by_id(self, campaign_id):
        with self._transaction.dict_cursor() as cur:
            try:
                cur.execute(
                    "SELECT campaign_id, title, instructions, header_image, "
                    "permitted_countries, language_key, "
                    "accepting_participants, "
                    "language_key_alt, title_alt, instructions_alt "
                    "FROM campaign.campaigns WHERE campaign_id = %s",
                    (campaign_id,)
                )
                r = cur.fetchone()
                if r is None:
                    return None
                else:
                    return self._row_to_campaign(r)
            except psycopg2.errors.InvalidTextRepresentation:
                # if someone tries to input a random/malformed campaign ID
                # we just want to return None and let the signup form display
                # the default campaign info
                return None

    def update_header_image(self, campaign_id, extension):
        if extension is not None and len(extension) > 0:
            with self._transaction.cursor() as cur:
                header_image = campaign_id + "." + extension
                cur.execute(
                    "UPDATE campaign.campaigns SET header_image = %s "
                    "WHERE campaign_id = %s",
                    (header_image, campaign_id)
                )

        return True

    def is_member_by_email(self, email, campaign_id):
        """Determine if an individual, by email, is associated with a campaign

        Validity is based off of either (a) direct association as though the
        interested_user table or (b) association with an account created using
        a kit that is part of a project with a the campaign.

        Note
        ----
        This method is imperfect for historical accounts under the edge case
        of a person creating an account with an unassociated project, and later
        claiming a sample from an associated project.

        Parameters
        ----------
        email : str
            The email to test for
        campaign_id : uuid4
            The campaign ID to examine

        Returns
        -------
        bool
            True if the user is part of the campaign
        """
        with self._transaction.cursor() as cur:
            # scenario (1)
            cur.execute("""SELECT EXISTS (
                               SELECT email
                               FROM campaign.interested_users
                               WHERE email=%s
                                   AND campaign_id=%s)""",
                        (email, campaign_id))
            if cur.fetchone()[0] is True:
                return True

            # scenario (2)
            cur.execute("""SELECT EXISTS (
                               SELECT email
                               FROM ag.account
                               INNER JOIN barcodes.barcode
                                   ON created_with_kit_id=kit_id
                               INNER JOIN barcodes.project_barcode
                                   USING (barcode)
                               INNER JOIN campaign.campaigns_projects
                                   USING (project_id)
                               WHERE email=%s
                                   AND campaign_id=%s)""",
                        (email, campaign_id))

            if cur.fetchone()[0] is True:
                return True

        return False

    def is_member_by_source(self, account_id, source_id, campaign_id):
        """Determine if an individual, by source, is associated with a campaign

        Validity is based off whether the account and source IDs are valid
        and the account was created using a kit that is part of a project
        associated with the campaign

        Note
        ----
        This method is imperfect for historical accounts under the edge case
        of a person creating an account with an unassociated project, and later
        claiming a sample from an associated project.

        Parameters
        ----------
        account_id : uuid4
            The account ID to test for
        source_id : uuid4
            The source ID to test for
        campaign_id : uuid4
            The campaign ID to consider

        Returns
        -------
        bool
            True if the user is part of the campaign
        """
        with self._transaction.cursor() as cur:

            cur.execute("""SELECT EXISTS (
                               SELECT account.email
                               FROM ag.account
                               INNER JOIN ag.source
                                   ON account.id=account_id
                               INNER JOIN barcodes.barcode
                                   ON created_with_kit_id=kit_id
                               INNER JOIN barcodes.project_barcode
                                   USING (barcode)
                               INNER JOIN campaign.campaigns_projects
                                   USING (project_id)
                               WHERE account.id=%s
                                   AND source.id=%s
                                   AND campaign_id=%s)""",
                        (account_id, source_id, campaign_id))

            if cur.fetchone()[0] is True:
                return True

        return False


class FundRazrCampaignRepo(BaseRepo):
    # 118 -> The Microsetta Initiative
    _DEFAULT_PROJECT_ASSOCIATION = (118, )

    def campaign_exists(self, id_):
        """Test if a fundrazr campaign ID is known

        Parameters
        ----------
        id_ : str
            A fundrazr campaign ID

        Returns
        -------
        bool
            True if the campaign is known in our database
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT EXISTS (
                               SELECT internal_campaign_id
                               FROM campaign.transaction_source_to_campaign
                               WHERE remote_campaign_id=%s)""",
                        (id_, ))
            res = cur.fetchone()[0]
        return res

    def item_exists(self, campaign_id, item_id):
        """Test if a fundrazr perk exists for a campaign

        Parameters
        ----------
        campaign_id : str
            A fundrazr campaign ID
        item_id : str
            A fundrazr perk ID

        Returns
        -------
        bool
            True if the item is part of the queried campaign in our database
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT EXISTS (
                               SELECT id
                               FROM campaign.fundrazr_perk
                               WHERE remote_campaign_id=%s
                                   AND id=%s)""",
                        (campaign_id, item_id))
            res = cur.fetchone()[0]
        return res

    def insert_campaign(self, campaign_obj, assoc_projects=None):
        """Add a fundrazr campaign and its items to the database

        NOTE: we *do not* know associated projects other than default to
        a microsetta association. This may need to be revised in the future

        Parameters
        ----------
        campaign_obj : FundRazrCampaign
            A campaign instance
        assoc_projects : Iterable of int
            Projects to associate with, defaults to Microsetta (118)
        """
        if assoc_projects is None:
            assoc_projects = self._DEFAULT_PROJECT_ASSOCIATION

        cr = CampaignRepo(self._transaction)
        known = cr.get_all_campaigns()
        known = {c.title: c.campaign_id for c in known}

        if not self.campaign_exists(campaign_obj.campaign_id):
            if campaign_obj.title not in known:
                new_ = cr.create_campaign(title=campaign_obj.title,
                                          associated_projects=assoc_projects)
                internal_campaign_id = new_.campaign_id
            else:
                internal_campaign_id = known[campaign_obj.title]

            sql = ("""INSERT INTO campaign.transaction_source_to_campaign
                      (remote_campaign_id, internal_campaign_id, currency)
                      VALUES (%s, %s, %s)""",
                   (campaign_obj.campaign_id, internal_campaign_id,
                    campaign_obj.currency))

            with self._transaction.cursor() as cur:
                cur.execute(*sql)

        for item in campaign_obj.items:
            if not self.item_exists(campaign_obj.campaign_id, item.id):
                self.add_perk_to_campaign(campaign_obj.campaign_id, item)

    def add_perk_to_campaign(self, campaign_id, perk):
        """Add a fundazr perk to a campaign

        Parameters
        ----------
        campaign_id : str
            A fundrazr campaign ID
        perk : Item
            An instance of a campaign Item
        """
        sql = ("""INSERT INTO campaign.fundrazr_perk
                  (id, remote_campaign_id, title, price)
                  VALUES (%s, %s, %s, %s)""",
               (perk.id, campaign_id, perk.title, perk.price))

        with self._transaction.cursor() as cur:
            cur.execute(*sql)


class UserTransaction(BaseRepo):
    TRN_TYPE_FUNDRAZR = 'fundrazr'

    def add_transaction(self, payment):
        """Adds a received transaction to the database

        Parameters
        ----------
        payment : Payment object
            An instantiated Payment model, with or without shipping
            and with or without claimed items

        Raises
        ------
        DuplicateTransaction
            If the transaction already exists

        Returns
        -------
            True if inserted
        """
        # gatekeep first thing to avoid adding an interested user if
        # an unknown trn type
        if payment.TRANSACTION_TYPE != self.TRN_TYPE_FUNDRAZR:
            raise ValueError("'%s' is unrecognized" % payment.TRANSACTION_TYPE)

        interested_user_id = self._add_interested_user(payment)

        # begin address verification
        i_u_repo = InterestedUserRepo(self._transaction)
        try:
            valid_address = i_u_repo.verify_address(interested_user_id)
        except RepoException:
            # we shouldn't reach this point, but address wasn't verified
            valid_address = False

        # we specifically care if valid_address is False, as verify_address
        # will return None if the user doesn't have a shipping address
        # in this case, that implies a perk that doesn't require shipping
        if valid_address is False:
            cn = payment.payer_first_name + " " + payment.payer_last_name

            # casting str to avoid concatenation error
            resolution_url = SERVER_CONFIG["interface_endpoint"] + \
                "/update_address?uid=" + str(interested_user_id) + \
                "&email=" + payment.contact_email
            try:
                # TODO - will need to add actual language flag to the email
                # Fundrazr doesn't provide a language flag, defer for now
                send_email(payment.contact_email,
                           "address_invalid",
                           {"contact_name": cn,
                            "resolution_url": resolution_url},
                           EN_US)
            except:  # noqa
                # try our best to email
                pass
        # end address verification

        if payment.TRANSACTION_TYPE == self.TRN_TYPE_FUNDRAZR:
            return self._add_transaction_fundrazr(payment, interested_user_id)
        else:
            # TODO: add more transaction types...
            pass

    def _add_interested_user(self, payment):
        # if we don't have an interested user
        if payment.contact_email is None:
            return None

        # be responsive to new campaigns being created
        cr = FundRazrCampaignRepo(self._transaction)
        if not cr.campaign_exists(payment.campaign_id):
            fc = FundrazrClient()
            campaign = fc.campaign(payment.campaign_id)
            # TODO: expose a means to modify associated projects,
            # but for right now, just default to microsetta
            cr.insert_campaign(campaign)

        # determine the internal campaign the payment is associated with
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT internal_campaign_id
                           FROM campaign.transaction_source_to_campaign
                           WHERE remote_campaign_id = %s""",
                        (payment.campaign_id, ))
            res = cur.fetchone()
            internal_campaign_id = res[0]

        shipping = payment.shipping_address
        address = shipping.address if shipping is not None else None

        if shipping is None:
            data = (internal_campaign_id, payment.payer_first_name,
                    payment.payer_last_name, payment.contact_email,
                    payment.phone_number)
            fields = ('campaign_id', 'first_name', 'last_name', 'email',
                      'phone')
        else:
            data = (internal_campaign_id, shipping.first_name,
                    shipping.last_name, payment.contact_email,
                    payment.phone_number, address.street, address.street2,
                    address.city, address.country_code, address.state,
                    address.post_code)
            fields = ('campaign_id', 'first_name', 'last_name', 'email',
                      'phone', 'address_1', 'address_2', 'city', 'country',
                      'state', 'postal_code')

        placeholders = ', '.join(['%s'] * len(fields))
        fields_formatted = ', '.join(fields)
        sql = (f"""INSERT INTO campaign.interested_users
                   ({fields_formatted})
                   VALUES ({placeholders})
                   RETURNING interested_user_id""",
               data)

        with self._transaction.cursor() as cur:
            cur.execute(*sql)
            interested_user_id = cur.fetchone()

        return interested_user_id

    def _add_transaction_fundrazr(self, payment, interested_user_id):
        items = payment.claimed_items
        fields = ('id', 'interested_user_id', 'remote_campaign_id', 'created',
                  'amount', 'net_amount', 'currency', 'message',
                  'subscribed_to_updates', 'account_type', 'payer_first_name',
                  'payer_last_name', 'payer_email', 'transaction_type')
        data = (payment.transaction_id,
                interested_user_id,
                payment.campaign_id,
                payment.created,
                payment.amount,
                payment.net_amount,
                payment.currency,
                payment.message,
                payment.subscribe_to_updates,
                payment.account,
                payment.payer_first_name,
                payment.payer_last_name,
                payment.payer_email,
                self.TRN_TYPE_FUNDRAZR)

        placeholders = ', '.join(['%s'] * len(fields))
        fields_formatted = ', '.join(fields)

        # historical perks may not be represented by the database
        # as the list of perks (directly) associated with a campaign
        # through the fundrazr API, is limited to the *current* state
        # of available perks
        if items is not None:
            cr = FundRazrCampaignRepo(self._transaction)
            for item in items:
                if not cr.item_exists(payment.campaign_id, item.id):
                    cr.add_perk_to_campaign(payment.campaign_id, item)

        with self._transaction.cursor() as cur:
            cur.execute(f"""INSERT INTO campaign.transaction
                            ({fields_formatted})
                            VALUES ({placeholders})""",
                        data)

            if items is not None:
                inserts = [(payment.transaction_id, i.id, i.quantity)
                           for i in items]

                try:
                    cur.executemany("""INSERT INTO
                                           campaign.fundrazr_transaction_perk
                                       (transaction_id, perk_id, quantity)
                                       VALUES (%s, %s, %s)""",
                                    inserts)
                except psycopg2.errors.ForeignKeyViolation:
                    # this would indicate a synchronization issue, where
                    # fundrazr knows of a perk which we do not
                    detail = [i.to_api() for i in items]
                    raise UnknownItem(f"One or more perks are unknown:\n"
                                      f"{json.dumps(detail, indent=2)}")

        return True

    def most_recent_transaction(self, transaction_source=None,
                                campaign_id=None, include_anonymous=False,
                                email=None):
        """Return the latest transaction

        campaign_id : str, optional
            Limit to a particular campaign
        transaction_source : str, optional
            Limit to a particular transcation source type
        include_anonymous : bool, optional
            Include anonymous transactions w/o interested users, default is
            False.
        email : str, optional
            Limit by a persons contact email

        Returns
        -------
        Payment or None
            Constructed Payment instance of the most recent transaction
        """
        trns = self.get_transactions(transaction_source=transaction_source,
                                     campaign_id=campaign_id,
                                     include_anonymous=include_anonymous,
                                     email=email, most_recent=True)
        if len(trns) > 0:
            return trns[0]
        else:
            return None

    def get_transactions(self, before=None, after=None, transaction_id=None,
                         email=None, transaction_source=None,
                         campaign_id=None, include_anonymous=False,
                         most_recent=False):
        """Somewhat flexible getter for transactions

        Parameters
        ----------
        before : datetime, optional
            Limit transactions to before a specific date
        after : datetime, optional
            Limit transactions to after a specific date
        transaction_id : str, optional
            Limit to a specific transaction ID
        email : str, optional
            Limit by a persons contact email
        transaction_source : str, optional
            Limit to a particular transcation source type
        include_anonymous : bool, optional
            Include anonymous transactions w/o interested users, default is
            False.
        most_recent : bool, optional
            Only obtain the most recent transaction

        Returns
        -------
        list of Payment
            A list of constructed Payment instances
        """
        clauses = []
        data = []
        if before is not None:
            clauses.append("created < %s")
            data.append(before)
        if after is not None:
            clauses.append("created > %s")
            data.append(after)
        if transaction_id is not None:
            clauses.append("id = %s")
            data.append(transaction_id)
        if email is not None:
            clauses.append("email = %s")
            data.append(email)
        if campaign_id is not None:
            clauses.append("internal_campaign_id = %s")
            data.append(campaign_id)
        if transaction_source is not None:
            clauses.append("transaction_type = %s")
            data.append(transaction_source)

        if include_anonymous:
            anonymous_join = 'LEFT'
        else:
            anonymous_join = 'INNER'

        if len(clauses) > 0:
            clauses = 'WHERE ' + ' AND '.join(clauses)
            data = tuple(data)
        else:
            clauses = ''
            data = None

        if most_recent:
            limit_or_not = 'ORDER BY created DESC LIMIT 1'
        else:
            limit_or_not = ''

        sql = (f"""SELECT id
                   FROM campaign.transaction t
                   JOIN campaign.transaction_source_to_campaign tstc
                       USING (remote_campaign_id)
                   {anonymous_join} JOIN campaign.interested_users
                       USING (interested_user_id)
                   {clauses} {limit_or_not}""",
               data)

        with self._transaction.cursor() as cur:
            cur.execute(*sql)
            res = cur.fetchall()

        if len(res) > 0:
            return self._payments_from_transactions(res)
        else:
            return []

    def _payments_from_transactions(self, ids):
        """Construct a payment instance from a transaction ID"""
        # first obtain general transaction information
        transaction_sql = ("""SELECT iu.first_name as shipping_first_name,
                                     iu.last_name as shipping_last_name,
                                     iu.email as contact_email,
                                     iu.phone as phone_number,
                                     iu.address_1 as shipping_address1,
                                     iu.address_2 as shipping_address2,
                                     iu.city as shipping_city,
                                     iu.state as shipping_state,
                                     iu.postal_code as shipping_postal,
                                     iu.country as shipping_country,
                                     t.*
                              FROM campaign.transaction t
                              LEFT JOIN campaign.interested_users iu
                                  USING (interested_user_id)
                              WHERE id IN %s
                              ORDER BY created DESC
                              """,
                           (tuple(ids), ))
        with self._transaction.dict_cursor() as cur:
            cur.execute(*transaction_sql)
            trn_data = cur.fetchall()

        trn_data = [dict(r) for r in trn_data]

        # determine if we have fundrazr data
        fundrazr_ids = [row['id'] for row in trn_data
                        if row['transaction_type'] == self.TRN_TYPE_FUNDRAZR]

        # ...and if so, pull out the respective perk information
        if len(fundrazr_ids) > 0:
            # we have to jump through hoops with array_agg in order to get a
            # mixed data type return back :/
            items_sql = ("""SELECT ftp.transaction_id,
                                   ARRAY_AGG(array[fp.title,
                                                   ftp.quantity::VARCHAR,
                                                   fp.id])
                                       as items
                            FROM campaign.fundrazr_transaction_perk ftp
                            JOIN campaign.fundrazr_perk fp
                               ON fp.id=ftp.perk_id
                            WHERE ftp.transaction_id IN %s
                            GROUP BY ftp.transaction_id""",
                         (tuple(fundrazr_ids), ))
            with self._transaction.dict_cursor() as cur:
                cur.execute(*items_sql)

                fundrazr_data = {}
                for row in cur.fetchall():
                    tid, perks = row
                    fundrazr_data[tid] = [{'title': p[0],
                                           'quantity': int(p[1]),
                                           'id': p[2]}
                                          for p in perks]

            for entry in trn_data:
                entry['fundrazr_perks'] = fundrazr_data.get(entry['id'])

        return [payment_from_db(data) for data in trn_data]
