import pytest
from unittest import TestCase
from unittest.mock import patch
from flask import Response
import json
import microsetta_private_api.server
from microsetta_private_api.model.account import Account, Address
from microsetta_private_api.model.project import Project
from microsetta_private_api.model.daklapack_order \
    import SHIPPING_TYPES_BY_PROVIDER
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.api.tests.test_api import (  # noqa
    client,
    MOCK_HEADERS,  ACCT_ID_1, ACCT_MOCK_ISS, ACCT_MOCK_SUB,
    extract_last_id_from_location_header)
from microsetta_private_api.admin.tests.test_admin_repo import \
    FIRST_LIVE_DAK_ARTICLE, delete_test_scan
from microsetta_private_api.model.tests.test_daklapack_order import \
    DUMMY_PROJ_ID_LIST, DUMMY_DAK_ARTICLE_CODE, DUMMY_ADDRESSES, \
    DUMMY_DAK_ORDER_DESC, DUMMY_PLANNED_SEND_DATE, DUMMY_FEDEX_REFS, \
    DUMMY_SHIPPING_PROVIDER, DUMMY_SHIPPING_TYPE
from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo


DUMMY_PROJ_NAME = "test project"


def teardown_test_data():
    with Transaction() as t:
        acct_repo = AccountRepo(t)
        admin_repo = AdminRepo(t)
        acct_repo.delete_account(ACCT_ID_1)
        admin_repo.delete_project_by_name(DUMMY_PROJ_NAME)
        with t.cursor() as cur:
            cur.execute("UPDATE barcodes.project"
                        " SET is_active = TRUE"
                        " WHERE project_id = 2")

        t.commit()


def setup_test_data():
    teardown_test_data()

    with Transaction() as t:
        acct_repo = AccountRepo(t)

        acc = Account(ACCT_ID_1,
                      "bar@baz.com",
                      "admin",
                      ACCT_MOCK_ISS,
                      ACCT_MOCK_SUB,
                      "Dan",
                      "H",
                      Address(
                          "456 Dan Lane",
                          "Danville",
                          "CA",
                          12345,
                          "US"
                      ),
                      32.8798916,
                      -117.2363115,
                      False,
                      "en_US",
                      True)
        acct_repo.create_account(acc)

        with t.cursor() as cur:
            cur.execute("UPDATE barcodes.project"
                        " SET is_active = FALSE"
                        " WHERE project_id = 2")
        t.commit()


def delete_test_daklapack_orders(order_submissions):
    if order_submissions is not None:
        with Transaction() as t:
            with t.cursor() as cur:
                for curr_submission in order_submissions:
                    new_order_id = curr_submission.get("order_id")
                    if new_order_id is not None:
                        cur.execute("DELETE FROM barcodes."
                                    "daklapack_order_to_project "
                                    "WHERE "
                                    "dak_order_id = %s",
                                    (new_order_id,))

                        cur.execute("DELETE FROM barcodes.daklapack_order "
                                    "WHERE "
                                    "dak_order_id = %s",
                                    (new_order_id,))
            t.commit()


def make_test_response(status_code):
    result = Response()
    result.status_code = status_code
    result.data = f"Got {status_code}"
    return result


@pytest.mark.usefixtures("client")
class AdminApiTests(TestCase):
    FULL_PROJ_INFO = {"project_name": DUMMY_PROJ_NAME,
                      "is_microsetta": True,
                      "bank_samples": False,
                      "plating_start_date": None,
                      "contact_name": "Jane Doe",
                      "contact_email": "jd@test.com",
                      "additional_contact_name": "John Doe",
                      "deadlines": "Spring 2021",
                      "num_subjects": "Variable",
                      "num_timepoints": "4",
                      "start_date": "Fall 2020",
                      "disposition_comments": "Store",
                      "collection": "AGP",
                      "is_fecal": "X",
                      "is_saliva": "",
                      "is_skin": "?",
                      "is_blood": "X",
                      "is_other": "Nares, mouth",
                      "do_16s": "",
                      "do_shallow_shotgun": "Subset",
                      "do_shotgun": "X",
                      "do_rt_qpcr": "",
                      "do_serology": "",
                      "do_metatranscriptomics": "X",
                      "do_mass_spec": "X",
                      "mass_spec_comments": "Dorrestein",
                      "mass_spec_contact_name": "Ted Doe",
                      "mass_spec_contact_email": "td@test.com",
                      "do_other": "",
                      "branding_associated_instructions":
                          "branding_doc.pdf",
                      "branding_status": "In Review",
                      "subproject_name": "IBL SIBL",
                      "alias": "Healthy Sitting",
                      "sponsor": "Crowdfunded",
                      "coordination": "TMI",
                      "is_active": True}

    TEST_BARCODE = '000000001'

    def setUp(self):
        app = microsetta_private_api.server.build_app()
        self.client = app.app.test_client()
        self.client.__enter__()
        setup_test_data()

    def tearDown(self):
        self.client.__exit__(None, None, None)
        teardown_test_data()

    def test_vioscreen_samples_to_barcodes(self):
        response = self.client.get(
            '/api/admin/vioscreen/username_to_barcode',
            headers=MOCK_HEADERS
        )
        self.assertEqual(200, response.status_code)
        response_obj = json.loads(response.data)
        self.assertEqual(response_obj['000031536'],
                         'b98c5ac966b754ff')

    def _test_project_create_success(self, project_info):
        input_json = json.dumps(project_info)

        # execute project post (create)
        response = self.client.post(
            "/api/admin/projects",
            content_type='application/json',
            data=input_json,
            headers=MOCK_HEADERS
        )

        # check for successful create response code
        self.assertEqual(201, response.status_code)

        # check that a positive integer id was returned
        # (isdigit fails if str contains '-')
        new_id = extract_last_id_from_location_header(response)
        self.assertTrue(new_id.isdigit())

    def test_project_create_success_full(self):
        self._test_project_create_success(self.FULL_PROJ_INFO)

    def test_project_create_success_unbanked_no_date(self):
        """Successfully create a new, unbanked project, do not pass date"""

        # create post input json without a date field
        project_info = {
            "project_name": DUMMY_PROJ_NAME,
            "is_microsetta": False,
            "bank_samples": False
        }
        self._test_project_create_success(project_info)

    def test_project_create_success_banked_no_date(self):
        """Successfully create a new banked project with no plating date"""

        # create post input json without a date field
        project_info = {
            "project_name": DUMMY_PROJ_NAME,
            "is_microsetta": False,
            "bank_samples": True
        }
        self._test_project_create_success(project_info)

    def test_project_create_success_banked_blank_date(self):
        """Successfully create a new project banked till an unspecified date"""

        # create post input json with a blank date field
        project_info = {
            "project_name": DUMMY_PROJ_NAME,
            "is_microsetta": False,
            "bank_samples": True,
            "plating_start_date": None
        }
        self._test_project_create_success(project_info)

    def test_project_create_success_banked_real_date(self):
        """Successfully create a new project banked till a specific date"""

        # create post input json
        project_info = {
            "project_name": DUMMY_PROJ_NAME,
            "is_microsetta": False,
            "bank_samples": True,
            "plating_start_date": "2020-07-31"
        }
        self._test_project_create_success(project_info)

    def test_project_create_success_not_banked_blank_date(self):
        """Successfully create a new unbanked project with a blank date"""

        # create post input json with a blank date field
        project_info = {
            "project_name": DUMMY_PROJ_NAME,
            "is_microsetta": False,
            "bank_samples": False,
            "plating_start_date": None
        }
        self._test_project_create_success(project_info)

    def test_project_create_fail_not_banked_with_date(self):
        """Disallow creating a new unbanked project with a plating date"""

        # create post input json
        project_info = {
            "project_name": DUMMY_PROJ_NAME,
            "is_microsetta": False,
            "bank_samples": False,
            "plating_start_date": "2020-07-31"
        }
        input_json = json.dumps(project_info)

        # execute project post (create)
        response = self.client.post(
            "/api/admin/projects",
            content_type='application/json',
            data=input_json,
            headers=MOCK_HEADERS
        )

        # check response code
        self.assertEqual(422, response.status_code)

    def test_project_create_fail_banked_nonsense_date(self):
        """Disallow creating a new banked project with a nonsense date"""

        # create post input json with a nonsense date field
        project_info = {
            "project_name": DUMMY_PROJ_NAME,
            "is_microsetta": False,
            "bank_samples": True,
            "plating_start_date": "red"
        }
        input_json = json.dumps(project_info)

        # execute project post (create)
        response = self.client.post(
            "/api/admin/projects",
            content_type='application/json',
            data=input_json,
            headers=MOCK_HEADERS
        )

        self.assertEqual(422, response.status_code)

    def test_update_project(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            proj_id = admin_repo.create_project(
                Project(project_name=DUMMY_PROJ_NAME,
                        is_microsetta=False,
                        bank_samples=False))
            t.commit()

        # create post input json
        input_json = json.dumps(self.FULL_PROJ_INFO)

        # execute project put (update)
        response = self.client.put(
            f"/api/admin/projects/{proj_id}",
            content_type='application/json',
            data=input_json,
            headers=MOCK_HEADERS
        )

        # check response code
        self.assertEqual(204, response.status_code)

        with Transaction() as t:
            with t.dict_cursor() as cur:
                cur.execute("select * FROM project "
                            "WHERE "
                            "project_id = %s",
                            (proj_id,))
                row = cur.fetchone()
                stored_result = dict(row)

        expected_result = self.FULL_PROJ_INFO.copy()
        expected_result["project"] = expected_result.pop("project_name")
        expected_result["project_id"] = proj_id
        self.assertEqual(expected_result, stored_result)

    def test_get_projects_all_w_stats(self):
        # execute projects get
        response = self.client.get(
            "/api/admin/projects?include_stats=true",
            headers=MOCK_HEADERS
        )

        # check response code
        self.assertEqual(200, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)

        expected_record = {'additional_contact_name': None,
                           'alias': None,
                           'bank_samples': False,
                           'branding_associated_instructions': None,
                           'branding_status': None,
                           'collection': None,
                           'computed_stats': {
                               'num_fully_returned_kits': 1,
                               'num_kits': 5,
                               'num_kits_w_problems': 0,
                               'num_no_associated_source': 0,
                               'num_no_collection_info': 0,
                               'num_no_registered_account': 0,
                               'num_partially_returned_kits': 1,
                               'num_received_unknown_validity': 0,
                               'num_sample_is_valid': 4,
                               'num_samples': 20,
                               'num_samples_received': 4,
                               'num_unique_sources': 4},
                           'contact_email': None,
                           'contact_name': None,
                           'coordination': None,
                           'deadlines': None,
                           'disposition_comments': None,
                           'do_16s': None,
                           'do_mass_spec': None,
                           'do_metatranscriptomics': None,
                           'do_other': None,
                           'do_rt_qpcr': None,
                           'do_serology': None,
                           'do_shallow_shotgun': None,
                           'do_shotgun': None,
                           'is_blood': None,
                           'is_fecal': None,
                           'is_microsetta': False,
                           'is_other': None,
                           'is_saliva': None,
                           'is_skin': None,
                           'mass_spec_comments': None,
                           'mass_spec_contact_email': None,
                           'mass_spec_contact_name': None,
                           'num_subjects': None,
                           'num_timepoints': None,
                           'plating_start_date': None,
                           'project_id': 8,
                           'project_name': 'Project - %u[zGmÅq=g',
                           'sponsor': None,
                           'start_date': None,
                           'subproject_name': None,
                           'is_active': True}
        self.assertEqual(56, len(response_obj))
        self.assertEqual(expected_record, response_obj[7])

    def test_get_projects_active_w_stats(self):
        # execute projects get
        response = self.client.get(
            "/api/admin/projects?include_stats=true&is_active=true",
            headers=MOCK_HEADERS
        )

        # check response code
        self.assertEqual(200, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)

        expected_record = {'additional_contact_name': None,
                           'alias': None,
                           'bank_samples': False,
                           'branding_associated_instructions': None,
                           'branding_status': None,
                           'collection': None,
                           'computed_stats': {
                               'num_fully_returned_kits': 1,
                               'num_kits': 5,
                               'num_kits_w_problems': 0,
                               'num_no_associated_source': 0,
                               'num_no_collection_info': 0,
                               'num_no_registered_account': 0,
                               'num_partially_returned_kits': 1,
                               'num_received_unknown_validity': 0,
                               'num_sample_is_valid': 4,
                               'num_samples': 20,
                               'num_samples_received': 4,
                               'num_unique_sources': 4},
                           'contact_email': None,
                           'contact_name': None,
                           'coordination': None,
                           'deadlines': None,
                           'disposition_comments': None,
                           'do_16s': None,
                           'do_mass_spec': None,
                           'do_metatranscriptomics': None,
                           'do_other': None,
                           'do_rt_qpcr': None,
                           'do_serology': None,
                           'do_shallow_shotgun': None,
                           'do_shotgun': None,
                           'is_blood': None,
                           'is_fecal': None,
                           'is_microsetta': False,
                           'is_other': None,
                           'is_saliva': None,
                           'is_skin': None,
                           'mass_spec_comments': None,
                           'mass_spec_contact_email': None,
                           'mass_spec_contact_name': None,
                           'num_subjects': None,
                           'num_timepoints': None,
                           'plating_start_date': None,
                           'project_id': 8,
                           'project_name': 'Project - %u[zGmÅq=g',
                           'sponsor': None,
                           'start_date': None,
                           'subproject_name': None,
                           'is_active': True}
        self.assertEqual(55, len(response_obj))
        self.assertEqual(expected_record, response_obj[6])

    def test_get_projects_inactive_w_stats(self):
        # execute projects get
        response = self.client.get(
            "/api/admin/projects?include_stats=true&is_active=false",
            headers=MOCK_HEADERS
        )

        # check response code
        self.assertEqual(200, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)

        expected_record = {'additional_contact_name': None,
                           'alias': None,
                           'bank_samples': False,
                           'branding_associated_instructions': None,
                           'branding_status': None,
                           'collection': None,
                           'computed_stats':
                               {'num_fully_returned_kits': 0,
                                'num_kits': 0,
                                'num_kits_w_problems': 0,
                                'num_no_associated_source': 0,
                                'num_no_collection_info': 0,
                                'num_no_registered_account': 0,
                                'num_partially_returned_kits': 0,
                                'num_received_unknown_validity': 0,
                                'num_sample_is_valid': 0,
                                'num_samples': 800,
                                'num_samples_received': 0,
                                'num_unique_sources': 0},
                           'contact_email': None,
                           'contact_name': None,
                           'coordination': None,
                           'deadlines': None,
                           'disposition_comments': None,
                           'do_16s': None,
                           'do_mass_spec': None,
                           'do_metatranscriptomics': None,
                           'do_other': None,
                           'do_rt_qpcr': None,
                           'do_serology': None,
                           'do_shallow_shotgun': None,
                           'do_shotgun': None,
                           'is_active': False,
                           'is_blood': None,
                           'is_fecal': None,
                           'is_microsetta': False,
                           'is_other': None,
                           'is_saliva': None,
                           'is_skin': None,
                           'mass_spec_comments': None,
                           'mass_spec_contact_email': None,
                           'mass_spec_contact_name': None,
                           'num_subjects': None,
                           'num_timepoints': None,
                           'plating_start_date': None,
                           'project_id': 2,
                           'project_name': 'Project - /J/xL_|Eãt',
                           'sponsor': None,
                           'start_date': None,
                           'subproject_name': None}
        self.assertEqual(1, len(response_obj))
        self.assertEqual(expected_record, response_obj[0])

    def test_get_projects_all_wo_stats(self):
        # execute projects get
        response = self.client.get(
            "/api/admin/projects?include_stats=false",
            headers=MOCK_HEADERS
        )

        # check response code
        self.assertEqual(200, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)

        expected_record = {'additional_contact_name': None,
                           'alias': None,
                           'bank_samples': False,
                           'branding_associated_instructions': None,
                           'branding_status': None,
                           'collection': None,
                           'computed_stats': {},
                           'contact_email': None,
                           'contact_name': None,
                           'coordination': None,
                           'deadlines': None,
                           'disposition_comments': None,
                           'do_16s': None,
                           'do_mass_spec': None,
                           'do_metatranscriptomics': None,
                           'do_other': None,
                           'do_rt_qpcr': None,
                           'do_serology': None,
                           'do_shallow_shotgun': None,
                           'do_shotgun': None,
                           'is_blood': None,
                           'is_fecal': None,
                           'is_microsetta': False,
                           'is_other': None,
                           'is_saliva': None,
                           'is_skin': None,
                           'mass_spec_comments': None,
                           'mass_spec_contact_email': None,
                           'mass_spec_contact_name': None,
                           'num_subjects': None,
                           'num_timepoints': None,
                           'plating_start_date': None,
                           'project_id': 8,
                           'project_name': 'Project - %u[zGmÅq=g',
                           'sponsor': None,
                           'start_date': None,
                           'subproject_name': None,
                           'is_active': True}
        self.assertEqual(56, len(response_obj))
        self.assertEqual(expected_record, response_obj[7])

    def test_get_projects_active_wo_stats(self):
        # execute projects get
        response = self.client.get(
            "/api/admin/projects?include_stats=false&is_active=true",
            headers=MOCK_HEADERS
        )

        # check response code
        self.assertEqual(200, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)

        expected_record = {'additional_contact_name': None,
                           'alias': None,
                           'bank_samples': False,
                           'branding_associated_instructions': None,
                           'branding_status': None,
                           'collection': None,
                           'computed_stats': {},
                           'contact_email': None,
                           'contact_name': None,
                           'coordination': None,
                           'deadlines': None,
                           'disposition_comments': None,
                           'do_16s': None,
                           'do_mass_spec': None,
                           'do_metatranscriptomics': None,
                           'do_other': None,
                           'do_rt_qpcr': None,
                           'do_serology': None,
                           'do_shallow_shotgun': None,
                           'do_shotgun': None,
                           'is_blood': None,
                           'is_fecal': None,
                           'is_microsetta': False,
                           'is_other': None,
                           'is_saliva': None,
                           'is_skin': None,
                           'mass_spec_comments': None,
                           'mass_spec_contact_email': None,
                           'mass_spec_contact_name': None,
                           'num_subjects': None,
                           'num_timepoints': None,
                           'plating_start_date': None,
                           'project_id': 8,
                           'project_name': 'Project - %u[zGmÅq=g',
                           'sponsor': None,
                           'start_date': None,
                           'subproject_name': None,
                           'is_active': True}
        self.assertEqual(55, len(response_obj))
        self.assertEqual(expected_record, response_obj[6])

    def test_get_projects_inactive_wo_stats(self):
        # execute projects get
        response = self.client.get(
            "/api/admin/projects?include_stats=false&is_active=false",
            headers=MOCK_HEADERS
        )

        # check response code
        self.assertEqual(200, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)

        expected_record = {'additional_contact_name': None,
                           'alias': None,
                           'bank_samples': False,
                           'branding_associated_instructions': None,
                           'branding_status': None,
                           'collection': None,
                           'computed_stats': {},
                           'contact_email': None,
                           'contact_name': None,
                           'coordination': None,
                           'deadlines': None,
                           'disposition_comments': None,
                           'do_16s': None,
                           'do_mass_spec': None,
                           'do_metatranscriptomics': None,
                           'do_other': None,
                           'do_rt_qpcr': None,
                           'do_serology': None,
                           'do_shallow_shotgun': None,
                           'do_shotgun': None,
                           'is_active': False,
                           'is_blood': None,
                           'is_fecal': None,
                           'is_microsetta': False,
                           'is_other': None,
                           'is_saliva': None,
                           'is_skin': None,
                           'mass_spec_comments': None,
                           'mass_spec_contact_email': None,
                           'mass_spec_contact_name': None,
                           'num_subjects': None,
                           'num_timepoints': None,
                           'plating_start_date': None,
                           'project_id': 2,
                           'project_name': 'Project - /J/xL_|Eãt',
                           'sponsor': None,
                           'start_date': None,
                           'subproject_name': None}
        self.assertEqual(1, len(response_obj))
        self.assertEqual(expected_record, response_obj[0])

    def test_scan_barcode_success(self):
        """Store info on new scan for valid barcode"""

        new_scan_id = None
        try:
            # create post input json with a nonsense date field
            scan_info = {
                "sample_barcode": self.TEST_BARCODE,
                "sample_status": "sample-is-valid",
                "technician_notes": ""
            }
            input_json = json.dumps(scan_info)

            # execute project post (create)
            response = self.client.post(
                "/api/admin/scan/{0}".format(self.TEST_BARCODE),
                content_type='application/json',
                data=input_json,
                headers=MOCK_HEADERS
            )

            # check for successful create response code
            self.assertEqual(201, response.status_code)

            returned_barcode = extract_last_id_from_location_header(response)
            self.assertEqual(self.TEST_BARCODE, returned_barcode)

            response_obj = json.loads(response.data)
            new_scan_id = response_obj['scan_id']
        finally:
            delete_test_scan(new_scan_id)

    def test_scan_barcode_fail_invalid_status(self):
        """Refuse to store scan info with invalid sample_status"""

        new_scan_id = None
        try:
            # create post input json with a nonsense date field
            scan_info = {
                "sample_barcode": self.TEST_BARCODE,
                "sample_status": "happy",
                "technician_notes": ""
            }
            input_json = json.dumps(scan_info)

            # execute project post (create)
            response = self.client.post(
                "/api/admin/scan/{0}".format(self.TEST_BARCODE),
                content_type='application/json',
                data=input_json,
                headers=MOCK_HEADERS
            )

            # check for successful create response code
            self.assertEqual(400, response.status_code)
        finally:
            delete_test_scan(new_scan_id)

    def test_get_daklapack_shipping_options(self):
        # execute shipping options get
        response = self.client.get(
            "/api/admin/daklapack_shipping",
            headers=MOCK_HEADERS
        )

        # check response code
        self.assertEqual(200, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)

        self.assertDictEqual(SHIPPING_TYPES_BY_PROVIDER, response_obj)

    def test_get_daklapack_articles(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            article_dicts_list = admin_repo.get_daklapack_articles()
            t.commit()

        # execute articles get
        response = self.client.get(
            "/api/admin/daklapack_articles",
            headers=MOCK_HEADERS
        )

        # check response code
        self.assertEqual(200, response.status_code)

        # load the response body
        response_obj = json.loads(response.data)

        # get the first article returned and pop out its id
        first_article = response_obj[0]
        first_article.pop("dak_article_id")

        self.assertEqual(len(article_dicts_list), len(response_obj))
        self.assertEqual(FIRST_LIVE_DAK_ARTICLE, response_obj[0])

    def test_email_stats(self):
        with Transaction() as t:
            accts = AccountRepo(t)
            acct1 = accts.get_account("65dcd6c8-69fa-4de8-a33a-3de4957a0c79")
            acct2 = accts.get_account("556f5dc4-8cf2-49ae-876c-32fbdfb005dd")

            # execute articles get
            for project in [None, "American Gut Project", "NotAProj"]:
                response = self.client.post(
                    "/api/admin/account_email_summary",
                    headers=MOCK_HEADERS,
                    content_type='application/json',
                    data=json.dumps({
                        "emails": [acct1.email, acct2.email],
                        "project": project
                    })
                )
                self.assertEqual(200, response.status_code)
                result = json.loads(response.data)
                self.assertEqual(result[0]["account_id"],
                                 "65dcd6c8-69fa-4de8-a33a-3de4957a0c79")
                self.assertEqual(result[1]["account_id"],
                                 "556f5dc4-8cf2-49ae-876c-32fbdfb005dd")
                if project is None or project == "American Gut Project":
                    self.assertEqual(result[0]["sample-is-valid"], 1)
                else:
                    self.assertEqual(result[0].get("sample-is-valid", 0), 0)

    def test_metadata_qiita_compatible_invalid(self):
        data = json.dumps({'sample_barcodes': ['bad']})
        response = self.client.post('/api/admin/metadata/qiita-compatible',
                                    content_type='application/json',
                                    data=data,
                                    headers=MOCK_HEADERS)
        self.assertEqual(404, response.status_code)

        data = json.dumps({'sample_barcodes': ['bad', '000043062']})
        response = self.client.post('/api/admin/metadata/qiita-compatible',
                                    content_type='application/json',
                                    data=data,
                                    headers=MOCK_HEADERS)
        self.assertEqual(404, response.status_code)

    def test_metadata_qiita_compatible_valid(self):
        data = json.dumps({'sample_barcodes': ['000069747', '000051101']})

        response = self.client.post('/api/admin/metadata/qiita-compatible',
                                    content_type='application/json',
                                    data=data,
                                    headers=MOCK_HEADERS)

        self.assertEqual(200, response.status_code)
        result = json.loads(response.data)
        self.assertEqual(set(result.keys()), {'000069747', '000051101'})

    def test_metadata_qiita_compatible_two_templates(self):
        # The surveys attached to barcode '000069747' are known to be 1 and
        # 10001. Submit a template 10 survey and confirm that the code is
        # able to merge filled answers from 1 and 10, and pick the values
        # closest to the timestamp of the original survey.
        with Transaction() as t:
            with t.dict_cursor() as cur:
                # first, find the ids for the barcode and survey we're using
                # as they are dynamically generated.
                cur.execute("select ag_login_id, source_id from "
                            "ag_login_surveys a join source_barcodes_surveys b"
                            " on a.survey_id = b.survey_id and b.barcode = "
                            "'000069747' and survey_template_id = 1")
                row = cur.fetchone()
                account_id = row[0]
                source_id = row[1]

                cur.execute("select ag_kit_barcode_id from ag_kit_barcodes "
                            "where barcode = '000069747'")
                row = cur.fetchone()
                sample_id = row[0]

            sar = SurveyAnswersRepo(t)
            survey_10 = {
                '22': 'Unspecified',
                '108': 'Unspecified',
                '109': 'Unspecified',
                '110': 'Unspecified',
                '111': 'Unspecified',
                '112': '1990',
                '113': 'Unspecified',
                '115': 'Unspecified',
                '148': 'Unspecified',
                '492': 'Unspecified',
                '493': 'Unspecified',
                '502': 'Male'
            }
            survey_id = sar.submit_answered_survey(
                account_id,
                source_id,
                'en_US', 10, survey_10)
            sar.associate_answered_survey_with_sample(
                account_id,
                source_id,
                sample_id,
                survey_id)
            t.commit()

        # query the barcodes
        data = json.dumps({'sample_barcodes': ['000069747', '000051101']})
        response = self.client.post('/api/admin/metadata/qiita-compatible',
                                    content_type='application/json',
                                    data=data,
                                    headers=MOCK_HEADERS)
        self.assertEqual(200, response.status_code)
        result = json.loads(response.data)

        # confirm that the birth_year response from the new survey 10 (1990)
        # did not 'overwrite' the original response from survey 1 (1985).
        self.assertNotEqual(result['000069747']['birth_year'], '1990')
        self.assertEqual(result['000069747']['birth_year'], '1985')

        # confirm that the new attribute 502/gender_v2 (one that is not
        # present in the original survey 1) was merged into the results.
        self.assertEqual(result['000069747']['gender_v2'], 'Male')

        # confirm that the results for the other survey, attached to a
        # different source, did not receive the merged 502/gender_v2 attribute.
        self.assertEqual(result['000051101']['gender_v2'], 'not provided')
        self.assertEqual(result['000051101']['birth_year'], '1968')

        # clean up by deleting the survey we added for testing.
        with Transaction() as t:
            sar = SurveyAnswersRepo(t)
            sar.delete_answered_survey(account_id, survey_id)
            t.commit()

    def test_metadata_qiita_compatible_valid_private(self):
        # BIRTH_MONTH is a question assigned to template 10 and it is also
        # protected (present in EBI_REMOVE list). Query for template 10 and
        # confirm that BIRTH_MONTH (111) is not present in the results.
        with Transaction() as t:
            with t.dict_cursor() as cur:
                # first, find the ids for the barcode and survey we're using
                # as they are dynamically generated.
                cur.execute("select ag_login_id, source_id from "
                            "ag_login_surveys a join source_barcodes_surveys b"
                            " on a.survey_id = b.survey_id and b.barcode = "
                            "'000069747' and survey_template_id = 1")
                row = cur.fetchone()
                account_id = row[0]
                source_id = row[1]

                cur.execute("select ag_kit_barcode_id from ag_kit_barcodes "
                            "where barcode = '000069747'")
                row = cur.fetchone()
                sample_id = row[0]

            sar = SurveyAnswersRepo(t)
            survey_10 = {
                '22': 'Unspecified',
                '108': 'Unspecified',
                '109': 'Unspecified',
                '110': 'Unspecified',
                '111': 'February',
                '112': 'Unspecified',
                '113': 'Unspecified',
                '115': 'Unspecified',
                '148': 'Unspecified',
                '492': 'Unspecified',
                '493': 'Unspecified',
                '502': 'Male'
            }
            survey_id = sar.submit_answered_survey(
                account_id,
                source_id,
                'en_US', 10, survey_10)
            sar.associate_answered_survey_with_sample(
                account_id,
                source_id,
                sample_id,
                survey_id)
            t.commit()
        data = json.dumps({'sample_barcodes': ['000069747']})
        response = self.client.post('/api/admin/metadata/qiita-compatible'
                                    '?include_private=True',
                                    content_type='application/json',
                                    data=data,
                                    headers=MOCK_HEADERS)

        # clean up by deleting the survey we added for testing.
        with Transaction() as t:
            sar = SurveyAnswersRepo(t)
            sar.delete_answered_survey(account_id, survey_id)
            t.commit()

        self.assertEqual(200, response.status_code)
        result = json.loads(response.data)
        self.assertEqual(set(result.keys()), {'000069747'})
        obs = {c.lower() for c in result['000069747']}
        self.assertIn('birth_month', obs)

    def test_metadata_qiita_compatible_valid_no_private(self):
        # BIRTH_MONTH is a question assigned to template 10 and it is also
        # protected (present in EBI_REMOVE list). Query for template 10 and
        # confirm that BIRTH_MONTH (111) is not present in the results.
        with Transaction() as t:
            with t.dict_cursor() as cur:
                # first, find the ids for the barcode and survey we're using
                # as they are dynamically generated.
                cur.execute("select ag_login_id, source_id from "
                            "ag_login_surveys a join source_barcodes_surveys b"
                            " on a.survey_id = b.survey_id and b.barcode = "
                            "'000069747' and survey_template_id = 1")
                row = cur.fetchone()
                account_id = row[0]
                source_id = row[1]

                cur.execute("select ag_kit_barcode_id from ag_kit_barcodes "
                            "where barcode = '000069747'")
                row = cur.fetchone()
                sample_id = row[0]

            sar = SurveyAnswersRepo(t)
            survey_10 = {
                '22': 'Unspecified',
                '108': 'Unspecified',
                '109': 'Unspecified',
                '110': 'Unspecified',
                '111': 'February',
                '112': 'Unspecified',
                '113': 'Unspecified',
                '115': 'Unspecified',
                '148': 'Unspecified',
                '492': 'Unspecified',
                '493': 'Unspecified',
                '502': 'Male'
            }
            survey_id = sar.submit_answered_survey(
                account_id,
                source_id,
                'en_US', 10, survey_10)
            sar.associate_answered_survey_with_sample(
                account_id,
                source_id,
                sample_id,
                survey_id)
            t.commit()
        data = json.dumps({'sample_barcodes': ['000069747']})
        response = self.client.post('/api/admin/metadata/qiita-compatible'
                                    '?include_private=False',
                                    content_type='application/json',
                                    data=data,
                                    headers=MOCK_HEADERS)

        # clean up by deleting the survey we added for testing.
        with Transaction() as t:
            sar = SurveyAnswersRepo(t)
            sar.delete_answered_survey(account_id, survey_id)
            t.commit()

        self.assertEqual(200, response.status_code)
        result = json.loads(response.data)
        self.assertEqual(set(result.keys()), {'000069747'})
        obs = {c.lower() for c in result['000069747']}
        self.assertNotIn('birth_month', obs)

    def _test_post_daklapack_orders(self, order_info, expected_status):
        # NB: order_id and creation_date keys not included as different
        # every time
        expected = [{'order_address': {'address1': '123 Main St',
                                       'address2': '',
                                       'city': 'San Diego',
                                       'companyName': 'Dan H',
                                       'country': 'USA',
                                       'countryCode': 'us',
                                       'firstName': 'Jane',
                                       'insertion': 'Apt 2',
                                       'lastName': 'Doe',
                                       'phone': '(858) 555-1212',
                                       'postalCode': '92210',
                                       'state': 'CA'},
                     'order_success': True},
                    {'daklapack_api_error_code': 409,
                     'daklapack_api_error_msg': 'Got 409',
                     'order_address': {'address1': '29 Side St',
                                       'address2': 'Kew Gardens',
                                       'city': 'Gananoque',
                                       'companyName': 'Dan H',
                                       'country': 'Canada',
                                       'countryCode': 'ca',
                                       'firstName': 'Tom',
                                       'insertion': '',
                                       'lastName': 'Thumb',
                                       'phone': '(858) 555-1212',
                                       'postalCode': 'KG7-448',
                                       'state': 'Ontario'},
                     'order_success': False}]
        order_submissions = None

        input_json = json.dumps(order_info)

        # Not just checking if dicts are equal because there are some keys in
        # the real, returned dictionary that aren't in the expected dictionary
        # (order_id, creationDate) bc they change every time
        def _check_dict_contents(expected_dict, real_dict):
            for curr_expect_k, curr_expect_v in expected_dict.items():
                self.assertIn(curr_expect_k, real_dict)
                curr_real_v = real_dict[curr_expect_k]
                if isinstance(curr_real_v, dict):
                    _check_dict_contents(curr_expect_v, curr_real_v)
                else:
                    self.assertEqual(curr_expect_v, curr_real_v)

        try:
            # execute articles post
            response = self.client.post(
                "api/admin/daklapack_orders",
                content_type='application/json',
                data=input_json,
                headers=MOCK_HEADERS
            )

            response_data = json.loads(response.data)
            order_submissions = response_data.get("order_submissions")

            # check for expected response code & order count
            self.assertEqual(expected_status, response.status_code)
            self.assertEqual(len(expected), len(order_submissions))
            for i in range(0, len(order_submissions)):
                curr_expected = expected[i]
                curr_real = order_submissions[i]
                _check_dict_contents(curr_expected, curr_real)

            return order_submissions
        finally:
            delete_test_daklapack_orders(order_submissions)

    def test_post_daklapack_orders_fully_specified(self):
        # create post input json
        order_info = {
            "project_ids": DUMMY_PROJ_ID_LIST,
            "article_code": DUMMY_DAK_ARTICLE_CODE,
            "addresses": DUMMY_ADDRESSES,
            "shipping_provider": DUMMY_SHIPPING_PROVIDER,
            "shipping_type": DUMMY_SHIPPING_TYPE,
            "description": DUMMY_DAK_ORDER_DESC,
            "fedex_ref_1": DUMMY_FEDEX_REFS[0],
            "fedex_ref_2": DUMMY_FEDEX_REFS[1],
            "fedex_ref_3": DUMMY_FEDEX_REFS[2],
            "planned_send_date": DUMMY_PLANNED_SEND_DATE,
            "quantity": 2
        }

        # NB: these have to be patched *where they will be looked up*, not
        # where they are originally defined; see
        # https://docs.python.org/3/library/unittest.mock.html#where-to-patch
        with patch("microsetta_private_api.admin.admin_impl."
                   "post_daklapack_orders") as mock_dak_post:
            mock_dak_post.side_effect = [make_test_response(201),
                                         make_test_response(409)]

            self._test_post_daklapack_orders(order_info, 200)

    def test_post_daklapack_orders_wo_optionals(self):
        # create post input json
        order_info = {
            "project_ids": DUMMY_PROJ_ID_LIST,
            "article_code": DUMMY_DAK_ARTICLE_CODE,
            "addresses": DUMMY_ADDRESSES,
            "shipping_provider": DUMMY_SHIPPING_PROVIDER,
            "shipping_type": DUMMY_SHIPPING_TYPE,
            "description": None,
            "fedex_ref_1": None,
            "fedex_ref_2": None,
            "fedex_ref_3": None,
            "planned_send_date": None,
            "quantity": 1
        }

        # NB: these have to be patched *where they will be looked up*, not
        # where they are originally defined; see
        # https://docs.python.org/3/library/unittest.mock.html#where-to-patch
        with patch("microsetta_private_api.admin.admin_impl."
                   "post_daklapack_orders") as mock_dak_post:
            mock_dak_post.side_effect = [make_test_response(201),
                                         make_test_response(409)]

            self._test_post_daklapack_orders(order_info, 200)

    def test_query_project_barcode_stats_project_without_strip(self):
        input_json = json.dumps({'project': 7, 'email': 'foobar'})

        with patch("microsetta_private_api.tasks."
                   "per_sample_summary.delay") as mock_delay:
            mock_delay.return_value = None
            response = self.client.post(
                "api/admin/account_project_barcode_summary?"
                "strip_sampleid=false",
                content_type='application/json',
                data=input_json,
                headers=MOCK_HEADERS
            )

        # ...we assume the system is processing to send an email
        # so nothing specific to verify on the response data
        self.assertEqual(200, response.status_code)

    def test_query_project_barcode_stats_project_with_strip(self):
        input_json = json.dumps({'project': 7, 'email': 'foobar'})

        with patch("microsetta_private_api.tasks."
                   "per_sample_summary.delay") as mock_delay:
            mock_delay.return_value = None
            response = self.client.post(
                "api/admin/account_project_barcode_summary?"
                "strip_sampleid=True",
                content_type='application/json',
                data=input_json,
                headers=MOCK_HEADERS
            )

        # ...we assume the system is processing to send an email
        # so nothing specific to verify on the response data
        self.assertEqual(200, response.status_code)

    def test_query_barcode_stats_project_barcodes_without_strip(self):
        barcodes = ['000010307', '000023344', '000036855']
        input_json = json.dumps({'sample_barcodes': barcodes})

        response = self.client.post(
            "api/admin/account_barcode_summary?strip_sampleid=False",
            content_type='application/json',
            data=input_json,
            headers=MOCK_HEADERS
        )
        # an empty string project should be unknown
        self.assertEqual(200, response.status_code)
        response_obj = json.loads(response.data)
        self.assertIn('samples', response_obj)
        response_obj = response_obj['samples']
        self.assertEqual(len(response_obj), 3)

        self.assertEqual([v['sampleid'] for v in response_obj],
                         barcodes)
        exp_status = [None, 'no-associated-source', 'sample-is-valid']
        self.assertEqual([v['sample-status'] for v in response_obj],
                         exp_status)

    def test_query_barcode_stats_project_barcodes_with_strip(self):
        barcodes = ['000010307', '000023344', '000036855']
        input_json = json.dumps({'sample_barcodes': barcodes})

        response = self.client.post(
            "api/admin/account_barcode_summary?strip_sampleid=True",
            content_type='application/json',
            data=input_json,
            headers=MOCK_HEADERS
        )
        # an empty string project should be unkown
        self.assertEqual(200, response.status_code)

        response_obj = json.loads(response.data)
        self.assertIn('samples', response_obj)
        response_obj = response_obj['samples']
        self.assertEqual(len(response_obj), 3)

        self.assertEqual([v['sampleid'] for v in response_obj],
                         [None] * len(barcodes))
        exp_status = [None, 'no-associated-source', 'sample-is-valid']
        self.assertEqual([v['sample-status'] for v in response_obj],
                         exp_status)

    def test_send_email(self):
        def mock_func(*args, **kwargs):
            pass

        info = {
            "issue_type": 'sample',
            "template_args": {"sample_barcode": '000004220'},
            'template': 'sample_is_valid'
        }

        with patch("microsetta_private_api.admin.admin_impl."
                   "celery_send_email") as mock_celery_send_email:
            mock_celery_send_email.apply_async = mock_func

            response = self.client.post(
                "api/admin/email",
                content_type="application/json",
                data=json.dumps(info),
                headers=MOCK_HEADERS)
            self.assertEqual(204, response.status_code)

    def test_generate_ffq_codes(self):
        input_json = json.dumps({"code_quantity": 2})

        response = self.client.post(
            "api/admin/generate_ffq_codes",
            content_type='application/json',
            data=input_json,
            headers=MOCK_HEADERS
        )
        self.assertEqual(200, response.status_code)

        response_obj = json.loads(response.data)

        for ffq_code in response_obj:
            self.assertEqual("TMI", ffq_code[0:3])
