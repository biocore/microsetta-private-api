import unittest
import datetime
import uuid
from unittest.mock import patch
import dateutil.parser

from microsetta_private_api.config_manager import SERVER_CONFIG
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
from microsetta_private_api.model.account import Account

ACCT_ID_1 = '7a98df6a-e4db-40f4-91ec-627ac315d881'
DUMMY_ACCT_INFO_1 = {
    "address": {
        "city": "Springfield",
        "country_code": "US",
        "post_code": "12345",
        "state": "CA",
        "street": "123 Main St. E. Apt. 2"
    },
    "email": "microbe@bar.com",
    "first_name": "Jane",
    "last_name": "Doe",
    "language": "en_US",
    "kit_name": 'jb_qhxqe',
    "id": ACCT_ID_1
}
ACCT_MOCK_ISS_1 = "MrUnitTest.go"
ACCT_MOCK_SUB_1 = "NotARealSub"

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

FFQ_TRANSACTION_ID = "FFQ_TRANS"
KIT_TRANSACTION_ID = "KIT_TRANS"
SUB_TRANSACTION_ID = "SUB_TRANS"

TRANSACTION_ONE_FFQ = FundRazrPayment(
    FFQ_TRANSACTION_ID,
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
    KIT_TRANSACTION_ID,
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
    SUB_TRANSACTION_ID,
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
DUMMY_ORDER_ID2 = str(uuid.uuid4())
SUBMITTER_ID = SERVER_CONFIG['fulfillment_account_id']
SUBMITTER_NAME = "demo demo"
PROJECT_IDS = [1, ]
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
DUMMY_DAKLAPACK_ORDER2 = {
    'orderId': DUMMY_ORDER_ID2,
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
DUMMY_KIT_UUID = str(uuid.uuid4())
DUMMY_KIT_ID = "SOMEKIT44"
DUMMY_TRACKING = "qwerty123456"


class PerkFulfillmentRepoTests(unittest.TestCase):
    @patch("microsetta_private_api.repo.interested_user_repo.verify_address")
    def setUp(self, verify_address_result):
        verify_address_result.return_value = VERIFY_ADDRESS_DICT

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

            # We need to insert some dummy transactions
            ut = UserTransaction(t)
            ut.add_transaction(TRANSACTION_ONE_FFQ)
            cur.execute(
                "SELECT id "
                "FROM campaign.fundrazr_transaction_perk "
                "WHERE transaction_id = %s",
                (FFQ_TRANSACTION_ID, )
            )
            res = cur.fetchone()
            self.ffq_ftp_id = res[0]

            ut.add_transaction(TRANSACTION_ONE_KIT)
            cur.execute(
                "SELECT id "
                "FROM campaign.fundrazr_transaction_perk "
                "WHERE transaction_id = %s",
                (KIT_TRANSACTION_ID, )
            )
            res = cur.fetchone()
            self.kit_ftp_id = res[0]

            ut.add_transaction(TRANSACTION_ONE_SUBSCRIPTION)
            cur.execute(
                "SELECT id "
                "FROM campaign.fundrazr_transaction_perk "
                "WHERE transaction_id = %s",
                (SUB_TRANSACTION_ID, )
            )
            res = cur.fetchone()
            self.sub_ftp_id = res[0]

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
            cur.execute(
                "DELETE FROM campaign.fundrazr_transaction_perk "
                "WHERE id IN %s",
                ((self.ffq_ftp_id, self.kit_ftp_id, self.sub_ftp_id), )
            )
            cur.execute(
                "DELETE FROM campaign.transaction "
                "WHERE id IN %s",
                ((
                     FFQ_TRANSACTION_ID,
                     KIT_TRANSACTION_ID,
                     SUB_TRANSACTION_ID
                 ), )
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

    def test_get_pending_fulfillments(self):
        with Transaction() as t:
            pfr = PerkFulfillmentRepo(t)
            res = pfr.get_pending_fulfillments()

            # We created three transactions in setUp(), so we should observe
            # a list of three ftp_ids
            self.assertEqual(len(res), 3)
            self.assertTrue(self.ffq_ftp_id in res)
            self.assertTrue(self.kit_ftp_id in res)
            self.assertTrue(self.sub_ftp_id in res)

    @patch(
        "microsetta_private_api.repo.perk_fulfillment_repo."
        "create_daklapack_order_internal"
    )
    def test_process_pending_fulfillment_kit_succeed(
            self,
            test_daklapack_order_result
    ):
        test_daklapack_order_result.return_value = {
            "order_address": "wedontcareaboutthis",
            "order_success": True,
            "order_id": DUMMY_ORDER_ID
        }

        # res simulates what comes back from
        # PerkFulfillmentRepo.get_pending_fulfillments()
        res = [self.kit_ftp_id]
        for ftp_id in res:
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
                                       PROJECT_IDS, DUMMY_DAKLAPACK_ORDER,
                                       desc, planned_send_date,
                                       creation_timestamp,
                                       last_polling_timestamp, last_status)

                # call create_daklapack_order
                admin_repo = AdminRepo(t)
                returned_id = admin_repo.create_daklapack_order(input)

                pfr = PerkFulfillmentRepo(t)
                _ = pfr.process_pending_fulfillment(ftp_id)

                cur = t.cursor()

                # Confirm that the order populated into
                # fundrazr_daklapack_orders
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
    def test_process_pending_fulfillments_one_kit_fail(
            self,
            test_daklapack_order_result
    ):
        test_daklapack_order_result.return_value = {
            "order_address": "wedontcareaboutthis",
            "order_success": False,
            "daklapack_api_error_msg": "Some error message",
            "daklapack_api_error_code": "Some error code"
        }

        # res simulates what comes back from
        # PerkFulfillmentRepo.get_pending_fulfillments()
        res = [self.kit_ftp_id]
        for ftp_id in res:
            with Transaction() as t:
                pfr = PerkFulfillmentRepo(t)
                res = pfr.process_pending_fulfillment(ftp_id)

                # We should observe an error reflecting a Daklapack issue
                found_dak_error = False
                for e in res:
                    if e.startswith(
                            f"Error placing Daklapack order for ftp_id "
                            f"{ftp_id}"
                    ):
                        found_dak_error = True
                self.assertTrue(found_dak_error)

    def test_process_pending_fulfillments_one_ffq(self):
        res = [self.ffq_ftp_id]
        for ftp_id in res:
            with Transaction() as t:
                ffq_r_c_count = self._count_ffq_registration_codes(t)
                exp_ffq_r_c_count = ffq_r_c_count+1

                fundrazr_ffq_count = self._count_fundrazr_ffq_codes(t)
                exp_fundrazr_ffq_count = fundrazr_ffq_count+1

                pfr = PerkFulfillmentRepo(t)
                _ = pfr.process_pending_fulfillment(ftp_id)

                new_ffq_r_c_count = self._count_ffq_registration_codes(t)
                self.assertEqual(new_ffq_r_c_count, exp_ffq_r_c_count)

                new_fundrazr_ffq_count = self._count_fundrazr_ffq_codes(t)
                self.assertEqual(
                    new_fundrazr_ffq_count,
                    exp_fundrazr_ffq_count
                )

    @patch(
        "microsetta_private_api.repo.perk_fulfillment_repo."
        "create_daklapack_order_internal"
    )
    def test_transaction_one_subscription(
            self,
            test_daklapack_order_result
    ):
        test_daklapack_order_result.return_value = {
            "order_address": "wedontcareaboutthis",
            "order_success": True,
            "order_id": DUMMY_ORDER_ID
        }

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

            pfr = PerkFulfillmentRepo(t)
            _ = pfr.process_pending_fulfillment(self.sub_ftp_id)

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

    @patch(
        "microsetta_private_api.repo.perk_fulfillment_repo."
        "create_daklapack_order_internal"
    )
    def test_get_subscription_by_id(
            self,
            test_daklapack_order_result
    ):
        test_daklapack_order_result.return_value = {
            "order_address": "wedontcareaboutthis",
            "order_success": True,
            "order_id": DUMMY_ORDER_ID
        }

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

            pfr = PerkFulfillmentRepo(t)
            pfr.process_pending_fulfillment(self.sub_ftp_id)

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

            subscription = pfr.get_subscription_by_id(subscription_id)

            # Confirm that we can retrieve the subscription by id
            self.assertEqual(subscription.subscription_id, subscription_id)

    @patch(
        "microsetta_private_api.repo.perk_fulfillment_repo."
        "create_daklapack_order_internal"
    )
    def test_get_unclaimed_subscriptions_by_email_and_claim(
            self,
            test_daklapack_order_result
    ):
        test_daklapack_order_result.return_value = {
            "order_address": "wedontcareaboutthis",
            "order_success": True,
            "order_id": DUMMY_ORDER_ID
        }

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
            _ = admin_repo.create_daklapack_order(input)

            pfr = PerkFulfillmentRepo(t)
            pfr.process_pending_fulfillment(self.sub_ftp_id)

            res = pfr.get_unclaimed_subscriptions_by_email("microbe@bar.com")
            subscription_id = res[0]
            # verify that we received a subscription_id back
            self.assertEqual(len(res), 1)

            # create a dummy account
            ar = AccountRepo(t)
            acct_1 = Account.from_dict(DUMMY_ACCT_INFO_1,
                                       ACCT_MOCK_ISS_1,
                                       ACCT_MOCK_SUB_1)
            ar.create_account(acct_1)

            # now let's claim it
            res = pfr.claim_unclaimed_subscription(subscription_id, ACCT_ID_1)
            self.assertEqual(res, 1)

            # and make sure get_subscription_by_account works
            res = pfr.get_subscriptions_by_account(ACCT_ID_1)
            self.assertEqual(subscription_id, res[0].subscription_id)

    @patch(
        "microsetta_private_api.repo.perk_fulfillment_repo."
        "create_daklapack_order_internal"
    )
    def test_cancel_subscription(
            self,
            test_daklapack_order_result
    ):
        test_daklapack_order_result.return_value = {
            "order_address": "wedontcareaboutthis",
            "order_success": True,
            "order_id": DUMMY_ORDER_ID
        }

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

            pfr = PerkFulfillmentRepo(t)
            pfr.process_pending_fulfillment(self.sub_ftp_id)

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

            rowcount = pfr.cancel_subscription(subscription_id)

            # Confirm that we can retrieve the subscription by id
            self.assertEqual(rowcount, 1)

            # Confirm that there are six cancelled and unfulfilled rows
            cur.execute(
                "SELECT * "
                "FROM campaign.subscriptions_fulfillment "
                "WHERE subscription_id = %s AND cancelled = TRUE "
                "AND fulfilled = FALSE",
                (subscription_id, )
            )
            cancelled_fulfillments = cur.rowcount

            self.assertEqual(cancelled_fulfillments, 6)

    @patch(
        "microsetta_private_api.repo.perk_fulfillment_repo."
        "create_daklapack_order_internal"
    )
    @patch(
        "microsetta_private_api.repo.perk_fulfillment_repo.send_email"
    )
    def test_check_for_shipping_updates(
        self,
        test_send_email_result,
        test_daklapack_order_result
    ):
        test_send_email_result = True
        test_daklapack_order_result.return_value = {
            "order_address": "wedontcareaboutthis",
            "order_success": True,
            "order_id": DUMMY_ORDER_ID
        }

        # res simulates what comes back from
        # PerkFulfillmentRepo.get_pending_fulfillments()
        res = [self.kit_ftp_id]
        for ftp_id in res:
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
                                       PROJECT_IDS, DUMMY_DAKLAPACK_ORDER,
                                       desc, planned_send_date,
                                       creation_timestamp,
                                       last_polling_timestamp, last_status)

                # call create_daklapack_order
                admin_repo = AdminRepo(t)
                _ = admin_repo.create_daklapack_order(input)

                cur = t.cursor()

                # To simulate a shipped order, we need to update the status,
                # create a kit, and map the kit to the order
                cur.execute(
                    "UPDATE barcodes.daklapack_order "
                    "SET last_polling_status = 'Sent' "
                    "WHERE dak_order_id = %s",
                    (DUMMY_ORDER_ID, )
                )
                cur.execute(
                    "INSERT INTO barcodes.kit ("
                    "kit_uuid, kit_id, outbound_fedex_tracking, box_id"
                    ") VALUES ("
                    "%s, %s, %s, 'ABOX'"
                    ")",
                    (DUMMY_KIT_UUID, DUMMY_KIT_ID, DUMMY_TRACKING)
                )
                cur.execute(
                    "INSERT INTO barcodes.daklapack_order_to_kit ("
                    "dak_order_id, kit_uuid"
                    ") VALUES ("
                    "%s, %s"
                    ")",
                    (DUMMY_ORDER_ID, DUMMY_KIT_UUID)
                )

                pfr = PerkFulfillmentRepo(t)
                _ = pfr.process_pending_fulfillment(ftp_id)

                # Need to do something with this variable to satisfy lint
                self.assertEqual(test_send_email_result, True)

                emails_sent, error_report = pfr.check_for_shipping_updates()

                self.assertEqual(emails_sent, 1)
                self.assertEqual(len(error_report), 0)

    @patch(
        "microsetta_private_api.repo.perk_fulfillment_repo."
        "create_daklapack_order_internal"
    )
    @patch(
        "microsetta_private_api.repo.perk_fulfillment_repo.send_email"
    )
    def test_get_subscription_fulfillments(
            self,
            test_send_email_result,
            test_daklapack_order_result
    ):
        test_send_email_result = True
        # Need to do something with this variable to satisfy lint
        self.assertEqual(test_send_email_result, True)

        test_daklapack_order_result.side_effect = [
            {
                "order_address": "wedontcareaboutthis",
                "order_success": True,
                "order_id": DUMMY_ORDER_ID
            },
            {
                "order_address": "wedontcareaboutthis",
                "order_success": True,
                "order_id": DUMMY_ORDER_ID2
            }
        ]

        # We're going to add a transaction for one subscription.
        # Then we're going to set the first pending fulfillment to be due
        # today so we can observe it as ready for processing.

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

            # create dummy daklapack order object for first shipment
            input = DaklapackOrder(DUMMY_ORDER_ID, submitter_acct,
                                   PROJECT_IDS, DUMMY_DAKLAPACK_ORDER, desc,
                                   planned_send_date, creation_timestamp,
                                   last_polling_timestamp, last_status)

            # call create_daklapack_order
            admin_repo = AdminRepo(t)
            returned_id = admin_repo.create_daklapack_order(input)

            # create dummy daklapack order object for second shipment
            input2 = DaklapackOrder(DUMMY_ORDER_ID2, submitter_acct,
                                    PROJECT_IDS, DUMMY_DAKLAPACK_ORDER2, desc,
                                    planned_send_date, creation_timestamp,
                                    last_polling_timestamp, last_status)

            # call create_daklapack_order
            _ = admin_repo.create_daklapack_order(input2)

            pfr = PerkFulfillmentRepo(t)
            _ = pfr.process_pending_fulfillment(self.sub_ftp_id)

            cur = t.dict_cursor()

            # We need to grab the subscription ID
            cur.execute(
                "SELECT s.subscription_id "
                "FROM campaign.subscriptions s "
                "INNER JOIN campaign.fundrazr_daklapack_orders fdo "
                "ON s.fundrazr_transaction_perk_id = "
                "fdo.fundrazr_transaction_perk_id AND fdo.dak_order_id = %s",
                (returned_id,)
            )
            row = cur.fetchone()
            subscription_id = row['subscription_id']

            # Grab the first two unfilfilled records for the subscription.
            # Given the subscription setup, this will be one FFQ and one kit.
            cur.execute(
                "SELECT fulfillment_id "
                "FROM campaign.subscriptions_fulfillment "
                "WHERE subscription_id = %s AND fulfilled = FALSE "
                "ORDER BY fulfillment_date LIMIT 2",
                (subscription_id,)
            )
            rows = cur.fetchall()
            for row in rows:
                # Update them to be due to fulfill today
                cur.execute(
                    "UPDATE campaign.subscriptions_fulfillment "
                    "SET fulfillment_date = CURRENT_DATE "
                    "WHERE fulfillment_id = %s",
                    (row['fulfillment_id'], )
                )

            # Get pending fulfillments
            pending_ful = pfr.get_subscription_fulfillments()

            # Verify that there are two records
            self.assertEqual(len(pending_ful), 2)

            # Process the pending fulfillments
            for f_id in pending_ful:
                error_list = pfr.process_subscription_fulfillment(f_id)
                self.assertEqual(len(error_list), 0)

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
