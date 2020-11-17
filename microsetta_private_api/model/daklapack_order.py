from datetime import datetime, timezone
import json

ORDER_ID_KEY = 'daklapack_order_id'
ORDER_JSON_KEY = 'order_json'
PROJECT_IDS_LIST_KEY = 'project_ids'
DAK_ARTICLE_CODE_KEY = 'article_code'
ADDR_DICTS_LIST_KEY = 'addresses'
FEDEX_REF_1_KEY = 'fedex_ref_1'
FEDEX_REF_2_KEY = 'fedex_ref_2'
FEDEX_REF_3_KEY = 'fedex_ref_3'
FULFILLMENT_HOLD_MSG = 'fulfillment_hold_msg'
DESCRIPTION_KEY = 'description'
SUBMITTER_ACCT_KEY = "submitter_acct"


class DaklapackOrder:
    def __init__(self, daklapack_order_id, submitter_acct, project_ids_list,
                 order_structure, description, fulfillment_hold_msg,
                 creation_timestamp=None, last_polling_timestamp=None,
                 last_polling_status=None):

        # NB: these are the only fields that exists in BOTH the db record
        # AND, separately, in the json
        self.id = daklapack_order_id
        self.creation_timestamp = creation_timestamp
        if self.creation_timestamp is None:
            self.creation_timestamp = datetime.now(timezone.utc)

        self.submitter_acct = submitter_acct
        self.project_ids_list = project_ids_list
        self.description = description
        self.fulfillment_hold_msg = fulfillment_hold_msg

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
    def from_api(cls, **kwargs):
        curr_timestamp = None
        # note: api can't set last_polling_status and last_polling_timestamp:
        # they will default to None.

        # fields that don't go into json (only db):
        # required:
        submitter_acct = kwargs[SUBMITTER_ACCT_KEY]
        project_ids_list = kwargs[PROJECT_IDS_LIST_KEY]
        # optional:
        description = kwargs.get(DESCRIPTION_KEY)
        fulfillment_hold_msg = kwargs.get(FULFILLMENT_HOLD_MSG)

        # fields that eventually go only into json:
        # required:
        order_id = kwargs[ORDER_ID_KEY]
        article_code = kwargs[DAK_ARTICLE_CODE_KEY]
        address_dicts_list = kwargs[ADDR_DICTS_LIST_KEY]

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

        # creation date is now
        curr_timestamp = datetime.now(timezone.utc)
        curr_timestamp_str = curr_timestamp.isoformat()
        curr_timestamp_str = curr_timestamp_str.replace("+00:00", "Z")

        for curr_addr_dict in address_dicts_list:
            curr_addr_dict["creationDate"] = curr_timestamp_str
            # "companyName" is actually the name of the submitter
            curr_addr_dict["companyName"] = f"{submitter_acct.first_name} " \
                                            f"{submitter_acct.last_name}"

        # Generate daklapack-required order structure
        order_structure = {
            "orderId": order_id,
            "articles": [
                {
                    "articleCode": article_code,
                    "addresses": address_dicts_list
                }
            ],
            "shippingProvider": "FedEx",
            "shippingType": "FEDEX_2_DAY",
            "shippingProviderMetadata": fedex_refs_dicts_list
        }

        return cls(order_id, submitter_acct, project_ids_list,
                   order_structure, description, fulfillment_hold_msg,
                   creation_timestamp=curr_timestamp)

    def set_last_polling_info(self, last_polling_status,
                              last_polling_timestamp=None):
        if last_polling_timestamp is None:
            last_polling_timestamp = datetime.now()
        self._last_polling_status = last_polling_status
        self._last_polling_timestamp = last_polling_timestamp
