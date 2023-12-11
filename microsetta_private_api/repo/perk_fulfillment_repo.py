import pycountry
import uuid
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
from microsetta_private_api.tasks import send_email
from microsetta_private_api.localization import EN_US
from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.model.log_event import LogEvent
from microsetta_private_api.repo.event_log_repo import EventLogRepo
from microsetta_private_api.admin.email_templates import EmailMessage


class PerkFulfillmentRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    @staticmethod
    def _row_to_subscription(r):
        return Subscription.from_dict(r)

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

    def get_pending_fulfillments(self):
        with self._transaction.dict_cursor() as cur:
            """Find all purchased perks that have yet to be processed """
            cur.execute(
                "SELECT ftp.id "
                "FROM campaign.fundrazr_transaction_perk ftp "
                "INNER JOIN campaign.transaction ft "
                "ON ftp.transaction_id = ft.id "
                "INNER JOIN campaign.interested_users iu "
                "ON ft.interested_user_id = iu.interested_user_id "
                "AND iu.address_valid = TRUE "
                "WHERE ftp.processed = FALSE"
            )
            rows = cur.fetchall()
            return [r['id'] for r in rows]

    def process_pending_fulfillment(self, ftp_id):
        """Process a single pending fulfillment"""
        error_report = []

        with self._transaction.dict_cursor() as cur:
            # Lock the table to ensure that two concurrent operations
            # can't fulfill the same row
            self._transaction.lock_table("fundrazr_transaction_perk")

            # Once the table is locked, verify that the row has not
            # been processed and collect the necessary fields
            cur.execute(
                "SELECT ftp.id ftp_id, ftp.transaction_id, ftp.perk_id, "
                "ftp.quantity, fpfd.ffq_quantity, "
                "fpfd.kit_quantity, fpfd.dak_article_code, "
                "fpfd.fulfillment_spacing_number, "
                "fpfd.fulfillment_spacing_unit, iu.first_name, iu.last_name, "
                "iu.phone, iu.address_1, iu.address_2, iu.city, iu.state, "
                "iu.postal_code, iu.country, iu.campaign_id, iu.email "
                "FROM campaign.fundrazr_transaction_perk ftp "
                "INNER JOIN campaign.transaction ft "
                "ON ftp.transaction_id = ft.id "
                "INNER JOIN campaign.fundrazr_perk_fulfillment_details fpfd "
                "ON ftp.perk_id = fpfd.perk_id "
                "INNER JOIN campaign.interested_users iu "
                "ON ft.interested_user_id = iu.interested_user_id "
                "AND iu.address_valid = true "
                "WHERE ftp.processed = FALSE AND ftp.id = %s",
                (ftp_id, )
            )
            row = cur.fetchone()
            if row is not None:
                for perk_qty in range(row['quantity']):
                    if self._is_subscription(row):
                        subscription_id = \
                            self._create_subscription(row['email'],
                                                      row['transaction_id'],
                                                      row['ftp_id'])
                    else:
                        subscription_id = None

                    # If there are any FFQs attached to the perk, immediately
                    # fulfill the first one
                    if row['ffq_quantity'] > 0:
                        # If the perk is a kit or subscription, send thank you
                        # email with kit content. Otherwise, send thank you
                        # for FFQ only
                        if row['kit_quantity'] > 0:
                            template = "thank_you_with_kit"
                        else:
                            template = "thank_you_no_kit"

                        error_info = self._fulfill_ffq(
                            row['ftp_id'],
                            template,
                            row['email'],
                            row['first_name'],
                            subscription_id
                        )
                        if error_info is not None:
                            error_report.append(
                                f"Error sending FFQ email for ftp_id "
                                f"{row['ftp_id']}: {error_info}"
                            )

                    # Then, if there are more FFQs, schedule/fulfill them as
                    # appropriate based on fulfillment_spacing_number
                    for x in range(1, row['ffq_quantity']):
                        if row['fulfillment_spacing_number'] > 0:
                            fulfillment_date =\
                                self._future_fulfillment_date(
                                    row['fulfillment_spacing_number'],
                                    row['fulfillment_spacing_unit'],
                                    x
                                )
                            self._schedule_ffq(
                                subscription_id,
                                fulfillment_date,
                                fulfilled=False
                            )
                        else:
                            error_info = self._fulfill_ffq(
                                row['ftp_id'],
                                row['kit_quantity'],
                                row['email'],
                                row['first_name']
                            )
                            if error_info is not None:
                                error_report.append(
                                    f"Error sending FFQ email for ftp_id "
                                    f"{row['ftp_id']}: {error_info}"
                                )

                    # If there are any kits attached to the perk, immediately
                    # fulfill the first one
                    if row['kit_quantity'] > 0:
                        status, return_val = self._fulfill_kit(
                            row,
                            1,
                            subscription_id
                        )
                        if not status:
                            # Daklapack order failed, let the error percolate
                            error_report.append(
                                f"Error placing Daklapack order for ftp_id "
                                f"{row['ftp_id']}: {return_val}"
                            )

                    for x in range(1, row['kit_quantity']):
                        if row['fulfillment_spacing_number'] > 0:
                            fulfillment_date =\
                                self._future_fulfillment_date(
                                    row['fulfillment_spacing_number'],
                                    row['fulfillment_spacing_unit'],
                                    x
                                )
                            self._schedule_kit(subscription_id,
                                               fulfillment_date,
                                               row['dak_article_code'],
                                               fulfilled=False)
                        else:
                            # We hard-code a quantity of 1 here because
                            # the actual quantity is controlled by
                            # row['quantity'] and row['kit_quantity'].
                            status, return_val = self._fulfill_kit(
                                row,
                                1,
                                subscription_id
                            )
                            if not status:
                                # Dak order failed, let the error percolate
                                error_report.append(
                                    f"Error placing Daklapack order for "
                                    f"ftp_id {row['ftp_id']}: {return_val}"
                                )

                cur.execute(
                    "UPDATE campaign.fundrazr_transaction_perk "
                    "SET processed = true "
                    "WHERE id = %s",
                    (row['ftp_id'], )
                )

        return error_report

    def get_subscription_fulfillments(self):
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT fulfillment_id "
                "FROM campaign.subscriptions_fulfillment "
                "WHERE fulfilled = FALSE AND cancelled = FALSE "
                "AND fulfillment_date <= CURRENT_DATE"
            )
            rows = cur.fetchall()
            return [r['fulfillment_id'] for r in rows]

    def process_subscription_fulfillment(self, fulfillment_id):
        error_report = []

        with self._transaction.dict_cursor() as cur:
            # Lock the table to ensure that two concurrent operations
            # can't fulfill the same row
            self._transaction.lock_table("subscriptions_fulfillment")

            # Once the table is locked, verify that the row has not
            # been processed and collect the necessary fields
            cur.execute(
                "SELECT sf.fulfillment_id, sf.fulfillment_type, "
                "sf.dak_article_code, sf.subscription_id, ftp.id ftp_id, "
                "iu.email iu_email, iu.first_name, iu.last_name, iu.phone, "
                "iu.address_1, iu.address_2, iu.city, iu.state, "
                "iu.postal_code, iu.country, iu.campaign_id, s.account_id, "
                "a.email a_email, a.first_name a_first_name, "
                "a.last_name a_last_name, a.street a_address_1, "
                "a.city a_city, a.state a_state, a.post_code a_postal_code, "
                "a.country_code a_country "
                "FROM campaign.subscriptions_fulfillment sf "
                "INNER JOIN campaign.subscriptions s "
                "ON sf.subscription_id = s.subscription_id "
                "INNER JOIN campaign.fundrazr_transaction_perk ftp "
                "ON s.fundrazr_transaction_perk_id = ftp.id "
                "INNER JOIN campaign.transaction ft "
                "ON ftp.transaction_id = ft.id "
                "INNER JOIN campaign.interested_users iu "
                "ON ft.interested_user_id = iu.interested_user_id "
                "LEFT JOIN ag.account a "
                "ON s.account_id = a.id "
                "WHERE sf.fulfilled = FALSE AND sf.cancelled = FALSE "
                "AND sf.fulfillment_date <= CURRENT_DATE "
                "AND sf.fulfillment_id = %s",
                (fulfillment_id, )
            )
            row = cur.fetchone()
            if row is not None:
                fulfillment_error = False

                if row['fulfillment_type'] == "ffq":
                    # If an account is linked to the subscription, we use
                    # that account's first name and email
                    if row['account_id'] is not None:
                        email = row['a_email']
                        first_name = row['a_first_name']
                    # If no account, fall back to original Fundrazr data
                    else:
                        email = row['iu_email']
                        first_name = row['first_name']

                    email_error = self._fulfill_ffq(
                        row['ftp_id'],
                        "subscription_ffq_code",
                        email,
                        first_name
                    )
                    if email_error is not None:
                        fulfillment_error = True
                        error_report.append(
                            f"Error sending FFQ email for subscription "
                            f"fulfillment {row['fulfillment_id']}: "
                            f"{email_error}"
                        )

                elif row['fulfillment_type'] == "kit":
                    status, return_val = \
                        self._fulfill_kit(row, 1, row['subscription_id'])
                    if not status:
                        # Daklapack order failed, let the error percolate
                        error_report.append(
                            f"Error placing Daklapack order for subscription "
                            f"fulfillment {row['fulfillment_id']}: "
                            f"{return_val}"
                        )
                else:
                    fulfillment_error = True
                    error_report.append(
                        f"Subscription fulfillment {row['fulfillment_id']} "
                        f"contains malformed fulfillment_type "
                        f"{row['fulfillment_type']}"
                    )

                if not fulfillment_error:
                    cur.execute(
                        "UPDATE campaign.subscriptions_fulfillment "
                        "SET fulfilled = true "
                        "WHERE fulfillment_id = %s",
                        (row['fulfillment_id'], )
                    )

        return error_report

    def check_for_shipping_updates(self):
        """Find orders for which we have not provided a tracking number,
        see whether Daklapack has processed the order(s), and send out
        tracking details as necessary."""
        emails_sent = 0
        error_report = []

        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT fdo.fundrazr_transaction_perk_id ftp_id, "
                "fdo.dak_order_id, kit.outbound_fedex_tracking, "
                "iu.email, iu.first_name "
                "FROM campaign.fundrazr_daklapack_orders fdo "
                "INNER JOIN barcodes.daklapack_order dako "
                "ON fdo.dak_order_id = dako.dak_order_id "
                "AND dako.last_polling_status = 'Sent' "
                "INNER JOIN barcodes.daklapack_order_to_kit dotk "
                "ON dako.dak_order_id = dotk.dak_order_id "
                "INNER JOIN barcodes.kit kit "
                "ON dotk.kit_uuid = kit.kit_uuid "
                "INNER JOIN campaign.fundrazr_transaction_perk ftp "
                "ON fdo.fundrazr_transaction_perk_id = ftp.id "
                "INNER JOIN campaign.transaction t "
                "ON ftp.transaction_id = t.id "
                "INNER JOIN campaign.interested_users iu "
                "ON t.interested_user_id = iu.interested_user_id "
                "WHERE fdo.tracking_sent = false"
            )
            rows = cur.fetchall()
            template = "kit_tracking_number"
            for r in rows:
                try:
                    email_args = {
                        "first_name": r['first_name'],
                        "tracking_number": r['outbound_fedex_tracking']
                    }

                    email_address = r['email']

                    send_email(
                        email_address,
                        template,
                        email_args,
                        EN_US
                    )

                    # Log the email being sent
                    self._log_email(template, email_address, email_args)

                    # Mark the email sent for the order
                    cur.execute(
                        "UPDATE campaign.fundrazr_daklapack_orders "
                        "SET tracking_sent = true "
                        "WHERE fundrazr_transaction_perk_id = %s "
                        "AND dak_order_id = %s",
                        (r['ftp_id'], r['dak_order_id'])
                    )
                    emails_sent += 1
                except Exception as e:  # noqa
                    # if the email fails, we'll log why but continue executing
                    email_error = f"FedEx tracking code email failed " \
                                  f"for ftp_id={r['ftp_id']} and " \
                                  f"dak_order_id={r['dak_order_id']} with " \
                                  f"the following: {repr(e)}"
                    error_report.append(email_error)

        return emails_sent, error_report

    def _fulfill_kit(self, row, quantity, subscription_id):
        projects = \
            self._campaign_id_to_projects(row['campaign_id'])

        if "account_id" in row and row['account_id'] is not None:
            country = pycountry.countries.get(
                alpha_2=row['a_country']
            )
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
            country = pycountry.countries.get(
                alpha_2=row['country']
            )
            country_name = country.name

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

        # TODO: If we expand automated perk fulfillment beyond the US, we'll
        # need to handle shipping provider/type more elegantly.
        daklapack_order = {
            "project_ids": projects,
            "article_code": row['dak_article_code'],
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
                    (row['ftp_id'], result['order_id'], False)
                )

                # If this is the first kit of a subscription,
                # we mark it as both scheduled and fulfilled
                if subscription_id is not None:
                    cur_date = datetime.now()
                    cur_date = cur_date.strftime("%Y-%m-%d")
                    self._schedule_kit(subscription_id,
                                       cur_date,
                                       row['dak_article_code'],
                                       True)

            return True, result['order_id']

    def _fulfill_ffq(self, ftp_id, template, email,
                     first_name, subscription_id=None):
        code = ActivationCode.generate_code()
        with self._transaction.cursor() as cur:
            # Insert the newly created registration code
            cur.execute(
                "INSERT INTO campaign.ffq_registration_codes ("
                "ffq_registration_code"
                ") VALUES (%s)",
                (code,)
            )

            # Log the registration code as a fulfillment of a given FTP
            cur.execute(
                "INSERT INTO campaign.fundrazr_ffq_codes ("
                "fundrazr_transaction_perk_id, ffq_registration_code"
                ") VALUES (%s, %s)",
                (ftp_id, code)
            )

            # If this is the first FFQ of a subscription,
            # we mark it as both scheduled and fulfilled
            if subscription_id is not None:
                cur_date = datetime.now()
                cur_date = cur_date.strftime("%Y-%m-%d")
                self._schedule_ffq(subscription_id, cur_date,
                                   True)

            email_error = None
            try:
                email_args = {
                    "first_name": first_name,
                    "registration_code": code,
                    "interface_endpoint": SERVER_CONFIG["interface_endpoint"]
                }

                send_email(
                    email,
                    template,
                    email_args,
                    EN_US
                )

                self._log_email(template, email, email_args)
            except Exception as e:  # noqa
                # if the email fails, we'll log why but continue executing
                email_error = f"FFQ registration code email failed "\
                              f"for ftp_id={ftp_id} and code={code} with "\
                              f"the following: {repr(e)}"

        return email_error

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

    def _schedule_ffq(self, subscription_id, fulfillment_date,
                      fulfilled):
        with self._transaction.cursor() as cur:
            cur.execute(
                "INSERT INTO campaign.subscriptions_fulfillment ("
                "subscription_id, fulfillment_type, "
                "fulfillment_date, fulfillment_date_changed, fulfilled, "
                "cancelled) VALUES (%s, %s, %s, %s, %s, %s)",
                (subscription_id, 'ffq', fulfillment_date,
                 False, fulfilled, False)
            )

    def _create_subscription(self, email, transaction_id,
                             ftp_id):
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

        # AuthRocket automatically returns email addresses as lowercase, so
        # we can safely perform matching by converting the search email. ILIKE
        # is not a suitable solution, as it can return false positives.
        email = email.lower()

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
                "WHERE account_id = %s AND account_id IS NOT NULL",
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
                return PerkFulfillmentRepo._row_to_subscription(row)

    def get_unclaimed_subscriptions_by_email(self, email):
        """Find any subscriptions that are not yet attached to an account
           based on the email address that obtained them

        Parameters
        ----------
        email : str
            An email address

        Returns
        -------
        List of subscription_ids (UUID) or None
            A list of subscription_ids if any exist for provided email.
            Otherwise, None.
        """

        email = email.lower()
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT subscription_id "
                "FROM campaign.subscriptions s "
                "INNER JOIN campaign.transaction t "
                "ON s.transaction_id = t.id "
                "INNER JOIN campaign.interested_users iu "
                "ON t.interested_user_id = iu.interested_user_id "
                "WHERE account_id IS NULL AND LOWER(iu.email) = %s",
                (email, )
            )
            rows = cur.fetchall()
            if rows is None:
                return None
            else:
                return [r['subscription_id'] for r in rows]

    def claim_unclaimed_subscription(self, subscription_id, account_id):
        """Attach an account_id to a subscription that doesn't yet have one

        Parameters
        ----------
        subscription_id : UUID
            A subscription's ID
        account_id : UUID
            An account ID

        Returns
        -------
        int
            Number of rows affected
        """
        with self._transaction.cursor() as cur:
            cur.execute(
                "UPDATE campaign.subscriptions "
                "SET account_id = %s "
                "WHERE subscription_id = %s",
                (account_id, subscription_id)
            )
            return cur.rowcount

    def cancel_subscription(self, subscription_id):
        """Cancels a subscription and associated future fulfillments

        Parameters
        ----------
        subscription_id : str
            A subscription ID

        Returns
        -------
        int
            The number of records affected in campaign.subscription
        """
        with self._transaction.cursor() as cur:
            cur.execute(
                "UPDATE campaign.subscriptions "
                "SET cancelled = true "
                "WHERE subscription_id = %s",
                (subscription_id,)
            )
            return_val = cur.rowcount
            cur.execute(
                "UPDATE campaign.subscriptions_fulfillment "
                "SET cancelled = true "
                "WHERE subscription_id = %s ",
                (subscription_id,)
            )
            return return_val

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
        spacing = abs(spacing_number)*multiplier
        if spacing_unit == "days":
            new_date = cur_date + relativedelta(
                days=+spacing
            )
        elif spacing_unit == "months":
            new_date = cur_date + relativedelta(
                months=+spacing
            )
        else:
            raise RepoException("Unknown "
                                "fulfillment_spacing_unit")

        return new_date.strftime("%Y-%m-%d")

    def _is_subscription(self, perk):
        return (perk['ffq_quantity'] > 1 or perk['kit_quantity'] > 1) and \
           (perk['fulfillment_spacing_number'] > 0)

    def _log_email(self, template, email_address, email_args):
        # Log the event of the email being sent
        template_info = EmailMessage[template]
        event = LogEvent(
            uuid.uuid4(),
            template_info.event_type,
            template_info.event_subtype,
            None,
            {
                # account_id and email are necessary to allow searching the
                # event log.
                "account_id": None,
                "email": email_address,
                "template": template,
                "template_args": email_args
            })
        EventLogRepo(self._transaction).add_event(event)

    def check_perk_fulfillment_active(self):
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT perk_fulfillment_active "
                "FROM ag.settings "
            )
            row = cur.fetchone()
            return row['perk_fulfillment_active']

    def get_ffq_codes_by_email(self, email):
        email = "%" + email + "%"
        with self._transaction.dict_cursor() as cur:
            # Note: Use left join to differentiate email not found possibility
            cur.execute(
                """
                WITH all_codes AS (
                    SELECT
                        iu.email,
                        tr.created AS transaction_created_time,
                        frc.ffq_registration_code,
                        frc.registration_code_used
                    FROM campaign.interested_users AS iu
                    LEFT JOIN campaign.transaction AS tr
                    ON iu.interested_user_id = tr.interested_user_id
                    LEFT JOIN campaign.fundrazr_transaction_perk AS ftp
                    ON tr.id = ftp.transaction_id
                    LEFT JOIN campaign.fundrazr_ffq_codes AS ffc
                    ON ftp.id = ffc.fundrazr_transaction_perk_id
                    LEFT JOIN campaign.ffq_registration_codes AS frc
                    ON ffc.ffq_registration_code = frc.ffq_registration_code
                    WHERE iu.email ILIKE %s
                ), count_codes AS (
                    SELECT
                        ac1.email,
                        COUNT(ac1.ffq_registration_code) AS num_codes
                    FROM all_codes AS ac1
                    GROUP BY ac1.email
                )
                SELECT DISTINCT
                    ac.email,
                    CASE WHEN
                        cc.num_codes = 0 THEN NULL
                    ELSE
                        ac.transaction_created_time
                    END,
                    ac.ffq_registration_code,
                    ac.registration_code_used
                FROM all_codes AS ac
                LEFT JOIN count_codes AS cc
                ON ac.email = cc.email
                WHERE
                    ac.ffq_registration_code IS NOT NULL
                OR
                    cc.num_codes = 0
                ORDER BY
                    ac.email ASC,
                    ac.registration_code_used DESC
                """,
                (email,)
            )
            rows = cur.fetchall()
            return [dict(row) for row in rows]
