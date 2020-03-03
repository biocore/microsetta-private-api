import pytest
import werkzeug

import microsetta_private_api.server
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.model.account import Account
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo
from microsetta_private_api.model.source import \
    Source, HumanInfo, AnimalInfo, EnvironmentInfo
from microsetta_private_api.model.address import Address
from microsetta_private_api.util.util import json_converter, fromisotime
import datetime
import json
from unittest import TestCase
from microsetta_private_api.LEGACY.locale_data import american_gut, british_gut
import copy

ACCT_ID = "aaaaaaaa-bbbb-cccc-dddd-eeeeffffffff"
NOT_ACCT_ID = "12341234-1234-1234-1234-123412341234"
HUMAN_ID = "b0b0b0b0-b0b0-b0b0-b0b0-b0b0b0b0b0b0"
BOBO_FAVORITE_SURVEY_TEMPLATE = 1
DOGGY_ID = "dddddddd-dddd-dddd-dddd-dddddddddddd"
PLANTY_ID = "eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee"

SUPPLIED_KIT_ID = "FooFooFoo"
KIT_ID = '77777777-8888-9999-aaaa-bbbbcccccccc'
MOCK_SAMPLE_ID = '99999999-aaaa-aaaa-aaaa-bbbbcccccccc'
BARCODE = '777777777'


@pytest.fixture(scope="class")
def client(request):
    app = microsetta_private_api.server.build_app()
    app.app.testing = True
    with app.app.test_client() as client:
        request.cls.client = client
        yield client


def check_response(response, expected_status=None):
    if expected_status is not None:
        assert response.status_code == expected_status
    elif response.status_code >= 400:
        raise Exception("Scary response code: " + str(response.status_code))

    if response.status_code == 204 and len(response.data) == 0:
        # No content to check.
        pass
    elif response.headers.get("Content-Type") == "application/json":
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
        fuzzy = {x: fuzz(y) for x, y in val.items()}
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
    def setup_test_data():

        american_gut._NEW_PARTICIPANT = \
            copy.deepcopy(american_gut._NEW_PARTICIPANT)
        american_gut._NEW_PARTICIPANT['SEL_AGE_RANGE'] = "Murica!"
        british_gut._NEW_PARTICIPANT = \
            copy.deepcopy(british_gut._NEW_PARTICIPANT)
        british_gut._NEW_PARTICIPANT['SEL_AGE_RANGE'] = "QQBritannia"

        IntegrationTests.teardown_test_data()

        with Transaction() as t:
            acct_repo = AccountRepo(t)
            source_repo = SourceRepo(t)

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
                HumanInfo("Bo", "bo@bo.com", False, None, None,
                          False, datetime.datetime.utcnow(), None,
                          "Mr. Obtainer",
                          "18-plus")
            ))
            source_repo.create_source(Source.create_animal(
                DOGGY_ID,
                ACCT_ID,
                AnimalInfo("Doggy", "Doggy The Dog")))
            source_repo.create_source(Source.create_environment(
                PLANTY_ID,
                ACCT_ID,
                EnvironmentInfo("Planty", "The green one")))

            _create_mock_kit(t)

            with t.cursor() as cur:
                # american and british are ALWAYS the same!
                # Need to mock a row where they differ, which will be on
                # question 107.
                cur.execute("SELECT american, british FROM survey_question "
                            "WHERE survey_question_id = 107")
                row = cur.fetchone()
                # If this fails, it most likely means the teardown failed
                # last time the tests were run.  But it could also mean
                # someone changed survey question 107!!!
                assert row[0] == "Gender:"
                assert row[1] == "Gender:"

                cur.execute("UPDATE survey_question "
                            "SET "
                            "american = 'Gender:', "
                            "british = 'Gandalf:' "
                            "WHERE survey_question_id = 107")

                cur.execute("UPDATE survey_response SET "
                            "british = 'Wizard' "
                            "WHERE "
                            "american = 'Male'")

            t.commit()

    @staticmethod
    def teardown_test_data():
        with Transaction() as t:
            with t.cursor() as cur:
                # TODO:  This restoration plan is terrible!  We need a better
                #  way to mock out the database!!
                cur.execute("UPDATE survey_question "
                            "SET "
                            "american = 'Gender:', "
                            "british = 'Gender:' "
                            "WHERE survey_question_id = 107")

                cur.execute("UPDATE survey_response SET "
                            "british = 'Male' "
                            "WHERE "
                            "american = 'Male'")
            t.commit()

        with Transaction() as t:
            acct_repo = AccountRepo(t)
            source_repo = SourceRepo(t)
            _remove_mock_kit(t)
            survey_answers_repo = SurveyAnswersRepo(t)
            for source in source_repo.get_sources_in_account(ACCT_ID):
                answers = survey_answers_repo.list_answered_surveys(ACCT_ID,
                                                                    source.id)
                for survey_id in answers:
                    survey_answers_repo.delete_answered_survey(ACCT_ID,
                                                               survey_id)
                source_repo.delete_source(ACCT_ID, source.id)
            acct_repo.delete_account(ACCT_ID)

            t.commit()

    def test_get_sources(self):
        resp = self.client.get(
            '/api/accounts/%s/sources?language_tag=en-US' % ACCT_ID)
        check_response(resp)
        sources = json.loads(resp.data)
        self.assertEqual(
            len([x for x in sources if x['source_name'] == 'Bo']),
            1,
            "Expected one source named Bo")
        self.assertEqual(
            len([x for x in sources if x['source_name'] == 'Doggy']),
            1,
            "Expected 1 source named Doggy")
        self.assertEqual(
            len([x for x in sources if x['source_name'] == 'Planty']),
            1,
            "Expected 1 source named Planty")

    def test_put_source(self):
        resp = self.client.get(
            '/api/accounts/%s/sources?language_tag=en-US' % ACCT_ID)

        check_response(resp)
        sources = json.loads(resp.data)
        self.assertGreaterEqual(len(sources), 3)
        to_edit = sources[2]
        source_id = to_edit["source_id"]
        fuzzy = fuzz(to_edit)
        fuzzy["source_type"] = to_edit["source_type"]
        fuzzy.pop("source_id")
        resp = self.client.put(
            '/api/accounts/%s/sources/%s?language_tag=en-US' %
            (ACCT_ID, source_id),
            content_type='application/json',
            data=json.dumps(fuzzy)
        )
        check_response(resp)
        fuzzy_resp = json.loads(resp.data)
        self.assertEqual(fuzzy["source_name"], fuzzy_resp["source_name"])
        self.assertEqual(fuzzy["source_description"],
                         fuzzy_resp["source_description"])
        to_edit.pop("source_id")
        resp = self.client.put(
            '/api/accounts/%s/sources/%s?language_tag=en-US' %
            (ACCT_ID, source_id),
            content_type='application/json',
            data=json.dumps(to_edit)
        )
        check_response(resp)
        edit_resp = json.loads(resp.data)
        self.assertEqual(to_edit["source_name"], edit_resp["source_name"])
        self.assertEqual(to_edit["source_description"],
                         edit_resp["source_description"])

    def test_surveys(self):
        resp = self.client.get(
            '/api/accounts/%s/sources?language_tag=en-US' % ACCT_ID)
        check_response(resp)

        sources = json.loads(resp.data)
        bobo = [x for x in sources if x['source_name'] == 'Bo'][0]
        doggy = [x for x in sources if x['source_name'] == 'Doggy'][0]
        env = [x for x in sources if x['source_name'] == 'Planty'][0]

        resp = self.client.get(
            '/api/accounts/%s/sources/%s/survey_templates?language_tag=en-US' %
            (ACCT_ID, bobo['source_id']), )
        bobo_surveys = json.loads(resp.data)
        resp = self.client.get(
            '/api/accounts/%s/sources/%s/survey_templates?language_tag=en-US' %
            (ACCT_ID, doggy['source_id']))
        doggy_surveys = json.loads(resp.data)
        resp = self.client.get(
            '/api/accounts/%s/sources/%s/survey_templates?language_tag=en-US' %
            (ACCT_ID, env['source_id']))
        env_surveys = json.loads(resp.data)

        self.assertListEqual(bobo_surveys, [1, 3, 4, 5])
        self.assertListEqual(doggy_surveys, [2])
        self.assertListEqual(env_surveys, [])

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
            '/api/accounts/%s/sources?language_tag=en-US' % ACCT_ID)
        check_response(resp)
        sources = json.loads(resp.data)
        bobo = [x for x in sources if x['source_name'] == 'Bo'][0]
        resp = self.client.get(
            '/api/accounts/%s/sources/%s/survey_templates?language_tag=en-US' %
            (ACCT_ID, bobo['source_id']))
        bobo_surveys = json.loads(resp.data)
        chosen_survey = bobo_surveys[0]
        resp = self.client.get(
            '/api/accounts/%s/sources/%s/survey_templates/%s'
            '?language_tag=en-US' %
            (ACCT_ID, bobo['source_id'], chosen_survey))
        check_response(resp)

        model = fuzz_form(json.loads(resp.data))
        resp = self.client.post(
            '/api/accounts/%s/sources/%s/surveys?language_tag=en-US'
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
        resp = self.client.get(loc + "?language_tag=en-US")
        check_response(resp)
        retrieved_survey = json.loads(resp.data)
        self.assertDictEqual(retrieved_survey, model)

        # Clean up after the new survey
        with Transaction() as t:
            repo = SurveyAnswersRepo(t)
            found = repo.delete_answered_survey(ACCT_ID, survey_id)
            self.assertTrue(found, "Couldn't find survey to delete, oops!")
            t.commit()

    def test_create_new_account(self):
        # Had to change from janedoe@example.com after I ran api/ui to create
        # a janedoe@example.com address in my test db.
        FAKE_EMAIL = "zbkhasdahl4wlnas@asdjgakljesgnoqe.com"
        # Clean up before the test in case we already have a janedoe
        with Transaction() as t:
            AccountRepo(t).delete_account_by_email(FAKE_EMAIL)
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
                "email": FAKE_EMAIL,
                "first_name": "Jane",
                "last_name": "Doe",
                "kit_name": "jb_qhxqe"
            })

        # First register should succeed
        response = self.client.post(
            '/api/accounts?language_tag=en-US',
            content_type='application/json',
            data=acct_json
        )
        check_response(response)

        # TODO: Is it weird that we return the new object AND its location?

        # And should give us the account with ID and the location of it
        loc = response.headers.get("Location")
        url = werkzeug.urls.url_parse(loc)
        acct_id_from_loc = url.path.split('/')[-1]
        new_acct = json.loads(response.data)
        acct_id_from_obj = new_acct['account_id']
        self.assertIsNotNone(acct_id_from_loc,
                             "Couldn't retrieve acct from Location header")
        self.assertEqual(acct_id_from_loc, acct_id_from_obj,
                         "Different account ids in location header and json "
                         "response")

        # Second register should fail with duplicate email 422
        response = self.client.post(
            '/api/accounts?language_tag=en-US',
            content_type='application/json',
            data=acct_json
        )
        check_response(response, 422)

        # Clean up after this test so we don't leave the account around
        with Transaction() as t:
            AccountRepo(t).delete_account_by_email(FAKE_EMAIL)
            t.commit()

    def test_edit_account_info(self):
        """ Test: Can we edit account information """
        response = self.client.get(
            '/api/accounts/%s?language_tag=en-US' % (ACCT_ID,),
            headers={'Authorization': 'Bearer PutMySecureOauthTokenHere'})
        check_response(response)

        acc = json.loads(response.data)

        regular_data = \
            {
                "account_id": "aaaaaaaa-bbbb-cccc-dddd-eeeeffffffff",
                "account_type": "standard",
                "address": {
                    "street": "123 Dan Lane",
                    "city": "Danville",
                    "state": "CA",
                    "post_code": "12345",
                    "country_code": "US"
                },
                "email": "foo@baz.com",
                "first_name": "Dan",
                "last_name": "H"
            }

        # Hard to guess these two, so let's pop em out
        acc.pop("creation_time")
        acc.pop("update_time")
        self.assertDictEqual(acc, regular_data, "Check Initial Account Match")

        regular_data.pop("account_id")
        fuzzy_data = fuzz(regular_data)

        fuzzy_data['account_type'] = "Voldemort"
        print("---\nYou should see a validation error in unittest:")
        response = self.client.put(
            '/api/accounts/%s?language_tag=en-US' % (ACCT_ID,),
            content_type='application/json',
            data=json.dumps(fuzzy_data)
        )
        print("---")
        # Check that malicious user can't write any field they want
        check_response(response, 400)

        # Check that data can be written once request is not malformed
        fuzzy_data.pop('account_type')
        response = self.client.put(
            '/api/accounts/%s?language_tag=en-US' % (ACCT_ID,),
            content_type='application/json',
            data=json.dumps(fuzzy_data)
        )

        check_response(response)

        acc = json.loads(response.data)
        fuzzy_data['account_type'] = 'standard'
        fuzzy_data["account_id"] = "aaaaaaaa-bbbb-cccc-dddd-eeeeffffffff"
        acc.pop('creation_time')
        acc.pop('update_time')
        self.assertDictEqual(fuzzy_data, acc, "Check Fuzz Account Match")

        # Attempt to restore back to old data.
        regular_data.pop('account_type')
        response = self.client.put(
            '/api/accounts/%s?language_tag=en-US' % (ACCT_ID,),
            content_type='application/json',
            data=json.dumps(regular_data)
        )
        check_response(response)

        acc = json.loads(response.data)
        acc.pop('creation_time')
        acc.pop('update_time')
        regular_data['account_type'] = 'standard'
        regular_data["account_id"] = "aaaaaaaa-bbbb-cccc-dddd-eeeeffffffff"

        self.assertDictEqual(regular_data, acc, "Check restore to regular")

    def test_add_sample_from_kit(self):
        """ We list the samples in a kit, grab an unassociated one,
            and then associate that sample with our account
        """
        response = self.client.get(
            '/api/kits/?language_tag=en-US&kit_name=%s' % SUPPLIED_KIT_ID)
        check_response(response)

        unused_samples = json.loads(response.data)
        sample_id = unused_samples[0]['sample_id']

        response = self.client.post(
            '/api/accounts/%s/sources/%s/samples?language_tag=en-US' %
            (ACCT_ID, DOGGY_ID),
            content_type='application/json',
            data=json.dumps(
                {
                    "sample_id": sample_id
                })
        )
        check_response(response)

        # Check that we can now see this sample
        response = self.client.get(
            '/api/accounts/%s/sources/%s/samples/%s?language_tag=en-US' %
            (ACCT_ID, DOGGY_ID, sample_id)
        )
        check_response(response)

        # Check that we can't see this sample from outside the account/source
        response = self.client.get(
            '/api/accounts/%s/sources/%s/samples/%s?language_tag=en-US' %
            (NOT_ACCT_ID, DOGGY_ID, sample_id)
        )
        check_response(response, 404)

        response = self.client.get(
            '/api/accounts/%s/sources/%s/samples/%s?language_tag=en-US' %
            (ACCT_ID, HUMAN_ID, sample_id)
        )
        check_response(response, 404)

    def test_create_non_human_sources(self):
        # TODO: Looks like the 201 for sources are specified to
        #  both return a Location header and the newly created object.  This
        #  seems inconsistent maybe?  Consistent with Account, inconsistent
        #  with survey_answers and maybe source+sample assocations?  What's
        #  right?

        kitty = {
            "source_type": "animal",
            "source_name": "Fluffy",
            "source_description": "FLUFFERNUTTER!!!"
        }
        desky = {
            "source_type": "environmental",
            "source_name": "The Desk",
            "source_description": "It's a desk."
        }

        for new_source in [kitty, desky]:
            resp = self.client.post(
                '/api/accounts/%s/sources?language_tag=en-US' % (ACCT_ID,),
                content_type='application/json',
                data=json.dumps(new_source)
            )

            check_response(resp)
            loc = resp.headers.get("Location")
            url = werkzeug.urls.url_parse(loc)
            source_id_from_loc = url.path.split('/')[-1]
            result_source = json.loads(resp.data)
            source_id_from_obj = result_source['source_id']
            self.assertIsNotNone(source_id_from_loc,
                                 "Couldn't parse source id from location "
                                 "header")
            self.assertEqual(source_id_from_loc, source_id_from_obj,
                             "Different source id from loc header and resp")

            self.assertEqual(new_source["source_type"],
                             result_source["source_type"])
            self.assertEqual(new_source["source_description"],
                             result_source["source_description"])
            self.assertEqual(new_source["source_name"],
                             result_source["source_name"])

            # TODO: It would be standard to make a test database and delete it
            #  or keep it entirely in memory.  But the change scripts add in
            #  too much data to a default database to make this feasible for
            #  quickly running tests during development.  Can we do better than
            #  this pattern of adding and immediately deleting data during
            #  testing?  The cleanup is not particularly robust

            # Clean Up by deleting the new sources
            # TODO: Do I -really- need to specify a language_tag to delete???
            self.client.delete(loc + "?language_tag=en-US")

    def test_create_human_source(self):
        """To add a human source, we need to get consent"""
        resp = self.client.get('/api/accounts/%s/consent?language_tag=en-US' %
                               (ACCT_ID,))
        check_response(resp)

        # TODO: This should probably fail as it doesn't perfectly match one of
        #  the four variants of consent that can be passed in.  Split it up?
        resp = self.client.post(
            '/api/accounts/%s/consent?language_tag=en-US' %
            (ACCT_ID,),
            content_type='application/x-www-form-urlencoded',
            data="age_range=18-plus&"
                 "participant_name=Joe%20Schmoe&"
                 "participant_email=joe%40schmoe%2Ecom&"
                 "parent_1_name=Mr%2E%20Schmoe&"
                 "parent_2_name=Mrs%2E%20Schmoe&"
                 "deceased_parent=false&"
                 "obtainer_name=MojoJojo"
        )
        check_response(resp, 201)

        check_response(resp)
        loc = resp.headers.get("Location")
        url = werkzeug.urls.url_parse(loc)
        source_id_from_loc = url.path.split('/')[-1]
        new_source = json.loads(resp.data)
        source_id_from_obj = new_source['source_id']
        self.assertIsNotNone(source_id_from_loc,
                             "Couldn't parse source_id from loc header")
        self.assertEqual(source_id_from_obj, source_id_from_obj,
                         "Different source id from loc header and json resp")

        self.client.delete(loc + "?language_tag=en-US")

    def test_associate_sample_and_survey(self):
        """
            Submit a survey for a source
            Assign a sample to that source
            Associate the sample and the survey answers
        """

        # Part 1: Submit a survey
        chosen_survey = BOBO_FAVORITE_SURVEY_TEMPLATE
        resp = self.client.get(
            '/api/accounts/%s/sources/%s/survey_templates/%s'
            '?language_tag=en-US' %
            (ACCT_ID, HUMAN_ID, chosen_survey))
        check_response(resp)

        model = fuzz_form(json.loads(resp.data)["survey_template_text"])
        resp = self.client.post(
            '/api/accounts/%s/sources/%s/surveys?language_tag=en-US'
            % (ACCT_ID, HUMAN_ID),
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

        # Part 2: Claim a sample
        resp = self.client.get(
            '/api/kits/?language_tag=en-US&kit_name=%s' % SUPPLIED_KIT_ID)
        check_response(resp)

        unused_samples = json.loads(resp.data)
        sample_id = unused_samples[0]['sample_id']

        resp = self.client.post(
            '/api/accounts/%s/sources/%s/samples?language_tag=en-US' %
            (ACCT_ID, HUMAN_ID),
            content_type='application/json',
            data=json.dumps(
                {
                    "sample_id": sample_id
                })
        )
        check_response(resp)

        # Part 3: Link the sample with the survey
        resp = self.client.post(
            '/api/accounts/%s/sources/%s/samples/%s/surveys?language_tag=en-US'
            % (ACCT_ID, HUMAN_ID, sample_id),
            content_type='application/json',
            data=json.dumps(
                {
                    "survey_id": survey_id
                })
        )
        check_response(resp, 201)

        # Check that we can see the association
        resp = self.client.get(
            '/api/accounts/%s/sources/%s/samples/%s/surveys?language_tag=en-US'
            % (ACCT_ID, HUMAN_ID, sample_id),
        )
        check_response(resp)
        assoc_surveys = json.loads(resp.data)
        self.assertTrue(any([survey_id == survey['survey_id']
                             for survey in assoc_surveys]),
                        "Couldn't find newly linked survey association")

        # Check that we can delete the association
        resp = self.client.delete(
            '/api/accounts/%s/sources/%s/samples/%s/surveys/%s'
            '?language_tag=en-US'
            % (ACCT_ID, HUMAN_ID, sample_id, survey_id)
        )
        check_response(resp, 204)

        # Check that we no longer see the association
        resp = self.client.get(
            '/api/accounts/%s/sources/%s/samples/%s/surveys?language_tag=en-US'
            % (ACCT_ID, HUMAN_ID, sample_id),
        )
        check_response(resp)
        assoc_surveys = json.loads(resp.data)
        self.assertFalse(any([survey_id == survey['survey_id']
                              for survey in assoc_surveys]),
                         "Deleted survey association was still around")

        # Check that we can't assign a sample to a survey owned by a source
        #  other than the source which is associated with the sample
        #  ie - bobo's sample can't associate a survey from bobo's dog
        resp = self.client.post(
            '/api/accounts/%s/sources/%s/samples/%s/surveys?language_tag=en-US'
            % (ACCT_ID, DOGGY_ID, sample_id),
            content_type='application/json',
            data=json.dumps(
                {
                    "survey_id": survey_id
                })
        )
        check_response(resp, 404)

        # Check that we can't assign a sample to a survey in another account
        resp = self.client.post(
            '/api/accounts/%s/sources/%s/samples/%s/surveys?language_tag=en-US'
            % (NOT_ACCT_ID, HUMAN_ID, sample_id),
            content_type='application/json',
            data=json.dumps(
                {
                    "survey_id": survey_id
                })
        )
        check_response(resp, 404)

        # Clean up after the new survey
        with Transaction() as t:
            repo = SurveyAnswersRepo(t)
            found = repo.delete_answered_survey(ACCT_ID, survey_id)
            self.assertTrue(found, "Couldn't find survey for database cleanup")
            t.commit()

    def test_edit_sample_info(self):
        """
        This test will claim a sample, write some data, edit that data
        Dissociate that sample, grab it with a different source, edit some data
        Mark the sample as received and check that editing is locked
        """
        # Claim a sample
        response = self.client.get(
            '/api/kits/?language_tag=en-US&kit_name=%s' % SUPPLIED_KIT_ID)
        check_response(response)

        unused_samples = json.loads(response.data)
        sample_id = unused_samples[0]['sample_id']

        response = self.client.post(
            '/api/accounts/%s/sources/%s/samples?language_tag=en-US' %
            (ACCT_ID, HUMAN_ID),
            content_type='application/json',
            data=json.dumps(
                {
                    "sample_id": sample_id
                })
        )
        check_response(response)

        response = self.client.get(
            '/api/accounts/%s/sources/%s/samples/%s?language_tag=en-US' %
            (ACCT_ID, HUMAN_ID, sample_id)
        )
        sample_info = json.loads(response.data)

        # Edit that sample info
        fuzzy_info = fuzz(sample_info)

        # Ensure that we have required fields
        fuzzy_info['sample_site'] = "Tears"
        fuzzy_info['sample_datetime'] = datetime.datetime.utcnow()

        # Many fields are not writable, each should individually cause failure.
        readonly_fields = [
            'sample_id', 'sample_barcode',
            'sample_locked', 'sample_projects'
        ]

        for readonly_field in readonly_fields:
            fuzzy_info.pop(readonly_field)

        for readonly_field in readonly_fields:
            print("---\nYou should see a validation error in unittest:")
            fuzzy_info[readonly_field] = "Voldemort"
            response = self.client.put(
                '/api/accounts/%s/sources/%s/samples/%s?language_tag=en-US' %
                (ACCT_ID, HUMAN_ID, sample_id),
                content_type='application/json',
                data=json.dumps(fuzzy_info, default=json_converter)
            )
            check_response(response, 400)
            fuzzy_info.pop(readonly_field)
            print("---")

        # But after removing all these fields, we should be able to edit.
        response = self.client.put(
            '/api/accounts/%s/sources/%s/samples/%s?language_tag=en-US' %
            (ACCT_ID, HUMAN_ID, sample_id),
            content_type='application/json',
            data=json.dumps(fuzzy_info, default=json_converter)
        )
        check_response(response, 200)

        # Now we can try writing and checking that our updates went through
        fuzzy_info['sample_notes'] = "Oboe Is For Bobo"
        fuzzy_info['sample_site'] = "Forehead"
        fuzzy_info['sample_datetime'] = datetime.datetime.now()

        response = self.client.put(
            '/api/accounts/%s/sources/%s/samples/%s?language_tag=en-US' %
            (ACCT_ID, HUMAN_ID, sample_id),
            content_type='application/json',
            data=json.dumps(fuzzy_info, default=json_converter)
        )
        check_response(response, 200)

        response = self.client.get(
            '/api/accounts/%s/sources/%s/samples/%s?language_tag=en-US' %
            (ACCT_ID, HUMAN_ID, sample_id)
        )
        check_response(response, 200)
        new_info = json.loads(response.data)

        self.assertEqual(fuzzy_info['sample_notes'],
                         new_info['sample_notes'],
                         "sample_notes not written")
        self.assertEqual(fuzzy_info['sample_site'],
                         new_info['sample_site'],
                         "sample_site not written")
        self.assertEqual(fuzzy_info['sample_datetime'],
                         fromisotime(new_info['sample_datetime']),
                         "sample_datetime not written")

        # Now dissociate the sample from HUMAN_ID
        response = self.client.delete(
            '/api/accounts/%s/sources/%s/samples/%s?language_tag=en-US' %
            (ACCT_ID, HUMAN_ID, sample_id)
        )
        check_response(response, 204)

        # All of those fields should be gone when we claim it again
        response = self.client.post(
            '/api/accounts/%s/sources/%s/samples?language_tag=en-US' %
            (ACCT_ID, PLANTY_ID),  # This sample now belong to nature.
            content_type='application/json',
            data=json.dumps(
                {
                    "sample_id": sample_id
                })
        )
        check_response(response)

        response = self.client.get(
            '/api/accounts/%s/sources/%s/samples/%s?language_tag=en-US' %
            (ACCT_ID, PLANTY_ID, sample_id)
        )
        check_response(response, 200)
        plant_info = json.loads(response.data)

        self.assertIsNone(plant_info['sample_notes'],
                          "Reclaiming a sample with a new source should not "
                          "retain any data from the old association")
        self.assertIsNone(plant_info['sample_site'],
                          "Reclaiming a sample with a new source should not "
                          "retain any data from the old association")
        self.assertIsNone(plant_info['sample_datetime'],
                          "Reclaiming a sample with a new source should not "
                          "retain any data from the old association")

        # And planty should be able to edit info without setting sample_site
        response = self.client.put(
            '/api/accounts/%s/sources/%s/samples/%s?language_tag=en-US' %
            (ACCT_ID, PLANTY_ID, sample_id),
            content_type='application/json',
            data=json.dumps(
                {
                    "sample_site": None,
                    "sample_datetime": datetime.datetime.utcnow(),
                    "sample_notes": "Nature Nature Nature"
                }, default=json_converter)
        )
        check_response(response)

        # Finally, we lock the sample to prevent further edits
        with Transaction() as t:
            with t.cursor() as cur:
                cur.execute("UPDATE barcode "
                            "SET scan_date = %s "
                            "WHERE "
                            "barcode = %s",
                            (datetime.datetime.now(), BARCODE))
            t.commit()

        response = self.client.put(
            '/api/accounts/%s/sources/%s/samples/%s?language_tag=en-US' %
            (ACCT_ID, PLANTY_ID, sample_id),
            content_type='application/json',
            data=json.dumps(
                {
                    "sample_site": None,
                    "sample_datetime": datetime.datetime.utcnow(),
                    "sample_notes": "Mother Nature Mother Nature"
                }, default=json_converter)
        )
        check_response(response, 422)

    def test_survey_localization(self):
        # Retrieve Survey Template!
        # Should fail for en_qq
        resp = self.client.get(
            '/api/accounts/%s/sources/%s/survey_templates/%s'
            '?language_tag=en_qq' %
            (ACCT_ID, HUMAN_ID, BOBO_FAVORITE_SURVEY_TEMPLATE))
        check_response(resp, 404)

        # Should work for en-US
        resp = self.client.get(
            '/api/accounts/%s/sources/%s/survey_templates/%s'
            '?language_tag=en-US' %
            (ACCT_ID, HUMAN_ID, BOBO_FAVORITE_SURVEY_TEMPLATE))
        check_response(resp)
        form_us = json.loads(resp.data)

        # Should work for en-GB
        resp = self.client.get(
            '/api/accounts/%s/sources/%s/survey_templates/%s'
            '?language_tag=en-GB' %
            (ACCT_ID, HUMAN_ID, BOBO_FAVORITE_SURVEY_TEMPLATE))
        check_response(resp)
        form_gb = json.loads(resp.data)

        # Responses should differ by locale
        self.assertEqual(form_us['groups'][0]['fields'][0]['id'], '107',
                         "Survey question 107 moved, update the test!")
        self.assertEqual(form_us['groups'][0]['fields'][0]['label'], 'Gender:',
                         "Survey question 107 should say 'Gender:' in en-US")
        self.assertEqual(form_gb['groups'][0]['fields'][0]['id'], '107',
                         "Survey question 107 moved, update the test!")
        self.assertEqual(
            form_gb['groups'][0]['fields'][0]['label'],
            'Gandalf:',
            "Survey question 107 should say 'Gandalf:' (test setup for en-GB)")

        self.assertIn('Male', form_us['groups'][0]['fields'][0]['values'],
                      "One choice for 107 should be 'Male' in en-US")
        self.assertIn('Wizard', form_gb['groups'][0]['fields'][0]['values'],
                      "One choice for 107 should be 'Wizard' in en-GB"
                      "(After test setup for en-GB)")

        model_gb = fuzz_form(form_gb)
        model_gb['107'] = 'Wizard'  # British for 'Male' per test setup.

        # Submit a survey response!
        # Should fail for en_qq
        resp = self.client.post(
            '/api/accounts/%s/sources/%s/surveys?language_tag=en_qq'
            % (ACCT_ID, HUMAN_ID),
            content_type='application/json',
            data=json.dumps(
                {
                    'survey_template_id': BOBO_FAVORITE_SURVEY_TEMPLATE,
                    'survey_text': model_gb
                })
        )
        check_response(resp, 404)

        # But should work for en-GB
        resp = self.client.post(
            '/api/accounts/%s/sources/%s/surveys?language_tag=en-GB'
            % (ACCT_ID, HUMAN_ID),
            content_type='application/json',
            data=json.dumps(
                {
                    'survey_template_id': BOBO_FAVORITE_SURVEY_TEMPLATE,
                    'survey_text': model_gb
                })
        )
        check_response(resp, 201)
        loc = resp.headers.get("Location")
        url = werkzeug.urls.url_parse(loc)
        survey_id = url.path.split('/')[-1]

        # Also, posting an en-GB model as en-US should explode as Wizard is
        # invalid in american
        resp = self.client.post(
            '/api/accounts/%s/sources/%s/surveys?language_tag=en-US'
            % (ACCT_ID, HUMAN_ID),
            content_type='application/json',
            data=json.dumps(
                {
                    'survey_template_id': BOBO_FAVORITE_SURVEY_TEMPLATE,
                    'survey_text': model_gb
                })
        )
        check_response(resp, 400)

        # Lastly, posting an answer that does translate but is wrong
        # for the question should also fail out.
        # British for 'Large Mammal', an invalid choice for Gender
        model_gb['107'] = 'Large Mammal'
        resp = self.client.post(
            '/api/accounts/%s/sources/%s/surveys?language_tag=en-GB'
            % (ACCT_ID, HUMAN_ID),
            content_type='application/json',
            data=json.dumps(
                {
                    'survey_template_id': BOBO_FAVORITE_SURVEY_TEMPLATE,
                    'survey_text': model_gb
                })
        )
        check_response(resp, 400)

        with Transaction() as t:
            repo = SurveyAnswersRepo(t)
            # Though we passed up an en-GB model, answers stored should be
            # in en-US and converted to either locale
            result = repo.get_answered_survey(ACCT_ID, HUMAN_ID,
                                              survey_id, 'en-US')
            self.assertEqual(result['107'], 'Male',
                             "Couldn't read answer from db in en-US")
            result = repo.get_answered_survey(ACCT_ID, HUMAN_ID,
                                              survey_id, 'en-GB')
            self.assertEqual(result['107'], 'Wizard',
                             "Couldn't read answer from db in en-GB")

            # Clean up after the new survey
            found = repo.delete_answered_survey(ACCT_ID, survey_id)
            self.assertTrue(found, "Couldn't find survey answers in db")
            t.commit()

    def test_consent_localization(self):
        resp_us = self.client.get('/api/accounts/%s/consent?language_tag=en-US'
                                  % (ACCT_ID,))
        check_response(resp_us)
        resp_gb = self.client.get('/api/accounts/%s/consent?language_tag=en-GB'
                                  % (ACCT_ID,))
        check_response(resp_gb)

        self.assertNotEqual(resp_us.data, resp_gb.data,
                            "en-US and en-GB consent shouldn't be equal "
                            "(after test setup)")
        self.assertIn("Murica!", str(resp_us.data),
                      "String inserted into consent doc during test setup"
                      "not found (en-US)")
        self.assertIn("QQBritannia", str(resp_gb.data),
                      "String inserted into consent doc during test setup"
                      "not found (en-US)")


def _create_mock_kit(transaction):
    with transaction.cursor() as cur:
        cur.execute("INSERT INTO barcode (barcode, status) "
                    "VALUES(%s, %s)",
                    (BARCODE,
                     'MOCK SAMPLE FOR UNIT TEST'))
        cur.execute("INSERT INTO ag_kit "
                    "(ag_kit_id, "
                    "supplied_kit_id, swabs_per_kit) "
                    "VALUES(%s, %s, %s)",
                    (KIT_ID, SUPPLIED_KIT_ID, 1))
        cur.execute("INSERT INTO ag_kit_barcodes "
                    "(ag_kit_barcode_id, ag_kit_id, barcode) "
                    "VALUES(%s, %s, %s)",
                    (MOCK_SAMPLE_ID, KIT_ID, BARCODE))
        # Add the mock barcode to American Gut Project
        cur.execute("INSERT INTO project_barcode "
                    "(project_id, barcode) "
                    "VALUES(%s, %s)", (1, BARCODE))


def _remove_mock_kit(transaction):
    with transaction.cursor() as cur:
        cur.execute("DELETE FROM ag_kit_barcodes "
                    "WHERE ag_kit_barcode_id=%s",
                    (MOCK_SAMPLE_ID,))
        cur.execute("DELETE FROM ag_kit WHERE ag_kit_id=%s",
                    (KIT_ID,))

        # Some tests may leak leftover surveys, wipe those out also
        cur.execute("DELETE FROM source_barcodes_surveys WHERE barcode = %s",
                    (BARCODE,))

        # Remove the mock barcode from any projects
        cur.execute("DELETE FROM project_barcode WHERE barcode = %s",
                    (BARCODE,))

        cur.execute("DELETE FROM barcode WHERE barcode = %s",
                    (BARCODE,))