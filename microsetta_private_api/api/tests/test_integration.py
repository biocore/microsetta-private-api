import pytest
import werkzeug

import microsetta_private_api.server
from microsetta_private_api.repo.kit_repo import KitRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.model.account import Account
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo
from microsetta_private_api.model.source import \
    Source, HumanInfo, AnimalInfo, EnvironmentInfo
from microsetta_private_api.model.address import Address
import datetime
import json
from unittest import TestCase

ACCT_ID = "aaaaaaaa-bbbb-cccc-dddd-eeeeffffffff"
HUMAN_ID = "b0b0b0b0-b0b0-b0b0-b0b0-b0b0b0b0b0b0"
DOGGY_ID = "dddddddd-dddd-dddd-dddd-dddddddddddd"
PLANTY_ID = "eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee"

SUPPLIED_KIT_ID = "FooFooFoo"


@pytest.fixture(scope="class")
def client(request):
    IntegrationTests.setup_test_data()
    app = microsetta_private_api.server.build_app()
    app.app.testing = True
    with app.app.test_client() as client:
        request.cls.client = client
        yield client
    IntegrationTests.teardown_test_data()


def check_response(response, expected_status=None):
    if expected_status is not None:
        assert response.status_code == expected_status
    elif response.status_code >= 400:
        raise Exception("Scary response code: " + str(response.status_code))

    resp_obj = json.loads(response.data)
    if isinstance(resp_obj, dict) and "message" in resp_obj:
        msg = resp_obj["message"].lower()
        if "not" in msg and "implemented" in msg:
            raise Exception(response.data)


def fuzz(val):
    """ A fuzzer for json data """
    if isinstance(val, int):
        return val + 7
    if isinstance(val, str):
        return "FUZ" + val + "ZY"
    if isinstance(val, list):
        return ["Q(*.*)Q"] + [fuzz(x) for x in val] + ["P(*.*)p"]
    if isinstance(val, dict):
        fuzzy = {x: fuzz(y) for x, y in val}
        fuzzy['account_type'] = "Voldemort"
        return fuzzy


def fuzz_field(field, model):
    if field['type'] == "input" or field['type'] == "textArea":
        model[field['id']] = 'bo'
    if field['type'] == "select":
        model[field['id']] = field['values'][0]
    if field['type'] == 'checklist':
        model[field['id']] = [field['values'][0]]


def fuzz_form(form):
    """ Fills in a vue form with junk data """
    model = {}
    if form['fields'] is not None:
        for field in form['fields']:
            fuzz_field(field, model)
    if form['groups'] is not None:
        for group in form['groups']:
            if group['fields'] is not None:
                for field in group['fields']:
                    fuzz_field(field, model)
    return model


@pytest.mark.usefixtures("client")
class IntegrationTests(TestCase):
    def setUp(self):
        IntegrationTests.setup_test_data()
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
        IntegrationTests.teardown_test_data()

    @staticmethod
    def json_converter(o):
        if isinstance(o, datetime.datetime):
            return str(o)
        return o.__dict__

    @staticmethod
    def setup_test_data():
        with Transaction() as t:
            acct_repo = AccountRepo(t)
            source_repo = SourceRepo(t)
            kit_repo = KitRepo(t)
            survey_answers_repo = SurveyAnswersRepo(t)

            # Clean up any possible leftovers from failed tests
            kit_repo.remove_mock_kit()

            answers = survey_answers_repo.list_answered_surveys(ACCT_ID,
                                                                HUMAN_ID)
            for survey_id in answers:
                survey_answers_repo.delete_answered_survey(ACCT_ID, survey_id)
            source_repo.delete_source(ACCT_ID, DOGGY_ID)
            source_repo.delete_source(ACCT_ID, PLANTY_ID)
            source_repo.delete_source(ACCT_ID, HUMAN_ID)
            acct_repo.delete_account(ACCT_ID)

            # Set up test account with sources
            acc = Account(ACCT_ID,
                          "foo@baz.com",
                          "standard",
                          "GLOBUS",
                          "Dan",
                          "H",
                          Address(
                              "123 Dan Lane",
                              "Danville",
                              "CA",
                              12345,
                              "US"
                          ))
            acct_repo.create_account(acc)

            source_repo.create_source(Source.create_human(
                HUMAN_ID,
                ACCT_ID,
                HumanInfo("Bo", "bo@bo.com", False, "Mr Bo", "Mrs Bo",
                          False, datetime.datetime.utcnow(), None,
                          "Mr. Obtainer",
                          "18-plus")
            ))
            source_repo.create_source(Source.create_animal(
                DOGGY_ID,
                ACCT_ID,
                AnimalInfo("Doggy")))
            source_repo.create_source(Source.create_environment(
                PLANTY_ID,
                ACCT_ID,
                EnvironmentInfo("Planty", "The green one")))

            kit_repo.create_mock_kit(SUPPLIED_KIT_ID)

            t.commit()

    @staticmethod
    def teardown_test_data():
        with Transaction() as t:
            acct_repo = AccountRepo(t)
            source_repo = SourceRepo(t)
            kit_repo = KitRepo(t)
            kit_repo.remove_mock_kit()
            source_repo.delete_source(ACCT_ID, DOGGY_ID)
            source_repo.delete_source(ACCT_ID, PLANTY_ID)
            source_repo.delete_source(ACCT_ID, HUMAN_ID)
            acct_repo.delete_account(ACCT_ID)

            t.commit()

    def test_get_sources(self):
        resp = self.client.get(
            '/api/accounts/%s/sources?language_tag=en_us' % ACCT_ID)
        check_response(resp)
        sources = json.loads(resp.data)
        assert len([x for x in sources if x['source_name'] == 'Bo']) == 1
        assert len([x for x in sources if x['source_name'] == 'Doggy']) == 1
        assert len([x for x in sources if x['source_name'] == 'Planty']) == 1

    def test_surveys(self):
        resp = self.client.get(
            '/api/accounts/%s/sources?language_tag=en_us' % ACCT_ID)
        check_response(resp)

        sources = json.loads(resp.data)
        bobo = [x for x in sources if x['source_name'] == 'Bo'][0]
        doggy = [x for x in sources if x['source_name'] == 'Doggy'][0]
        env = [x for x in sources if x['source_name'] == 'Planty'][0]

        resp = self.client.get(
            '/api/accounts/%s/sources/%s/survey_templates?language_tag=en_us' %
            (ACCT_ID, bobo['source_id']), )
        bobo_surveys = json.loads(resp.data)
        resp = self.client.get(
            '/api/accounts/%s/sources/%s/survey_templates?language_tag=en_us' %
            (ACCT_ID, doggy['source_id']))
        doggy_surveys = json.loads(resp.data)
        resp = self.client.get(
            '/api/accounts/%s/sources/%s/survey_templates?language_tag=en_us' %
            (ACCT_ID, env['source_id']))
        env_surveys = json.loads(resp.data)

        assert bobo_surveys == [1, 3, 4, 5]
        assert doggy_surveys == [2]
        assert env_surveys == []

    def test_bobo_takes_a_survey(self):
        """
           Check that a user can login to an account,
           list sources,
           pick a source,
           list surveys for that source,
           pick a survey,
           retrieve that survey
           submit answers to that survey
        """
        resp = self.client.get(
            '/api/accounts/%s/sources?language_tag=en_us' % ACCT_ID)
        check_response(resp)
        sources = json.loads(resp.data)
        bobo = [x for x in sources if x['source_name'] == 'Bo'][0]
        resp = self.client.get(
            '/api/accounts/%s/sources/%s/survey_templates?language_tag=en_us' %
            (ACCT_ID, bobo['source_id']))
        bobo_surveys = json.loads(resp.data)
        chosen_survey = bobo_surveys[0]
        resp = self.client.get(
            '/api/accounts/%s/sources/%s/survey_templates/%s'
            '?language_tag=en_us' %
            (ACCT_ID, bobo['source_id'], chosen_survey))
        check_response(resp)

        model = fuzz_form(json.loads(resp.data))
        resp = self.client.post(
            '/api/accounts/%s/sources/%s/surveys?language_tag=en_us'
            % (ACCT_ID, bobo['source_id']),
            content_type='application/json',
            data=json.dumps(
                {
                    'survey_template_id': chosen_survey,
                    'survey_text': model
                })
        )
        check_response(resp, 201)
        loc = resp.headers.get("Location")
        url = werkzeug.urls.url_parse(loc)
        survey_id = url.path.split('/')[-1]

        # TODO: Need a sanity check, is returned Location supposed to specify
        #  query parameters?
        resp = self.client.get(loc + "?language_tag=en_us")
        check_response(resp)
        retrieved_survey = json.loads(resp.data)
        self.assertDictEqual(retrieved_survey, model)

        # Clean up after the new survey
        with Transaction() as t:
            repo = SurveyAnswersRepo(t)
            found = repo.delete_answered_survey(ACCT_ID, survey_id)
            assert found
            t.commit()

    def test_create_new_account(self):

        # Clean up before the test in case we already have a janedoe
        with Transaction() as t:
            AccountRepo(t).delete_account_by_email("janedoe@example.com")
            t.commit()

        """ Test: Create a new account using a kit id """
        acct_json = json.dumps(
            {
                "address": {
                    "city": "Springfield",
                    "country_code": "US",
                    "post_code": "12345",
                    "state": "CA",
                    "street": "123 Main St. E. Apt. 2"
                },
                "email": "janedoe@example.com",
                "first_name": "Jane",
                "last_name": "Doe",
                "kit_name": "jb_qhxqe"
            })

        # First register should succeed
        response = self.client.post(
            '/api/accounts?language_tag=en_us',
            content_type='application/json',
            data=acct_json
        )
        check_response(response)

        # Second should fail with duplicate email 422
        response = self.client.post(
            '/api/accounts?language_tag=en_us',
            content_type='application/json',
            data=acct_json
        )
        check_response(response, 422)

        # Clean up after this test so we don't leave the account around
        with Transaction() as t:
            AccountRepo(t).delete_account_by_email("janedoe@example.com")
            t.commit()

    def test_edit_account_info(self):
        """ Test: Can we edit account information """
        response = self.client.get(
            '/api/accounts/%s?language_tag=en_us' % (ACCT_ID,))
        check_response(response)

        acc = json.loads(response.data)

        regular_data = \
            {
                "address": {
                    "street": "123 Dan Lane",
                    "city": "Danville",
                    "state": "CA",
                    "post_code": 12345,
                    "country_code": "US"
                },
                "email": "foo@baz.com",
                "first_name": "Dan",
                "last_name": "H"
            }

        self.assertDictEqual(acc, regular_data, "Check Initial Account Match")

        fuzzy_data = fuzz(regular_data)

        response = self.client.put(
            '/api/accounts/%s?language_tag=en_us' % (ACCT_ID,),
            content_type='application/json',
            data=json.dumps(fuzzy_data)
        )
        check_response(response)

        acc = json.loads(response.data)
        # TODO: These actually probably shouldn't match exactly.  The api
        #  should only allow writing of certain fields, so need to check those
        #  fields were written and others were left out!!
        self.assertDictEqual(fuzzy_data, acc, "Check Fuzz Account Match")

        response = self.client.put(
            '/api/accounts/%s?language_tag=en_us' % (ACCT_ID,),
            content_type='application/json',
            data=json.dumps(regular_data)
        )
        check_response(response)
        self.assertDictEqual(regular_data, acc, "Check restore to regular")

    def test_add_sample_from_kit(self):
        """ Test:  Can we add a kit to an existing account?
            Note: With the changes in this api, rather than adding a kit
            we instead list the samples in that kit, grab an unassociated one,
            and then associate that sample with our account
        """
        response = self.client.get(
            '/api/kits/?language_tag=en_us&kit_name=%s' % SUPPLIED_KIT_ID)
        check_response(response)

        unused_samples = json.loads(response.data)
        sample_id = unused_samples[0]['sample_id']

        response = self.client.post(
            '/api/accounts/%s/sources/%s/samples?language_tag=en_us' %
            (ACCT_ID, DOGGY_ID),
            content_type='application/json',
            data=json.dumps(
                {
                    "sample_id": sample_id
                })
        )
        check_response(response)

        response = self.client.get(
            '/api/accounts/%s/sources/%s/samples/%s?language_tag=en_us' %
            (ACCT_ID, DOGGY_ID, sample_id)
        )
        print(response)
        check_response(response)
