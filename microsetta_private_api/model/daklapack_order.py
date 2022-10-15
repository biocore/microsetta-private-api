from datetime import datetime, timezone
import json

ORDER_ID_KEY = 'daklapack_order_id'
ORDER_JSON_KEY = 'order_json'
PROJECT_IDS_LIST_KEY = 'project_ids'
DAK_ARTICLE_CODE_KEY = 'article_code'
ADDR_DICT_KEY = 'address'
FEDEX_REF_1_KEY = 'fedex_ref_1'
FEDEX_REF_2_KEY = 'fedex_ref_2'
FEDEX_REF_3_KEY = 'fedex_ref_3'
PLANNED_SEND_DATE_KEY = 'planned_send_date'
DESCRIPTION_KEY = 'description'
SUBMITTER_ACCT_KEY = "submitter_acct"
QUANTITY_KEY = "quantity"
SHIPPING_PROVIDER_KEY = "shipping_provider"
FEDEX_PROVIDER = "FedEx"
FREIGHT_PROVIDER = "Freight"
TRANSSMART_PROVIDER = "TransSmart"
USPS_PROVIDER = "USPS"
SHIPPING_PROVIDERS = [FEDEX_PROVIDER, FREIGHT_PROVIDER, TRANSSMART_PROVIDER,
                      USPS_PROVIDER]
SHIPPING_TYPE_KEY = "shipping_type"
DEFAULT_SHIPPING = "Default"
FEDEX_2DAY_SHIPPING = "FEDEX_2_DAY"
FEDEX_GROUND_SHIPPING = "FEDEX_GROUND"
FEDEX_GROUND_HOME_SHIPPING = "GROUND_HOME_DELIVERY"
FEDEX_PRIORITY_OVERNIGHT_SHIPPING = "PRIORITY_OVERNIGHT"
FEDEX_STANDARD_OVERNIGHT_SHIPPING = "STANDARD_OVERNIGHT"
USPS_PRIORITY_SHIPPING = "PRIORITY"
USPS_PRIORITY_EXPRESS_SHIPPING = "PRIORITY_EXPRESS"
USPS_FIRST_CLASS_SHIPPING = "FIRST_CLASS"
SHIPPING_TYPES_BY_PROVIDER = {
    FEDEX_PROVIDER: [DEFAULT_SHIPPING, FEDEX_2DAY_SHIPPING,
                     FEDEX_GROUND_SHIPPING,
                     FEDEX_GROUND_HOME_SHIPPING,
                     FEDEX_PRIORITY_OVERNIGHT_SHIPPING,
                     FEDEX_STANDARD_OVERNIGHT_SHIPPING],
    FREIGHT_PROVIDER: [DEFAULT_SHIPPING],
    TRANSSMART_PROVIDER: [DEFAULT_SHIPPING],
    USPS_PROVIDER: [DEFAULT_SHIPPING, USPS_PRIORITY_EXPRESS_SHIPPING,
                    USPS_PRIORITY_SHIPPING, USPS_FIRST_CLASS_SHIPPING]
}


class DaklapackOrder:
    DATE_FORMAT = "%Y-%m-%d"
    DATESTAMP_FORMAT = f"{DATE_FORMAT} %H:%M:%S.%f"

    def __init__(self, daklapack_order_id, submitter_acct, project_ids_list,
                 order_structure, description, planned_send_date,
                 creation_timestamp=None, last_polling_timestamp=None,
                 last_polling_status=None):

        # NB: these are the only fields that exists in BOTH the db record
        # AND, separately, in the json
        self.id = daklapack_order_id
        self.creation_timestamp = creation_timestamp
        if self.creation_timestamp is None:
            self.creation_timestamp = datetime.now(timezone.utc)
        self.planned_send_date = planned_send_date

        # these fields exist in the db only
        self.submitter_acct = submitter_acct
        self.project_ids_list = project_ids_list
        self.description = description

        # keep these "private" as they really shouldn't be mucked with directly
        self._order_structure = order_structure
        self._last_polling_status = last_polling_status
        self._last_polling_timestamp = last_polling_timestamp

    @property
    def order_structure(self):
        return self._order_structure

    @property
    def order_json(self):
        return json.dumps(self._order_structure)

    @property
    def last_polling_status(self):
        return self._last_polling_status

    @property
    def last_polling_timestamp(self):
        return self._last_polling_timestamp

    @classmethod
    def validate_shipping(cls, shipping_provider, shipping_type):
        if shipping_provider not in SHIPPING_PROVIDERS:
            raise ValueError(f"Unrecognized shipping provider "
                             f"'{shipping_provider}'")

        valid_shipping_types = SHIPPING_TYPES_BY_PROVIDER[shipping_provider]
        if shipping_type not in valid_shipping_types:
            raise ValueError(f"Shipping type '{shipping_type}' is "
                             f"unrecognized for shipping provider "
                             f"'{shipping_provider}'")

    @classmethod
    def from_api(cls, **kwargs):
        curr_timestamp = None
        # note: api can't set last_polling_status and last_polling_timestamp:
        # they will default to None.

        # user-provided fields that don't go into json (only db):
        # required:
        submitter_acct = kwargs[SUBMITTER_ACCT_KEY]
        project_ids_list = kwargs[PROJECT_IDS_LIST_KEY]
        # optional:
        description = kwargs.get(DESCRIPTION_KEY)

        # field that goes into both the json and the db:
        # required but may be empty string:
        planned_send_date = kwargs.get(PLANNED_SEND_DATE_KEY)

        # fields that eventually go only into json:
        # required:
        order_id = kwargs[ORDER_ID_KEY]
        article_code = kwargs[DAK_ARTICLE_CODE_KEY]
        address_dict = kwargs[ADDR_DICT_KEY]
        quantity = kwargs[QUANTITY_KEY]
        shipping_provider = kwargs[SHIPPING_PROVIDER_KEY]
        shipping_type = kwargs[SHIPPING_TYPE_KEY]

        cls.validate_shipping(shipping_provider, shipping_type)

        # optional: fedex reference fields
        fedex_refs_dicts_list = []
        fedex_keys = {FEDEX_REF_1_KEY: "Reference 1",
                      FEDEX_REF_2_KEY: "Reference 2",
                      FEDEX_REF_3_KEY: "Reference 3"}
        for curr_key, curr_val in fedex_keys.items():
            curr_input = kwargs.get(curr_key)
            if curr_input:
                fedex_refs_dicts_list.append({
                    "key": curr_val,
                    "value": curr_input})

        # creation date is now; NB: not time-zone aware
        curr_timestamp_str = datetime.now().strftime(cls.DATESTAMP_FORMAT)
        # FYI, not enforced here, but planned send date must be in DATE_FORMAT,
        # *not* DATESTAMP format ... apparently the Daklapack API allows
        # createDate to have a time attached to it but doesn't allow that for
        # plannedSendDate
        # planned send date str goes into order as a date or an empty string
        # (but planned send date goes into db as a date or a null)
        planned_send_str = planned_send_date if planned_send_date else ''

        # Daklapack API expects that ALL aspects of an address are
        # represented as strings, including, e.g. numeric zip codes
        str_addr_dict = {k: str(v) for k, v in address_dict.items()}
        str_addr_dict["creationDate"] = curr_timestamp_str
        # "companyName" is actually the name of the submitter
        str_addr_dict["companyName"] = f"{submitter_acct.first_name} " \
                                       f"{submitter_acct.last_name}"

        # Generate daklapack-required order structure
        order_structure = {
            "orderId": order_id,
            "articles": [
                {
                    "articleCode": str(article_code),
                    "quantity": str(quantity)
                }
            ],
            "plannedSendDate": planned_send_str,
            ADDR_DICT_KEY: str_addr_dict,
            "shippingProvider": shipping_provider,
            "shippingType": shipping_type,
            "shippingProviderMetadata": fedex_refs_dicts_list
        }

        return cls(order_id, submitter_acct, project_ids_list,
                   order_structure, description, planned_send_date,
                   creation_timestamp=curr_timestamp)

    def set_last_polling_info(self, last_polling_status,
                              last_polling_timestamp=None):
        if last_polling_timestamp is None:
            last_polling_timestamp = datetime.now()
        self._last_polling_status = last_polling_status
        self._last_polling_timestamp = last_polling_timestamp
