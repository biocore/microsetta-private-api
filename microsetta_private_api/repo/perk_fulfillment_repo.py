import pycountry
from datetime import datetime
from dateutil.relativedelta import relativedelta

from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.model.subscription import Subscription
from microsetta_private_api.admin.admin_impl import\
    create_daklapack_order_internal
from microsetta_private_api.model.daklapack_order import FEDEX_PROVIDER,\
    FEDEX_2DAY_SHIPPING
from microsetta_private_api.model.activation_code import ActivationCode


class PerkFulfillmentRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def _row_to_subscription(self, r):
        return Subscription(r['subscription_id'], r['transaction_id'],
                            r['account_id'], r['cancelled'],)

    def find_perks_without_fulfillment_details(self):
        """If a perk isn't represented in our system at all, the transaction
        won't be imported. However, we need to have fulfillment details to
        act on a perk being selected. This finds any perks for which we
        haven't established fulfillment details and returns content for an
        alert email.
        """
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT transaction_id, perk_id "
                "FROM campaign.fundrazr_transaction_perk "
                "WHERE perk_id NOT IN ("
                "    SELECT DISTINCT(perk_id) "
                "    FROM campaign.fundrazr_perk_fulfillment_details"
                ")"
            )
            rows = cur.fetchall()
            if rows is None:
                return None
            else:
                return [dict(r) for r in rows]

    def process_pending_fulfillments(self):
        """Find all purchased perks that have yet to be processed
        and fulfill them"""
        error_report = []

        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT ftp.id ftp_id, ftp.transaction_id, ftp.perk_id, "
                "ftp.quantity, ft.payer_email, fpfd.ffq_quantity, "
                "fpfd.kit_quantity, fpfd.dak_article_code, "
                "fpfd.fulfillment_spacing_number, "
                "fpfd.fulfillment_spacing_unit, iu.first_name, iu.last_name, "
                "iu.phone, iu.address_1, iu.address_2, iu.city, iu.state, "
                "iu.postal_code, iu.country, iu.campaign_id "
                "FROM campaign.fundrazr_transaction_perk ftp "
                "INNER JOIN campaign.transaction ft "
                "ON ftp.transaction_id = ft.id "
                "INNER JOIN campaign.fundrazr_perk_fulfillment_details fpfd "
                "ON ftp.perk_id = fpfd.perk_id "
                "INNER JOIN campaign.interested_users iu "
                "ON ft.interested_user_id = iu.interested_user_id "
                "AND iu.address_valid = true "
                "WHERE ftp.processed = false"
            )
            rows = cur.fetchall()

            for row in rows:
                if (row['ffq_quantity'] > 1 or row['kit_quantity'] > 1) and \
                        row['fulfillment_spacing_number'] > 0:
                    subscription_id = \
                        self._create_subscription(row['payer_email'],
                                                  row['transaction_id'],
                                                  row['ftp_id'])

                for x in range(row['ffq_quantity']):
                    if x > 0 and row['fulfillment_spacing_number'] > 0:
                        fulfillment_date =\
                            self._future_fulfillment_date(
                                row['fulfillment_spacing_number'],
                                row['fulfillment_spacing_unit'],
                                x
                            )
                        self._schedule_ffq(subscription_id, fulfillment_date,
                                           False)
                    else:
                        self._fulfill_ffq(row['ftp_id'], row['first_name'],
                                          row['payer_email'])
                        if row['ffq_quantity'] > 0 and\
                                row['fulfillment_spacing_number'] > 0:
                            # If this is the first FFQ of a subscription,
                            # we mark it as both scheduled and fulfilled
                            cur_date = datetime.now()
                            cur_date = cur_date.strftime("%Y-%m-%d")
                            self._schedule_ffq(subscription_id, cur_date,
                                               True)

                for x in range(row['kit_quantity']):
                    if x > 0 and row['fulfillment_spacing_number'] > 0:
                        fulfillment_date =\
                            self._future_fulfillment_date(
                                row['fulfillment_spacing_number'],
                                row['fulfillment_spacing_unit'],
                                x
                            )
                        self._schedule_kit(subscription_id,
                                           fulfillment_date,
                                           row['dak_article_code'],
                                           False)
                    else:
                        country = pycountry.countries.get(alpha_2=
                                                          row['country'])
                        country_name = country.name

                        projects =\
                            self._campaign_id_to_projects(row['campaign_id'])
                        address_dict = {
                            "firstName": row['first_name'],
                            "lastName": row['last_name'],
                            "address1": row['address_1'],
                            "insertion": "",
                            "address2": row['address_2'],
                            "postalCode": row['postal_code'],
                            "city": row['city'],
                            "state": row['state'],
                            "country": country_name,
                            "countryCode": row['country'],
                            "phone": row['phone']
                        }
                        status, return_val =\
                           self._fulfill_kit(row['ftp_id'],
                                             projects,
                                             row['dak_article_code'],
                                             1,
                                             address_dict)
                        if not status:
                            # Daklapack order failed, let the error percolate
                            error_report.append(return_val)

                        if row['kit_quantity'] > 0 and\
                                row['fulfillment_spacing_number'] > 0:
                            # If this is the first kit of a subscription,
                            # we mark it as both scheduled and fulfilled
                            cur_date = datetime.now()
                            cur_date = cur_date.strftime("%Y-%m-%d")
                            self._schedule_kit(subscription_id,
                                               cur_date,
                                               row['dak_article_code'],
                                               True)
                cur.execute(
                    "UPDATE campaign.fundrazr_transaction_perk "
                    "SET processed = true "
                    "WHERE id = %s",
                    (row['ftp_id'], )
                )

        return error_report

    def process_subscription_fulfillments(self):
        error_report = []

        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT sf.fulfillment_id, sf.fulfillment_type, "
                "sf.dak_article_code, ftp.id ftp_id, ft.payer_email, "
                "iu.first_name iu_first_name, iu.last_name iu_last_name, "
                "iu.phone iu_phone, iu.address_1 iu_address_1, "
                "iu.address_2 iu_address_2, iu.city iu_city, "
                "iu.state iu_state, iu.postal_code iu_postal_code, "
                "iu.country iu_country, iu.campaign_id, s.account_id, "
                "a.email a_email, a.first_name a_first_name, "
                "a.last_name a_last_name, a.street a_address_1, "
                "a.city a_city, a.state a_state, a.post_code a_postal_code, "
                "a.country_code a_country "
                "FROM campaigns.subscriptions_fulfillment sf "
                "INNER JOIN campaigns.subscriptions s "
                "ON sf.subscription_id = s.subscription_id "
                "INNER JOIN campaigns.fundrazr_transaction_perk ftp "
                "ON s.fundrazr_transaction_perk_id = ftp.id "
                "INNER JOIN campaigns.transaction ft "
                "ON ftp.transaction_id = ft.id "
                "INNER JOIN campaign.interested_users iu "
                "ON ft.interested_user_id = iu.interested_user_id "
                "LEFT JOIN ag.account a"
                "ON s.account_id = a.id"
                "WHERE sf.fulfilled = false AND sf.cancelled = FALSE "
                "AND sf.fulfillment_date <= CURRENT_DATE"
            )
            rows = cur.fetchall()
            for row in rows:
                if row['fulfillment_type'] == "ffq":
                    # If an account is linked to the subscription, we use
                    # that account's first name and email
                    if row['account_id']:
                        self._fulfill_ffq(row['ftp_id'], row['a_first_name'],
                                          row['a_email'])
                    # If no account, fall back to original Fundrazr data
                    else:
                        self._fulfill_ffq(row['ftp_id'], row['iu_first_name'],
                                          row['payer_email'])
                elif row['fulfillment_type'] == "kit":
                    projects = \
                        self._campaign_id_to_projects(row['campaign_id'])

                    if row['account_id']:
                        country = pycountry.countries.get(alpha_2=
                                                          row['a_country'])
                        country_name = country.name

                        address_dict = {
                            "firstName": row['a_first_name'],
                            "lastName": row['a_last_name'],
                            "address1": row['a_address_1'],
                            "insertion": "",
                            "address2": "",
                            "postalCode": row['a_postal_code'],
                            "city": row['a_city'],
                            "state": row['a_state'],
                            "country": country_name,
                            "countryCode": row['a_country'],
                            "phone": row['a_phone']
                        }
                    else:
                        country = pycountry.countries.get(alpha_2=
                                                          row['country'])
                        country_name = country.name

                        address_dict = {
                            "firstName": row['iu_first_name'],
                            "lastName": row['iu_last_name'],
                            "address1": row['iu_address_1'],
                            "insertion": "",
                            "address2": row['iu_address_2'],
                            "postalCode": row['iu_postal_code'],
                            "city": row['iu_city'],
                            "state": row['iu_state'],
                            "country": country_name,
                            "countryCode": row['iu_country'],
                            "phone": row['iu_phone']
                        }

                    status, return_val = \
                        self._fulfill_kit(row['ftp_id'],
                                          projects,
                                          row['dak_article_code'],
                                          1,
                                          address_dict)
                    if not status:
                        # Daklapack order failed, let the error percolate
                        error_report.append(return_val)
                else:
                    error_report.append(
                        f"Subscription fulfillment {row['fulfillment_id']} "
                        f"contains malformed fulfillment_type "
                        f"{row['fulfillmnet_type']}"
                    )

                cur.execute(
                    "UPDATE campaign.subscriptions_fulfillment "
                    "SET fulfilled = true "
                    "WHERE fulfillment_id = %s",
                    (row['fulfillment_id'], )
                )

    def check_for_shipping_updates(self):
        """Find orders for which we have not provided a tracking number,
        see whether Daklapack has processed the order(s), and send out
        tracking details as necessary."""
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT fdo.fundrazr_transaction_perk_id, fdo.dak_order_id, "
                "kit.outbound_fedex_tracking, t.payer_email, "
                "t.payer_first_name "
                "FROM campaign.fundrazr_daklapack_orders fdo "
                "WHERE fdo.tracking_sent = false "
                "INNER JOIN barcodes.daklapack_order do "
                "ON fdo.dak_order_id = do.dak_order_id "
                "AND do.last_polling_status = 'Sent' "
                "INNER JOIN barcodes.daklapack_order_to_kit dotk"
                "ON do.dak_order_id = dotk.dak_order_id "
                "INNER JOIN barcodes.kit kit "
                "ON dotk.kit_uuid = kit.kit_uuid "
                "INNER JOIN campaign.fundrazr_transaction_perk ftp "
                "ON fdo.fundrazr_transaction_perk_id = ftp.id "
                "INNER JOIN campaign.transaction t"
                "ON ftp.transaction_id = t.id"
            )
            rows = cur.fetchall()
            for r in rows:
                print("Send tracking info!")
                # send the email here
                cur.execute(
                    "UPDATE campaign.fundrazr_daklapack_orders "
                    "SET tracking_sent = true "
                    "WHERE fundrazr_transaction_perk_id = %s "
                    "AND dak_order_id = %s",
                    (r['fundrazr_transaction_perk_id'], r['dak_order_id'])
                )

    def _fulfill_kit(self, ftp_id, projects, dak_article_code, quantity,
                     address_dict):
        # TODO: If we expand automated perk fulfillment beyond the US, we'll
        # need to handle shipping provider/type more elegantly.
        daklapack_order = {
            "project_ids": projects,
            "article_code": dak_article_code,
            "address": address_dict,
            "quantity": quantity,
            "shipping_provider": FEDEX_PROVIDER,
            "shipping_type": FEDEX_2DAY_SHIPPING
        }
        result = create_daklapack_order_internal(daklapack_order)
        if not result['order_success']:
            return False, result['daklapack_api_error_msg']
        else:
            with self._transaction.cursor() as cur:
                cur.execute(
                    "INSERT INTO campaign.fundrazr_daklapack_orders ("
                    "fundrazr_transaction_perk_id, dak_order_id, "
                    "tracking_sent"
                    ") VALUES ("
                    "%s, %s, %s"
                    ")",
                    (ftp_id, result['order_id'], False)
                )
            return True, result['order_id']

    def _fulfill_ffq(self, ftp_id, first_name, email):
        code = ActivationCode.generate_code()
        with self._transaction.cursor() as cur:
            cur.execute(
                "INSERT INTO campaign.ffq_registration_codes ("
                "ffq_registration_code"
                ") VALUES (%s)",
                (code,)
            )
            cur.execute(
                "INSERT INTO campaign.fundrazr_ffq_codes ("
                "fundrazr_transaction_perk_id, ffq_registration_code"
                ") VALUES (%s, %s)",
                (ftp_id, code)
            )
            # send the email here

    def _schedule_kit(self, subscription_id, fulfillment_date,
                      dak_article_code, fulfilled):
        with self._transaction.cursor() as cur:
            cur.execute(
                "INSERT INTO campaign.subscriptions_fulfillment ("
                "subscription_id, fulfillment_type, dak_article_code, "
                "fulfillment_date, fulfillment_date_changed, fulfilled, "
                "cancelled) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (subscription_id, 'kit', dak_article_code, fulfillment_date,
                 False, fulfilled, False)
            )

    def _schedule_ffq(self, subscription_id, fulfillment_date, fulfilled):
        with self._transaction.cursor() as cur:
            cur.execute(
                "INSERT INTO campaign.subscriptions_fulfillment ("
                "subscription_id, fulfillment_type, "
                "fulfillment_date, fulfillment_date_changed, fulfilled, "
                "cancelled) VALUES (%s, %s, %s, %s, %s, %s)",
                (subscription_id, 'ffq', fulfillment_date,
                 False, fulfilled, False)
            )

    def _create_subscription(self, email, transaction_id, ftp_id):
        """Create a subscription to schedule fulfillments for

        Parameters
        ----------
        email : str
            The email address of the participant who paid for a subscription
        transaction_id : str
            The transaction ID from Fundrazr
        ftp_id : str
            The fundrazr_transaction_perk.id value

        Returns
        -------
        subscription_id : uuid
            The ID of the newly created subscription
        """

        account_id = None
        cancelled = False

        # If an account exists under the email of the participant that
        # contributed to Fundrazr, we link the subscription to that account.
        # If not, we're going to watch for an account to be created using that
        # email. If that fails, we'll associate the subscription to the
        # account that uses the first kit from the subscription.
        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT id "
                "FROM ag.account "
                "WHERE email = %s",
                (email,)
            )
            r = cur.fetchone()
            if r:
                account_id = r['id']

            cur.execute(
                "INSERT INTO campaign.subscriptions "
                "(account_id, transaction_id, fundrazr_transaction_perk_id, "
                "cancelled) "
                "VALUES (%s, %s, %s, %s) "
                "RETURNING subscription_id",
                (account_id, transaction_id, ftp_id, cancelled)
            )
            subscription_id = cur.fetchone()[0]
        return subscription_id

    def get_subscriptions_by_account(self, account_id):
        """Find all subscriptions associated with a given account

        Parameters
        ----------
        account_id : str
            An account ID

        Returns
        -------
        Subscriptions or None
            An list of Subscriptions if any exist. Otherwise, None.
        """
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT subscription_id, transaction_id, account_id, "
                "cancelled "
                "FROM campaign.subscriptions "
                "WHERE account_id = %s",
                (account_id,)
            )
            rows = cur.fetchall()
            if rows is None:
                return None
            else:
                return [self._row_to_subscription(r) for r in rows]

    def get_subscription_by_id(self, subscription_id):
        """Find a subscription based on its id

        Parameters
        ----------
        subscription_id : str
            A subscription ID

        Returns
        -------
        Subscription or None
            A Subscription if one exists for provided id. Otherwise, None.
        """
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT subscription_id, transaction_id, account_id, "
                "cancelled "
                "FROM campaign.subscriptions "
                "WHERE subscription_id = %s",
                (subscription_id,)
            )
            row = cur.fetchone()
            if row is None:
                return None
            else:
                return self._row_to_subscription(row)

    def cancel_subscription(self, subscription_id):
        """Cancels a subscription and associated future fulfillments

        Parameters
        ----------
        subscription_id : str
            A subscription ID

        Returns
        -------
        True
            The function completed
        """
        with self._transaction.cursor() as cur:
            cur.execute(
                "UPDATE campaign.subscriptions "
                "SET cancelled = true "
                "WHERE subscription_id = %s",
                (subscription_id,)
            )
            cur.execute(
                "UPDATE campaign.subscriptions_fulfillment "
                "SET cancelled = true "
                "WHERE subscription_id = %s ",
                (subscription_id,)
            )

    def _campaign_id_to_projects(self, campaign_id):
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT project_id "
                "FROM campaign.campaigns_projects "
                "WHERE campaign_id = %s",
                (campaign_id,)
            )
            project_rows = cur.fetchall()
            project_ids = [project['project_id'] for project in project_rows]
            return project_ids

    def _future_fulfillment_date(self, spacing_number, spacing_unit,
                                 multiplier):
        cur_date = datetime.now()
        if spacing_unit == "days":
            new_date = cur_date + relativedelta(
                days=+(spacing_number*multiplier)
            )
        elif spacing_unit == "months":
            new_date = cur_date + relativedelta(
                months=+(spacing_number*multiplier)
            )
        else:
            raise RepoException("Unknown "
                                "fulfillment_spacing_unit")

        return new_date.strftime("%Y-%m-%d")
