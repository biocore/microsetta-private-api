import unittest
from unittest import skipIf
import datetime
import uuid
from unittest.mock import patch
import dateutil.parser

from microsetta_private_api.repo.perk_fulfillment_repo import\
    PerkFulfillmentRepo
from microsetta_private_api.repo.campaign_repo import UserTransaction
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.model.campaign import (FundRazrPayment, Item,
                                                   Shipping)
from microsetta_private_api.model.address import Address
from microsetta_private_api.model.daklapack_order import DaklapackOrder
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.admin_repo import AdminRepo


ADDRESS1 = Address(
    '9500 Gilman Dr',
    'La Jolla',
    'CA',
    '92093',
    'US')
SHIPPING1 = Shipping('Microbe', 'Researcher', ADDRESS1)

ITEM_ONE_FFQ = [
    Item('Analyze Your Nutrition', 1, '3QeVd')
]
ITEM_ONE_KIT = [
    Item('Explore Your Microbiome', 1, '3QeW6'),
]
ITEM_ONE_SUBSCRIPTION = [
    Item('Follow Your Gut', 1, '0QeXa')
]
ITEM_FAKE_PERK = [
    Item('Not a Perk', 1, 'FAKEFAKE')
]

TRANSACTION_ONE_FFQ = FundRazrPayment(
    '123abc',
    datetime.datetime.now(),
    '4Tqx5',
    20.,
    20.,
    'usd',
    'Microbe',
    'Researcher',
    'paypal',
    True,
    None,
    'coolcool',
    '123456789',
    SHIPPING1,
    ITEM_ONE_FFQ,
    payer_email='microbe@bar.com',
    contact_email='microbe@bar.com'
)
TRANSACTION_ONE_KIT = FundRazrPayment(
    '123abc',
    datetime.datetime.now(),
    '4Tqx5',
    180.,
    180.,
    'usd',
    'Microbe',
    'Researcher',
    'paypal',
    True,
    None,
    'coolcool',
    '123456789',
    SHIPPING1,
    ITEM_ONE_KIT,
    payer_email='microbe@bar.com',
    contact_email='microbe@bar.com'
)
TRANSACTION_ONE_SUBSCRIPTION = FundRazrPayment(
    '123abc',
    datetime.datetime.now(),
    '4Tqx5',
    720.,
    720.,
    'usd',
    'Microbe',
    'Researcher',
    'paypal',
    True,
    None,
    'coolcool',
    '123456789',
    SHIPPING1,
    ITEM_ONE_SUBSCRIPTION,
    payer_email='microbe@bar.com',
    contact_email='microbe@bar.com'
)
TRANSACTION_FAKE_PERK = FundRazrPayment(
    '123abc',
    datetime.datetime.now(),
    '4Tqx5',
    6.,
    6.,
    'usd',
    'Microbe',
    'Researcher',
    'paypal',
    True,
    None,
    'coolcool',
    '123456789',
    SHIPPING1,
    ITEM_FAKE_PERK,
    payer_email='microbe@bar.com',
    contact_email='microbe@bar.com'
)

DUMMY_ORDER_ID = str(uuid.uuid4())
SUBMITTER_ID = "000fc4cd-8fa4-db8b-e050-8a800c5d81b7"
SUBMITTER_NAME = "demo demo"
PROJECT_IDS = [1,]
DUMMY_DAKLAPACK_ORDER = {
    'orderId': DUMMY_ORDER_ID,
    'articles': [
        {
            'articleCode': '3510005E',
            'addresses': [
                {
                    'firstName': 'Microbe',
                    'lastName': 'Researcher',
                    'address1': '9500 Gilman Dr',
                    'insertion': '',
                    'address2': '',
                    'postalCode': 92093,
                    'city': 'La Jolla',
                    'state': 'CA',
                    'country': 'United States',
                    'countryCode': 'US',
                    'phone': '1234567890',
                    'creationDate': '2020-10-09T22:43:52.219328Z',
                    'companyName': SUBMITTER_NAME
                }
            ]
        }
    ],
    'shippingProvider': 'FedEx',
    'shippingType': 'FEDEX_2_DAY',
    'shippingProviderMetadata': [
        {'key': 'Reference 1',
         'value': 'Bill Ted'}
    ]
}
VERIFY_ADDRESS_DICT = {
    "valid": True,
    "address_1": "9500 Gilman Dr",
    "address_2": "",
    "address_3": "",
    "city": "La Jolla",
    "state": "CA",
    "postal": "92093",
    "latitude": 32.879215217102335,
    "longitude": -117.24106063080784
}


class PerkFulfillmentRepoTests(unittest.TestCase):
    def setUp(self):
        self.test_campaign_title_1 = 'Test Campaign'
        with Transaction() as t:
            cur = t.cursor()
            cur.execute(
                "INSERT INTO campaign.campaigns (title) "
                "VALUES (%s) "
                "RETURNING campaign_id",
                (self.test_campaign_title_1, )
            )
            self.test_campaign_id1 = cur.fetchone()[0]

            cur.execute(
                "INSERT INTO campaign.campaigns_projects "
                "(campaign_id, project_id) "
                "VALUES (%s, 1)",
                (self.test_campaign_id1, )
            )
            t.commit()

    def tearDown(self):
        with Transaction() as t:
            cur = t.cursor()
            cur.execute(
                "DELETE FROM campaign.campaigns_projects "
                "WHERE campaign_id = %s",
                (self.test_campaign_id1,)
            )
            cur.execute(
                "DELETE FROM campaign.campaigns "
                "WHERE campaign_id = %s",
                (self.test_campaign_id1, )
            )
            t.commit()

    def test_find_perks_without_fulfillment_details(self):
        with Transaction() as t:
            cur = t.cursor()

            # Create a fake perk
            cur.execute(
                "INSERT INTO campaign.fundrazr_perk "
                "(id, remote_campaign_id, title, price) "
                "VALUES ('FAKEFAKE', '4Tqx5', 'Not a Perk', 6)"
            )

            ut = UserTransaction(t)
            ut.add_transaction(TRANSACTION_FAKE_PERK)
            pfr = PerkFulfillmentRepo(t)
            res = pfr.find_perks_without_fulfillment_details()

            # Our result should contain at least one perk for which we don't
            # have fulfillment details
            self.assertTrue(len(res) > 0)

            # Verify that one of the perks is ours with a perk_id of FAKEFAKE
            found_fake = False
            for bad_perk in res:
                if bad_perk['perk_id'] == "FAKEFAKE":
                    found_fake = True

            self.assertTrue(found_fake)

    @patch(
        "microsetta_private_api.repo.perk_fulfillment_repo."
        "create_daklapack_order_internal"
    )
    @patch("microsetta_private_api.repo.interested_user_repo.verify_address")
    def test_process_pending_fulfillments_one_kit_succeed(
            self,
            verify_address_result,
            test_daklapack_order_result
    ):
        verify_address_result.return_value = VERIFY_ADDRESS_DICT
        test_daklapack_order_result.return_value = {
            "order_address": "wedontcareaboutthis",
            "order_success": True,
            "order_id": DUMMY_ORDER_ID
        }

        with Transaction() as t:
            # create a dummy Daklapack order
            acct_repo = AccountRepo(t)
            submitter_acct = acct_repo.get_account(SUBMITTER_ID)

            creation_timestamp = dateutil.parser.isoparse(
                "2020-10-09T22:43:52.219328Z")
            last_polling_timestamp = dateutil.parser.isoparse(
                "2020-10-19T12:40:19.219328Z")
            desc = "a description"
            planned_send_date = datetime.date(2032, 2, 9)
            last_status = "accepted"

            # create dummy daklapack order object
            input = DaklapackOrder(DUMMY_ORDER_ID, submitter_acct,
                                   PROJECT_IDS, DUMMY_DAKLAPACK_ORDER, desc,
                                   planned_send_date, creation_timestamp,
                                   last_polling_timestamp, last_status)

            # call create_daklapack_order
            admin_repo = AdminRepo(t)
            returned_id = admin_repo.create_daklapack_order(input)

            ut = UserTransaction(t)
            ut.add_transaction(TRANSACTION_ONE_KIT)
            pfr = PerkFulfillmentRepo(t)
            res = pfr.process_pending_fulfillments()

            # res is a list of errors, which should be 0
            self.assertEqual(len(res), 0)

            cur = t.cursor()

            # Confirm that the order populated into fundrazr_daklapack_orders
            cur.execute(
                "SELECT COUNT(*) "
                "FROM campaign.fundrazr_daklapack_orders "
                "WHERE dak_order_id = %s",
                (returned_id, )
            )
            res = cur.fetchone()
            self.assertEqual(res[0], 1)

    @patch(
        "microsetta_private_api.repo.perk_fulfillment_repo."
        "create_daklapack_order_internal"
    )
    @patch("microsetta_private_api.repo.interested_user_repo.verify_address")
    def test_process_pending_fulfillments_one_kit_fail(
            self,
            verify_address_result,
            test_daklapack_order_result
    ):
        verify_address_result.return_value = VERIFY_ADDRESS_DICT
        test_daklapack_order_result.return_value = {
            "order_address": "wedontcareaboutthis",
            "order_success": False,
            "daklapack_api_error_msg": "Some error message",
            "daklapack_api_error_code": "Some error code"
        }

        with Transaction() as t:
            ut = UserTransaction(t)
            ut.add_transaction(TRANSACTION_ONE_KIT)
            pfr = PerkFulfillmentRepo(t)
            res = pfr.process_pending_fulfillments()

            # res is a list of errors, which should be 1
            self.assertEqual(len(res), 1)

    @patch("microsetta_private_api.repo.interested_user_repo.verify_address")
    def test_process_pending_fulfillments_one_ffq(self,
                                                  verify_address_result):
        verify_address_result.return_value = VERIFY_ADDRESS_DICT

        # We're going to add a transaction for one FFQ and process it.
        # We should observe one new record in the registration_codes and
        # fundrazr_ffq_codes tables.
        with Transaction() as t:
            ffq_r_c_count = self._count_ffq_registration_codes(t)
            exp_ffq_r_c_count = ffq_r_c_count+1

            fundrazr_ffq_count = self._count_fundrazr_ffq_codes(t)
            exp_fundrazr_ffq_count = fundrazr_ffq_count+1

            ut = UserTransaction(t)
            ut.add_transaction(TRANSACTION_ONE_FFQ)
            pfr = PerkFulfillmentRepo(t)
            pfr.process_pending_fulfillments()

            new_ffq_r_c_count = self._count_ffq_registration_codes(t)
            self.assertEqual(new_ffq_r_c_count, exp_ffq_r_c_count)

            new_fundrazr_ffq_count = self._count_fundrazr_ffq_codes(t)
            self.assertEqual(new_fundrazr_ffq_count, exp_fundrazr_ffq_count)

    @patch(
        "microsetta_private_api.repo.perk_fulfillment_repo."
        "create_daklapack_order_internal"
    )
    @patch("microsetta_private_api.repo.interested_user_repo.verify_address")
    def test_transaction_one_subscription(
            self,
            verify_address_result,
            test_daklapack_order_result
    ):
        test_daklapack_order_result.return_value = {
            "order_address": "wedontcareaboutthis",
            "order_success": True,
            "order_id": DUMMY_ORDER_ID
        }
        verify_address_result.return_value = VERIFY_ADDRESS_DICT

        # We're going to add a transaction for one subscription.
        # We should observe one new record in the registration_codes,
        # fundrazr_ffq_codes, fundrazr_daklapack_orders, and subscriptions
        # tables. We should also observe eight new records in the
        # subscriptions_fulfillment table.

        # We have to mock out the actual Daklapack order since it's an
        # external resource.
        with Transaction() as t:
            # create a dummy Daklapack order
            acct_repo = AccountRepo(t)
            submitter_acct = acct_repo.get_account(SUBMITTER_ID)

            creation_timestamp = dateutil.parser.isoparse(
                "2020-10-09T22:43:52.219328Z")
            last_polling_timestamp = dateutil.parser.isoparse(
                "2020-10-19T12:40:19.219328Z")
            desc = "a description"
            planned_send_date = datetime.date(2032, 2, 9)
            last_status = "accepted"

            # create dummy daklapack order object
            input = DaklapackOrder(DUMMY_ORDER_ID, submitter_acct,
                                   PROJECT_IDS, DUMMY_DAKLAPACK_ORDER, desc,
                                   planned_send_date, creation_timestamp,
                                   last_polling_timestamp, last_status)

            # call create_daklapack_order
            admin_repo = AdminRepo(t)
            returned_id = admin_repo.create_daklapack_order(input)

            ut = UserTransaction(t)
            ut.add_transaction(TRANSACTION_ONE_SUBSCRIPTION)
            pfr = PerkFulfillmentRepo(t)
            res = pfr.process_pending_fulfillments()

            # Confirm the fulfillment processed
            self.assertEqual(len(res), 0)

            cur = t.dict_cursor()

            # We need to grab the subscription ID
            cur.execute(
                "SELECT s.subscription_id "
                "FROM campaign.subscriptions s "
                "INNER JOIN campaign.fundrazr_daklapack_orders fdo "
                "ON s.fundrazr_transaction_perk_id = "
                "fdo.fundrazr_transaction_perk_id AND fdo.dak_order_id = %s",
                (returned_id, )
            )
            row = cur.fetchone()
            subscription_id = row['subscription_id']

            # Confirm that there's a fulfilled FFQ and a fulfilled kit
            # for the subscription_id
            cur.execute(
                "SELECT COUNT(*) kit_count "
                "FROM campaign.subscriptions_fulfillment "
                "WHERE subscription_id = %s AND fulfillment_type = 'kit' "
                "AND fulfilled = true",
                (subscription_id, )
            )
            row = cur.fetchone()
            self.assertEqual(row['kit_count'], 1)
            cur.execute(
                "SELECT COUNT(*) ffq_count "
                "FROM campaign.subscriptions_fulfillment "
                "WHERE subscription_id = %s AND fulfillment_type = 'ffq' "
                "AND fulfilled = true",
                (subscription_id, )
            )
            row = cur.fetchone()
            self.assertEqual(row['ffq_count'], 1)

            # Confirm there are three unfulfilled FFQ and kit records
            cur.execute(
                "SELECT COUNT(*) kit_count "
                "FROM campaign.subscriptions_fulfillment "
                "WHERE subscription_id = %s AND fulfillment_type = 'kit' "
                "AND fulfilled = false",
                (subscription_id, )
            )
            row = cur.fetchone()
            self.assertEqual(row['kit_count'], 3)
            cur.execute(
                "SELECT COUNT(*) ffq_count "
                "FROM campaign.subscriptions_fulfillment "
                "WHERE subscription_id = %s AND fulfillment_type = 'ffq' "
                "AND fulfilled = false",
                (subscription_id, )
            )
            row = cur.fetchone()
            self.assertEqual(row['ffq_count'], 3)

    def test_get_subscription_by_id(self):
        # create subscription
        # retrieve it using transaction_id
        # retrieve it using subscription_id
        print("Hello")

    def _count_ffq_registration_codes(self, t):
        cur = t.cursor()
        cur.execute(
            "SELECT COUNT(*) FROM campaign.ffq_registration_codes"
        )
        res = cur.fetchone()
        return res[0]

    def _count_fundrazr_ffq_codes(self, t):
        cur = t.cursor()
        cur.execute(
            "SELECT COUNT(*) FROM campaign.fundrazr_ffq_codes"
        )
        res = cur.fetchone()
        return res[0]


if __name__ == '__main__':
    unittest.main()
