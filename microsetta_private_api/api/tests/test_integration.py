import pytest
import microsetta_private_api.server
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.model.account import Account
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.model.source import \
    Source, HumanInfo, AnimalInfo, EnvironmentInfo
import datetime
import json
from unittest import TestCase

ACCT_ID = "aaaaaaaa-bbbb-cccc-dddd-eeeeffffffff"
HUMAN_ID = "b0b0b0b0-b0b0-b0b0-b0b0-b0b0b0b0b0b0"
DOGGY_ID = "dddddddd-dddd-dddd-dddd-dddddddddddd"
PLANTY_ID = "eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee"


@pytest.fixture(scope="class")
def client(request):
    IntegrationTests.setup_test_data()
    app = microsetta_private_api.server.build_app()
    with app.app.test_client() as client:
        request.cls.client = client
        yield client
    IntegrationTests.teardown_test_data()


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

            # Clean up any possible leftovers from failed tests
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
                          {
                              "street": "123 Dan Lane",
                              "city": "Danville",
                              "state": "CA",
                              "post_code": 12345,
                              "country_code": "US"
                          })
            acct_repo.create_account(acc)

            source_repo.create_source(Source.create_human(
                HUMAN_ID,
                ACCT_ID,
                HumanInfo("Bo", "bo@bo.com", False, "Mr Bo", "Mrs Bo",
                          False, datetime.datetime.utcnow(), None, "Mr. Obtainer",
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

            t.commit()

    @staticmethod
    def teardown_test_data():
        with Transaction() as t:
            acct_repo = AccountRepo(t)
            source_repo = SourceRepo(t)
            source_repo.delete_source(ACCT_ID, DOGGY_ID)
            source_repo.delete_source(ACCT_ID, PLANTY_ID)
            source_repo.delete_source(ACCT_ID, HUMAN_ID)
            acct_repo.delete_account(ACCT_ID)

            t.commit()

    def test_get_sources(self):
        resp = self.client.get('/api/accounts/%s/sources' % ACCT_ID).data
        sources = json.loads(resp)
        assert len([x for x in sources if x['source_name'] == 'Bo']) == 1
        assert len([x for x in sources if x['source_name'] == 'Doggy']) == 1
        assert len([x for x in sources if x['source_name'] == 'Planty']) == 1

    def test_surveys(self):
        resp = self.client.get('/api/accounts/%s/sources' % ACCT_ID).data

        sources = json.loads(resp)
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

    # def test_create_new_account(self):
    #     """ Test: Create a new account using a kit id """
    #     response = self.client.post(
    #         '/api/accounts',
    #         content_type='application/json',
    #         data=json.dumps(),
    #
    #
    #     cls.client.post()