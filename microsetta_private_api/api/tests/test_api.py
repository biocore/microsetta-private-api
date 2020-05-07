from unittest.mock import patch

import pytest
import werkzeug
import json
import copy
import collections
import datetime
from urllib.parse import urlencode
from unittest import TestCase
import microsetta_private_api.server
from microsetta_private_api import localization
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo
from microsetta_private_api.model.account import Account
from microsetta_private_api.model.source import Source, HumanInfo, NonHumanInfo


# region helper methods
QUERY_KEY = "query"
CONTENT_KEY = "content"

TEST_EMAIL = "test_email@example.com"
TEST_EMAIL_2 = "second_test_email@example.com"

ACCT_ID_1 = "7a98df6a-e4db-40f4-91ec-627ac315d881"
ACCT_ID_2 = "9457c58f-7464-46c9-b6e0-116273cf8f28"
MISSING_ACCT_ID = "a6cbd48e-f8da-4c0e-bdd6-3ffbbb5958ba"

KIT_NAME_KEY = "kit_name"
# these kits exists in the test db (NOT created by unit test code)
EXISTING_KIT_NAME = "jb_qhxqe"
EXISTING_KIT_NAME_2 = "fa_lrfiq"
# this kit does not exist in the test db
MISSING_KIT_NAME = "jb_qhxTe"

DUMMY_ACCT_INFO = {
    "address": {
        "city": "Springfield",
        "country_code": "US",
        "post_code": "12345",
        "state": "CA",
        "street": "123 Main St. E. Apt. 2"
    },
    "email": TEST_EMAIL,
    "first_name": "Jane",
    "last_name": "Doe",
    KIT_NAME_KEY: EXISTING_KIT_NAME
}
DUMMY_ACCT_INFO_2 = {
    "address": {
        "city": "Oberlin",
        "country_code": "US",
        "post_code": "44074",
        "state": "OH",
        "street": "489 College St."
    },
    "email": TEST_EMAIL_2,
    "first_name": "Obie",
    "last_name": "Dobie",
    KIT_NAME_KEY: EXISTING_KIT_NAME_2
}

SOURCE_ID_1 = "9fba75a5-6fbf-42be-9624-731b6a9a161a"

DUMMY_HUMAN_SOURCE = {
                'source_name': 'Bo',
                'source_type': 'human',
                'consent': {
                    'participant_email': 'bo@bo.com',
                    'age_range': "18-plus"
                },
            }
DUMMY_CONSENT_DATE = datetime.datetime.strptime('Jun 1 2005', '%b %d %Y')

ACCT_ID_KEY = "account_id"
ACCT_TYPE_KEY = "account_type"
ACCT_TYPE_VAL = "standard"

ACCT_MOCK_ISS = "MrUnitTest.go"
ACCT_MOCK_SUB = "NotARealSub"
ACCT_MOCK_ISS_2 = "NewPhone"
ACCT_MOCK_SUB_2 = "WhoDis"

SOURCE_ID_KEY = 'source_id'

MOCK_HEADERS = {"Authorization": "Bearer mockone"}
FAKE_TOKEN_IMPOSTOR = "mockimpostor"
FAKE_TOKEN_EMAIL_MISMATCH = "mockemailmismatch"


def make_headers(fake_token):
    return {"Authorization": "Bearer %s" % fake_token}


def mock_verify(token):
    if token == "mockone":
        return {
            'email': TEST_EMAIL,
            'iss': ACCT_MOCK_ISS,
            'sub': ACCT_MOCK_SUB
        }
    elif token == FAKE_TOKEN_EMAIL_MISMATCH:
        return {
            'email': TEST_EMAIL_2,
            'iss': ACCT_MOCK_ISS,
            'sub': ACCT_MOCK_SUB
        }
    elif token == FAKE_TOKEN_IMPOSTOR:
        return {
            'email': 'impostor@test.com',
            'iss': 'impostor',
            'sub': 'animpostor'
        }
    else:
        raise ValueError("Unrecognized mock token")


CREATION_TIME_KEY = "creation_time"
UPDATE_TIME_KEY = "update_time"


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


def extract_last_id_from_location_header(response):
    last_path_id = None
    try:
        loc = response.headers.get("Location")
        url = werkzeug.urls.url_parse(loc)
        last_path_id = url.path.split('/')[-1]
    finally:
        return last_path_id


def delete_dummy_accts():
    with Transaction() as t:
        source_repo = SourceRepo(t)
        survey_answers_repo = SurveyAnswersRepo(t)
        sources = source_repo.get_sources_in_account(ACCT_ID_1)
        for curr_source in sources:
            answers = survey_answers_repo.list_answered_surveys(
                ACCT_ID_1, curr_source.id)
            for survey_id in answers:
                survey_answers_repo.delete_answered_survey(
                    ACCT_ID_1, survey_id)

            source_repo.delete_source(ACCT_ID_1, curr_source.id)

        acct_repo = AccountRepo(t)
        acct_repo.delete_account(ACCT_ID_1)
        acct_repo.delete_account(ACCT_ID_2)
        # Belt and suspenders: these test emails are used by some tests outside
        # of this module as well, so can't be sure they are paired with the
        # above dummy account ids
        acct_repo.delete_account_by_email(TEST_EMAIL)
        acct_repo.delete_account_by_email(TEST_EMAIL_2)
        t.commit()


def create_dummy_acct(create_dummy_1=True,
                      iss=ACCT_MOCK_ISS,
                      sub=ACCT_MOCK_SUB):
    with Transaction() as t:
        dummy_acct_id = _create_dummy_acct_from_t(t, create_dummy_1, iss, sub)
        t.commit()

    return dummy_acct_id


def create_dummy_source(name, source_type, content_dict, create_dummy_1=True,
                        iss=ACCT_MOCK_ISS,
                        sub=ACCT_MOCK_SUB):
    with Transaction() as t:
        dummy_acct_id, dummy_source_id = _create_dummy_source_from_t(
            t, name, source_type, content_dict, create_dummy_1, iss, sub)
        t.commit()

    return dummy_acct_id, dummy_source_id


def _create_dummy_acct_from_t(t, create_dummy_1=True,
                              iss=ACCT_MOCK_ISS,
                              sub=ACCT_MOCK_SUB):
    if create_dummy_1:
        dummy_acct_id = ACCT_ID_1
        dict_to_copy = DUMMY_ACCT_INFO
    else:
        dummy_acct_id = ACCT_ID_2
        dict_to_copy = DUMMY_ACCT_INFO_2

    input_obj = copy.deepcopy(dict_to_copy)
    input_obj["id"] = dummy_acct_id
    acct_repo = AccountRepo(t)
    acct_repo.create_account(Account.from_dict(input_obj,
                                               iss,
                                               sub))

    return dummy_acct_id


def _create_dummy_source_from_t(t, name, source_type, content_dict,
                                create_dummy_1=True,
                                iss=ACCT_MOCK_ISS, sub=ACCT_MOCK_SUB):

    dummy_source_id = SOURCE_ID_1
    dummy_acct_id = _create_dummy_acct_from_t(t, create_dummy_1, iss, sub)
    source_repo = SourceRepo(t)
    if source_type == Source.SOURCE_TYPE_HUMAN:
        dummy_info_obj = HumanInfo.from_dict(content_dict, DUMMY_CONSENT_DATE,
                                             None)
    else:
        dummy_info_obj = NonHumanInfo.from_dict(content_dict)

    source_repo.create_source(Source(dummy_source_id, dummy_acct_id,
                                     source_type, name,
                                     dummy_info_obj))

    return dummy_acct_id, dummy_source_id
# endregion help methods


# We will mock out the jwt verification, but not the iss/sub validation,
# this means the tests have to send the right headers for the right account
@pytest.fixture(scope="class")
def client(request):
    app = microsetta_private_api.server.build_app()
    app.app.testing = True
    with app.app.test_client() as client:
        request.cls.client = client
        with patch("microsetta_private_api.api.implementation."
                   "verify_authrocket") as mock_v:
            mock_v.side_effect = mock_verify
            yield client


@pytest.mark.usefixtures("client")
class ApiTests(TestCase):
    default_querystring_dict = {
        localization.LANG_TAG_KEY: localization.EN_US
    }

    dummy_auth = MOCK_HEADERS

    default_lang_querystring = "{0}={1}".format(localization.LANG_TAG_KEY,
                                                localization.EN_US)

    def setUp(self):
        app = microsetta_private_api.server.build_app()
        self.client = app.app.test_client()
        # This isn't perfect, due to possibility of exceptions being thrown
        # is there some better pattern I can use to split up what should be
        # a 'with' call?
        self.client.__enter__()
        delete_dummy_accts()

    def tearDown(self):
        # This isn't perfect, due to possibility of exceptions being thrown
        # is there some better pattern I can use to split up what should be
        # a 'with' call?
        self.client.__exit__(None, None, None)
        delete_dummy_accts()

    def run_query_and_content_required_field_test(self, url, action,
                                                  valid_query_dict,
                                                  valid_content_dict=None):

        if valid_content_dict is None:
            valid_content_dict = {}
        dicts_to_test = {QUERY_KEY: valid_query_dict,
                         CONTENT_KEY: valid_content_dict}

        for curr_dict_type, dict_to_test in dicts_to_test.items():
            curr_query_dict = valid_query_dict
            curr_content_dict = valid_content_dict
            curr_expected_msg = None

            field_deleter = dictionary_mangler(dict_to_test,
                                               delete_fields=True)

            for curr_mangled_dict in field_deleter:
                if curr_dict_type == QUERY_KEY:
                    curr_query_dict = curr_mangled_dict
                    curr_expected_msg = "Missing query parameter "
                elif curr_dict_type == CONTENT_KEY:
                    curr_content_dict = curr_mangled_dict
                    curr_expected_msg = "is a required property"

                curr_query_str = urlencode(curr_query_dict)
                curr_content_json = json.dumps(curr_content_dict)
                curr_url = url if not curr_query_str else \
                    '{0}?{1}'.format(url, curr_query_str)
                if action == "get":
                    response = self.client.get(
                        curr_url,
                        headers=self.dummy_auth)
                elif action == "post":
                    response = self.client.post(
                        curr_url,
                        headers=self.dummy_auth,
                        content_type='application/json',
                        data=curr_content_json)
                elif action == "put":
                    response = self.client.put(
                        curr_url,
                        headers=self.dummy_auth,
                        content_type='application/json',
                        data=curr_content_json)
                else:
                    raise ValueError(format("unexpect request action: ",
                                            action))

                self.assertEqual(400, response.status_code)
                resp_obj = json.loads(response.data)
                self.assertTrue(curr_expected_msg in resp_obj['detail'])
            # next deleted field
        # next dict to test

    def validate_dummy_acct_response_body(self, response_obj,
                                          dummy_acct_dict=None):
        if dummy_acct_dict is None:
            dummy_acct_dict = DUMMY_ACCT_INFO

        # check expected additional fields/values appear in response body:
        # Note that "d.get()" returns none if key not found, doesn't throw err
        real_acct_id_from_body = response_obj.get(ACCT_ID_KEY)
        self.assertIsNotNone(real_acct_id_from_body)

        real_acct_type = response_obj.get(ACCT_TYPE_KEY)
        self.assertEqual(ACCT_TYPE_VAL, real_acct_type)

        real_creation_time = response_obj.get(CREATION_TIME_KEY)
        self.assertIsNotNone(real_creation_time)

        real_update_time = response_obj.get(UPDATE_TIME_KEY)
        self.assertIsNotNone(real_update_time)

        # check all input fields/values appear in response body EXCEPT kit_name
        # plus additional fields
        expected_dict = copy.deepcopy(dummy_acct_dict)
        try:
            expected_dict.pop(KIT_NAME_KEY)
        except KeyError:
            # is ok if input did not have a kit name, as this is
            # provided on account create but not account update
            pass
        expected_dict[ACCT_ID_KEY] = real_acct_id_from_body
        expected_dict[ACCT_TYPE_KEY] = ACCT_TYPE_VAL
        expected_dict[CREATION_TIME_KEY] = real_creation_time
        expected_dict[UPDATE_TIME_KEY] = real_update_time
        self.assertEqual(expected_dict, response_obj)

        return real_acct_id_from_body


@pytest.mark.usefixtures("client")
class AccountsTests(ApiTests):
    accounts_url = '/api/accounts?%s' % ApiTests.default_lang_querystring

    # region accounts create/post tests
    def test_accounts_create_success(self):
        """Successfully create a new account"""

        # create post input json
        input_json = json.dumps(DUMMY_ACCT_INFO)

        # execute accounts post (create)
        response = self.client.post(
            self.accounts_url,
            content_type='application/json',
            data=input_json,
            headers=MOCK_HEADERS
        )

        # check response code
        self.assertEqual(201, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)

        # check all elements of account object in body are correct
        real_acct_id_from_body = self.validate_dummy_acct_response_body(
            response_obj)

        # check location header was provided, with new acct id
        real_acct_id_from_loc = extract_last_id_from_location_header(response)
        self.assertIsNotNone(real_acct_id_from_loc)

        # check account id provided in body matches that in location header
        self.assertTrue(real_acct_id_from_loc, real_acct_id_from_body)

    def test_accounts_create_fail_400_without_required_fields(self):
        """Return 400 validation fail if don't provide a required field """

        self.run_query_and_content_required_field_test(
            "/api/accounts", "post",
            self.default_querystring_dict,
            DUMMY_ACCT_INFO)

    def test_accounts_create_fail_404(self):
        """Return 404 if provided kit name is not found in db."""

        # create post input json
        input_obj = copy.deepcopy(DUMMY_ACCT_INFO)
        input_obj[KIT_NAME_KEY] = MISSING_KIT_NAME
        input_json = json.dumps(input_obj)

        # execute accounts post (create)
        response = self.client.post(
            self.accounts_url,
            content_type='application/json',
            data=input_json,
            headers=MOCK_HEADERS
        )

        # check response code
        self.assertEqual(404, response.status_code)

    def test_accounts_create_fail_422(self):
        """Return 422 if provided email is in use in db."""

        # NB: I would rather do this with an email already in use in the
        # test db, but it appears the test db emails have been randomized
        # into strings that won't pass the api's email format validation :(

        # create a dummy account with email 1
        create_dummy_acct(create_dummy_1=True)

        # Now try to create a new account that is different in all respects
        # from the dummy made with email 1 EXCEPT that it has the same email
        test_acct_info = copy.deepcopy(DUMMY_ACCT_INFO_2)
        test_acct_info["email"] = TEST_EMAIL

        # create post input json
        input_json = json.dumps(test_acct_info)

        # execute accounts post (create)
        response = self.client.post(
            self.accounts_url,
            content_type='application/json',
            data=input_json,
            headers=MOCK_HEADERS
        )

        # check response code
        self.assertEqual(422, response.status_code)
    # endregion accounts create/post tests

    # region accounts/legacies post tests
    def test_accounts_legacies_post_success(self):
        """Successfully claim a legacy account for the current user"""

        create_dummy_acct(create_dummy_1=True, iss=None, sub=None)

        # execute accounts/legacies post (claim legacy account)
        url = '/api/accounts/legacies?%s' % self.default_lang_querystring
        response_1 = self.client.post(url, headers=MOCK_HEADERS)

        # check response code
        self.assertEqual(200, response_1.status_code)

        # load the response body
        response_obj_1 = json.loads(response_1.data)
        self.assertEqual(1, len(response_obj_1))

        # check all elements of account object in body are correct
        self.validate_dummy_acct_response_body(response_obj_1[0])

        # try to reclaim the same account
        response_2 = self.client.post(url, headers=MOCK_HEADERS)

        # check response is now a 200 but with an empty list
        self.assertEqual(200, response_2.status_code)

        # load the response body
        response_obj_2 = json.loads(response_2.data)
        self.assertEqual(0, len(response_obj_2))

    def test_accounts_legacies_post_success_empty_no_email(self):
        """Return empty list if no account with given email in token exists"""

        # do NOT create the dummy account--and check for a legacy account
        # containing that email (via the MOCK_HEADERS, which link to a fake
        # token containing TEST_EMAIL as its email claim)

        # execute accounts/legacies post (claim legacy account)
        url = '/api/accounts/legacies?%s' % self.default_lang_querystring
        response = self.client.post(url, headers=MOCK_HEADERS)

        # check response code
        self.assertEqual(200, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)
        self.assertEqual(0, len(response_obj))

    def test_accounts_legacies_post_success_empty_already_claimed(self):
        """Return empty list if account with email already is claimed."""

        create_dummy_acct(create_dummy_1=True)

        # execute accounts/legacies post (claim legacy account)
        url = '/api/accounts/legacies?%s' % self.default_lang_querystring
        response = self.client.post(url, headers=MOCK_HEADERS)

        # load the response body
        response_obj = json.loads(response.data)
        self.assertEqual(0, len(response_obj))

    def test_accounts_legacies_post_fail_422(self):
        """Return 422 if info in db somehow prevents claiming legacy"""

        # It is invalid to have one of the auth fields (e.g. sub)
        # be null while the other is filled.
        create_dummy_acct(create_dummy_1=True, iss=ACCT_MOCK_ISS,
                          sub=None)

        # execute accounts/legacies post (claim legacy account)
        url = '/api/accounts/legacies?%s' % self.default_lang_querystring
        response = self.client.post(url, headers=MOCK_HEADERS)

        # check response code
        self.assertEqual(422, response.status_code)

    # endregion accounts/legacies post tests


@pytest.mark.usefixtures("client")
class AccountTests(ApiTests):

    # region account view/get tests
    def test_account_view_success(self):
        """Successfully view existing account"""
        dummy_acct_id = create_dummy_acct(create_dummy_1=True)

        response = self.client.get(
            '/api/accounts/%s?%s' %
            (dummy_acct_id, self.default_lang_querystring),
            headers=self.dummy_auth)

        # check response code
        self.assertEqual(200, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)

        # check all elements of account object in body are correct
        self.validate_dummy_acct_response_body(response_obj)

    def test_account_view_fail_400_without_required_fields(self):
        """Return 400 validation fail if don't provide a required field """

        dummy_acct_id = create_dummy_acct()

        input_url = "/api/accounts/{0}".format(dummy_acct_id)
        self.run_query_and_content_required_field_test(
            input_url, "get",
            self.default_querystring_dict)

    def test_account_view_fail_401(self):
        """Return 401 if user does not have access to provided account."""

        dummy_acct_id = create_dummy_acct(create_dummy_1=True)

        response = self.client.get(
            '/api/accounts/%s?%s' %
            (dummy_acct_id, self.default_lang_querystring),
            headers=make_headers(FAKE_TOKEN_IMPOSTOR))

        # check response code
        self.assertEqual(response.status_code, 401)

    def test_account_view_fail_404(self):
        """Return 404 if provided account id is not found in db."""

        response = self.client.get(
            '/api/accounts/%s?%s' %
            (MISSING_ACCT_ID, self.default_lang_querystring),
            headers=self.dummy_auth)

        # check response code
        self.assertEqual(response.status_code, 404)
    # endregion account view/get tests

    # region account update/put tests
    @staticmethod
    def make_updated_acct_dict():
        result = copy.deepcopy(DUMMY_ACCT_INFO)
        result.pop(KIT_NAME_KEY)

        result["address"] = {
            "city": "Oakland",
            "country_code": "US",
            "post_code": "99228",
            "state": "CA",
            "street": "641 Queen St. E"
        }

        return result

    def test_account_update_success(self):
        """Successfully update existing account"""
        dummy_acct_id = create_dummy_acct()

        changed_acct_dict = self.make_updated_acct_dict()

        # create post input json
        input_json = json.dumps(changed_acct_dict)

        response = self.client.put(
            '/api/accounts/%s?%s' %
            (dummy_acct_id, self.default_lang_querystring),
            headers=self.dummy_auth,
            content_type='application/json',
            data=input_json)

        # check response code
        self.assertEqual(200, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)

        # check all elements of account object in body are correct
        self.validate_dummy_acct_response_body(response_obj,
                                               changed_acct_dict)

    def test_account_update_fail_400_without_required_fields(self):
        """Return 400 validation fail if don't provide a required field """

        dummy_acct_id = create_dummy_acct()
        changed_acct_dict = self.make_updated_acct_dict()

        input_url = "/api/accounts/{0}".format(dummy_acct_id)
        self.run_query_and_content_required_field_test(
            input_url, "put",
            self.default_querystring_dict,
            changed_acct_dict)

    def test_account_update_fail_404(self):
        """Return 404 if provided account id is not found in db."""

        changed_acct_dict = self.make_updated_acct_dict()

        # create post input json
        input_json = json.dumps(changed_acct_dict)

        response = self.client.put(
            '/api/accounts/%s?%s' %
            (MISSING_ACCT_ID, self.default_lang_querystring),
            headers=self.dummy_auth,
            content_type='application/json',
            data=input_json)

        # check response code
        self.assertEqual(response.status_code, 404)

    def test_account_update_fail_422(self):
        """Return 422 if provided email is in use in db."""

        # NB: I would rather do this with an email already in use in the
        # test db, but it appears the test db emails have been randomized
        # into strings that won't pass the api's email format validation :(

        # create an account with email 1
        dummy_acct_id = create_dummy_acct(create_dummy_1=True)

        # create an account with email 2
        create_dummy_acct(create_dummy_1=False, iss=ACCT_MOCK_ISS_2,
                          sub=ACCT_MOCK_SUB_2)

        # Now try to update the account made with email 1 with info that is
        # the same in all respects as those it was made with EXCEPT that it has
        # an email that is now in use by the account with email 2:
        changed_dummy_acct = copy.deepcopy(DUMMY_ACCT_INFO)
        changed_dummy_acct["email"] = TEST_EMAIL_2

        # create post input json
        input_json = json.dumps(changed_dummy_acct)

        response = self.client.put(
            '/api/accounts/%s?%s' %
            (dummy_acct_id, self.default_lang_querystring),
            headers=MOCK_HEADERS,
            content_type='application/json',
            data=input_json)

        # check response code
        self.assertEqual(422, response.status_code)
    # endregion account update/put tests

    # region account/email_match tests
    def test_email_match_success_true(self):
        """Returns true if account email matches auth email"""
        dummy_acct_id = create_dummy_acct(create_dummy_1=True)

        response = self.client.get(
            '/api/accounts/%s/email_match?%s' %
            (dummy_acct_id, self.default_lang_querystring),
            headers=self.dummy_auth)

        # check response code
        self.assertEqual(200, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)

        # check email_match is true
        self.assertEqual(response_obj["email_match"], True)

    def test_email_match_success_false(self):
        """Returns false if account email matches auth email"""
        dummy_acct_id = create_dummy_acct(create_dummy_1=True)

        response = self.client.get(
            '/api/accounts/%s/email_match?%s' %
            (dummy_acct_id, self.default_lang_querystring),
            headers=make_headers(FAKE_TOKEN_EMAIL_MISMATCH))

        # check response code
        self.assertEqual(200, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)

        # check email_match is true
        self.assertEqual(response_obj["email_match"], False)

    def test_email_match_fail_401(self):
        """Return 401 if user does not have access to provided account."""

        dummy_acct_id = create_dummy_acct(create_dummy_1=True)

        response = self.client.get(
            '/api/accounts/%s/email_match?%s' %
            (dummy_acct_id, self.default_lang_querystring),
            headers=make_headers(FAKE_TOKEN_IMPOSTOR))

        # check response code
        self.assertEqual(response.status_code, 401)

    def test_email_match_fail_404(self):
        """Return 404 if provided account id is not found in db."""

        response = self.client.get(
            '/api/accounts/%s/email_match?%s' %
            (MISSING_ACCT_ID, self.default_lang_querystring),
            headers=self.dummy_auth)

        # check response code
        self.assertEqual(response.status_code, 404)
    # endregion account/email_match tests


@pytest.mark.usefixtures("client")
class SourceTests(ApiTests):

    # region source view/get tests
    def test_source_view_success(self):
        """Successfully view existing human source"""
        dummy_acct_id, dummy_source_id = create_dummy_source(
            "Bo", Source.SOURCE_TYPE_HUMAN, DUMMY_HUMAN_SOURCE,
            create_dummy_1=True)

        response = self.client.get(
            '/api/accounts/%s/sources?%s' %
            (dummy_acct_id, self.default_lang_querystring),
            headers=self.dummy_auth)

        # check response code
        self.assertEqual(200, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)
        self.assertEqual(1, len(response_obj))

        # check all elements of object in body are correct
        expected_val = copy.deepcopy(DUMMY_HUMAN_SOURCE)
        expected_val[SOURCE_ID_KEY] = SOURCE_ID_1
        self.assertEqual([expected_val], response_obj)

    def test_source_view_success_legacy(self):
        """Successfully view existing human source with legacy age_range"""
        dummy_legacy_source = copy.deepcopy(DUMMY_HUMAN_SOURCE)
        # this would not be allowed through the api, but we can force it here
        dummy_legacy_source["consent"]["age_range"] = "legacy"
        dummy_acct_id, dummy_source_id = create_dummy_source(
            "Bo", Source.SOURCE_TYPE_HUMAN, dummy_legacy_source,
            create_dummy_1=True)

        response = self.client.get(
            '/api/accounts/%s/sources?%s' %
            (dummy_acct_id, self.default_lang_querystring),
            headers=self.dummy_auth)

        # check response code
        self.assertEqual(200, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)
        self.assertEqual(1, len(response_obj))

        # check all elements of object in body are correct
        expected_val = copy.deepcopy(dummy_legacy_source)
        expected_val[SOURCE_ID_KEY] = SOURCE_ID_1
        self.assertEqual([expected_val], response_obj)
    # endregion

    # region source create/post
    def test_source_create_success(self):
        """Successfully create a new human source"""
        dummy_acct_id = create_dummy_acct(create_dummy_1=True)

        response = self.client.post(
            '/api/accounts/%s/sources?%s' %
            (dummy_acct_id, self.default_lang_querystring),
            content_type='application/json',
            data=json.dumps(DUMMY_HUMAN_SOURCE),
            headers=self.dummy_auth
        )

        # check response code
        self.assertEqual(201, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)

        # get the id provided in the body
        real_src_id_from_body = response_obj.get(SOURCE_ID_KEY)

        # check location header was provided, with new source id
        real_src_id_from_loc = extract_last_id_from_location_header(response)
        self.assertIsNotNone(real_src_id_from_loc)

        # check id provided in body matches that in location header
        self.assertTrue(real_src_id_from_loc, real_src_id_from_body)

        # check all elements of object in body are correct
        expected_val = copy.deepcopy(DUMMY_HUMAN_SOURCE)
        expected_val[SOURCE_ID_KEY] = real_src_id_from_body
        self.assertEqual(expected_val, response_obj)

    def test_source_create_fail_422(self):
        """Return 422 if try to create a source with age_range 'legacy'"""
        dummy_acct_id = create_dummy_acct(create_dummy_1=True)

        bad_dummy_src_info = copy.deepcopy(DUMMY_HUMAN_SOURCE)
        bad_dummy_src_info['consent']['age_range'] = 'legacy'

        response = self.client.post(
            '/api/accounts/%s/sources?%s' %
            (dummy_acct_id, self.default_lang_querystring),
            content_type='application/json',
            data=json.dumps(bad_dummy_src_info),
            headers=self.dummy_auth
        )

        # check response code
        self.assertEqual(422, response.status_code)
    # endregion source create/post

    # region source update/put
    def test_source_update_success(self):
        """Successfully update an existing source"""
        dummy_acct_id, dummy_source_id = create_dummy_source(
            "Bo", Source.SOURCE_TYPE_HUMAN, DUMMY_HUMAN_SOURCE,
            create_dummy_1=True)

        new_name = "Not Bo after all"
        dummy_src_info = copy.deepcopy(DUMMY_HUMAN_SOURCE)
        dummy_src_info['source_name'] = new_name
        # value not allowed, but it will be ignored anyway
        dummy_src_info['consent']['age_range'] = 'legacy'

        response = self.client.put(
            '/api/accounts/%s/sources/%s?%s' %
            (dummy_acct_id, dummy_source_id, self.default_lang_querystring),
            content_type='application/json',
            data=json.dumps(dummy_src_info),
            headers=self.dummy_auth
        )

        # check response code
        self.assertEqual(200, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)

        # get the id provided in the body
        real_src_id_from_body = response_obj.get(SOURCE_ID_KEY)

        # check all elements of object in body are correct
        expected_val = copy.deepcopy(DUMMY_HUMAN_SOURCE)
        expected_val['source_name'] = new_name
        expected_val[SOURCE_ID_KEY] = real_src_id_from_body
        self.assertEqual(expected_val, response_obj)
    # endregion source update/put


@pytest.mark.usefixtures("client")
class SurveyTests(ApiTests):

    # region source create/post
    def test_survey_create_success(self):
        """Successfully create a new answered survey"""
        dummy_acct_id, dummy_source_id = create_dummy_source(
            "Bo", Source.SOURCE_TYPE_HUMAN, DUMMY_HUMAN_SOURCE,
            create_dummy_1=True)

        survey_template_id = 1  # primary survey
        # This is a model of a partially-filled survey that includes
        # a single-select field, a multi-select field with multiple
        # entries selected, an input field required to be an integer,
        # an input field required to be single-line string, and a text field
        # including a line break
        input_model = {'6': 'Yes',
                       '30': ['Red wine', 'Spirits/hard alcohol'],
                       '104': 'candy corn\ngreen m&ms',
                       '107': 'Female',
                       '108': 68,
                       '109': 'inches',
                       '115': 'K7G-2G8'}

        post_resp = self.client.post(
            '/api/accounts/%s/sources/%s/surveys?%s'
            % (dummy_acct_id, dummy_source_id, self.default_lang_querystring),
            content_type='application/json',
            data=json.dumps(
                {
                    'survey_template_id': survey_template_id,
                    'survey_text': input_model
                }),
            headers=self.dummy_auth
        )

        # check response code
        self.assertEqual(201, post_resp.status_code)

        # check location header was provided, with new survey id
        real_id_from_loc = extract_last_id_from_location_header(post_resp)
        self.assertIsNotNone(real_id_from_loc)

        # load that new survey and ensure it matches the expected contents
        get_resp = self.client.get(
            '%s?%s' %
            (post_resp.headers.get("Location"), self.default_lang_querystring),
            headers=self.dummy_auth)

        # check response code
        self.assertEqual(200, get_resp.status_code)

        # load the response body
        get_resp_obj = json.loads(get_resp.data)

        # check all elements of object in body are correct
        expected_model = copy.deepcopy(input_model)
        # TODO: determine whether the current behavior that returns
        #  fields input as numbers as strings is actually correct or not
        expected_model['108'] = "68"
        expected_output = {
            "survey_template_id": survey_template_id,
            "survey_template_title": "Primary",
            "survey_template_version": "1.0",
            "survey_template_type": "local",
            "survey_id": real_id_from_loc,
            "survey_text": expected_model
        }
        self.assertEqual(expected_output, get_resp_obj)

    def test_survey_create_success_empty(self):
        """Successfully create a new answered survey without any answers"""
        dummy_acct_id, dummy_source_id = create_dummy_source(
            "Bo", Source.SOURCE_TYPE_HUMAN, DUMMY_HUMAN_SOURCE,
            create_dummy_1=True)

        survey_template_id = 1  # primary survey

        post_resp = self.client.post(
            '/api/accounts/%s/sources/%s/surveys?%s'
            % (dummy_acct_id, dummy_source_id, self.default_lang_querystring),
            content_type='application/json',
            data=json.dumps(
                {
                    'survey_template_id': survey_template_id,
                    'survey_text': {}
                }),
            headers=self.dummy_auth
        )

        # check response code
        self.assertEqual(201, post_resp.status_code)

        # check location header was provided, with new survey id
        real_id_from_loc = extract_last_id_from_location_header(post_resp)
        self.assertIsNotNone(real_id_from_loc)

        # load that new survey and ensure it matches the expected contents
        get_resp = self.client.get(
            '%s?%s' %
            (post_resp.headers.get("Location"), self.default_lang_querystring),
            headers=self.dummy_auth)

        # check response code
        self.assertEqual(200, get_resp.status_code)

        # load the response body
        get_resp_obj = json.loads(get_resp.data)

        # check all elements of object in body are correct
        expected_model = {'108': ""}
        expected_output = {
            "survey_template_id": survey_template_id,
            "survey_template_title": "Primary",
            "survey_template_version": "1.0",
            "survey_template_type": "local",
            "survey_id": real_id_from_loc,
            "survey_text": expected_model
        }
        self.assertEqual(expected_output, get_resp_obj)
