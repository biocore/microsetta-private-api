from unittest import TestCase, main
from datetime import datetime
from microsetta_private_api.model.campaign import Payment, FundRazrCampaign


NO_SHIPPING = {
  "created": 1586423564,
  "campaign_id": "4Tqx5",
  "amount": 20,
  "net_amount": 18.32,
  "currency": "usd",
  "status": "completed",
  "payer_name": "a donation",
  "payer_first_name": "a",
  "payer_last_name": "donation",
  "payer_email": "a@donation.com",
  "transaction_id": "22334455",
  "account": "paypal",
  "contact_email": "a@donation.com",
  "subscribe_to_updates": True,
  "id": "5241564",
  "object": "payment"
}


NO_ITEMS = {
  "created": 1586387811,
  "campaign_id": "4Tqx5",
  "amount": 25,
  "net_amount": 22.97,
  "currency": "usd",
  "status": "completed",
  "payer_name": "a person",
  "payer_first_name": "a",
  "payer_last_name": "person",
  "payer_email": "person@a.com",
  "transaction_id": "123123",
  "account": "paypal",
  "contact_email": "person@a.com",
  "subscribe_to_updates": True,
  "phone_number": "5551231233",
  "shipping_address": {
    "first_name": "person",
    "last_name": "a",
    "street": "321 foo place",
    "city": "San Diego",
    "country": "US",
    "state": "CA",
    "postal_code": "92100"
  },
  "id": "5241253",
  "object": "payment"
}

ANONYMOUS = {
  "created": 1586389911,
  "campaign_id": "4Tqx5",
  "amount": 25,
  "net_amount": 22.97,
  "currency": "usd",
  "status": "completed",
  "payer_name": "anonymous",
  "payer_first_name": "anonymous",
  "payer_last_name": "",
  "transaction_id": "123123",
  "account": "paypal",
  "subscribe_to_updates": True,
  "phone_number": "5551231233",
  "id": "5241253",
  "object": "payment"
}


ONE_ITEM = {
  "created": 1584372532,
  "campaign_id": "4Tqx5",
  "amount": 520,
  "net_amount": 478.62,
  "currency": "usd",
  "status": "completed",
  "payer_name": "many sample",
  "payer_first_name": "many",
  "payer_last_name": "sample",
  "payer_email": "many@sample.com",
  "transaction_id": "321D123",
  "account": "paypal",
  "claimed_items": [
    {
      "title": "Microbes for Five",
      "image_url": "32c1b3276e054b089541bcc655f1a4af.png",
      "price": 470,
      "quantity": 1,
      "id": "dGKB5",
      "object": "claimed_item"
    }
  ],
  "contact_email": "many@sample.com",
  "subscribe_to_updates": True,
  "phone_number": "123-123-5432",
  "shipping_address": {
    "first_name": "many",
    "last_name": "sample",
    "street": "1122 wooplace",
    "city": "London",
    "country": "GB",
    "state": "Westminster",
    "postal_code": "aabbcc"
  },
  "id": "5215138",
  "object": "payment"
}


MULTIPLE_ITEMS = {
  "created": 1584479415,
  "campaign_id": "4Tqx5",
  "amount": 372.25,
  "net_amount": 346.27,
  "currency": "usd",
  "status": "completed",
  "payer_name": "foo bar",
  "payer_first_name": "foo",
  "payer_last_name": "bar",
  "payer_email": "foo@bar.com",
  "transaction_id": "1L234",
  "account": "paypal",
  "message": "cool",
  "claimed_items": [
    {
      "title": "USPS Priority Mail Shipping",
      "image_url": "82e38ff01c704c5a862322b22be667ff.jpg",
      "price": 6.45,
      "quantity": 5,
      "id": "bBbqf",
      "object": "claimed_item"
    },
    {
      "title": "Microbes For Two: See What You\u2019re Sharing",
      "image_url": "3592b87750064a89a04520d7b4af7df2.jpg",
      "price": 190,
      "quantity": 1,
      "id": "62bu7",
      "object": "claimed_item"
    },
    {
      "title": "ASD-Cohort Parent",
      "image_url": "72c795da6a7149ae87c91ba072669a84.jpg",
      "price": 75,
      "quantity": 2,
      "id": "65404",
      "object": "claimed_item"
    }
  ],
  "contact_email": "foo@bar.com",
  "subscribe_to_updates": True,
  "phone_number": "1235555555",
  "shipping_address": {
    "first_name": "foo",
    "last_name": "bar",
    "company_name": "sweet",
    "street": "123 place st",
    "city": "San Diego",
    "country": "US",
    "state": "CA",
    "postal_code": "92100"
  },
  "id": "11111",
  "object": "payment"
}


CAMPAIGN_WITH_ITEMS = {
    "url": "a place",
    "title": "American Gut",
    "introduction": "words and words",
    "image_url": "stuff",
    "location": {
      "city": "cool",
      "country": "ca",
      "state": "BC",
      "latitude": 49.2612,
      "longitude": -123.1139
    },
    "category": "community",
    "campaign_type": "standard",
    "type": "kia",
    "currency": "usd",
    "status": "active",
    "items": [
      {
        "title": "foobar",
        "description": "stuff",
        "image_url": "things",
        "price": 180,
        "claimed": 1,
        "id": "a2uQa",
        "object": "item"
      }
        ],
    "stats": {
        "total_raised": 714,
        "contribution_count": 5,
        "comment_count": 0,
        "update_count": 0
    },
    "id": "c4NG5",
    "object": "campaign"
}


CAMPAIGN_NO_ITEMS = {
    "url": "no place",
    "title": "not American Gut",
    "introduction": "words and words",
    "image_url": "stuff",
    "location": {
      "city": "cool",
      "country": "ca",
      "state": "BC",
      "latitude": 49.2612,
      "longitude": -123.1139
    },
    "category": "community",
    "campaign_type": "standard",
    "type": "kia",
    "currency": "usd",
    "status": "active",
    "stats": {
        "total_raised": 714,
        "contribution_count": 5,
        "comment_count": 0,
        "update_count": 0
    },
    "id": "c4NGxxx",
    "object": "campaign"
}


class FundrazrPaymentTests(TestCase):
    def test_order_with_one_item(self):
        obs = Payment.from_api(**ONE_ITEM)
        self.assertEqual(obs.shipping_address.first_name, 'many')
        self.assertEqual(obs.shipping_address.last_name, 'sample')
        self.assertEqual(obs.shipping_address.address.street, '1122 wooplace')
        self.assertEqual(len(obs.claimed_items), 1)
        self.assertEqual(obs.claimed_items[0].title, 'Microbes for Five')
        self.assertEqual(obs.claimed_items[0].quantity, 1)
        self.assertEqual(obs.claimed_items[0].id, 'dGKB5')

    def test_order_no_shipping(self):
        obs = Payment.from_api(**NO_SHIPPING)
        tz = Payment._TZ_US_PACIFIC
        self.assertEqual(obs.created, datetime.fromtimestamp(1586423564, tz))
        self.assertEqual(obs.shipping_address, None)
        self.assertEqual(obs.claimed_items, [])

    def test_order_with_no_items(self):
        obs = Payment.from_api(**NO_ITEMS)
        self.assertEqual(obs.shipping_address.first_name, 'person')
        self.assertEqual(obs.claimed_items, [])

    def test_anonymous_order(self):
        obs = Payment.from_api(**ANONYMOUS)
        self.assertEqual(obs.payer_first_name, 'anonymous')
        self.assertEqual(obs.claimed_items, [])

    def test_order_with_multiple_items(self):
        obs = Payment.from_api(**MULTIPLE_ITEMS)
        self.assertEqual(len(obs.claimed_items), 3)
        self.assertEqual(obs.claimed_items[0].title,
                         'USPS Priority Mail Shipping')
        self.assertEqual(obs.claimed_items[0].quantity, 5)

    def test_copy(self):
        a = Payment.from_api(**ONE_ITEM)
        b = a.copy()
        self.assertEqual(a, b)
        self.assertNotEqual(id(a), id(b))
        self.assertNotEqual(id(a.claimed_items), id(b.claimed_items))
        self.assertNotEqual(id(a.shipping_address), id(b.shipping_address))


class FundrazrCampaignTests(TestCase):
    def test_campaign_with_items(self):
        obs = FundRazrCampaign.from_api(**CAMPAIGN_WITH_ITEMS)
        self.assertEqual(obs.title, 'American Gut')
        self.assertEqual(obs.campaign_id, 'c4NG5')
        self.assertEqual(len(obs.items), 1)

    def test_campaign_without_items(self):
        obs = FundRazrCampaign.from_api(**CAMPAIGN_NO_ITEMS)
        self.assertEqual(obs.title, 'not American Gut')
        self.assertEqual(obs.campaign_id, 'c4NGxxx')
        self.assertEqual(obs.items, [])


if __name__ == '__main__':
    main()
