import pytest
from unittest import TestCase
from unittest.mock import patch
from flask import Response
import json
import microsetta_private_api.server
from microsetta_private_api.model.account import Account, Address
from microsetta_private_api.model.project import Project
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.api.tests.test_api import (  # noqa
    client,
    MOCK_HEADERS,  ACCT_ID_1, ACCT_MOCK_ISS, ACCT_MOCK_SUB,
    extract_last_id_from_location_header)
from microsetta_private_api.admin.tests.test_admin_repo import \
    FIRST_DAKLAPACK_ARTICLE, delete_test_scan
from microsetta_private_api.model.tests.test_daklapack_order import \
    DUMMY_PROJ_ID_LIST, DUMMY_DAK_ARTICLE_CODE, DUMMY_ADDRESSES, \
    DUMMY_DAK_ORDER_DESC, DUMMY_HOLD_MSG, DUMMY_FEDEX_REFS


DUMMY_PROJ_NAME = "test project"
# although the article code is stored as a string in the json that we
# send to daklapack, it is stored as an int in our db's daklapack_article table
# so our private api expects it to be sent as an int
DUMMY_INT_DAK_ARTICLE_CODE = int(DUMMY_DAK_ARTICLE_CODE)


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
                      "fakekit",
                      "en_US")
        acct_repo.create_account(acc)

        with t.cursor() as cur:
            cur.execute("UPDATE barcodes.project"
                        " SET is_active = FALSE"
                        " WHERE project_id = 2")
        t.commit()


def delete_test_daklapack_order(new_order_id):
    if new_order_id is not None:
        with Transaction() as t:
            with t.cursor() as cur:
                cur.execute("DELETE FROM barcodes.daklapack_order_to_project "
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
    result.text = f"Got {status_code}"
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
        self.assertEqual(FIRST_DAKLAPACK_ARTICLE, response_obj[0])

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
        data = json.dumps({'sample_barcodes': ['bad', '000004216']})
        response = self.client.post('/api/admin/metadata/qiita-compatible',
                                    content_type='application/json',
                                    data=data,
                                    headers=MOCK_HEADERS)
        self.assertEqual(404, response.status_code)

    def test_metadata_qiita_compatible_valid(self):
        data = json.dumps({'sample_barcodes': ['000004216', '000004213']})
        response = self.client.post('/api/admin/metadata/qiita-compatible',
                                    content_type='application/json',
                                    data=data,
                                    headers=MOCK_HEADERS)
        self.assertEqual(200, response.status_code)
        result = json.loads(response.data)
        self.assertEqual(set(result.keys()), {'000004216', '000004213'})

    def test_metadata_qiita_compatible_valid_private(self):
        data = json.dumps({'sample_barcodes': ['000004216', '000004213']})
        response = self.client.post('/api/admin/metadata/qiita-compatible'
                                    '?include_private=True',
                                    content_type='application/json',
                                    data=data,
                                    headers=MOCK_HEADERS)
        self.assertEqual(200, response.status_code)
        result = json.loads(response.data)
        self.assertEqual(set(result.keys()), {'000004216', '000004213'})
        obs = {c.lower() for c in result['000004216']}
        self.assertIn('about_yourself_text', obs)

    def test_metadata_qiita_compatible_valid_no_private(self):
        data = json.dumps({'sample_barcodes': ['000004216', '000004213']})
        response = self.client.post('/api/admin/metadata/qiita-compatible'
                                    '?include_private=False',
                                    content_type='application/json',
                                    data=data,
                                    headers=MOCK_HEADERS)
        self.assertEqual(200, response.status_code)
        result = json.loads(response.data)
        self.assertEqual(set(result.keys()), {'000004216', '000004213'})
        obs = {c.lower() for c in result['000004216']}
        self.assertNotIn('about_yourself_text', obs)

        # sanity check the the default is false
        data = json.dumps({'sample_barcodes': ['000004216', '000004213']})
        response = self.client.post('/api/admin/metadata/qiita-compatible',
                                    content_type='application/json',
                                    data=data,
                                    headers=MOCK_HEADERS)
        self.assertEqual(200, response.status_code)
        result = json.loads(response.data)
        self.assertEqual(set(result.keys()), {'000004216', '000004213'})
        obs = {c.lower() for c in result['000004216']}
        self.assertNotIn('about_yourself_text', obs)

    def _test_post_daklapack_orders(self, order_info, expected_status):
        input_json = json.dumps(order_info)

        result = None
        new_order_id = None

        try:
            # execute articles post
            response = self.client.post(
                "api/admin/daklapack_orders",
                content_type='application/json',
                data=input_json,
                headers=MOCK_HEADERS
            )

            # check for expected response code
            self.assertEqual(expected_status, response.status_code)

            if expected_status == 201:
                new_order_id = extract_last_id_from_location_header(response)

                result = json.loads(response.data)
                for a_key in ["order_id", "email_success"]:
                    self.assertTrue(a_key in result)

            return result
        finally:
            delete_test_daklapack_order(new_order_id)

    def test_post_daklapack_orders_success_fully_specified(self):
        # create post input json with a nonsense date field
        order_info = {
            "project_ids": DUMMY_PROJ_ID_LIST,
            "article_code": DUMMY_INT_DAK_ARTICLE_CODE,
            "addresses": DUMMY_ADDRESSES,
            "description": DUMMY_DAK_ORDER_DESC,
            "fedex_ref_1": DUMMY_FEDEX_REFS[0],
            "fedex_ref_2": DUMMY_FEDEX_REFS[1],
            "fedex_ref_3": DUMMY_FEDEX_REFS[2],
            "fulfillment_hold_msg": DUMMY_HOLD_MSG
        }

        # NB: these have to be patched *where they will be looked up*, not
        # where they are originally defined; see
        # https://docs.python.org/3/library/unittest.mock.html#where-to-patch
        with patch("microsetta_private_api.admin.admin_impl."
                   "post_daklapack_order") as mock_dak_post:
            mock_dak_post.side_effect = [make_test_response(201)]
            with patch("microsetta_private_api.admin.admin_impl."
                       "send_daklapack_hold_email") as mock_email:
                mock_email.side_effect = [True]

                real_out = self._test_post_daklapack_orders(order_info, 201)
                # has a hold message, so hold email sent
                self.assertTrue(real_out["email_success"])

    def test_post_daklapack_orders_success_but_email_failure(self):
        # create post input json with a nonsense date field
        order_info = {
            "project_ids": DUMMY_PROJ_ID_LIST,
            "article_code": DUMMY_INT_DAK_ARTICLE_CODE,
            "addresses": DUMMY_ADDRESSES,
            "description": DUMMY_DAK_ORDER_DESC,
            "fedex_ref_1": DUMMY_FEDEX_REFS[0],
            "fedex_ref_2": DUMMY_FEDEX_REFS[1],
            "fedex_ref_3": DUMMY_FEDEX_REFS[2],
            "fulfillment_hold_msg": DUMMY_HOLD_MSG
        }

        # NB: these have to be patched *where they will be looked up*, not
        # where they are originally defined; see
        # https://docs.python.org/3/library/unittest.mock.html#where-to-patch
        with patch("microsetta_private_api.admin.admin_impl."
                   "post_daklapack_order") as mock_dak_post:
            mock_dak_post.side_effect = [make_test_response(201)]
            with patch("microsetta_private_api.admin.admin_impl."
                       "send_daklapack_hold_email") as mock_email:
                mock_email.side_effect = [False]

                real_out = self._test_post_daklapack_orders(order_info, 201)
                # has a hold message, but hold email failed to send
                self.assertFalse(real_out["email_success"])

    def test_post_daklapack_orders_success_wo_optionals(self):
        # create post input json with a nonsense date field
        order_info = {
            "project_ids": DUMMY_PROJ_ID_LIST,
            "article_code": DUMMY_INT_DAK_ARTICLE_CODE,
            "addresses": DUMMY_ADDRESSES,
            "description": None,
            "fedex_ref_1": None,
            "fedex_ref_2": None,
            "fedex_ref_3": None,
            "fulfillment_hold_msg": None
        }

        # NB: these have to be patched *where they will be looked up*, not
        # where they are originally defined; see
        # https://docs.python.org/3/library/unittest.mock.html#where-to-patch
        with patch("microsetta_private_api.admin.admin_impl."
                   "post_daklapack_order") as mock_dak_post:
            mock_dak_post.side_effect = [make_test_response(201)]
            with patch("microsetta_private_api.admin.admin_impl."
                       "send_daklapack_hold_email") as mock_email:
                mock_email.side_effect = [True]
                real_out = self._test_post_daklapack_orders(order_info, 201)
                # has no hold message, so no hold email sent
                self.assertIsNone(real_out["email_success"])

    def test_post_daklapack_orders_failure_dak_api(self):
        # create post input json with a nonsense date field
        order_info = {
            "project_ids": DUMMY_PROJ_ID_LIST,
            "article_code": DUMMY_INT_DAK_ARTICLE_CODE,
            "addresses": DUMMY_ADDRESSES,
            "description": DUMMY_DAK_ORDER_DESC,
            "fedex_ref_1": DUMMY_FEDEX_REFS[0],
            "fedex_ref_2": DUMMY_FEDEX_REFS[1],
            "fedex_ref_3": DUMMY_FEDEX_REFS[2],
            "fulfillment_hold_msg": DUMMY_HOLD_MSG
        }

        # NB: these have to be patched *where they will be looked up*, not
        # where they are originally defined; see
        # https://docs.python.org/3/library/unittest.mock.html#where-to-patch
        with patch("microsetta_private_api.admin.admin_impl."
                   "post_daklapack_order") as mock_dak_post:
            mock_dak_post.side_effect = [make_test_response(401)]
            # actually shouldn't get to trying to send email, but just in case
            # code doesn't act as expected, don't want to really email anyone!
            with patch("microsetta_private_api.admin.admin_impl."
                       "send_daklapack_hold_email") as mock_email:
                mock_email.side_effect = [True]
                self._test_post_daklapack_orders(order_info, 401)

    def test_query_barcode_stats_no_project_no_barcodes(self):
        input_json = json.dumps({'project': 0, 'sample_barcodes': None})

        response = self.client.post(
            "api/admin/account_barcode_summary",
            content_type='application/json',
            data=input_json,
            headers=MOCK_HEADERS
        )

        # an empty string project should be unkown
        self.assertEqual(404, response.status_code)

    def test_query_barcode_stats_project_no_barcodes(self):
        input_json = json.dumps({'project': 7, 'sample_barcodes': None})

        response = self.client.post(
            "api/admin/account_barcode_summary",
            content_type='application/json',
            data=input_json,
            headers=MOCK_HEADERS
        )

        self.assertEqual(200, response.status_code)

        response_obj = json.loads(response.data)

        # there are 24 samples with project 7 in the test db
        self.assertEqual(len(response_obj), 24)

        # ...10 have been received
        self.assertEqual(sum([v['sample-received']
                              for v in response_obj]), 10)

        # ...9 are valid
        self.assertEqual(sum([v['sample-is-valid']
                              for v in response_obj]), 9)

        # ...1 is missing a source
        self.assertEqual(sum([v['no-associated-source']
                              for v in response_obj]), 1)

    def test_query_barcode_stats_project_barcodes(self):
        barcodes = ['000010307', '000023344', '000036855']
        input_json = json.dumps({'project': 7, 'sample_barcodes': barcodes})

        response = self.client.post(
            "api/admin/account_barcode_summary",
            content_type='application/json',
            data=input_json,
            headers=MOCK_HEADERS
        )
        # an empty string project should be unkown
        self.assertEqual(200, response.status_code)

        response_obj = json.loads(response.data)
        self.assertEqual(len(response_obj), 3)

        self.assertEqual([v['sampleid'] for v in response_obj],
                         barcodes)
        exp_status = [None, 'no-associated-source', 'sample-is-valid']
        self.assertEqual([v['sample-status'] for v in response_obj],
                         exp_status)
