import pytest
import copy
import collections
import json
import microsetta_private_api.server
from urllib.parse import urlencode
from unittest import TestCase
from microsetta_private_api.api.tests.test_integration import ACCT_ID


# region helper methods
def dictionary_mangler(a_dict, delete_fields=True, parent_dicts=None):
    """Generator to delete fields or add bogus fields in nested dictionary.

    Create a generator to travel recursively through the provided dictionary
    (which may contain child dictionaries).  If delete_fields, then for every
    leaf field, yield a copy of the whole dictionary with just that field
    deleted.  If not delete_fields, then for every leaf dictionary, yield a
    copy of the whole dictionary with one unexpected, bogus field added."""
    if parent_dicts is None:
        parent_dicts = collections.OrderedDict()
        parent_dicts["top"] = copy.deepcopy(a_dict)
    curr_dicts = {}

    for curr_key, curr_val in a_dict.items():
        curr_dicts = copy.deepcopy(parent_dicts)
        if isinstance(curr_val, dict):
            curr_dicts[curr_key] = curr_val
            yield from dictionary_mangler(curr_val, delete_fields,
                                          curr_dicts)
        else:
            if delete_fields:
                yield mangle_dictionary(a_dict, curr_dicts, curr_key)

    if not delete_fields:
        if curr_dicts is None:
            curr_dicts = copy.deepcopy(parent_dicts)
        yield mangle_dictionary(a_dict, curr_dicts)


URL_KEY = "url"
QUERY_KEY = "query"
CONTENT_KEY = "content"


def mangle_dictionary(a_dict, curr_dicts, key_to_delete=None):
    """Return copy of nested dictionary with a field popped or added.

     The popped or added field may be at any level of nesting within the
     original dictionary.  `curr_dicts` is an OrderedDict containing each
     nested dictionary in the original dictionary we are looping through
     (not necessarily the same as a_dict).  The first entry has the key "top"
     and holds the entire original dictionary. The second entry has the key of
     whatever the first nested dictionary is, and the value of that whole
     nested dictionary.  If that has nested dictionaries
     within it, they will be represented in the subsequent key/values, etc."""
    curr_dict = a_dict.copy()
    if key_to_delete is not None:
        curr_dict.pop(key_to_delete)
    else:
        curr_dict["disallowed_key"] = "bogus_value"
    curr_parent_key, _ = curr_dicts.popitem(True)

    q = len(curr_dicts.keys())
    while q > 0:
        next_parent_key, next_parent_dict = curr_dicts.popitem(True)
        next_parent_dict[curr_parent_key] = copy.deepcopy(curr_dict)
        curr_dict = copy.deepcopy(next_parent_dict)
        curr_parent_key = next_parent_key
        q = q - 1

    return curr_dict
# endregion help methods


@pytest.fixture(scope="class")
def client(request):
    app = microsetta_private_api.server.build_app()
    app.app.testing = True
    with app.app.test_client() as client:
        request.cls.client = client
        yield client


@pytest.mark.usefixtures("client")
class IntegrationTests(TestCase):
    lang_query_dict = {
        "language_tag": "en_US"
    }

    def setUp(self):
        app = microsetta_private_api.server.build_app()
        self.client = app.app.test_client()
        # This isn't perfect, due to possibility of exceptions being thrown
        # is there some better pattern I can use to split up what should be
        # a 'with' call?
        self.client.__enter__()

    def tearDown(self):
        # This isn't perfect, due to possibility of exceptions being thrown
        # is there some better pattern I can use to split up what should be
        # a 'with' call?
        self.client.__exit__(None, None, None)

    def run_query_and_content_required_field_test(self, url, dicts_to_test,
                                                  content_dict,
                                                  query_dict):
        for key in dicts_to_test:
            curr_query_dict = query_dict
            curr_content_dict = content_dict
            curr_expected_msg = None

            dict_to_test = dicts_to_test[key]
            field_deleter = dictionary_mangler(dict_to_test,
                                               delete_fields=True)
            for i in field_deleter:
                if key == QUERY_KEY:
                    curr_query_dict = i
                    curr_expected_msg = "Missing query parameter "
                elif key == CONTENT_KEY:
                    curr_content_dict = i
                    curr_expected_msg = "is a required property"

                curr_query_str = urlencode(curr_query_dict)
                curr_content_json = json.dumps(curr_content_dict)
                response = self.client.post(
                    '{0}?{1}'.format(url, curr_query_str),
                    content_type='application/json',
                    data=curr_content_json
                )

                self.assertEqual(400, response.status_code)
                resp_obj = json.loads(response.data)
                self.assertTrue(curr_expected_msg in resp_obj['detail'])
            # next deleted field
        # next dict to test

    # region account

    def test_accounts_post_without_required_fields(self):
        """Not providing any required field returns validation fail code"""

        content_dict = {
            "address": {
                "city": "Springfield",
                "country_code": "US",
                "post_code": "12345",
                # No state because state is optional
                "street": "123 Main St. E. Apt. 2"
            },
            "email": "janedoe@example.com",
            "first_name": "Jane",
            "last_name": "Doe",
            "kit_name": "jb_qhxqe"
        }

        dicts_to_test = {QUERY_KEY: self.lang_query_dict,
                         CONTENT_KEY: content_dict}

        self.run_query_and_content_required_field_test("/api/accounts",
                                                       dicts_to_test,
                                                       content_dict,
                                                       self.lang_query_dict)

    def test_account_get_without_required_fields(self):
        """Not providing any required field returns validation fail code"""

        content_dict = {}

        dicts_to_test = {QUERY_KEY: self.lang_query_dict,
                         CONTENT_KEY: content_dict}

        url = "/api/account/{0}".format(ACCT_ID)
        self.run_query_and_content_required_field_test(url,
                                                       dicts_to_test,
                                                       content_dict,
                                                       self.lang_query_dict)


    # def test_accounts_post_with_extra_fields(self):
    #     """Providing any field not in api returns validation fail code"""
    #     my_dict = {
    #         "address": {
    #             "city": "Springfield",
    #             "country_code": "US",
    #             "post_code": "12345",
    #             "state": "shouldn't have to be here",
    #             "street": "123 Main St. E. Apt. 2"
    #         },
    #         "email": "janedoe@example.com",
    #         "first_name": "Jane",
    #         "last_name": "Doe",
    #         "kit_name": "jb_qhxqe"
    #     }
    #
    #     field_adder = dictionary_mangler(my_dict, delete_fields=False)
    #     for i in field_adder:
    #         print(i)
    #         acct_json = json.dumps(i)
    #         continue
    #
    #         response = self.client.post(
    #             '/api/accounts?language_tag=en-US',
    #             content_type='application/json',
    #             data=acct_json
    #         )
    #
    #         self.assertEqual(400, response.status_code)
    #         resp_obj = json.loads(response.data)
    #         self.assertTrue("is a required property" in resp_obj['detail'])
    # endregion account post
