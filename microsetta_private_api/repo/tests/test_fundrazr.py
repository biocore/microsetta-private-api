import unittest
from microsetta_private_api.model.fundrazr import Payment, Item, Shipping
from microsetta_private_api.model.address import Address
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.fundrazr import (Fundrazr,
                                                  DuplicateTransaction,
                                                  UnknownItem)


ADDRESS1 = Address(
    '123 foo',
    'baz city',
    'CA',
    '92111',
    'US')


SHIPPING1 = Shipping('foo', 'bar', ADDRESS1)


CLAIMED_ITEMS1 = [
    Item('Find Out Who’s In Your Gut', 2, '0I5n8'),
]


CLAIMED_ITEMS2 = [
    Item('Find Out Who’s In Your Gut', 2, '0I5n8'),
    Item("See What You're Sharing", 1, '6I5fd')
]


CLAIMED_ITEMS3 = [
    Item('baditem', 2, '0I5n8'),
]


TRANSACTION_ONE_ITEM = Payment(
    '123abc',
    1365172131,
    '31l0S2',
    100,
    80,
    'usd',
    'completed',
    'foo',
    'bar',
    'foo bar',
    'foo@bar.com',
    'baz@bar.com',
    'paypal',
    True,
    'coolcool',
    '123456789',
    SHIPPING1,
    CLAIMED_ITEMS1)


TRANSACTION_TWO_ITEMS = Payment(
    '123abc',
    1365172131,
    '31l0S2',
    100,
    80,
    'usd',
    'completed',
    'foo',
    'bar',
    'foo bar',
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
    1365172131,
    '31l0S2',
    100,
    80,
    'usd',
    'completed',
    'foo',
    'bar',
    'foo bar',
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
    1365172131,
    '31l0S2',
    100,
    80,
    'usd',
    'completed',
    'foo',
    'bar',
    'foo bar',
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
    1365172131,
    '31l0S2',
    100,
    80,
    'usd',
    'completed',
    'foo',
    'bar',
    'foo bar',
    'foo@bar.com',
    'baz@bar.com',
    'paypal',
    True,
    'coolcool',
    '123456789',
    None,
    None)


class FundrazrTests(unittest.TestCase):
    def test_add_transaction(self):
        with Transaction() as t:
            r = Fundrazr(t)
            r.add_transaction(TRANSACTION_ONE_ITEM)

            cur = t.cursor()
            cur.execute("""SELECT id
                           FROM barcodes.fundrazr_transaction
                           WHERE id='123abc'""")
            res = cur.fetchone()
            self.assertEqual(res[0], '123abc')

    def test_add_transaction_duplicate(self):
        with Transaction() as t:
            r = Fundrazr(t)
            r.add_transaction(TRANSACTION_ONE_ITEM)

            with self.assertRaises(DuplicateTransaction):
                r.add_transaction(TRANSACTION_ONE_ITEM)

    def test_add_transaction_no_perk(self):
        with Transaction() as t:
            r = Fundrazr(t)
            r.add_transaction(TRANSACTION_NO_ITEMS)

            cur = t.cursor()
            cur.execute("""SELECT id
                           FROM barcodes.fundrazr_transaction
                           WHERE id='123abc'""")
            res = cur.fetchone()
            self.assertEqual(res[0], '123abc')

    def test_add_transaction_unknown_item(self):
        with Transaction() as t:
            r = Fundrazr(t)
            with self.assertRaises(UnknownItem):
                r.add_transaction(TRANSACTION_UNKNOWN_ITEM)

    def test_update_transaction_address(self):
        pass

    def test_set_transaction_status(self):
        # received, valid-address, invalid-address, shipment-requested
        self.fail()

    def test_udpate_transaction_other(self):
        self.fail()

    def test_get_transactions_by_date(self):
        pass

    def test_get_transactions_by_status(self):
        pass

    def test_get_transaction_by_id(self):
        pass

    def test_get_transaction_by_email(self):
        pass


if __name__ == '__main__':
    unittest.main()
