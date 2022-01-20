from datetime import datetime
import pytz
from microsetta_private_api.model.model_base import ModelBase
from microsetta_private_api.model.address import Address
import time


# fundrazr fields
TRANSACTION_TYPE = 'transaction_type'
CREATED_TIMESTAMP = "created"
CAMPAIGN_ID = "campaign_id"
ID = 'id'
AMOUNT = "amount"
NET_AMOUNT = "net_amount"
CURRENCY = "currency"
PAYER_NAME = "payer_name"
PAYER_FIRST_NAME = "payer_first_name"
PAYER_LAST_NAME = "payer_last_name"
PAYER_EMAIL = "payer_email"
TRANSACTION_ID = "transaction_id"
FUNDRAZR_ACCOUNT_TYPE = "account"
MESSAGE = "message"
CLAIMED_ITEMS = "claimed_items"
ITEMS = "items"
TITLE = "title"
ITEM_QUANTITY = "quantity"
ITEM_ID = "id"
CONTACT_EMAIL = "contact_email"
SUBSCRIBE_TO_UPDATES = "subscribe_to_updates"
PHONE_NUMBER = "phone_number"
SHIPPING_ADDRESS = "shipping_address"
SHIPPING_FIRST_NAME = "first_name"
SHIPPING_LAST_NAME = "last_name"
SHIPPING_COMPANY = "company_name"
SHIPPING_POSTAL_CODE = "postal_code"
SHIPPING_COUNTRY = "country"
SHIPPING_STATE = "state"
ADDRESS_POST_CODE = "post_code"
ADDRESS_COUNTRY_CODE = "country_code"
STATS = 'stats'
PRICE = 'price'


class FundRazrCampaign:
    def __init__(self, campaign_id, title, currency, items, stats):
        self.campaign_id = campaign_id
        self.title = title
        self.currency = currency
        self.stats = stats

        if items is None:
            self.items = []
        elif isinstance(items, list):
            self.items = items
        elif isinstance(items, Item):
            self.items = [items, ]
        else:
            raise ValueError(f"Cannot handle item of type {type(items)}")

    @classmethod
    def from_api(cls, **kwargs):
        title = kwargs[TITLE]
        campaign_id = kwargs[ID]
        currency = kwargs[CURRENCY]

        items = []
        for item in kwargs.get(ITEMS, []):
            item = item.copy()
            item[ITEM_QUANTITY] = 0
            items.append(Item.from_api(**item))

        stats = kwargs[STATS]
        return cls(campaign_id, title, currency, items, stats)


class Shipping(ModelBase):
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    @classmethod
    def from_api(cls, **kwargs):
        # we are mutating so be polite
        kwargs = kwargs.copy()

        first_name = kwargs.pop(SHIPPING_FIRST_NAME)
        last_name = kwargs.pop(SHIPPING_LAST_NAME)

        if SHIPPING_COMPANY in kwargs:
            kwargs.pop(SHIPPING_COMPANY)

        # rewrite key to correspond to our Address model object
        kwargs[ADDRESS_POST_CODE] = kwargs[SHIPPING_POSTAL_CODE]
        kwargs.pop(SHIPPING_POSTAL_CODE)

        # rewrite country to correspond to our Address model object
        kwargs[ADDRESS_COUNTRY_CODE] = kwargs[SHIPPING_COUNTRY]
        kwargs.pop(SHIPPING_COUNTRY)

        # observed in at least one transaction
        if SHIPPING_STATE not in kwargs:
            kwargs[SHIPPING_STATE] = 'not provided'

        return cls(first_name, last_name, Address(**kwargs))

    def to_api(self):
        d = {SHIPPING_FIRST_NAME: self.first_name,
             SHIPPING_LAST_NAME: self.last_name}
        d.update(self.address.to_api())
        return d


class Item(ModelBase):
    REQUIRED = (TITLE, ITEM_QUANTITY, ITEM_ID)
    OPTIONAL = (PRICE, )

    def __init__(self, title, quantity, id, price=None):
        self.title = title
        self.quantity = quantity
        self.id = id
        self.price = price

    @classmethod
    def from_api(cls, **kwargs):
        d = {k: kwargs[k] for k in cls.REQUIRED}
        d.update({k: kwargs[k] for k in cls.OPTIONAL})
        return cls(**d)

    def to_api(self):
        return self.__dict__.copy()


class Payment(ModelBase):
    # PAYER_FIRST_NAME and PAYER_LAST_NAME are required
    # but there is an edge case where at least one transaction
    # lacks these, and so we will obtain the name from
    # shipping instead
    REQUIRED = (CREATED_TIMESTAMP, CAMPAIGN_ID, AMOUNT,
                NET_AMOUNT, CURRENCY,
                TRANSACTION_ID,
                FUNDRAZR_ACCOUNT_TYPE)

    # offline transactions do not necessarily
    # have payer or contact emails per fundrazr's
    # dev team.
    OPTIONAL = (MESSAGE, SHIPPING_ADDRESS, CLAIMED_ITEMS,
                PHONE_NUMBER, SUBSCRIBE_TO_UPDATES,
                PAYER_EMAIL, CONTACT_EMAIL)

    TRANSACTION_TYPE = None

    _TZ_US_PACIFIC = pytz.timezone('US/Pacific')

    def __init__(self,
                 transaction_id,
                 created,
                 campaign_id,
                 amount,
                 net_amount,
                 currency,
                 payer_first_name,
                 payer_last_name,
                 account,
                 subscribe_to_updates=False,
                 interested_user_id=None,
                 message=None,
                 phone_number=None,
                 shipping_address=None,
                 claimed_items=None,
                 payer_email=None,
                 contact_email=None,
                 **kwargs):
        self.transaction_id = transaction_id
        self.created = created
        self.campaign_id = campaign_id
        self.amount = amount
        self.net_amount = net_amount
        self.currency = currency
        self.payer_first_name = payer_first_name
        self.payer_last_name = payer_last_name
        self.payer_email = payer_email
        self.contact_email = contact_email
        self.shipping_address = shipping_address
        self.account = account
        self.subscribe_to_updates = subscribe_to_updates
        self.phone_number = phone_number
        self.message = message
        self.interested_user_id = interested_user_id

        if claimed_items is None:
            self.claimed_items = []
        else:
            self.claimed_items = claimed_items

    def copy(self):
        # we have nested objects, and the default copy on model base doesn't
        # cascade, so let's do the extra work here
        if self.shipping_address is None:
            address = None
        else:
            address = self.shipping_address.copy()

        claimed_items = [i.copy() for i in self.claimed_items]

        cls = self.__class__(**self.__dict__)
        cls.shipping_address = address
        cls.claimed_items = claimed_items

        return cls

    def to_api(self):
        return {
            TRANSACTION_ID: self.transaction_id,
            TRANSACTION_TYPE: self.transaction_type,
            CREATED_TIMESTAMP: str(self.created),
            CAMPAIGN_ID: self.campaign_id,
            AMOUNT: self.amount,
            NET_AMOUNT: self.net_amount,
            CURRENCY: self.currency,
            PAYER_FIRST_NAME: self.payer_first_name,
            PAYER_LAST_NAME: self.payer_lase_name,
            PAYER_EMAIL: self.payer_email,
            CONTACT_EMAIL: self.contact_email,
            SHIPPING_ADDRESS: self.shipping.to_api(),
            FUNDRAZR_ACCOUNT_TYPE: self.fundrazr_account_type,
            SUBSCRIBE_TO_UPDATES: self.subscribe_to_updates,
            PHONE_NUMBER: self.phone_number,
            MESSAGE: self.message,
            CLAIMED_ITEMS: [i.to_api() for i in self.claimed_items]
        }

    @classmethod
    def from_api(cls, **kwargs):
        structured = {k: kwargs[k] for k in cls.REQUIRED}
        structured.update({k: kwargs[k] for k in cls.OPTIONAL if k in kwargs})

        # force everything to be relative to UCSD
        structured['created'] = datetime.fromtimestamp(structured['created'],
                                                       cls._TZ_US_PACIFIC)

        if CLAIMED_ITEMS in structured:
            items = structured[CLAIMED_ITEMS]
            structured[CLAIMED_ITEMS] = [Item.from_api(**item)
                                         for item in items]

        shipping = None
        if SHIPPING_ADDRESS in structured:
            shipping = Shipping.from_api(**structured[SHIPPING_ADDRESS])
            structured[SHIPPING_ADDRESS] = shipping

        # one of out ~16000 transactions lacks payer_first and last names
        # so rather than coercing the database schema, we will work around
        # this unusual case
        if PAYER_FIRST_NAME in kwargs:
            structured[PAYER_FIRST_NAME] = kwargs[PAYER_FIRST_NAME]
            structured[PAYER_LAST_NAME] = kwargs[PAYER_LAST_NAME]
        else:
            if shipping is not None:
                structured[PAYER_FIRST_NAME] = shipping.first_name
                structured[PAYER_LAST_NAME] = shipping.last_name
            else:
                structured[PAYER_FIRST_NAME] = 'not provided'
                structured[PAYER_LAST_NAME] = 'not provided'

        return cls(**structured)

    @classmethod
    def from_db(cls, trn):
        if trn.get('shipping_postal') is not None:
            first = trn['shipping_first_name']
            last = trn['shipping_last_name']
            address = Address(trn['shipping_address1'],
                              trn['shipping_city'],
                              trn['shipping_state'],
                              trn['shipping_postal'],
                              trn['shipping_country'],
                              trn['shipping_address2'])
            shipping = Shipping(first, last, address)
        else:
            shipping = None

        items = trn['fundrazr_perks']
        if items is not None:
            items = [Item(**item) for item in items]
        else:
            items = None

        d = dict(trn)
        d[TRANSACTION_ID] = d['id']
        d[FUNDRAZR_ACCOUNT_TYPE] = d['account_type']
        d[SUBSCRIBE_TO_UPDATES] = d['subscribed_to_updates']
        d[CAMPAIGN_ID] = d['remote_campaign_id']
        d[CLAIMED_ITEMS] = items
        d[PAYER_EMAIL] = d['payer_email']
        d[SHIPPING_ADDRESS] = shipping
        return cls(**d)

    def created_as_unixts(self):
        """Express .created as a unix timestamp"""
        return int(time.mktime(self.created.timetuple()))


class FundRazrPayment(Payment):
    TRANSACTION_TYPE = 'fundrazr'


def payment_from_db(data):
    if data['transaction_type'] == FundRazrPayment.TRANSACTION_TYPE:
        return FundRazrPayment.from_db(data)
    else:
        raise KeyError(f"Unknown type '{data['transaction_type']}'")


class Campaign(ModelBase):
    def __init__(self, campaign_id, title, instructions, header_image,
                 permitted_countries, language_key, accepting_participants,
                 associated_projects, language_key_alt, title_alt,
                 instructions_alt):
        self.campaign_id = campaign_id
        self.title = title
        self.instructions = instructions
        self.header_image = header_image
        self.permitted_countries = permitted_countries
        self.language_key = language_key
        self.accepting_participants = accepting_participants
        self.associated_projects = associated_projects
        self.language_key_alt = language_key_alt
        self.title_alt = title_alt
        self.instructions_alt = instructions_alt

    def to_api(self):
        return self.__dict__.copy()
