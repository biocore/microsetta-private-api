import datetime
from dateutil.relativedelta import relativedelta

from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.tasks import send_email
from microsetta_private_api.model.activation_code import ActivationCode
from microsetta_private_api.config_manager import SERVER_CONFIG


class PerkTypeRepo(BaseRepo):

    def add_perk_type_to_campaign(self, perk_id, perk_type):
        with self._transaction.cursor() as cur:
            sql = ("""UPDATE campaign.fundrazr_perk
                  SET perk_type=%s
                  WHERE ID=%s""",
                   (perk_type, perk_id))
            cur.execute(*sql)

    def add_subscription(self, contact_email, transaction_id):
        account_id = self.get_account_id(contact_email)
        no_of_kits = 3
        subscription_add_sql = ("""INSERT INTO campaign.subscriptions
                    (submitter_acct_id, email,
                    transaction_id, no_of_kits, status)
                    VALUES (%s, %s, %s, %s, %s)""",
                                (account_id, contact_email,
                                 transaction_id,
                                 no_of_kits, 'ACTIVE'))

        with self._transaction.cursor() as cur:
            cur.execute(*subscription_add_sql)
            subscription_id = cur.lastrowid

            for i in range(no_of_kits + 1):
                today = datetime.date.today()
                first_quarter = relativedelta(months=4 * i)
                planned_send_date = today + first_quarter

                subscription_shipment_sql = ("""INSERT INTO
                    campaign.subscription_shipment
                    subscription_id, planned_send_date, status)
                    VALUES (%s, %s, %s)""",
                                             (subscription_id,
                                              planned_send_date, 'PENDING'))
                cur.execute(*subscription_shipment_sql)

    def get_account_id(self, contact_email):
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT id
                            FROM ag.account
                            WHERE email=%s""",
                        (contact_email,))
            res = cur.fetchone()

            if not res:
                account_id = res['id']

            else:
                account_id = '00000000-0000-0000-0000-000000000000'

            return account_id

    def add_activation_code(self, campaign_id, perk_id, perk_type,
                            contact_email, payer_name):
        account_id = self.get_account_id(contact_email)
        code = ActivationCode.generate_code()

        if not account_id and perk_type == "FFQ_ONE_YEAR":
            # send mail to the user, who is already not in the system yet
            sign_up_url = SERVER_CONFIG["interface_endpoint"] + \
                          "/create_account"
            try:
                send_email(contact_email,
                           "new_sigup_mail",
                           {"payer_name": payer_name,
                            "activation_code": code,
                            "sign_up_url": sign_up_url,
                            }),
            except Exception as e:
                print(str(e))
        with self._transaction.cursor() as cur:

            sql = ("""INSERT INTO campaign.fundrazr_perk_activation_code
                (code, campaign_id, perk_id, account_id, email)
                VALUES (%s, %s, %s, %s, %s)""",
                   (code, campaign_id, perk_id, account_id,
                    contact_email))
            cur.execute(*sql)

    def get_perk_type(self, perk_id):
        with self._transaction.cursor() as cur:
            sql = ("""SELECT perk_tpe.fundrazr_perk
                  WHERE ID=%s""",
                   (perk_id,))
            r = cur.execute(*sql)
            return r

    def get_pending_shipments(self):
        with self._transaction.cursor() as cur:
            subscription_shipment_sql = ("""SELECT *
                    FROM campaign.subscription AS T1
                   JOIN campaign.subscription_shipment AS T2
                   ON T1.id = T2.id""")
            r = cur.execute(*subscription_shipment_sql)
            return r

    def get_account_details(self, email):
        with self._transaction.cursor() as cur:
            sql = ("""SELECT *
                    FROM ag.account
                  WHERE email=%s""",
                   (email,))
            r = cur.execute(*sql)
            return r

    def update_shipment(self, subscription_id, no_of_kits_remain):
        with self._transaction.cursor() as cur:
            shipment_sql = ("""UPDATE campaign.subscription_shipment
                  SET status=%s
                  WHERE subscription_id=%s""",
                            ('COMPLETED', subscription_id))
            subscription_sql = ("""UPDATE campaign.subscription_shipment
                  SET no_of_kits=%s
                  WHERE id=%s""",
                                (no_of_kits_remain, subscription_id))

            cur.execute(*shipment_sql)
            cur.execute(*subscription_sql)
