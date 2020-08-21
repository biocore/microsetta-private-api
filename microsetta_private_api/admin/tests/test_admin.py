from unittest import TestCase
from datetime import date
import datetime
import psycopg2

from werkzeug.exceptions import Unauthorized, NotFound

from microsetta_private_api.model.account import Account
from microsetta_private_api.model.address import Address
from microsetta_private_api.model.project import Project, PROJ_NAME_KEY, \
    IS_MICROSETTA_KEY, BANK_SAMPLES_KEY, PLATING_START_DATE_KEY
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.admin.admin_impl import validate_admin_access
from microsetta_private_api.admin.tests.test_admin_api import delete_test_scan

STANDARD_ACCT_ID = "12345678-bbbb-cccc-dddd-eeeeffffffff"
ADMIN_ACCT_ID = "12345678-1234-1234-1234-123412341234"


def add_dummy_scan(scan_dict):
    with Transaction() as t:
        with t.cursor() as cur:
            cur.execute("INSERT INTO barcode_scans "
                        "VALUES "
                        "(%s, %s, %s, %s,%s)",
                        (scan_dict["barcode_scan_id"],
                         scan_dict["barcode"],
                         scan_dict["scan_timestamp"],
                         scan_dict["sample_status"],
                         scan_dict["technician_notes"]))
        t.commit()


class AdminTests(TestCase):
    def setUp(self):
        AdminTests.setup_test_data()

    def tearDown(self):
        AdminTests.teardown_test_data()

    @staticmethod
    def setup_test_data():
        AdminTests.teardown_test_data()

        with Transaction() as t:
            acct_repo = AccountRepo(t)

            acc = Account(STANDARD_ACCT_ID,
                          "foo@baz.com",
                          "standard",
                          "https://MOCKUNITTEST.com",
                          "1234ThisIsNotARealSub",
                          "NotDan",
                          "NotH",
                          Address(
                              "123 Dan Lane",
                              "NotDanville",
                              "CA",
                              12345,
                              "US"
                          ),
                          "fakekit")
            acct_repo.create_account(acc)

            acc = Account(ADMIN_ACCT_ID,
                          "bar@baz.com",
                          "admin",
                          "https://MOCKUNITTEST.com",
                          "5678ThisIsNotARealAdminSub",
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

    @staticmethod
    def teardown_test_data():
        with Transaction() as t:
            acct_repo = AccountRepo(t)
            acct_repo.delete_account(STANDARD_ACCT_ID)
            acct_repo.delete_account(ADMIN_ACCT_ID)
            t.commit()

    def test_validate_admin_access(self):
        token_info_std = {
            "iss": "https://MOCKUNITTEST.com",
            "sub": "1234ThisIsNotARealSub",
        }
        token_info_admin = {
            "iss": "https://MOCKUNITTEST.com",
            "sub": "5678ThisIsNotARealAdminSub",
        }
        token_info_no_such_issuer = {
            "iss": "qqNoZuchIzzuerpp",
            "sub": "NoZuchZub"
        }

        validate_admin_access(token_info_admin)
        try:
            validate_admin_access(token_info_std)
            self.fail("Should have thrown unauthorized")
        except Unauthorized:
            pass
        try:
            validate_admin_access(token_info_no_such_issuer)
            self.fail("Should have thrown unauthorized")
        except Unauthorized:
            pass

class AdminRepoTests(AdminTests):
    # TODO FIXME HACK:  Need to build mock barcodes rather than using
    #  these fixed ones
    def test_retrieve_diagnostics_by_barcode_w_extra_info(self):
        def make_tz_datetime(y, m, d):
            return datetime.datetime(y, m, d, 0, 0,
                                     tzinfo=psycopg2.tz.FixedOffsetTimezone(
                                         offset=-420, name=None))

        # Non-AGP barcode so no acct, source, or sample;
        # also no preexisting scans in test db
        test_barcode = '000004531'
        first_scan_id = 'f7fd3022-3a9c-4f79-b92c-5cebd83cba38'
        second_scan_id = '76aec821-aa28-4dea-a796-2cfd1276f78c'

        first_scan = {
            "barcode_scan_id": first_scan_id,
            "barcode": test_barcode,
            "scan_timestamp": make_tz_datetime(2017, 7, 16),
            "sample_status": 'no-registered-account',
            "technician_notes": "huh?"
        }

        second_scan = {
            "barcode_scan_id": second_scan_id,
            "barcode": test_barcode,
            "scan_timestamp": make_tz_datetime(2020, 12, 4),
            "sample_status": 'sample-is-valid',
            "technician_notes": None
        }
        try:
            add_dummy_scan(first_scan)
            add_dummy_scan(second_scan)

            with Transaction() as t:
                admin_repo = AdminRepo(t)
                diag = admin_repo.retrieve_diagnostics_by_barcode(test_barcode)
                self.assertIsNotNone(diag['barcode_info'])
                self.assertIsNone(diag['account'])
                self.assertIsNone(diag['source'])
                self.assertIsNone(diag['sample'])
                self.assertGreater(len(diag['projects_info']), 0)
                self.assertEqual(len(diag['scans_info']), 2)
                # order matters in the returned vals, so test that
                self.assertEqual(diag['scans_info'][0], first_scan)
                self.assertEqual(diag['scans_info'][1], second_scan)
                self.assertEqual(diag['latest_scan'], second_scan)
        finally:
            delete_test_scan(first_scan_id)
            delete_test_scan(second_scan_id)

    def test_retrieve_diagnostics_by_barcode_wo_scans(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            diag = admin_repo.retrieve_diagnostics_by_barcode('000033903')
            self.assertIsNotNone(diag['barcode_info'])
            self.assertIsNone(diag['account'])
            self.assertIsNone(diag['source'])
            self.assertIsNone(diag['sample'])
            self.assertGreater(len(diag['projects_info']), 0)
            self.assertEqual(len(diag['scans_info']), 0)

    def test_retrieve_diagnostics_by_barcode_nonexistent(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            # Uhh, should this return a 404 not found or just an empty
            # diagnostic object...?
            diag = admin_repo.retrieve_diagnostics_by_barcode('NotABarcode :D')
            self.assertIsNone(diag)

    def test_retrieve_diagnostics_by_barcode_valid_sample(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            diag = admin_repo.retrieve_diagnostics_by_barcode('000004801')
            self.assertIsNotNone(diag['barcode_info'])
            self.assertIsNotNone(diag['account'])
            self.assertIsNotNone(diag['source'])
            self.assertIsNotNone(diag['sample'])
            self.assertGreater(len(diag['scans_info']), 0)
            self.assertGreater(len(diag['projects_info']), 0)

    def test_retrieve_diagnostics_by_barcode_no_source(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            diag = admin_repo.retrieve_diagnostics_by_barcode('000009207')
            self.assertIsNotNone(diag['barcode_info'])
            self.assertIsNotNone(diag['account'])
            self.assertIsNone(diag['source'])
            self.assertIsNotNone(diag['sample'])
            self.assertGreater(len(diag['scans_info']), 0)
            self.assertGreater(len(diag['projects_info']), 0)

    def test_retrieve_diagnostics_by_barcode_no_account(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            diag = admin_repo.retrieve_diagnostics_by_barcode('000030673')
            self.assertIsNotNone(diag['barcode_info'])
            self.assertIsNone(diag['account'])
            self.assertIsNone(diag['source'])
            self.assertIsNotNone(diag['sample'])
            self.assertGreater(len(diag['scans_info']), 0)
            self.assertGreater(len(diag['projects_info']), 0)

    def test_retrieve_diagnostics_by_barcode_not_agp(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            diag = admin_repo.retrieve_diagnostics_by_barcode('000044481')
            self.assertIsNotNone(diag['barcode_info'])
            self.assertIsNone(diag['account'])
            self.assertIsNone(diag['source'])
            self.assertIsNone(diag['sample'])
            self.assertGreater(len(diag['scans_info']), 0)
            self.assertGreater(len(diag['projects_info']), 0)

    def test_create_project_success_no_banking(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            with t.cursor() as cur:
                cur.execute("SELECT project "
                            "FROM barcodes.project "
                            "WHERE project = 'doesnotexist'")
                self.assertEqual(len(cur.fetchall()), 0)

                minimal_project_dict = {PROJ_NAME_KEY: 'doesnotexist',
                                        IS_MICROSETTA_KEY: True,
                                        BANK_SAMPLES_KEY: False}
                input = Project(**minimal_project_dict)

                admin_repo.create_project(input)

                cur.execute("SELECT project, is_microsetta, bank_samples, "
                            "plating_start_date "
                            "FROM barcodes.project "
                            "WHERE project = 'doesnotexist'")
                obs = cur.fetchall()
                self.assertEqual(obs, [('doesnotexist', True, False, None), ])

                # NB: No need to clean up test project created because it is in
                # a transaction that is never committed!

    def test_create_project_success_banking(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            with t.cursor() as cur:
                plating_start = date(2020, 7, 31)
                minimal_proj_dict = {PROJ_NAME_KEY: 'doesnotexist2',
                                     IS_MICROSETTA_KEY: False,
                                     BANK_SAMPLES_KEY: True,
                                     PLATING_START_DATE_KEY: "2020-07-31"}
                input = Project(**minimal_proj_dict)
                admin_repo.create_project(input)
                cur.execute("SELECT project, is_microsetta, bank_samples, "
                            "plating_start_date "
                            "FROM barcodes.project "
                            "WHERE project = 'doesnotexist2'")
                obs = cur.fetchall()
                self.assertEqual(obs, [('doesnotexist2', False, True,
                                        plating_start), ])

                # NB: No need to clean up test project created because it is in
                # a transaction that is never committed!

    def test_create_kits_fail_nonexistent_project(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)

            with self.assertRaisesRegex(KeyError, "does not exist"):
                admin_repo.create_kits(5, 3, '', ['foo', 'bar'])

    def test_create_kits_success_not_microsetta(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            non_tmi = admin_repo.create_kits(5, 3, '',
                                             ['Project - lm3eáqç(>?'])
            self.assertEqual(['created', ], list(non_tmi.keys()))
            self.assertEqual(len(non_tmi['created']), 5)
            for obj in non_tmi['created']:
                self.assertEqual(len(obj['sample_barcodes']), 3)
                self.assertEqual({'kit_id', 'kit_uuid', 'sample_barcodes'},
                                 set(obj))

            # should not be present in the ag tables
            non_tmi_kits = [k['kit_id'] for k in non_tmi['created']]
            with t.cursor() as cur:
                cur.execute("SELECT supplied_kit_id "
                            "FROM ag.ag_kit "
                            "WHERE supplied_kit_id IN %s",
                            (tuple(non_tmi_kits), ))
                observed = cur.fetchall()
                self.assertEqual(len(observed), 0)

    def test_create_kits_success_is_microsetta(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            tmi = admin_repo.create_kits(4, 2, 'foo',
                                         ['American Gut Project'])
            self.assertEqual(['created', ], list(tmi.keys()))
            self.assertEqual(len(tmi['created']), 4)
            for obj in tmi['created']:
                self.assertEqual(len(obj['sample_barcodes']), 2)
                self.assertEqual({'kit_id', 'kit_uuid', 'sample_barcodes'},
                                 set(obj))
                self.assertTrue(obj['kit_id'].startswith('foo_'))

            # should be present in the ag tables
            tmi_kits = [k['kit_id'] for k in tmi['created']]
            with t.cursor() as cur:
                cur.execute("SELECT supplied_kit_id "
                            "FROM ag.ag_kit "
                            "WHERE supplied_kit_id IN %s",
                            (tuple(tmi_kits), ))
                observed = cur.fetchall()
                self.assertEqual(len(observed), 4)

    def test_search_kit_id(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            diag = admin_repo.retrieve_diagnostics_by_kit_id('test')
            self.assertIsNotNone(diag)
            self.assertIsNotNone(diag['kit'])

            diag = admin_repo.retrieve_diagnostics_by_kit_id('NotAKitId!!!!')
            self.assertIsNone(diag)

    def test_search_email(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            diag = admin_repo.retrieve_diagnostics_by_email(
                'yqrc&3x9_9@h7yx5.com')
            self.assertIsNotNone(diag)
            self.assertEqual(len(diag['accounts']), 1)

            diag = admin_repo.retrieve_diagnostics_by_email(
                '.com'
            )
            self.assertIsNotNone(diag)
            self.assertGreater(len(diag['accounts']), 1)

    def test_scan_barcode_success(self):
        with Transaction() as t:
            # TODO FIXME HACK:  Need to build mock barcodes rather than using
            #  these fixed ones

            TEST_BARCODE = '000000001'
            TEST_STATUS = "sample-has-inconsistencies"
            TEST_NOTES = "THIS IS A UNIT TEST"
            admin_repo = AdminRepo(t)

            # check that before doing a scan, no scans are recorded for this
            diag = admin_repo.retrieve_diagnostics_by_barcode(TEST_BARCODE)
            self.assertEqual(len(diag['scans_info']), 0)

            # do a scan
            admin_repo.scan_barcode(
                TEST_BARCODE,
                {
                    "sample_status": TEST_STATUS,
                    "technician_notes": TEST_NOTES
                }
            )

            # show that now a scan is recorded for this barcode
            diag = admin_repo.retrieve_diagnostics_by_barcode(TEST_BARCODE)
            self.assertEqual(len(diag['scans_info']), 1)
            first_scan = diag['scans_info'][0]
            self.assertEqual(first_scan['technician_notes'], TEST_NOTES)
            self.assertEqual(first_scan['sample_status'], TEST_STATUS)

    def test_scan_barcode_error_nonexistent(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            with self.assertRaises(NotFound):
                admin_repo.scan_barcode(
                    "THIZIZNOTAREALBARCODEISWARE",
                    {
                        "sample_status": "Abc",
                        "technician_notes": "123"
                    }
                )
                self.fail("Shouldn't get here")

    def test_get_survey(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)

            BARCODE = '000004216'

            with self.assertRaises(NotFound):
                admin_repo.get_survey_metadata("NOTABARCODE")

            meta = admin_repo.get_survey_metadata(BARCODE,
                                                  survey_template_id=1)

            self.assertEqual(meta['sample_barcode'], BARCODE)
            self.assertIn('host_subject_id', meta)
            # And there should be one survey answered
            self.assertEqual(len(meta['survey_answers']), 1)

            all_meta = admin_repo.get_survey_metadata(BARCODE)

            self.assertEqual(all_meta['sample_barcode'], BARCODE)
            self.assertEqual(all_meta['host_subject_id'],
                             all_meta['host_subject_id'])
            # And there should be more than one survey answered
            self.assertGreater(len(all_meta['survey_answers']), 1)

            # And the meta survey should exist somewhere in all_meta
            found = False
            for survey in all_meta['survey_answers']:
                if "1" in survey["response"] and \
                        survey["response"]["1"][0] == 'DIET_TYPE':
                    found = True
                    self.assertDictEqual(meta['survey_answers'][0],
                                         survey)
            self.assertTrue(found)

    def test_get_projects(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)

            output = admin_repo.get_projects()
            self.assertGreater(len(output), 1)
            first_proj = output[0]
            self.assertEqual(1, first_proj.project_id)
            self.assertEqual("American Gut Project", first_proj.project_name)
            # TODO: expand tests
