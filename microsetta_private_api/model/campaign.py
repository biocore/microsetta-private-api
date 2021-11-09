from datetime import datetime
from microsetta_private_api.model.model_base import ModelBase
from microsetta_private_api.model.address import Address


CREATED_TIMESTAMP = "created"
CAMPAIGN_ID = "campaign_id"
AMOUNT = "amount"
NET_AMOUNT = "net_amount"
CURRENCY = "currency"
STATUS = "status"
PAYER_NAME = "payer_name"
PAYER_FIRST_NAME = "payer_first_name"
PAYER_LAST_NAME = "payer_last_name"
PAYER_EMAIL = "payer_email"
TRANSACTION_ID = "transaction_id"
FUNDRAZR_ACCOUNT_TYPE = "account"
MESSAGE = "message"
CLAIMED_ITEMS = "claimed_items"
ITEM_TITLE = "title"
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
ADDRESS_POST_CODE = "post_code"
ADDRESS_COUNTRY_CODE = "country_code"
TMI_STATUS = 'microsetta_status'


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

        return cls(first_name, last_name, Address(**kwargs))

    def to_api(self):
        d = {SHIPPING_FIRST_NAME: self.first_name,
             SHIPPING_LAST_NAME: self.last_name}
        d.update(self.address.to_api())


class Item(ModelBase):
    def __init__(self, title, quantity, id):
        self.title = title
        self.quantity = quantity
        self.id = id

    @classmethod
    def from_api(cls, **kwargs):
        REQUIRED = [ITEM_TITLE, ITEM_QUANTITY, ITEM_ID]
        return cls(**{k: kwargs[k] for k in REQUIRED})

    def to_api(self):
        return self.__dict__.copy()


class Payment(ModelBase):
    def __init__(self,
                 transaction_id,
                 created,
                 campaign_id,
                 amount,
                 net_amount,
                 currency,
                 status,
                 payer_first_name,
                 payer_last_name,
                 payer_email,
                 contact_email,
                 account,
                 subscribe_to_updates,
                 message=None,
                 phone_number=None,
                 shipping_address=None,
                 claimed_items=None,
                 tmi_status=None):  # if coming from the API
        self.transaction_id = transaction_id
        self.created = created
        self.campaign_id = campaign_id
        self.amount = amount
        self.net_amount = net_amount
        self.currency = currency

        # from fundrazr api doc, one of
        # completed, preapproved, cancelled, refunded, reversed
        self.status = status
        self.payer_first_name = payer_first_name
        self.payer_last_name = payer_last_name
        self.payer_email = payer_email
        self.contact_email = contact_email
        self.shipping_address = shipping_address
        self.account = account
        self.subscribe_to_updates = subscribe_to_updates
        self.claimed_items = claimed_items
        self.phone_number = phone_number
        self.message = message
        self.tmi_status = tmi_status

    def copy(self):
        # we have nested objects, and the default copy on model base doesn't
        # cascade, so let's do the extra work here
        if self.shipping_address is None:
            address = None
        else:
            address = self.shipping_address.copy()

        if self.claimed_items is None:
            claimed_items = None
        else:
            claimed_items = [i.copy() for i in self.claimed_items]

        cls = self.__class__(**self.__dict__)
        cls.shipping_address = address
        cls.claimed_items = claimed_items

        return cls

    def to_api(self):
        return {
            TRANSACTION_ID: self.transaction_id,
            CREATED_TIMESTAMP: str(self.created),
            CAMPAIGN_ID: self.campaign_id,
            AMOUNT: self.amount,
            NET_AMOUNT: self.net_amount,
            CURRENCY: self.currency,
            STATUS: self.status,
            PAYER_FIRST_NAME: self.payer_first_name,
            PAYER_LAST_NAME: self.payer_lase_name,
            PAYER_EMAIL: self.payer_email,
            CONTACT_EMAIL: self.contact_email,
            SHIPPING_ADDRESS: self.shipping.to_api(),
            FUNDRAZR_ACCOUNT_TYPE: self.fundrazr_account_type,
            SUBSCRIBE_TO_UPDATES: self.subscribe_to_updates,
            PHONE_NUMBER: self.phone_number,
            TMI_STATUS: self.tmi_status,
            MESSAGE: self.message,
            CLAIMED_ITEMS: [i.to_api() for i in self.claimed_items]
        }

    @classmethod
    def from_api(cls, **kwargs):
        required = [CREATED_TIMESTAMP, CAMPAIGN_ID, AMOUNT, NET_AMOUNT,
                    CURRENCY, STATUS, PAYER_FIRST_NAME, SUBSCRIBE_TO_UPDATES,
                    PAYER_LAST_NAME, PAYER_EMAIL, TRANSACTION_ID,
                    FUNDRAZR_ACCOUNT_TYPE, CONTACT_EMAIL]

        optional = [MESSAGE, SHIPPING_ADDRESS, CLAIMED_ITEMS, PHONE_NUMBER]

        structured = {k: kwargs[k] for k in required}
        structured.update({k: kwargs[k] for k in optional if k in kwargs})

        structured['created'] = datetime.fromtimestamp(structured['created'])

        if CLAIMED_ITEMS in structured:
            structured[CLAIMED_ITEMS] = [Item.from_api(**item)
                                         for item in structured[CLAIMED_ITEMS]]

        if SHIPPING_ADDRESS in structured:
            shipping = Shipping.from_api(**structured[SHIPPING_ADDRESS])
            structured[SHIPPING_ADDRESS] = shipping

        return cls(**structured)

    @classmethod
    def from_db(cls, trn, items):
        if trn.get('shipping_first_name') is not None:
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

        if items is not None:
            items = [Item(**item) for item in items]
        else:
            items = None

        # rewrite some fields becuase daniel wasn't paying attention
        d = dict(trn)
        d['transaction_id'] = d['id']
        d['account'] = d['account_type']
        d['subscribe_to_updates'] = d['subscribed_to_updates']
        d['campaign_id'] = d['remote_campaign_id']
        d['status'] = d['fundrazr_status']
        d['claimed_items'] = items
        d['shipping_address'] = shipping

        for k in ['id', 'account_type', 'subscribed_to_updates',
                  'remote_campaign_id', 'fundrazr_status',
                  'shipping_first_name', 'shipping_last_name',
                  'shipping_address1', 'shipping_city',
                  'shipping_state', 'shipping_postal',
                  'shipping_country', 'shipping_address2']:
            d.pop(k)

        return cls(**d)


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
        return {
            "campaign_id": self.campaign_id,
            "title": self.title,
            "instructions": self.instructions,
            "header_image": self.header_image,
            "permitted_countries": self.permitted_countries,
            "language_key": self.language_key,
            "accepting_participants": self.accepting_participants,
            "associated_projects": self.associated_projects,
            "language_key_alt": self.language_key_alt,
            "title_alt": self.title_alt,
            "instructions_alt": self.instructions_alt
        }
