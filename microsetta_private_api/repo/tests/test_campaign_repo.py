import unittest
import datetime

from microsetta_private_api.repo.campaign_repo import (UserTransaction,
                                                       CampaignRepo,
                                                       UnknownItem)
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.model.campaign import (FundRazrPayment, Item,
                                                   Shipping)
from microsetta_private_api.model.address import Address

from psycopg2.errors import UniqueViolation, ForeignKeyViolation


ADDRESS1 = Address(
    '123 foo',
    'baz city',
    'CA',
    '92111',
    'US')
ADDRESS2 = Address(
    '123 bar',
    'okay city',
    'CA',
    '92111',
    'US')


SHIPPING1 = Shipping('foo', 'bar', ADDRESS1)
SHIPPING2 = Shipping('baz', 'bing', ADDRESS2)


CLAIMED_ITEMS1 = [
    Item('Find Out Who’s In Your Gut', 2, '0I5n8'),
]


CLAIMED_ITEMS2 = [
    Item('Find Out Who’s In Your Gut', 2, '0I5n8'),
    Item("See What You're Sharing", 1, '6I5fd')
]


CLAIMED_ITEMS3 = [
    Item('baditem', 2, 'baditem'),
]


TRANSACTION_ONE_ITEM = FundRazrPayment(
    '123abc',
    datetime.datetime.now(),
    '31l0S2',
    100.,
    80.,
    'usd',
    'foo',
    'bar',
    'paypal',
    True,
    None,
    'coolcool',
    '123456789',
    SHIPPING1,
    CLAIMED_ITEMS1,
    payer_email='foo@bar.com',
    contact_email='baz@bar.com')


TRANSACTION_ONE_ITEM_ALT_ADDRESS = FundRazrPayment(
    '123abc',
    datetime.datetime.now(),
    '31l0S2',
    100.,
    80.,
    'usd',
    'foo',
    'bar',
    'paypal',
    True,
    None,
    'coolcool',
    '123456789',
    SHIPPING2,
    CLAIMED_ITEMS1,
    payer_email='foo@bar.com',
    contact_email='baz@bar.com')


TRANSACTION_TWO_ITEMS = FundRazrPayment(
    '123abc',
    datetime.datetime.now(),
    '31l0S2',
    100.,
    80.,
    'usd',
    'foo',
    'bar',
    'paypal',
    True,
    None,
    'coolcool',
    '123456789',
    SHIPPING1,
    CLAIMED_ITEMS2,
    payer_email='foo@bar.com',
    contact_email='baz@bar.com')


TRANSACTION_UNKNOWN_ITEM = FundRazrPayment(
    '123abc',
    datetime.datetime.now(),
    '31l0S2',
    100.,
    80.,
    'usd',
    'foo',
    'bar',
    'paypal',
    True,
    None,
    'coolcool',
    '123456789',
    SHIPPING1,
    CLAIMED_ITEMS3,
    payer_email='foo@bar.com',
    contact_email='baz@bar.com')


TRANSACTION_NO_ITEMS = FundRazrPayment(
    '123abc',
    datetime.datetime.now(),
    '31l0S2',
    100.,
    80.,
    'usd',
    'foo',
    'bar',
    'paypal',
    True,
    None,
    'coolcool',
    '123456789',
    SHIPPING1,
    None,
    payer_email='foo@bar.com',
    contact_email='baz@bar.com')


TRANSACTION_NO_SHIPPING = FundRazrPayment(
    '123abc',
    datetime.datetime.now(),
    '31l0S2',
    100.,
    80.,
    'usd',
    'foo',
    'bar',
    'paypal',
    True,
    None,
    'coolcool',
    '123456789',
    None,
    None,
    payer_email='foo@bar.com',
    contact_email='baz@bar.com')


TRANSACTION_ANONYMOUS = FundRazrPayment(
    '123abc',
    datetime.datetime.now(),
    '31l0S2',
    100.,
    80.,
    'usd',
    'foo',
    'bar',
    'paypal',
    True,
    None,
    'coolcool',
    None,
    None,
    None,
    payer_email=None,
    contact_email=None)


class CampaignRepoTests(unittest.TestCase):
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

    def test_create_campaign_valid(self):
        # create a campaign with minimal required fields
        with Transaction() as t:
            new_campaign = {
                "title": "Unique Campaign Name",
                "associated_projects": "1"
            }
            campaign_repo = CampaignRepo(t)
            obs = campaign_repo.create_campaign(**new_campaign)
            self.assertTrue(obs is not None)
            t.rollback()

    def test_create_campaign_invalid(self):
        # test to verify unique constraint on title
        with Transaction() as t:
            duplicate_campaign = {
                "title": "Test Campaign",
                "associated_projects": "1"
            }
            campaign_repo = CampaignRepo(t)
            with self.assertRaises(UniqueViolation):
                campaign_repo.create_campaign(**duplicate_campaign)

        # test to verify requirement of associated_projects
        with Transaction() as t:
            campaign_no_projects = {
                "title": "Unique Campaign Name"
            }
            campaign_repo = CampaignRepo(t)
            with self.assertRaises(KeyError):
                campaign_repo.create_campaign(**campaign_no_projects)

        # test to verify that associated_projects must be valid project_ids
        with Transaction() as t:
            campaign_bad_projects = {
                "title": "Unique Campaign Name",
                "associated_projects": "-1"
            }
            campaign_repo = CampaignRepo(t)
            with self.assertRaises(ForeignKeyViolation):
                campaign_repo.create_campaign(**campaign_bad_projects)

    def test_get_campaign_by_id_valid(self):
        # verify that it does not return None when using valid campaign_id
        with Transaction() as t:
            campaign_repo = CampaignRepo(t)
            obs = campaign_repo.get_campaign_by_id(self.test_campaign_id1)
            self.assertTrue(obs is not None)

    def test_get_campaign_by_id_invalid(self):
        # verify that it returns None when using an invalid campaign_id
        with Transaction() as t:
            campaign_repo = CampaignRepo(t)
            obs = campaign_repo.get_campaign_by_id('INVALID_ID')
            self.assertEqual(obs, None)


class FundrazrTransactionTests(unittest.TestCase):
    def setUp(self):
        # setup a few additional variations for get tests
        obj1 = TRANSACTION_NO_SHIPPING.copy()
        obj2 = obj1.copy()
        obj3 = obj1.copy()
        obj4 = obj1.copy()
        obj5 = obj1.copy()

        obj1.transaction_id = 'obj1'
        obj2.transaction_id = 'obj2'
        obj3.transaction_id = 'obj3'
        obj4.transaction_id = 'obj4'
        obj5.transaction_id = 'obj5'

        obj1.created = datetime.datetime(2021, 11, 1)
        obj2.created = datetime.datetime(2021, 10, 1)
        obj3.created = datetime.datetime(2021, 1, 1)
        obj4.created = datetime.datetime(2011, 11, 1)
        obj5.created = datetime.datetime(2015, 11, 1)

        obj1.contact_email = 'obj1obj2@foo.com'
        obj2.contact_email = 'obj1obj2@foo.com'
        obj3.contact_email = 'obj3@foo.com'
        obj4.contact_email = 'obj4@foo.com'
        obj5.contact_email = None
        obj5.phone_number = None

        self.obj1 = obj1
        self.obj2 = obj2
        self.obj3 = obj3
        self.obj4 = obj4
        self.obj5 = obj5

    def _load_some_transactions(self, r):
        r.add_transaction(self.obj1)
        r.add_transaction(self.obj2)
        r.add_transaction(self.obj3)
        r.add_transaction(self.obj4)
        r.add_transaction(self.obj5)

    def _verify_insertion_count_perks(self, t, tid, expected_count):
        cur = t.cursor()
        cur.execute("""SELECT id
                       FROM campaign.transaction
                       WHERE id=%s""",
                    (tid, ))
        res = cur.fetchone()
        self.assertEqual(res[0], tid)

        cur.execute("""SELECT COUNT(*)
                       FROM campaign.fundrazr_transaction_perk
                       WHERE transaction_id=%s""",
                    (tid, ))
        res = cur.fetchall()
        self.assertEqual(res, [(expected_count, ), ])

    def test_add_transaction(self):
        with Transaction() as t:
            r = UserTransaction(t)
            r.add_transaction(TRANSACTION_ONE_ITEM)
            tid = TRANSACTION_ONE_ITEM.transaction_id
            self._verify_insertion_count_perks(t, tid, 1)

    def test_add_transaction_anonymous(self):
        with Transaction() as t:
            r = UserTransaction(t)
            r.add_transaction(TRANSACTION_ANONYMOUS)
            tid = TRANSACTION_ANONYMOUS.transaction_id
            self._verify_insertion_count_perks(t, tid, 0)

    def test_add_transaction_duplicate(self):
        with Transaction() as t:
            r = UserTransaction(t)
            r.add_transaction(TRANSACTION_ONE_ITEM)

            with self.assertRaises(UniqueViolation):
                r.add_transaction(TRANSACTION_ONE_ITEM)

    def test_add_transaction_no_perk(self):
        with Transaction() as t:
            r = UserTransaction(t)
            r.add_transaction(TRANSACTION_NO_ITEMS)
            tid = TRANSACTION_NO_ITEMS.transaction_id
            self._verify_insertion_count_perks(t, tid, 0)

    def test_add_transaction_multiple_perk(self):
        with Transaction() as t:
            r = UserTransaction(t)
            r.add_transaction(TRANSACTION_TWO_ITEMS)
            tid = TRANSACTION_TWO_ITEMS.transaction_id
            self._verify_insertion_count_perks(t, tid, 2)

    def test_add_transaction_unknown_item(self):
        with Transaction() as t:
            r = UserTransaction(t)
            with self.assertRaises(UnknownItem):
                r.add_transaction(TRANSACTION_UNKNOWN_ITEM)

    def test_get_transactions_by_date(self):
        with Transaction() as t:
            r = UserTransaction(t)
            self._load_some_transactions(r)

            obs = r.get_transactions(before=datetime.datetime(2021, 12, 1))
            exp = [self.obj1, self.obj2, self.obj3, self.obj4]
            self._payment_equal(obs, exp)

            obs = r.get_transactions(before=datetime.datetime(2021, 10, 1))
            exp = [self.obj3, self.obj4]
            self._payment_equal(obs, exp)

            obs = r.get_transactions(before=datetime.datetime(2021, 10, 15),
                                     after=datetime.datetime(2020, 12, 1))
            exp = [self.obj2, self.obj3]
            self._payment_equal(obs, exp)

    def test_get_transactions_with_anonymous(self):
        with Transaction() as t:
            r = UserTransaction(t)
            self._load_some_transactions(r)

            obs = r.get_transactions(include_anonymous=True)
            exp = [self.obj1, self.obj2, self.obj3, self.obj5, self.obj4]
            self._payment_equal(obs, exp)

    def _payment_equal(self, obs, exp):
        # ignore the interested_user_id as it's made on insertion
        # and has db enforcement
        for o in obs:
            o.interested_user_id = None
        self.assertEqual(obs, exp)

    def test_get_transaction_by_id(self):
        with Transaction() as t:
            r = UserTransaction(t)
            self._load_some_transactions(r)

            for obj in [self.obj1, self.obj2, self.obj3, self.obj4]:
                obs = r.get_transactions(transaction_id=obj.transaction_id)
                self._payment_equal(obs, [obj, ])

    def test_get_transaction_by_email(self):
        with Transaction() as t:
            r = UserTransaction(t)
            self._load_some_transactions(r)

            obs = r.get_transactions(email=self.obj1.contact_email)
            exp = [self.obj1, self.obj2]
            self._payment_equal(obs, exp)

            obs = r.get_transactions(email=self.obj2.contact_email)
            exp = [self.obj1, self.obj2]
            self._payment_equal(obs, exp)

            obs = r.get_transactions(email=self.obj3.contact_email)
            exp = [self.obj3, ]
            self._payment_equal(obs, exp)

            obs = r.get_transactions(email=self.obj4.contact_email)
            exp = [self.obj4, ]
            self._payment_equal(obs, exp)


if __name__ == '__main__':
    unittest.main()
