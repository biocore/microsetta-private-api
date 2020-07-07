import pytest
from unittest import TestCase
import json
import microsetta_private_api.server
from microsetta_private_api.model.account import Account, Address
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.api.tests.test_api import client, MOCK_HEADERS, \
    ACCT_ID_1, ACCT_MOCK_ISS, ACCT_MOCK_SUB  # noqa

DUMMY_PROJ_NAME = "test project"


def teardown_test_data():
    with Transaction() as t:
        acct_repo = AccountRepo(t)
        admin_repo = AdminRepo(t)
        acct_repo.delete_account(ACCT_ID_1)
        admin_repo.delete_project_by_name(DUMMY_PROJ_NAME)
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
                      "fakekit")
        acct_repo.create_account(acc)
        t.commit()


@pytest.mark.usefixtures("client")
class AdminApiTests(TestCase):

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
            "/api/admin/create/project",
            content_type='application/json',
            data=input_json,
            headers=MOCK_HEADERS
        )

        # check for successful create response code
        self.assertEqual(201, response.status_code)

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
            "/api/admin/create/project",
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
            "/api/admin/create/project",
            content_type='application/json',
            data=input_json,
            headers=MOCK_HEADERS
        )

        self.assertEqual(400, response.status_code)
