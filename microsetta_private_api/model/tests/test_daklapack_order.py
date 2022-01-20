from copy import deepcopy
from datetime import datetime, timedelta, date
from unittest import TestCase
from microsetta_private_api.api.tests.test_api import DUMMY_ACCT_INFO_2
from microsetta_private_api.model.account import Account
from microsetta_private_api.model.daklapack_order import DaklapackOrder

DUMMY_DAK_ORDER_ID = '7ed917ef-0c4d-431a-9aa0-0a1f4f41f44b'
DUMMY_PROJ_ID_LIST = [1, 12]
DUMMY_DAK_ORDER_DESC = "test daklapack order"
DUMMY_PLANNED_SEND_DATE = date(2032, 2, 9).strftime(DaklapackOrder.DATE_FORMAT)
DUMMY_DAK_ARTICLE_CODE = '350102'
DUMMY_ADDRESSES = [{
    'firstName': 'Jane',
    'lastName': 'Doe',
    'address1': '123 Main St',
    'insertion': 'Apt 2',
    'address2': '',
    'postalCode': '92210',
    'city': 'San Diego',
    'state': 'CA',
    'country': 'USA',
    'countryCode': 'us',
    'phone': '(858) 555-1212',
},
    {
        'firstName': 'Tom',
        'lastName': 'Thumb',
        'address1': '29 Side St',
        'insertion': '',
        'address2': 'Kew Gardens',
        'postalCode': 'KG7-448',
        'city': 'Gananoque',
        'state': 'Ontario',
        'country': 'Canada',
        'countryCode': 'ca',
        'phone': '(858) 555-1212',
    }]
DUMMY_FEDEX_REFS = ['Bill Ted', 'Mine', 'Yours']


def make_dummies(include_fedex_refs=False, include_planned_send_date=False):
    dummy_acct_dict = deepcopy(DUMMY_ACCT_INFO_2)
    dummy_acct_dict['id'] = 'dummy_acct_id'
    dummy_acct = Account.from_dict(dummy_acct_dict, "an_iss", "a_sub")
    submitter_name = f"{dummy_acct.first_name} {dummy_acct.last_name}"

    dummy_order_struct = {
        'orderId': DUMMY_DAK_ORDER_ID,
        'articles': [
            {
                'articleCode': '350102',
                'quantity': '2'
            }
        ],
        'address':
            {'firstName': 'Jane',
             'lastName': 'Doe',
             'address1': '123 Main St',
             'insertion': 'Apt 2',
             'address2': '',
             'postalCode': '92210',
             'city': 'San Diego',
             'state': 'CA',
             'country': 'USA',
             'countryCode': 'us',
             'phone': '(858) 555-1212',
             'companyName': submitter_name
             },
        "plannedSendDate": "",
        'shippingProvider': 'FedEx',
        'shippingType': 'FEDEX_2_DAY',
        'shippingProviderMetadata': []
    }

    if include_fedex_refs:
        dummy_order_struct['shippingProviderMetadata'] = [
            {'key': 'Reference 1',
             'value': 'Bill Ted'},
            {'key': 'Reference 2',
             'value': 'Mine'},
            {'key': 'Reference 3',
             'value': 'Yours'}
        ]

    if include_planned_send_date:
        dummy_order_struct['plannedSendDate'] = DUMMY_PLANNED_SEND_DATE

    return dummy_order_struct, dummy_acct


class DaklapackOrderTests(TestCase):
    def _compare_base_orders(self, dummy_acct, dummy_order_struct, real_out):
        self.assertEqual(dummy_acct, real_out.submitter_acct)
        self.assertEqual(DUMMY_PROJ_ID_LIST, real_out.project_ids_list)
        self.assertEqual(DUMMY_DAK_ORDER_ID, real_out.id)

        real_address = real_out.order_structure['address']
        # pop out creation date and make sure it is approximately now :)
        curr_create_str = real_address.pop("creationDate")
        curr_create_time = datetime.strptime(
            curr_create_str, DaklapackOrder.DATESTAMP_FORMAT)
        self.assertAlmostEqual(datetime.now(),
                               curr_create_time,
                               delta=timedelta(minutes=2))
        self.assertEqual(dummy_order_struct, real_out.order_structure)

    def test_from_api_fully_specified(self):
        dummy_order_struct, dummy_acct = make_dummies(
            include_fedex_refs=True, include_planned_send_date=True)

        real_out = DaklapackOrder.from_api(
            submitter_acct=dummy_acct,
            project_ids=DUMMY_PROJ_ID_LIST,
            description=DUMMY_DAK_ORDER_DESC,
            planned_send_date=DUMMY_PLANNED_SEND_DATE,
            daklapack_order_id=DUMMY_DAK_ORDER_ID,
            article_code=DUMMY_DAK_ARTICLE_CODE,
            address=DUMMY_ADDRESSES[0],
            fedex_ref_1=DUMMY_FEDEX_REFS[0],
            fedex_ref_2=DUMMY_FEDEX_REFS[1],
            fedex_ref_3=DUMMY_FEDEX_REFS[2],
            quantity=2)

        self._compare_base_orders(dummy_acct, dummy_order_struct, real_out)
        self.assertEqual(DUMMY_DAK_ORDER_DESC, real_out.description)
        self.assertEqual(DUMMY_PLANNED_SEND_DATE, real_out.planned_send_date)

    def test_from_api_wo_optionals(self):
        dummy_order_struct, dummy_acct = make_dummies(
            include_fedex_refs=False, include_planned_send_date=False)

        real_out = DaklapackOrder.from_api(
            submitter_acct=dummy_acct,
            project_ids=DUMMY_PROJ_ID_LIST,
            daklapack_order_id=DUMMY_DAK_ORDER_ID,
            article_code=DUMMY_DAK_ARTICLE_CODE,
            address=DUMMY_ADDRESSES[0],
            quantity=2)

        self._compare_base_orders(dummy_acct, dummy_order_struct, real_out)
        self.assertEqual(None, real_out.description)
        self.assertEqual(None, real_out.planned_send_date)
