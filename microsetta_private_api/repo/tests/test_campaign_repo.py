import unittest
from unittest import skipIf
import datetime
import uuid

from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.repo.campaign_repo import (UserTransaction,
                                                       CampaignRepo,
                                                       FundRazrCampaignRepo)
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.model.campaign import (FundRazrPayment, Item,
                                                   Shipping, FundRazrCampaign)
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
    Item('unseen item', 2, 'unseen item', 100),
]


TRANSACTION_NO_EXISTING_CAMPAIGN = FundRazrPayment(
    '123abc',
    datetime.datetime.now(),
    '14i22',  # this ID exists in fundrazr staging only
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


EMAIL_1 = 'foo@bar.com'
EMAIL_2 = 'wwbhsqo5s9@fi9s6.nzb'  # a valid email stable in the test database
ACCT_ID_1 = 'c979cc9e-a82f-4f53-a456-9fa9be9f52d4'
SRC_ID_1 = ''


# source IDs are constructed during patching and are not stable
# so let's pull one at runtime
with Transaction() as t:
    cur = t.cursor()
    cur.execute("""SELECT id as source_id
                   FROM ag.source
                   WHERE account_id=%s
                   LIMIT 1""",
                (ACCT_ID_1, ))
    SRC_ID_1 = cur.fetchone()[0]


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
                "associated_projects": ["1", ]
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
                "associated_projects": ["1", ]
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
                "associated_projects": ["-1", ]
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

    def test_is_member_by_source(self):
        with Transaction() as t:
            cr = CampaignRepo(t)
            obs = cr.is_member_by_source(ACCT_ID_1, SRC_ID_1,
                                         self.test_campaign_id1)
            self.assertTrue(obs)

            for aid, sid, cid in [(str(uuid.uuid4()), str(uuid.uuid4()),
                                   str(uuid.uuid4())),
                                  (ACCT_ID_1, str(uuid.uuid4()),
                                   str(uuid.uuid4())),
                                  (str(uuid.uuid4()), SRC_ID_1,
                                   str(uuid.uuid4())),
                                  (ACCT_ID_1, SRC_ID_1,
                                   str(uuid.uuid4()))]:
                obs = cr.is_member_by_source(aid, sid, cid)
                self.assertFalse(obs)

    def test_is_member_by_email(self):
        with Transaction() as t:
            cur = t.cursor()
            cur.execute("""INSERT INTO campaign.interested_users
                           (campaign_id, first_name, last_name, email,
                            address_checked, address_valid,
                            converted_to_account)
                           VALUES (%s, 'cool', 'bob', %s,
                                   'N', 'N', 'N')""",
                        (self.test_campaign_id1, EMAIL_1))

            cr = CampaignRepo(t)
            obs = cr.is_member_by_email(EMAIL_1, self.test_campaign_id1)
            self.assertTrue(obs)

            obs = cr.is_member_by_email(EMAIL_2, self.test_campaign_id1)
            self.assertTrue(obs)

            for email, cid in [('foobar@baz.com', self.test_campaign_id1),

                               # this email exists and is stable in the test
                               # database, and is not associated with project
                               # 1
                               ('bsbk(ounxw@)9t30.wid',
                                self.test_campaign_id1),

                               (EMAIL_1, str(uuid.uuid4()))]:
                obs = cr.is_member_by_email(email, cid)
                self.assertFalse(obs)


class FundrazrTransactionTests(unittest.TestCase):
    def setUp(self):
        # setup a few additional variations for get tests
        obj1 = TRANSACTION_NO_SHIPPING.copy()
        obj2 = obj1.copy()
        obj3 = obj1.copy()
        obj4 = obj1.copy()
        obj5 = obj1.copy()
        obj6 = TRANSACTION_ONE_ITEM.copy()

        obj1.transaction_id = 'obj1'
        obj2.transaction_id = 'obj2'
        obj3.transaction_id = 'obj3'
        obj4.transaction_id = 'obj4'
        obj5.transaction_id = 'obj5'
        obj6.transaction_id = 'obj6'

        obj1.created = datetime.datetime(2021, 11, 1)
        obj2.created = datetime.datetime(2021, 10, 1)
        obj3.created = datetime.datetime(2021, 1, 1)
        obj4.created = datetime.datetime(2011, 11, 1)
        obj5.created = datetime.datetime(2015, 11, 1)
        obj6.created = datetime.datetime(2016, 11, 1)

        obj1.contact_email = 'obj1obj2@foo.com'
        obj2.contact_email = 'obj1obj2@foo.com'
        obj3.contact_email = 'obj3@foo.com'
        obj4.contact_email = 'obj4@foo.com'
        obj6.contact_email = 'obj6@foo.com'

        # make obj5 look anonymous
        obj5.contact_email = None
        obj5.phone_number = None

        self.obj1 = obj1
        self.obj2 = obj2
        self.obj3 = obj3
        self.obj4 = obj4
        self.obj5 = obj5
        self.obj6 = obj6

        # ensure the default exists
        self.old_default = FundRazrCampaignRepo._DEFAULT_PROJECT_ASSOCIATION
        FundRazrCampaignRepo._DEFAULT_PROJECT_ASSOCIATION = (1, )

    def tearDown(self):
        FundRazrCampaignRepo._DEFAULT_PROJECT_ASSOCIATION = self.old_default

    def _load_some_transactions(self, r):
        # slight order tweak to ensure the "most recent"
        # is not loaded first or last
        r.add_transaction(self.obj2)
        r.add_transaction(self.obj1)
        r.add_transaction(self.obj3)
        r.add_transaction(self.obj4)
        r.add_transaction(self.obj5)
        r.add_transaction(self.obj6)

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

    @skipIf(SERVER_CONFIG['fundrazr_url'] in ('', 'fundrazr_url_placeholder'),
            "Fundrazr secrets not provided")
    def test_add_transaction_new_campaign(self):
        with Transaction() as t:
            r = UserTransaction(t)
            r.add_transaction(TRANSACTION_NO_EXISTING_CAMPAIGN)
            tid = TRANSACTION_NO_EXISTING_CAMPAIGN.transaction_id
            self._verify_insertion_count_perks(t, tid, 0)

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
            r.add_transaction(TRANSACTION_UNKNOWN_ITEM)
            tid = TRANSACTION_UNKNOWN_ITEM.transaction_id
            self._verify_insertion_count_perks(t, tid, 1)

    def test_most_recent_transaction(self):
        with Transaction() as t:
            r = UserTransaction(t)
            self._load_some_transactions(r)
            obs = r.most_recent_transaction()
            exp = self.obj1
            self._payment_equal([obs, ], [exp, ])

    def test_get_transactions_by_date(self):
        with Transaction() as t:
            r = UserTransaction(t)
            self._load_some_transactions(r)

            # obj5 is not included as it is anonymous, and the anonymous
            # flag is not set
            obs = r.get_transactions(before=datetime.datetime(2021, 12, 1))
            exp = [self.obj1, self.obj2, self.obj3, self.obj6, self.obj4]
            self._payment_equal(obs, exp)

            # obj5 is not included as it is anonymous, and the anonymous
            # flag is not set
            obs = r.get_transactions(before=datetime.datetime(2021, 10, 1))
            exp = [self.obj3, self.obj6, self.obj4]
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
            exp = [self.obj1, self.obj2, self.obj3, self.obj6, self.obj5,
                   self.obj4]
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

            for obj in [self.obj1, self.obj2, self.obj3, self.obj4, self.obj6]:
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


class FundrazrCampaignTests(unittest.TestCase):
    def setUp(self):
        self.campaign_with_item = FundRazrCampaign('c1', 'test1', 'usd',
                                                   Item('xyz', 0, 'i1', 10),
                                                   None)
        self.campaign_without_item = FundRazrCampaign('c2', 'test2', 'usd',
                                                      None, None)
        self.perk = Item('zyx', 0, 'i2', 5)

    def test_campaign_exists_doesnt_exist(self):
        with Transaction() as t:
            c = FundRazrCampaignRepo(t)
            self.assertFalse(c.campaign_exists('foobar'))

    def test_campaign_exists(self):
        with Transaction() as t:
            c = FundRazrCampaignRepo(t)
            c.insert_campaign(self.campaign_with_item, [1, ])
            self.assertTrue(c.campaign_exists('c1'))

    def test_item_exists_doesnt_exist(self):
        with Transaction() as t:
            c = FundRazrCampaignRepo(t)
            c.insert_campaign(self.campaign_with_item, [1, ])
            self.assertFalse(c.item_exists('c1', 'notpresent'))

    def test_item_exists(self):
        with Transaction() as t:
            c = FundRazrCampaignRepo(t)
            c.insert_campaign(self.campaign_with_item, [1, ])
            self.assertTrue(c.item_exists('c1', 'i1'))

    def test_insert_campaign_with_item(self):
        with Transaction() as t:
            c = FundRazrCampaignRepo(t)
            c.insert_campaign(self.campaign_with_item, [1, ])
            self.assertTrue(c.campaign_exists('c1'))
            self.assertTrue(c.item_exists('c1', 'i1'))

    def test_insert_campaign_without_item(self):
        with Transaction() as t:
            c = FundRazrCampaignRepo(t)
            c.insert_campaign(self.campaign_without_item, [1, ])
            self.assertTrue(c.campaign_exists('c2'))

    def test_add_perk_to_campaign(self):
        with Transaction() as t:
            c = FundRazrCampaignRepo(t)
            c.insert_campaign(self.campaign_without_item, [1, ])
            c.add_perk_to_campaign('c2', self.perk)
            self.assertTrue(c.item_exists('c2', 'i2'))


if __name__ == '__main__':
    unittest.main()
