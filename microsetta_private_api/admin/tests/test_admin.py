from unittest import TestCase
from datetime import date

from werkzeug.exceptions import Unauthorized, NotFound

from microsetta_private_api.model.account import Account
from microsetta_private_api.model.address import Address
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.admin.admin_impl import validate_admin_access

STANDARD_ACCT_ID = "12345678-bbbb-cccc-dddd-eeeeffffffff"
ADMIN_ACCT_ID = "12345678-1234-1234-1234-123412341234"


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

    def test_search_barcode(self):
        with Transaction() as t:
            # TODO FIXME HACK:  Need to build mock barcodes rather than using
            #  these fixed ones
            admin_repo = AdminRepo(t)
            diag = admin_repo.retrieve_diagnostics_by_barcode('000038448')
            self.assertIsNotNone(diag['barcode'])
            self.assertIsNone(diag['account'])
            self.assertIsNone(diag['source'])
            self.assertIsNotNone(diag['sample'])
            self.assertGreater(len(diag['barcode_info']['projects']), 0)

            diag = admin_repo.retrieve_diagnostics_by_barcode('000033903')
            self.assertIsNotNone(diag['barcode'])
            self.assertIsNone(diag['account'])
            self.assertIsNone(diag['source'])
            self.assertIsNone(diag['sample'])
            self.assertGreater(len(diag['barcode_info']['projects']), 0)

            # Uhh, should this return a 404 not found or just an empty
            # diagnostic object...?
            diag = admin_repo.retrieve_diagnostics_by_barcode('NotABarcode :D')
            self.assertIsNone(diag)

    def test_create_project(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            with t.cursor() as cur:
                cur.execute("SELECT project "
                            "FROM barcodes.project "
                            "WHERE project = 'doesnotexist'")
                self.assertEqual(len(cur.fetchall()), 0)

                admin_repo.create_project('doesnotexist', True, False)
                cur.execute("SELECT project, is_microsetta, bank_samples, "
                            "plating_start_date "
                            "FROM barcodes.project "
                            "WHERE project = 'doesnotexist'")
                obs = cur.fetchall()
                self.assertEqual(obs, [('doesnotexist', True, False, None), ])

                plating_start_date = date(2020, 7, 31)
                admin_repo.create_project('doesnotexist2', False, True,
                                          plating_start_date)
                cur.execute("SELECT project, is_microsetta, bank_samples, "
                            "plating_start_date "
                            "FROM barcodes.project "
                            "WHERE project = 'doesnotexist2'")
                obs = cur.fetchall()
                self.assertEqual(obs, [('doesnotexist2', False, True,
                                        plating_start_date), ])

    def test_create_kits(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)

            with self.assertRaisesRegex(KeyError, "does not exist"):
                admin_repo.create_kits(5, 3, '', ['foo', 'bar'])

            non_tmi = admin_repo.create_kits(5, 3, '',
                                             ['Project - /J/xL_|Eãt'])
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

    def test_scan_barcode(self):
        with Transaction() as t:
            # TODO FIXME HACK:  Need to build mock barcodes rather than using
            #  these fixed ones

            TEST_BARCODE = '000000001'
            TEST_STATUS = "sample-has-inconsistencies"
            TEST_NOTES = "THIS IS A UNIT TEST"
            admin_repo = AdminRepo(t)

            diag = admin_repo.retrieve_diagnostics_by_barcode(TEST_BARCODE)
            prestatus = diag['barcode_info']['status']

            admin_repo.scan_barcode(
                TEST_BARCODE,
                {
                    "sample_status": TEST_STATUS,
                    "technician_notes": TEST_NOTES
                }
            )

            diag = admin_repo.retrieve_diagnostics_by_barcode(TEST_BARCODE)
            self.assertEqual(diag['barcode_info']['technician_notes'],
                             TEST_NOTES)
            self.assertEqual(diag['barcode_info']['sample_status'],
                             TEST_STATUS)
            self.assertEqual(diag['barcode_info']['status'],
                             prestatus)

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

    def test_summary_statistics(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)

            summary = admin_repo.get_project_summary_statistics()
            self.assertGreater(len(summary), 1)
            for stats in summary:
                self.assertIn('project_id', stats)
                self.assertIn('project_name', stats)
                self.assertIn('number_of_samples', stats)

    def test_detailed_project_statistics(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)

            agp_summary = admin_repo.get_project_detailed_statistics(1)
            self.assertIn('project_id', agp_summary)
            self.assertIn('project_name', agp_summary)
            self.assertIn('number_of_samples', agp_summary)
            self.assertIn('number_of_samples_scanned_in', agp_summary)
            self.assertIn('sample_status_counts', agp_summary)
