from unittest import TestCase
from datetime import date
import datetime
import dateutil.parser
import psycopg2

import microsetta_private_api.model.project as p

from werkzeug.exceptions import Unauthorized, NotFound

from microsetta_private_api.model.account import Account
from microsetta_private_api.model.address import Address
from microsetta_private_api.model.daklapack_order import DaklapackOrder
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.admin.admin_impl import validate_admin_access

STANDARD_ACCT_ID = "12345678-bbbb-cccc-dddd-eeeeffffffff"
ADMIN_ACCT_ID = "12345678-1234-1234-1234-123412341234"
FIRST_DAKLAPACK_ARTICLE = {'dak_article_code': 350100,
                           'short_description': 'TMI 1 tube',
                           'num_2point5ml_etoh_tubes': 1,
                           'num_7ml_etoh_tube': 0,
                           'num_neoteryx_kit': 0,
                           'outer_sleeve': 'Microsetta',
                           'box': 'Microsetta',
                           'return_label': 'Microsetta',
                           'compartment_bag': 'Microsetta',
                           'num_stool_collector': 0,
                           'instructions': 'Fv1',
                           'registration_card': 'Microsetta',
                           'swabs': '1x bag of two',
                           'rigid_safety_bag': 'yes'}


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


def delete_test_scan(new_scan_id):
    if new_scan_id is not None:
        with Transaction() as t:
            with t.cursor() as cur:
                cur.execute("DELETE FROM barcode_scans "
                            "WHERE "
                            "barcode_scan_id = %s",
                            (new_scan_id,))
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
    _FULL_PROJECT_DICT = {p.PROJ_NAME_KEY: 'full_test_proj',
                          p.IS_MICROSETTA_KEY: True,
                          p.BANK_SAMPLES_KEY: False,
                          p.PLATING_START_DATE_KEY: None,
                          p.CONTACT_NAME_KEY: "Jane Doe",
                          # note key out of order from that used
                          # in project inputs list, sql, etc:
                          # should be fine bc everything SHOULD
                          # be done by name rather than order
                          p.CONTACT_EMAIL_KEY: "jd@test.com",
                          p.ADDTL_CONTACT_NAME_KEY: "John Doe",
                          p.DEADLINES_KEY: "Spring 2021",
                          p.NUM_SUBJECTS_KEY: "Variable",
                          p.NUM_TIMEPOINTS_KEY: "4",
                          p.START_DATE_KEY: "Fall 2020",
                          p.DISPOSITION_COMMENTS_KEY: "Store",
                          p.COLLECTION_KEY: "AGP",
                          p.IS_FECAL_KEY: "X",
                          p.IS_SALIVA_KEY: "",
                          p.IS_SKIN_KEY: "?",
                          p.IS_BLOOD_KEY: "X",
                          p.IS_OTHER_KEY: "Nares, mouth",
                          p.DO_16S_KEY: "",
                          p.DO_SHALLOW_SHOTGUN_KEY: "Subset",
                          p.DO_SHOTGUN_KEY: "X",
                          p.DO_RT_QPCR_KEY: "",
                          p.DO_SEROLOGY_KEY: "",
                          p.DO_METATRANSCRIPTOMICS_KEY: "X",
                          p.DO_MASS_SPEC_KEY: "X",
                          p.MASS_SPEC_COMMENTS_KEY: "Dorrestein",
                          p.MASS_SPEC_CONTACT_NAME_KEY: "Ted Doe",
                          p.MASS_SPEC_CONTACT_EMAIL_KEY:
                              "td@test.com",
                          p.DO_OTHER_KEY: "",
                          p.BRANDING_ASSOC_INSTRUCTIONS_KEY:
                              "branding_doc.pdf",
                          p.BRANDING_STATUS_KEY: "In Review",
                          p.SUBPROJECT_NAME_KEY: "IBL SIBL",
                          p.ALIAS_KEY: "Healthy Sitting",
                          p.SPONSOR_KEY: "Crowdfunded",
                          p.COORDINATION_KEY: "TMI",
                          p.IS_ACTIVE_KEY: True}

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

    def test_create_project_success_full(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            # Note: using dict_cursor here so results are DictRow
            # objects that can easily be converted to a dictionary
            with t.dict_cursor() as cur:
                cur.execute("SELECT project "
                            "FROM barcodes.project "
                            "WHERE project = 'full_test_proj'")
                self.assertEqual(len(cur.fetchall()), 0)

                full_project_dict = self._FULL_PROJECT_DICT.copy()
                full_project_dict[p.PROJ_NAME_KEY] = 'full_test_proj'
                input = p.Project.from_dict(full_project_dict)

                output_id = admin_repo.create_project(input)

                cur.execute("SELECT * "
                            "FROM barcodes.project "
                            "WHERE project = 'full_test_proj'")
                row = cur.fetchone()
                obs_dict = dict(row)
                full_project_dict["project_id"] = output_id
                full_project_dict[p.DB_PROJ_NAME_KEY] = \
                    full_project_dict.pop(p.PROJ_NAME_KEY)
                self.assertEqual(obs_dict, full_project_dict)

                # NB: No need to clean up test project created because it is in
                # a transaction that is never committed!

    def test_create_project_success_no_banking(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            with t.cursor() as cur:
                cur.execute("SELECT project "
                            "FROM barcodes.project "
                            "WHERE project = 'doesnotexist'")
                self.assertEqual(len(cur.fetchall()), 0)

                minimal_project_dict = {p.PROJ_NAME_KEY: 'doesnotexist',
                                        p.IS_MICROSETTA_KEY: True,
                                        p.BANK_SAMPLES_KEY: False}
                input = p.Project.from_dict(minimal_project_dict)

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
                minimal_proj_dict = {p.PROJ_NAME_KEY: 'doesnotexist2',
                                     p.IS_MICROSETTA_KEY: False,
                                     p.BANK_SAMPLES_KEY: True,
                                     p.PLATING_START_DATE_KEY: "2020-07-31"}
                input = p.Project.from_dict(minimal_proj_dict)
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

    def test_update_project_success(self):
        updated_dict = self._FULL_PROJECT_DICT.copy()
        updated_dict[p.PROJ_NAME_KEY] = 'test_proj'
        with Transaction() as t:
            admin_repo = AdminRepo(t)

            input = p.Project.from_dict(updated_dict)
            # existing project 8 in test db
            admin_repo.update_project(8, input)

            with t.dict_cursor() as cur:
                cur.execute("SELECT * "
                            "FROM barcodes.project "
                            "WHERE project_id = 8")
                obs_dict = dict(cur.fetchone())

                updated_dict["project_id"] = 8
                updated_dict[p.DB_PROJ_NAME_KEY] = \
                    updated_dict.pop(p.PROJ_NAME_KEY)
                self.assertEqual(obs_dict, updated_dict)

    def test_create_kits_fail_nonexistent_project(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)

            with self.assertRaisesRegex(KeyError, "does not exist"):
                admin_repo.create_kits(5, 3, '', [10000, 10001])

    def test_create_kits_success_not_microsetta(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            non_tmi = admin_repo.create_kits(5, 3, '',
                                             [33])
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
                            (tuple(non_tmi_kits),))
                observed = cur.fetchall()
                self.assertEqual(len(observed), 0)

    def test_create_kits_success_is_microsetta(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            tmi = admin_repo.create_kits(4, 2, 'foo',
                                         [1])
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
                            (tuple(tmi_kits),))
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

    def _set_up_and_query_projects(self, t, include_stats, is_active_val):
        updated_dict = self._FULL_PROJECT_DICT.copy()
        updated_dict[p.PROJ_NAME_KEY] = 'test_proj'
        input = p.Project.from_dict(updated_dict)

        admin_repo = AdminRepo(t)
        # existing project 8 in test db
        admin_repo.update_project(8, input)

        set_up_sql = """
            -- add some additional scans to project 8 so can test that
            -- computed statistics based on latest scans are choosing all
            -- (and only) the scans that they should:
            -- add a scan w an earlier timestamp (though added into db
            -- later) than existing one showing that this barcode USED TO
            -- have a problem but no longer does.
            insert into barcodes.barcode_scans
            (barcode, scan_timestamp, sample_status)
            VALUES ('000007640', '2012-11-01', 'no-registered-account');

            -- add a second *sample-is-valid* scan for the same barcode
            -- so can ensure that sample status count are distinct
            insert into barcodes.barcode_scans
            (barcode, scan_timestamp, sample_status)
            VALUES ('000007640', '2012-12-01', 'sample-is-valid');

            -- add two additional scans for a different barcode: a valid
            -- scan followed by a problem scan, thus indicting this sample
            -- currently has a problem.
            insert into barcodes.barcode_scans
            (barcode, scan_timestamp, sample_status)
            VALUES ('000070796', '2020-07-01', 'sample-is-valid');

            insert into barcodes.barcode_scans
            (barcode, scan_timestamp, sample_status)
            VALUES ('000070796', '2020-09-01', 'no-registered-account');

            UPDATE barcodes.project SET is_active = FALSE
            WHERE project_id = 2;
        """
        with t.cursor() as cur:
            cur.execute(set_up_sql)

        output = admin_repo.get_projects(include_stats, is_active_val)

        updated_dict["project_id"] = 8
        computed_stats = \
            {p.NUM_FULLY_RETURNED_KITS_KEY: 1,
             p.NUM_KITS_KEY: 5,
             p.NUM_KITS_W_PROBLEMS_KEY: 1,
             'num_no_associated_source': 0,
             'num_no_collection_info': 0,
             'num_no_registered_account': 1,
             'num_received_unknown_validity': 0,
             'num_sample_is_valid': 4,
             p.NUM_PARTIALLY_RETURNED_KITS_KEY: 2,
             p.NUM_SAMPLES_KEY: 20,
             p.NUM_SAMPLES_RECEIVED_KEY: 5,
             p.NUM_UNIQUE_SOURCES_KEY: 4}

        updated_dict[p.COMPUTED_STATS_KEY] = \
            computed_stats if include_stats else {}

        return updated_dict, output

    def test_get_projects_all_w_stats(self):
        with Transaction() as t:
            updated_dict, output = self._set_up_and_query_projects(
                t, include_stats=True, is_active_val=None)

        # Test we have the correct number of total projects
        self.assertEqual(len(output), 56)

        # For one fully-characterized test project, ensure all the
        # output values are what we expect (project 8)
        self.assertEqual(updated_dict, output[7].to_api())

    def test_get_projects_active_w_stats(self):
        with Transaction() as t:
            updated_dict, output = self._set_up_and_query_projects(
                t, include_stats=True, is_active_val=True)

        # Test we have the correct number of active projects
        self.assertEqual(len(output), 55)

        # For one fully-characterized test project, ensure all the
        # output values are what we expect.  Project 8 is now 7th in
        # list (note zero-based) bc project 2 is inactive, so not returned
        self.assertEqual(updated_dict, output[6].to_api())

    def test_get_projects_inactive_w_stats(self):
        with Transaction() as t:
            with t.cursor() as cur:
                cur.execute("UPDATE barcodes.project"
                            " SET is_active = FALSE"
                            " WHERE project_id = 8;")

            updated_dict, output = self._set_up_and_query_projects(
                t, include_stats=True, is_active_val=False)

        updated_dict["is_active"] = False

        # Test we have the correct number of inactive projects
        self.assertEqual(len(output), 2)

        # For one fully-characterized test project, ensure all the
        # output values are what we expect.  Project 8 is now inactive,
        # and is 2nd in (zero-based) list, after project 2
        self.assertEqual(updated_dict, output[1].to_api())

    def test_get_projects_all_wo_stats(self):
        with Transaction() as t:
            updated_dict, output = self._set_up_and_query_projects(
                t, include_stats=False, is_active_val=None)

        # Test we have the correct number of total projects
        self.assertEqual(len(output), 56)

        # For one fully-characterized test project, ensure all the
        # output values are what we expect (project 8)
        self.assertEqual(updated_dict, output[7].to_api())

    def test_get_projects_active_wo_stats(self):
        with Transaction() as t:
            updated_dict, output = self._set_up_and_query_projects(
                t, include_stats=False, is_active_val=True)

        # Test we have the correct number of active projects
        self.assertEqual(len(output), 55)

        # For one fully-characterized test project, ensure all the
        # output values are what we expect.  Project 8 is now 7th in
        # list (note zero-based) bc project 2 is inactive, so not returned
        self.assertEqual(updated_dict, output[6].to_api())

    def test_get_projects_inactive_wo_stats(self):
        with Transaction() as t:
            with t.cursor() as cur:
                cur.execute("UPDATE barcodes.project"
                            " SET is_active = FALSE"
                            " WHERE project_id = 8;")

            updated_dict, output = self._set_up_and_query_projects(
                t, include_stats=False, is_active_val=False)

        updated_dict["is_active"] = False

        # Test we have the correct number of inactive projects
        self.assertEqual(len(output), 2)

        # For one fully-characterized test project, ensure all the
        # output values are what we expect.  Project 8 is now inactive,
        # and is 2nd in (zero-based) list, after project 2
        self.assertEqual(updated_dict, output[1].to_api())

    def test_get_daklapack_articles(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            articles = admin_repo.get_daklapack_articles()
            self.assertEqual(24, len(articles))
            first_article = articles[0]
            first_article.pop("dak_article_id")
            self.assertEqual(FIRST_DAKLAPACK_ARTICLE, first_article)

    def test_create_daklapack_order(self):
        with Transaction() as t:
            # need a valid submitter id from the account table to input
            with t.dict_cursor() as cur:
                cur.execute("SELECT id, first_name, last_name "
                            "FROM ag.account "
                            "WHERE account_type = 'admin' "
                            "ORDER BY id "
                            "LIMIT 1;")
                submitter_record = cur.fetchone()
                submitter_id = submitter_record[0]
                submitter_name = f"{submitter_record[1]} " \
                                 f"{submitter_record[2]}"

                # need real project ids to show can link order to project
                cur.execute("SELECT project_id "
                            "FROM barcodes.project "
                            "ORDER BY project_id "
                            "LIMIT 2;")
                project_id_records = cur.fetchall()
                project_ids = [x[0] for x in project_id_records]

            order_struct = {
                'orderId': '7ed917ef-0c4d-431a-9aa0-0a1f4f41f44b',
                'articles': [
                    {
                        'articleCode': '350102',
                        'addresses': [
                            {
                                'firstName': 'Jane',
                                'lastName': 'Doe',
                                'address1': '123 Main St',
                                'insertion': 'Apt 2',
                                'address2': '',
                                'postalCode': 92210,
                                'city': 'San Diego',
                                'state': 'CA',
                                'country': 'USA',
                                'countryCode': 'us',
                                'phone': '(858) 555-1212',
                                'creationDate': '2020-10-09T22:43:52.219328Z',
                                'companyName': submitter_name
                            },
                            {
                                'firstName': 'Tom',
                                'lastName': 'Thumb',
                                'address1': '29 Side St',
                                'insertion': '',
                                'address2': 'Kew Gardens',
                                'postalCode': 'KG7-448',
                                'city': 'Gananoque',
                                'state': 'Ontario',
                                'country': 'Canada',
                                'countryCode': 'ca',
                                'phone': '(858) 555-1212',
                                'creationDate': '2020-10-09T22:43:52.219350Z',
                                'companyName': submitter_name
                            }
                        ]
                    }
                ],
                'shippingProvider': 'FedEx',
                'shippingType': 'FEDEX_2_DAY',
                'shippingProviderMetadata': [
                    {'key': 'Reference 1',
                     'value': 'Bill Ted'}
                ]
            }

            acct_repo = AccountRepo(t)
            submitter_acct = acct_repo.get_account(submitter_id)

            input_id = '7ed917ef-0c4d-431a-9aa0-0a1f4f41f44b'
            creation_timestamp = dateutil.parser.isoparse(
                "2020-10-09T22:43:52.219328Z")
            last_polling_timestamp = dateutil.parser.isoparse(
                "2020-10-19T12:40:19.219328Z")
            desc = "a description"
            hold_msg = "hold this order"
            last_status = "accepted"

            # create dummy daklapack order object
            input = DaklapackOrder(input_id, submitter_acct, list(project_ids),
                                   order_struct, desc, hold_msg,
                                   creation_timestamp, last_polling_timestamp,
                                   last_status)

            # call create_daklapack_order
            admin_repo = AdminRepo(t)
            returned_id = admin_repo.create_daklapack_order(input)

            self.assertEqual(input_id, returned_id)

            expected_record = [input_id,
                               submitter_id,
                               desc,
                               hold_msg,
                               order_struct,
                               creation_timestamp,
                               last_polling_timestamp,
                               last_status]

            # check db to show new records exist
            with t.dict_cursor() as cur:
                # need real project ids to show can link order to project
                cur.execute("SELECT * "
                            "FROM barcodes.daklapack_order "
                            "WHERE dak_order_id =  %s",
                            (input_id, ))
                curr_records = cur.fetchall()
                self.assertEqual(len(curr_records), 1)
                self.assertEqual(expected_record, curr_records[0])

                cur.execute("SELECT project_id "
                            "FROM barcodes.daklapack_order_to_project "
                            "WHERE dak_order_id =  %s",
                            (input_id, ))
                curr_proj_records = cur.fetchall()
                self.assertEqual(len(curr_proj_records), 2)
                for curr_proj_rec in curr_proj_records:
                    self.assertTrue(curr_proj_rec[0] in project_ids)

        # NB: all the above happens within a transaction that we then DO NOT
        # commit so the db changes are not permanent
