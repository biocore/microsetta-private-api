import unittest
import psycopg2
from microsetta_private_api.model.fundrazr import Payment, Item, Shipping
from microsetta_private_api.model.address import Address
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.fundrazr import (FundRazr,
                                                  UnknownItem,
                                                  InvalidStatusChange)
import datetime


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


TRANSACTION_ONE_ITEM = Payment(
    '123abc',
    datetime.datetime.now(),
    '31l0S2',
    100.,
    80.,
    'usd',
    'completed',
    'foo',
    'bar',
    'foo@bar.com',
    'baz@bar.com',
    'paypal',
    True,
    'coolcool',
    '123456789',
    SHIPPING1,
    CLAIMED_ITEMS1)
TRANSACTION_ONE_ITEM_ALT_ADDRESS = Payment(
    '123abc',
    datetime.datetime.now(),
    '31l0S2',
    100.,
    80.,
    'usd',
    'completed',
    'foo',
    'bar',
    'foo@bar.com',
    'baz@bar.com',
    'paypal',
    True,
    'coolcool',
    '123456789',
    SHIPPING2,
    CLAIMED_ITEMS1)


TRANSACTION_TWO_ITEMS = Payment(
    '123abc',
    datetime.datetime.now(),
    '31l0S2',
    100.,
    80.,
    'usd',
    'completed',
    'foo',
    'bar',
    'foo@bar.com',
    'baz@bar.com',
    'paypal',
    True,
    'coolcool',
    '123456789',
    SHIPPING1,
    CLAIMED_ITEMS2)


TRANSACTION_UNKNOWN_ITEM = Payment(
    '123abc',
    datetime.datetime.now(),
    '31l0S2',
    100.,
    80.,
    'usd',
    'completed',
    'foo',
    'bar',
    'foo@bar.com',
    'baz@bar.com',
    'paypal',
    True,
    'coolcool',
    '123456789',
    SHIPPING1,
    CLAIMED_ITEMS3)


TRANSACTION_NO_ITEMS = Payment(
    '123abc',
    datetime.datetime.now(),
    '31l0S2',
    100.,
    80.,
    'usd',
    'completed',
    'foo',
    'bar',
    'foo@bar.com',
    'baz@bar.com',
    'paypal',
    True,
    'coolcool',
    '123456789',
    SHIPPING1,
    None)


TRANSACTION_NO_SHIPPING = Payment(
    '123abc',
    datetime.datetime.now(),
    '31l0S2',
    100.,
    80.,
    'usd',
    'completed',
    'foo',
    'bar',
    'foo@bar.com',
    'baz@bar.com',
    'paypal',
    True,
    'coolcool',
    '123456789',
    None,
    None)


class FundrazrTests(unittest.TestCase):
    def setUp(self):
        # setup a few additional variations for get tests
        obj1 = TRANSACTION_NO_SHIPPING.copy()
        obj2 = obj1.copy()
        obj3 = obj1.copy()
        obj4 = obj1.copy()

        obj1.transaction_id = 'obj1'
        obj2.transaction_id = 'obj2'
        obj3.transaction_id = 'obj3'
        obj4.transaction_id = 'obj4'

        obj1.created = datetime.datetime(2021, 11, 1)
        obj2.created = datetime.datetime(2021, 10, 1)
        obj3.created = datetime.datetime(2021, 1, 1)
        obj4.created = datetime.datetime(2011, 11, 1)

        obj1.contact_email = 'obj1obj2@foo.com'
        obj2.contact_email = 'obj1obj2@foo.com'
        obj3.contact_email = 'obj3@foo.com'
        obj4.contact_email = 'obj4@foo.com'

        obj1.tmi_status = FundRazr.TMI_STATUS_RECEIVED
        obj2.tmi_status = FundRazr.TMI_STATUS_RECEIVED
        obj3.tmi_status = FundRazr.TMI_STATUS_RECEIVED
        obj4.tmi_status = FundRazr.TMI_STATUS_RECEIVED

        self.obj1 = obj1
        self.obj2 = obj2
        self.obj3 = obj3
        self.obj4 = obj4

    def _load_some_transactions(self, r):
        r.add_transaction(self.obj1)
        r.add_transaction(self.obj2)
        r.add_transaction(self.obj3)
        r.add_transaction(self.obj4)

    def _verify_insertion_count_perks(self, t, tid, expected_count):
        cur = t.cursor()
        cur.execute("""SELECT id
                       FROM campaign.fundrazr_transaction
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
            r = FundRazr(t)
            r.add_transaction(TRANSACTION_ONE_ITEM)
            tid = TRANSACTION_ONE_ITEM.transaction_id
            self._verify_insertion_count_perks(t, tid, 1)

    def test_add_transaction_duplicate(self):
        with Transaction() as t:
            r = FundRazr(t)
            r.add_transaction(TRANSACTION_ONE_ITEM)

            with self.assertRaises(psycopg2.errors.UniqueViolation):
                r.add_transaction(TRANSACTION_ONE_ITEM)

    def test_add_transaction_no_perk(self):
        with Transaction() as t:
            r = FundRazr(t)
            r.add_transaction(TRANSACTION_NO_ITEMS)
            tid = TRANSACTION_NO_ITEMS.transaction_id
            self._verify_insertion_count_perks(t, tid, 0)

    def test_add_transaction_multiple_perk(self):
        with Transaction() as t:
            r = FundRazr(t)
            r.add_transaction(TRANSACTION_TWO_ITEMS)
            tid = TRANSACTION_TWO_ITEMS.transaction_id
            self._verify_insertion_count_perks(t, tid, 2)

    def test_add_transaction_unknown_item(self):
        with Transaction() as t:
            r = FundRazr(t)
            with self.assertRaises(UnknownItem):
                r.add_transaction(TRANSACTION_UNKNOWN_ITEM)

    def test_update_transaction_address(self):
        with Transaction() as t:
            r = FundRazr(t)
            r.add_transaction(TRANSACTION_ONE_ITEM)
            r.update_transaction(TRANSACTION_ONE_ITEM_ALT_ADDRESS)

            cur = t.cursor()
            cur.execute("""SELECT shipping_first_name, shipping_last_name
                           FROM campaign.fundrazr_transaction
                           WHERE id=%s""",
                        (TRANSACTION_ONE_ITEM.transaction_id, ))
            first, last = cur.fetchone()
            self.assertEqual(first, SHIPPING2.first_name)
            self.assertEqual(last, SHIPPING2.last_name)

    def test_set_transaction_status(self):
        with Transaction() as t:
            r = FundRazr(t)
            r.add_transaction(TRANSACTION_ONE_ITEM)

            with self.assertRaises(InvalidStatusChange):
                r.set_transaction_status(TRANSACTION_ONE_ITEM,
                                         FundRazr.TMI_STATUS_SHIPMENT_REQUESTED)  # noqa

            r.set_transaction_status(TRANSACTION_ONE_ITEM,
                                     FundRazr.TMI_STATUS_INVALID_ADDRESS)

            with self.assertRaises(InvalidStatusChange):
                # We cannot revert to received
                r.set_transaction_status(TRANSACTION_ONE_ITEM,
                                         FundRazr.TMI_STATUS_RECEIVED)

            with self.assertRaises(InvalidStatusChange):
                r.set_transaction_status(TRANSACTION_ONE_ITEM,
                                         FundRazr.TMI_STATUS_SHIPMENT_REQUESTED)  # noqa

            r.set_transaction_status(TRANSACTION_ONE_ITEM,
                                     FundRazr.TMI_STATUS_VALID_ADDRESS)

            with self.assertRaises(InvalidStatusChange):
                # We cannot go from valid to invalid address
                r.set_transaction_status(TRANSACTION_ONE_ITEM,
                                         FundRazr.TMI_STATUS_INVALID_ADDRESS)

            with self.assertRaises(InvalidStatusChange):
                # We cannot revert to received
                r.set_transaction_status(TRANSACTION_ONE_ITEM,
                                         FundRazr.TMI_STATUS_RECEIVED)

            final = r.set_transaction_status(TRANSACTION_ONE_ITEM,
                                             FundRazr.TMI_STATUS_SHIPMENT_REQUESTED)  # noqa

            self.assertEqual(final.tmi_status,
                             FundRazr.TMI_STATUS_SHIPMENT_REQUESTED)

    def test_get_transactions_by_date(self):
        with Transaction() as t:
            r = FundRazr(t)
            self._load_some_transactions(r)

            obs = r.get_transactions(before=datetime.datetime(2021, 12, 1))
            exp = [self.obj1, self.obj2, self.obj3, self.obj4]
            self.assertEqual(obs, exp)

            obs = r.get_transactions(before=datetime.datetime(2021, 10, 1))
            exp = [self.obj3, self.obj4]
            self.assertEqual(obs, exp)

            obs = r.get_transactions(before=datetime.datetime(2021, 10, 15),
                                     after=datetime.datetime(2020, 12, 1))
            exp = [self.obj2, self.obj3]
            self.assertEqual(obs, exp)

    def test_get_transactions_by_status(self):
        with Transaction() as t:
            r = FundRazr(t)
            self._load_some_transactions(r)
            obs = r.get_transactions(tmi_status=FundRazr.TMI_STATUS_RECEIVED)
            self.assertEqual(obs, [self.obj1, self.obj2, self.obj3, self.obj4])

            va = FundRazr.TMI_STATUS_VALID_ADDRESS
            new_obj2 = r.set_transaction_status(self.obj2, va)
            obs = r.get_transactions(tmi_status=FundRazr.TMI_STATUS_RECEIVED)
            self.assertEqual(obs, [self.obj1, self.obj3, self.obj4])
            obs = r.get_transactions(tmi_status=va)
            self.assertEqual(obs, [new_obj2, ])

    def test_get_transaction_by_id(self):
        with Transaction() as t:
            r = FundRazr(t)
            self._load_some_transactions(r)

            for obj in [self.obj1, self.obj2, self.obj3, self.obj4]:
                obs = r.get_transactions(transaction_id=obj.transaction_id)
                self.assertEqual(obs, [obj, ])

    def test_get_transaction_by_email(self):
        with Transaction() as t:
            r = FundRazr(t)
            self._load_some_transactions(r)

            obs = r.get_transactions(contact_email=self.obj1.contact_email)
            exp = [self.obj1, self.obj2]
            self.assertEqual(obs, exp)

            obs = r.get_transactions(contact_email=self.obj2.contact_email)
            exp = [self.obj1, self.obj2]
            self.assertEqual(obs, exp)

            obs = r.get_transactions(contact_email=self.obj3.contact_email)
            exp = [self.obj3, ]
            self.assertEqual(obs, exp)

            obs = r.get_transactions(contact_email=self.obj4.contact_email)
            exp = [self.obj4, ]
            self.assertEqual(obs, exp)


if __name__ == '__main__':
    unittest.main()
