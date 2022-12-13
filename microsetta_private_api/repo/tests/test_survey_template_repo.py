import unittest
import uuid
from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo
from microsetta_private_api.repo.transaction import Transaction
from psycopg2.errors import ForeignKeyViolation, InvalidTextRepresentation
from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.model.source import Source, HumanInfo
import datetime


# test identifiers with a vio ID
TEST1_ACCOUNT_ID = "80c327ca-a5c7-4c7f-b64b-b219d9ff0b47"
TEST1_SOURCE_ID = None
TEST1_SAMPLE_ID = "125a7cc5-41ae-44ef-983c-6f1a5213f668"
TEST1_SURVEY_ID = None
TEST1_VIO_ID = "1c689634cea0d11b"
TEST1_REGISTRATION_CODE = None


# not in registry
TEST2_ACCOUNT_ID = "735e1689-6976-4d96-9a33-7a19f06602bf"
TEST2_SOURCE_ID = None
TEST2_SAMPLE_ID = "7380bb81-7401-45bd-85a0-51001f5f5cf1"
TEST2_REGISTRATION_CODE = None


# source IDs are not stable in the test database as these
# IDs are derived from a patch
with Transaction() as t:
    with t.cursor() as cur:
        cur.execute("""SELECT source_id
                       FROM ag.ag_kit_barcodes
                       WHERE ag_kit_barcode_id=%s""",
                    (TEST1_SAMPLE_ID, ))
        TEST1_SOURCE_ID = cur.fetchone()

        cur.execute("""SELECT source_id
                       FROM ag.ag_kit_barcodes
                       WHERE ag_kit_barcode_id=%s""",
                    (TEST2_SAMPLE_ID, ))
        TEST2_SOURCE_ID = cur.fetchone()

        cur.execute("""SELECT survey_id
                       FROM ag.ag_login_surveys
                       WHERE ag_login_id=%s
                           AND source_id=%s
                           AND vioscreen_status IS NULL""",
                    (TEST1_ACCOUNT_ID, TEST1_SOURCE_ID))
        TEST1_SURVEY_ID = cur.fetchone()


class SurveyTemplateTests(unittest.TestCase):

    def test_fetch_user_basic_physiology(self):
        with Transaction() as t:
            tr = SurveyTemplateRepo(t)

            # year and gender already set for this survey
            # weight and height are scrambled in the test
            # database as they're remarked as free text
            with t.cursor() as cur:
                cur.execute("""UPDATE ag.survey_answers_other
                               SET response='["254"]'
                               WHERE survey_id=%s AND survey_question_id=%s""",
                            (TEST1_SURVEY_ID, 108))  # height_cm
                cur.execute("""UPDATE ag.survey_answers_other
                               SET response='["100"]'
                               WHERE survey_id=%s AND survey_question_id=%s""",
                            (TEST1_SURVEY_ID, 113))  # weight_kg

                tr = SurveyTemplateRepo(t)

                obs = tr.fetch_user_basic_physiology(TEST1_ACCOUNT_ID,
                                                     TEST1_SOURCE_ID)
                exp = (1973, 'Male', 100, 220.462)
                self.assertEqual(obs, exp)

                cur.execute("""UPDATE ag.survey_answers_other
                               SET response='["100"]'
                               WHERE survey_id=%s AND survey_question_id=%s""",
                            (TEST1_SURVEY_ID, 108))  # height_cm
                cur.execute("""UPDATE ag.survey_answers
                               SET response='inches'
                               WHERE survey_id=%s AND survey_question_id=%s""",
                            (TEST1_SURVEY_ID, 109))  # height_units
                cur.execute("""UPDATE ag.survey_answers
                               SET response='pounds'
                               WHERE survey_id=%s AND survey_question_id=%s""",
                            (TEST1_SURVEY_ID, 114))  # weight_units

                obs = tr.fetch_user_basic_physiology(TEST1_ACCOUNT_ID,
                                                     TEST1_SOURCE_ID)
                exp = (1973, 'Male', 100, 100)
                self.assertEqual(obs, exp)

                # equiv of Unspecified for height
                cur.execute("""UPDATE ag.survey_answers_other
                               SET response='[""]'
                               WHERE survey_id=%s AND survey_question_id=%s""",
                            (TEST1_SURVEY_ID, 108))  # height_cm

                obs = tr.fetch_user_basic_physiology(TEST1_ACCOUNT_ID,
                                                     TEST1_SOURCE_ID)
                exp = (1973, 'Male', None, 100)
                self.assertEqual(obs, exp)

                # equiv of Unspecified for weight
                cur.execute("""UPDATE ag.survey_answers_other
                               SET response='[""]'
                               WHERE survey_id=%s AND survey_question_id=%s""",
                            (TEST1_SURVEY_ID, 113))  # weight_kg

                obs = tr.fetch_user_basic_physiology(TEST1_ACCOUNT_ID,
                                                     TEST1_SOURCE_ID)
                exp = (1973, 'Male', None, None)
                self.assertEqual(obs, exp)

    def test_delete_myfoodrepo(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            template_repo.create_myfoodrepo_entry(TEST2_ACCOUNT_ID,
                                                  TEST2_SOURCE_ID)
            template_repo.set_myfoodrepo_id(TEST2_ACCOUNT_ID,
                                            TEST2_SOURCE_ID,
                                            'foobar')
            e, c = template_repo.get_myfoodrepo_id_if_exists(TEST2_ACCOUNT_ID,
                                                             TEST2_SOURCE_ID)
            self.assertEqual(e, 'foobar')
            template_repo.delete_myfoodrepo(TEST2_ACCOUNT_ID,
                                            TEST2_SOURCE_ID)

            e, c = template_repo.get_myfoodrepo_id_if_exists(TEST2_ACCOUNT_ID,
                                                             TEST2_SOURCE_ID)
            self.assertEqual(e, None)

            # make sure we can delete something that doesn't exist
            template_repo.delete_myfoodrepo(TEST2_ACCOUNT_ID,
                                            TEST2_SOURCE_ID)

            t.rollback()

    def test_set_myfoodrepo_id_valid(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs = template_repo.create_myfoodrepo_entry(TEST2_ACCOUNT_ID,
                                                        TEST2_SOURCE_ID)
            self.assertTrue(obs)

            template_repo.set_myfoodrepo_id(TEST2_ACCOUNT_ID,
                                            TEST2_SOURCE_ID,
                                            "asubject")
            t.rollback()

    def test_set_myfoodrepo_cannot_assign_new_id(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)

            obs = template_repo.create_myfoodrepo_entry(TEST2_ACCOUNT_ID,
                                                        TEST2_SOURCE_ID)
            self.assertTrue(obs)

            template_repo.set_myfoodrepo_id(TEST2_ACCOUNT_ID,
                                            TEST2_SOURCE_ID,
                                            "asubject")

            with self.assertRaises(KeyError):
                template_repo.set_myfoodrepo_id(TEST2_ACCOUNT_ID,
                                                TEST2_SOURCE_ID,
                                                "adifferentsubject")
            t.rollback()

    def test_set_myfoodrepo_no_slot(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)

            with self.assertRaises(KeyError):
                template_repo.set_myfoodrepo_id(TEST2_ACCOUNT_ID,
                                                TEST2_SOURCE_ID,
                                                "asubject")
            t.rollback()

    def test_create_myfoodrepo_id(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs = template_repo.create_myfoodrepo_entry(TEST2_ACCOUNT_ID,
                                                        TEST2_SOURCE_ID)
            self.assertTrue(obs)

            t.rollback()

    def test_create_myfoodrepo_id_no_slots(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)

            # insert 1 less than the available slots
            slots = SERVER_CONFIG['myfoodrepo_slots']
            cur = t.cursor()
            cur.execute("""INSERT INTO ag.myfoodrepo_registry
                           (account_id, source_id)
                           SELECT account_id, id as source_id
                                 FROM ag.source
                                 WHERE id NOT IN %s
                                 LIMIT %s""",
                        ((TEST1_SOURCE_ID, TEST2_SOURCE_ID), slots - 1))

            # our next insertion should work
            obs = template_repo.create_myfoodrepo_entry(TEST1_ACCOUNT_ID,
                                                        TEST1_SOURCE_ID)
            self.assertTrue(obs)

            # we should now be at the maximum number of slots, so our final
            # insertion should fail
            obs = template_repo.create_myfoodrepo_entry(TEST2_ACCOUNT_ID,
                                                        TEST2_SOURCE_ID)
            self.assertFalse(obs)

            # update some of our creation timestamps
            cur.execute("""UPDATE ag.myfoodrepo_registry
                           SET creation_timestamp=NOW() - INTERVAL '30 days'
                           WHERE source_id IN (
                               SELECT source_id
                               FROM ag.myfoodrepo_registry
                               WHERE source_id != %s
                               LIMIT 5
                           )""",
                        (TEST2_SOURCE_ID, ))

            # we now have slots, so we should be successful creating an entry
            obs = template_repo.create_myfoodrepo_entry(TEST2_ACCOUNT_ID,
                                                        TEST2_SOURCE_ID)
            self.assertTrue(obs)

    def test_create_myfoodrepo_id_bad_source_or_account(self):
        # transaction needs to be created each time as the FK violation
        # disrupts the active transaction
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            with self.assertRaises(ForeignKeyViolation):
                template_repo.create_myfoodrepo_entry(str(uuid.uuid4()),
                                                      TEST2_SOURCE_ID)

        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            with self.assertRaises(ForeignKeyViolation):
                template_repo.create_myfoodrepo_entry(TEST2_ACCOUNT_ID,
                                                      str(uuid.uuid4()))

    def test_get_myfoodrepo_id_if_exists(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs = template_repo.get_myfoodrepo_id_if_exists(TEST1_ACCOUNT_ID,
                                                            TEST1_SOURCE_ID)
            self.assertEqual(obs, (None, None))

            obs = template_repo.create_myfoodrepo_entry(TEST1_ACCOUNT_ID,
                                                        TEST1_SOURCE_ID)
            self.assertTrue(obs)

            template_repo.set_myfoodrepo_id(TEST1_ACCOUNT_ID, TEST1_SOURCE_ID,
                                            "asubject")
            obs = template_repo.get_myfoodrepo_id_if_exists(TEST1_ACCOUNT_ID,
                                                            TEST1_SOURCE_ID)
            self.assertEqual(obs[0], "asubject")
            self.assertTrue(obs[1] is not None)

    def test_create_polyphenol_ffq_entry_valid(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs = template_repo.create_polyphenol_ffq_entry(TEST1_ACCOUNT_ID,
                                                            TEST1_SOURCE_ID,
                                                            'en_US',
                                                            'THDMI')
            try:
                uuid.UUID(obs)
                valid_uuid_returned = True
            except ValueError:
                valid_uuid_returned = False
            self.assertTrue(valid_uuid_returned)

    def test_create_polyphenol_ffq_entry_invalid(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            with self.assertRaises(InvalidTextRepresentation):
                template_repo.create_polyphenol_ffq_entry('',
                                                          TEST1_SOURCE_ID,
                                                          '',
                                                          '')

    def test_get_polyphenol_ffq_id_if_exists_true(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            test_pffq_id = \
                template_repo.create_polyphenol_ffq_entry(TEST1_ACCOUNT_ID,
                                                          TEST1_SOURCE_ID,
                                                          'en_US',
                                                          'THDMI')
            obs = \
                template_repo.get_polyphenol_ffq_id_if_exists(TEST1_ACCOUNT_ID,
                                                              TEST1_SOURCE_ID)
            self.assertEqual((test_pffq_id, 'THDMI'), obs)

    def test_get_polyphenol_ffq_id_if_exists_false(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs = \
                template_repo.get_polyphenol_ffq_id_if_exists(TEST1_ACCOUNT_ID,
                                                              TEST1_SOURCE_ID)
            self.assertEqual(obs, (None, None))

    def test_delete_polyphenol_ffq(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            template_repo.create_polyphenol_ffq_entry(TEST1_ACCOUNT_ID,
                                                      TEST1_SOURCE_ID,
                                                      'en_US',
                                                      'THDMI')
            obs, _ = \
                template_repo.get_polyphenol_ffq_id_if_exists(TEST1_ACCOUNT_ID,
                                                              TEST1_SOURCE_ID)
            self.assertTrue(obs is not None)
            template_repo.delete_polyphenol_ffq(TEST1_ACCOUNT_ID,
                                                TEST1_SOURCE_ID)
            obs, _ = \
                template_repo.get_polyphenol_ffq_id_if_exists(TEST1_ACCOUNT_ID,
                                                              TEST1_SOURCE_ID)
            self.assertTrue(obs is None)

            # test we can delete something that doesn't exist
            template_repo.delete_polyphenol_ffq(TEST1_ACCOUNT_ID,
                                                TEST1_SOURCE_ID)

    def test_delete_spain_ffq(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            template_repo.create_spain_ffq_entry(TEST1_ACCOUNT_ID,
                                                 TEST1_SOURCE_ID)
            obs = template_repo.get_spain_ffq_id_if_exists(TEST1_ACCOUNT_ID,
                                                           TEST1_SOURCE_ID)
            self.assertTrue(obs is not None)
            template_repo.delete_spain_ffq(TEST1_ACCOUNT_ID,
                                           TEST1_SOURCE_ID)
            obs = template_repo.get_spain_ffq_id_if_exists(TEST1_ACCOUNT_ID,
                                                           TEST1_SOURCE_ID)
            self.assertTrue(obs is None)

            # test we can delete something that doesn't exist
            template_repo.delete_spain_ffq(TEST1_ACCOUNT_ID,
                                           TEST1_SOURCE_ID)

    def test_create_spain_ffq_entry_valid(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs = template_repo.create_spain_ffq_entry(TEST1_ACCOUNT_ID,
                                                       TEST1_SOURCE_ID)
            try:
                uuid.UUID(obs)
                valid_uuid_returned = True
            except ValueError:
                valid_uuid_returned = False
            self.assertTrue(valid_uuid_returned)

    def test_create_spain_ffq_entry_invalid(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            with self.assertRaises(InvalidTextRepresentation):
                template_repo.create_spain_ffq_entry('',
                                                     TEST1_SOURCE_ID)

    def test_get_spain_ffq_id_if_exists_true(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            test_sffq_id = \
                template_repo.create_spain_ffq_entry(TEST1_ACCOUNT_ID,
                                                     TEST1_SOURCE_ID)
            obs = \
                template_repo.get_spain_ffq_id_if_exists(TEST1_ACCOUNT_ID,
                                                         TEST1_SOURCE_ID)
            self.assertEqual(test_sffq_id, obs)

    def test_get_spain_ffq_id_if_exists_false(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs = \
                template_repo.get_spain_ffq_id_if_exists(TEST1_ACCOUNT_ID,
                                                         TEST1_SOURCE_ID)
            self.assertEqual(obs, None)

    def test_create_vioscreen_id_valid(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs = template_repo.create_vioscreen_id(TEST2_ACCOUNT_ID,
                                                    TEST2_SOURCE_ID)
            self.assertTrue(obs is not None)
            t.rollback()

    def test_create_vioscreen_id_idempotent(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs1 = template_repo.create_vioscreen_id(TEST2_ACCOUNT_ID,
                                                     TEST2_SOURCE_ID,
                                                     TEST2_SAMPLE_ID,
                                                     TEST2_REGISTRATION_CODE)
            obs2 = template_repo.create_vioscreen_id(TEST2_ACCOUNT_ID,
                                                     TEST2_SOURCE_ID,
                                                     TEST2_SAMPLE_ID,
                                                     TEST2_REGISTRATION_CODE)
            self.assertEqual(obs1, obs2)

            obs = template_repo.create_vioscreen_id(TEST1_ACCOUNT_ID,
                                                    TEST1_SOURCE_ID,
                                                    TEST1_SAMPLE_ID,
                                                    TEST1_REGISTRATION_CODE)
            self.assertEqual(obs, TEST1_VIO_ID)
            t.rollback()

    def test_create_vioscreen_id_bad_source_or_account(self):
        # transaction needs to be created each time as the FK violation
        # disrupts the active transaction
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            with self.assertRaises(ForeignKeyViolation):
                template_repo.create_vioscreen_id(str(uuid.uuid4()),
                                                  TEST2_SOURCE_ID)

        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            with self.assertRaises(ForeignKeyViolation):
                template_repo.create_vioscreen_id(TEST2_ACCOUNT_ID,
                                                  str(uuid.uuid4()))

    def test_get_vioscreen_all_ids_if_exists_valid(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs = \
                template_repo.get_vioscreen_all_ids_if_exists(TEST1_ACCOUNT_ID,
                                                              TEST1_SOURCE_ID)
            self.assertEqual(obs, (TEST1_VIO_ID, ))

    def test_get_vioscreen_id_if_exists_valid(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs = template_repo.get_vioscreen_id_if_exists(TEST1_ACCOUNT_ID,
                                                           TEST1_SOURCE_ID)
            self.assertEqual(obs, TEST1_VIO_ID)

    def test_get_vioscreen_id_if_exists_invalid(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs = template_repo.get_vioscreen_id_if_exists(TEST2_ACCOUNT_ID,
                                                           TEST2_SOURCE_ID)
            self.assertEqual(obs, None)

    def test_get_vioscreen_sample_to_user(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs = template_repo.get_vioscreen_sample_to_user()

        # manually checked using
        # select barcode, sample_id, vio_id
        # from ag.vioscreen_registry
        #    join ag.ag_kit_barcodes on sample_id=ag_kit_barcode_id
        # limit 10;
        tests = [('000031536', 'b98c5ac966b754ff'),
                 ('000020495', '8fecc8f34a133eb8'),
                 ('000023245', '52abc2ea83c08b96')]
        for sample, user in tests:
            self.assertEqual(obs.get(sample), user)

    def test_delete_vioscreen(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)

            obs = template_repo.get_vioscreen_id_if_exists(TEST1_ACCOUNT_ID,
                                                           TEST1_SOURCE_ID,
                                                           TEST1_SAMPLE_ID)
            self.assertEqual(obs, TEST1_VIO_ID)

            template_repo.delete_vioscreen(TEST1_ACCOUNT_ID,
                                           TEST1_SOURCE_ID)

            obs = template_repo.get_vioscreen_id_if_exists(TEST1_ACCOUNT_ID,
                                                           TEST1_SOURCE_ID,
                                                           TEST1_SAMPLE_ID)
            self.assertEqual(obs, None)

            # test we can delete something that doesn't exist
            obs = template_repo.get_vioscreen_id_if_exists(TEST1_ACCOUNT_ID,
                                                           TEST1_SOURCE_ID,
                                                           TEST1_SAMPLE_ID)
            self.assertEqual(obs, None)

    def test_has_external_surveys(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)

            obs = template_repo.has_external_surveys(TEST1_ACCOUNT_ID,
                                                     TEST1_SOURCE_ID)
            self.assertTrue(obs)

            obs = template_repo.has_external_surveys(TEST2_ACCOUNT_ID,
                                                     TEST2_SOURCE_ID)
            self.assertFalse(obs)

    def test_generate_empty_survey(self):
        with Transaction() as t:
            sar = SurveyTemplateRepo(t)

            # generate a legacy (retired) template "Primary Questionnaire"
            obs = sar._generate_empty_survey(1)
            self.assertEqual(obs, self.empty_survey_1)

            # generate a current template "Basic Information"
            obs = sar._generate_empty_survey(SurveyTemplateRepo.BASIC_INFO_ID)
            self.assertEqual(obs, self.empty_survey_10)

            # handle invalid template values
            with self.assertRaises(ValueError):
                sar._generate_empty_survey(0)
            with self.assertRaises(ValueError):
                sar._generate_empty_survey(-1)
            with self.assertRaises(ValueError):
                sar._generate_empty_survey(100)

            # handle remote template id
            with self.assertRaises(ValueError):
                sar._generate_empty_survey(SurveyTemplateRepo.VIOSCREEN_ID)

    def _create_source(self, account_id, source_id=None):
        with Transaction() as t:
            sr = SourceRepo(t)

            HUMAN_INFO = HumanInfo(None, None, None, None, None, None, None,
                                   None)
            HUMAN_INFO.email = 'foo@bar.com'
            HUMAN_INFO.is_juvenile = False
            HUMAN_INFO.parent1_name = None
            HUMAN_INFO.parent2_name = None
            HUMAN_INFO.deceased_parent = None
            HUMAN_INFO.consent_date = datetime.datetime.now()
            HUMAN_INFO.date_revoked = None
            HUMAN_INFO.assent_obtainer = None
            HUMAN_INFO.age_range = '18-plus'

            if not source_id:
                source_id = 'ffffffff-ffff-ffff-aaaa-aaaaaaaaaaaa'

            HUMAN_SOURCE = Source(source_id,
                                  account_id,
                                  Source.SOURCE_TYPE_HUMAN,
                                  'test person',
                                  HUMAN_INFO)

            sr.create_source(HUMAN_SOURCE)

            t.commit()

            return HUMAN_SOURCE

    def _clean_up(self, account_id, source_id, survey_ids):
        with Transaction() as t:
            sr = SourceRepo(t)
            sar = SurveyAnswersRepo(t)
            for survey_id in survey_ids:
                sar.delete_answered_survey(account_id, survey_id)

            sr.delete_source(account_id, source_id)
            t.commit()

    def _submit_test_survey(self, account_id, human_source, month):
        with Transaction() as t:
            sar = SurveyAnswersRepo(t)
            survey_10 = {
                '22': 'Unspecified',
                '108': 'Unspecified',
                '109': 'Unspecified',
                '110': 'Unspecified',
                '111': month,
                '112': 'Unspecified',
                '113': 'Unspecified',
                '115': 'Unspecified',
                '148': 'Unspecified',
                '492': 'Unspecified',
                '493': 'Unspecified',
                '502': 'Unspecified'
            }

            survey_id = sar.submit_answered_survey(account_id,
                                                   human_source,
                                                   'en_US',
                                                   10,
                                                   survey_10)

            t.commit()

            return survey_id

    def test_migrate_responses(self):
        with Transaction() as t:
            with t.cursor() as cur:
                # get source_id associated with survey_id 6d16832b84358c93 as
                # it is randomly generated each install.
                cur.execute("SELECT source_id FROM ag_login_surveys WHERE "
                            "survey_id = '6d16832b84358c93'")
                source_id = cur.fetchone()[0]

        with Transaction() as t:
            str = SurveyTemplateRepo(t)
            # use data from an old template 1 survey and return a subset of it
            # in a generated template 10.

            obs, obs_pc = str.migrate_responses(source_id, 10)
            self.assertDictEqual(obs, self.filled_survey_10a)
            self.assertAlmostEqual(obs_pc, 0.615, 2)

            # use an invalid template id
            with self.assertRaises(ValueError):
                str.migrate_responses('d8592c74-8148-2135-e040-8a80115d6401',
                                      -1)

            # request a test from a valid account, but contributes no prior
            # values to the result.
            obs, obs_pc = str.migrate_responses(source_id, 19)
            self.assertDictEqual(obs, self.filled_survey_19a)
            self.assertAlmostEqual(obs_pc, 0.0, 2)

            # the following statements create a new source and submits a
            # survey. It then changes the value for one of the survey
            # questions, and submits it again. Upon retrieving the template 10
            # for ACCOUNT_ID, 111 (Birth Month) should return 'March' if the
            # surveys were submitted correctly and the latest value is being
            # taken.
            account_id = '607f6723-c704-4b52-bc26-556a9aec85f6'
            human_source = self._create_source(account_id)
            survey_ids = []
            survey_ids.append(
                self._submit_test_survey(account_id, human_source.id,
                                         'February'))
            survey_ids.append(
                self._submit_test_survey(account_id, human_source.id,
                                         'March'))

            result, result_pc = str.migrate_responses(human_source.id, 10)
            self.assertNotEqual(result['111'], 'February')
            self.assertEqual(result['111'], 'March')
            self.assertAlmostEqual(obs_pc, 0.0, 2)

            # clean up. These methods were not put into setUp and tearDown
            # as this is the only test that needs them. Each submit needs its
            # own commit(), this was the way to keep it better managed.
            self._clean_up(account_id, human_source.id, survey_ids)

    def test_migrate_responses_by_barcode(self):
        with Transaction() as t:
            with t.cursor() as cur:
                cur.execute("SELECT ag_login_id, source_id FROM "
                            "ag.ag_login_surveys WHERE survey_id = "
                            "'6d16832b84358c93'")

                # get the account and source id associated w/barcode 000001410
                # and survey 6d16832b84358c93. We'll need them later.
                row = cur.fetchone()
                account_id = row[0]
                source_id = row[1]

            rpo = SurveyTemplateRepo(t)

            # use data from an old template 1 survey and return a subset of it
            # in a generated template 10.
            obs = rpo.migrate_responses_by_barcode('000001410', 10)
            self.assertDictEqual(obs, self.filled_survey_10a)

            # use an invalid template id
            with self.assertRaises(ValueError):
                rpo.migrate_responses('d8592c74-8148-2135-e040-8a80115d6401',
                                      -1)

            # request a test from a valid source, but contributes no prior
            # values to the result.
            obs = rpo.migrate_responses_by_barcode('000001410', 19)
            self.assertDictEqual(obs, self.filled_survey_19a)

            # the following statements create a new source and submits a
            # survey. It then submits a survey to the existing source
            # associated with barcode '000001410'. Neither survey should
            # affect the results for the final query.

            new_source_id = str(uuid.uuid4())

            human_source = self._create_source(account_id,
                                               source_id=new_source_id)
            survey_ids = []
            survey_ids.append(
                self._submit_test_survey(account_id, human_source.id,
                                         'February'))
            survey_ids.append(
                self._submit_test_survey(account_id, source_id,
                                         'March'))

            result = rpo.migrate_responses_by_barcode('000001410', 10)

            self.assertNotEqual(result['111'], 'February')
            self.assertNotEqual(result['111'], 'March')
            self.assertEqual(result['111'], 'June')

            # clean up. These methods were not put into setUp and tearDown
            # as this is the only test that needs them. Each submit needs its
            # own commit(), this was the way to keep it better managed.
            self._clean_up(account_id, human_source.id, survey_ids)

    def test_get_template_ids_from_survey_ids(self):
        with Transaction() as t:
            sar = SurveyTemplateRepo(t)

            # since survey ids aren't always UUIDS of equal length, we'll
            # treat any string input as valid, so long as it's not ''.

            # valid
            obs = sar.get_template_ids_from_survey_ids(['6d16832b84358c93'])
            exp = [('6d16832b84358c93', 1)]
            self.assertEqual(obs, exp)

            # malformed - too short
            obs = sar.get_template_ids_from_survey_ids(['6d18284358c93'])
            exp = []
            self.assertEqual(obs, exp)

            # invalid - id is not in db
            obs = sar.get_template_ids_from_survey_ids(['9326832b84358c93'])
            exp = []
            self.assertEqual(obs, exp)

            # this should just return one tuple.
            obs = sar.get_template_ids_from_survey_ids(['6d16832b84358c93',
                                                        '6d1682845c93'])
            exp = [('6d16832b84358c93', 1)]
            self.assertEqual(obs, exp)

            # this should just return two tuples.
            obs = sar.get_template_ids_from_survey_ids(['6d16832b84358c93',
                                                        '001e19ab6ea2f7de'])

            exp = [('6d16832b84358c93', 1), ('001e19ab6ea2f7de', 1)]
            self.assertEqual(obs, exp)

    filled_surveys = {
        "10": {
            "22": "I am right handed",
            "108": "[\"Free text - 5A.\u00f6h?L~8\u00d3qwqy\u012bG +21\"]",
            "109": "inches",
            "110": "United States",
            "111": "February",
            "112": "1945",
            "113": "[\"Free text - S#G\u00e4e\u00c9n0x='\u00e8u)`\u00dfJ\u00dfM=\"]",   # noqa
            "115": "[\"Free text - bC\u00c4\u012bx*N*0\u00d3Ha7\r*/b3\u010dD\"]",   # noqa
            "148": "Unspecified",
            "492": "Unspecified",
            "493": "Unspecified",
            "502": "Unspecified",
            "81": "Diagnosed by a medical professional (doctor, physician assistant)",  # noqa
            "122": "[\"Free text - \u010d/ueIW|mFZK^g6+\u00fc\u00e1|i3\"]",
            "55": "No",
            "63": "Never",
            "10": "Yes",
            "119": "[\"Free text - Dt\u00e3\u012b>\"3`\u00d6\u00f6)\u00e3\u00d6YQL&+\u00df_\"]",    # noqa
            # noqa
            "12": "Yes",
            "31": "Daily",
            "23": "Graduate or Professional degree",
            "107": "Female",
            "118": "[\"Free text - U\u00e47\u00c9.\u00faH v.kSmP#j, '\u00fc\"]",    # noqa
            "120": "[\"Free text - $>K\u00e8yT*@\u00d8=Bf.P\u00bfl*v%\u00fa\"]",    # noqa
            "98": "[\"Free text - !\u0161z:s\u00d8*,+e`.\u00c4R>*Kd'z\"]",
            "114": "pounds",
            "13": "Bottled",
            "101": "[\"Free text -  TQ$>\u00e5_-:F+!j=\u00bf~\u00f8#=)\"]",
            "117": "[\"Free text - m%a)F--~-1\u00d8\u00e7$l*Q~K\u00e3P\"]",
            "103": "[\"Free text - ;LD?;;\u00c45AT\u0161,f \"UO7u\u00d3\"]",
            "97": "I do not have this condition",
            "52": "Yes",
            "105": "[\"Free text - @jtQ\r_*ih>l\u0161\u00e8k\u00c4\u00d6L<(\u00e1\"]",  # noqa
            "88": "Diagnosed by a medical professional (doctor, physician assistant)",  # noqa
            "116": "[\"Free text - G't\tUkV\u00f3.$lig50A\u00dfFFr\"]",
            "41": "No",
            "14": "Caucasian"
        },
        "11": {
            "15": ("I have lived in my current state of residence for more "
                   "than a year."),
            # noqa
            "17": "One",
            "18": "No",
            "19": "Unspecified",
            "20": "No",
            "21": "Yes",
            "149": "Unspecified",
            "150": "Unspecified",
            "313": "Unspecified",
            "316": "Unspecified",
            "319": "Unspecified",
            "326": "Unspecified",
            "501": "Unspecified",
            "503": "Unspecified",
            "508": "Unspecified",
            "509": "Unspecified",
            "510": "Unspecified"
        },
        "12": {
            "16": ("I have not been outside of my country of residence in the"
                   " past year."),
            "24": "Rarely (a few times/month)",
            "25": "Indoors",
            "26": "No",
            "27": "Never",
            "28": "Never",
            "29": "Never",
            "32": "Rarely (a few times/month)",
            "33": "Never",
            "34": "I use deodorant",
            "35": "8 or more hours",
            "36": "No",
            "163": "Unspecified",
            "328": [
                "Unspecified"
            ],
            "331": [
                "Unspecified"
            ],
            "332": [
                "Unspecified"
            ],
            "333": "Unspecified",
            "334": "Unspecified",
            "344": "Unspecified",
            "345": "Unspecified",
            "346": "Unspecified",
            "347": "Unspecified",
            "348": "Unspecified",
            "349": "Unspecified",
            "350": "Unspecified",
            "354": "Unspecified",
            "494": [
                "Unspecified"
            ],
            "495": "Unspecified"
        },
        "13": {
            "37": "Two",
            "38": "Unspecified",
            "78": "I do not have this condition",
            "79": "I do not have this condition",
            "83": "I do not have this condition",
            "95": "I do not have this condition",
            "360": "Unspecified",
            "362": "Unspecified",
            "363": "Unspecified",
            "364": "Unspecified",
            "365": "Unspecified"
        },
        "14": {
            "39": "I have not taken antibiotics in the past year.",
            "40": "6 months",
            "42": "No",
            "43": "Remained stable",
            "44": "Yes",
            "45": "No",
            "46": "Not sure",
            "47": "No",
            "48": "No",
            "49": "No",
            "50": "No",
            "51": "Primarily infant formula",
            "99": "[\"Free text - \\\u00e7y\u00ed\u00fc \"b$Ug~z@W\u00bfvDB=\"]",   # noqa
            "124": "[\"Free text - n\u00bf\u00c54\u00df\u00e9\u00f6lM,;Bo\u00f8\u00d3P\u00c9D\u00d3/\"]",   # noqa
            "126": "[\"Free text - m\u00bf\t\u012b\u00f3\u0161Drj\u00e1/F$j*I'%h\u00e9\"]",   # noqa
            "156": "Unspecified",
            "370": "Unspecified",
            "374": "Unspecified",
            "375": "Unspecified",
            "387": "Unspecified",
            "497": "Unspecified",
            "500": "Unspecified"
        },
        "15": {
            "60": "I do not have this condition",
            "77": "I do not have this condition",
            "80": "I do not have this condition",
            "82": "I do not have this condition",
            "84": "I do not have this condition",
            "85": "I do not have this condition",
            "86": "I do not have this condition",
            "87": "I do not have this condition",
            "89": "I do not have this condition",
            "90": "I do not have this condition",
            "92": "I do not have this condition",
            "93": ("Diagnosed by a medical professional (doctor, physician "
                   "assistant)"),
            "94": "I do not have this condition",
            "96": "I do not have this condition",
            "106": "[\"Free text - &ePd\u00e1\u00f6P\u00d8NJ#E$Q\"\\y'/h\"]",
            "407": "Unspecified",
            "408": "Unspecified",
            "409": [
                "Unspecified"
            ],
            "410": [
                "Unspecified"
            ],
            "413": "Unspecified",
            "499": "Unspecified",
            "504": "Unspecified",
            "505": "Unspecified",
            "506": "Unspecified",
            "507": "Unspecified"
        },
        "16": {
            "7": "No",
            "8": "I do not eat gluten because it makes me feel bad",
            "9": [
                "Other"
            ],
            "53": "Yes",
            "54": [
                "Sun",
                "Pet dander",
                "Drug (e.g. Penicillin)"
            ],
            "415": "Unspecified"
        },
        "17": {
            "1": "Omnivore",
            "2": "No",
            "3": "Daily",
            "4": "Daily",
            "5": "Daily",
            "6": "Yes",
            "11": "Yes",
            "104": "[\"Free text - H\u00f6~\u00c9\u00e5(r\u00ed@:P;uw<\u00df\u00d3W*\u00fa\"]", # noqa
            # noqa
            "162": [
                "Unspecified"
            ],
            "423": "Unspecified",
            "424": "Unspecified",
            "425": "Unspecified",
            "426": "Unspecified",
            "427": "Unspecified",
            "428": "Unspecified",
            "433": [
                "Unspecified"
            ],
            "434": "Unspecified",
            "498": "Unspecified"
        },
        "18": {
            "56": "Occasionally (1-2 times/week)",
            "57": "Regularly (3-5 times/week)",
            "58": "Never",
            "59": "Occasionally (1-2 times/week)",
            "61": "Regularly (3-5 times/week)",
            "62": "Occasionally (1-2 times/week)",
            "64": "Rarely (less than once/week)",
            "65": "Regularly (3-5 times/week)",
            "66": "Rarely (less than once/week)",
            "67": "Rarely (less than once/week)",
            "68": "Never",
            "69": "Occasionally (1-2 times/week)",
            "70": "Rarely (less than once/week)",
            "71": "Occasionally (1-2 times/week)",
            "72": "Rarely (less than once/week)",
            "73": "Occasionally (1-2 times/week)",
            "74": "Occasionally (1-2 times/week)",
            "75": "Never",
            "76": "Daily",
            "91": "Rarely (less than once/week)",
            "146": "Unspecified",
            "157": "Unspecified",
            "165": "Unspecified",
            "166": "Unspecified",
            "167": [
                "Unspecified"
            ],
            "169": [
                "Unspecified"
            ],
            "171": [
                "Unspecified"
            ],
            "236": "Unspecified",
            "237": "Unspecified",
            "239": "Unspecified",
            "240": "Unspecified",
            "241": "Unspecified",
            "242": "Unspecified",
            "243": "Unspecified",
            "244": "Unspecified",
            "443": "Unspecified",
            "462": "Unspecified",
            "463": "Unspecified",
            "464": [
                "Unspecified"
            ],
            "465": "Unspecified",
            "466": [
                "Unspecified"
            ],
            "474": "Unspecified",
            "475": "Unspecified",
            "476": "Unspecified",
            "477": "Unspecified",
            "478": "Unspecified"
        }
    }

    empty_survey_1 = {
        '1': 'Unspecified',
        '2': 'Unspecified',
        '3': 'Unspecified',
        '4': 'Unspecified',
        '5': 'Unspecified',
        '6': 'Unspecified',
        '7': 'Unspecified',
        '8': 'Unspecified',
        '9': [
            'Unspecified'
        ],
        '11': 'Unspecified',
        '15': 'Unspecified',
        '16': 'Unspecified',
        '17': 'Unspecified',
        '18': 'Unspecified',
        '19': 'Unspecified',
        '20': 'Unspecified',
        '21': 'Unspecified',
        '22': 'Unspecified',
        '24': 'Unspecified',
        '25': 'Unspecified',
        '26': 'Unspecified',
        '27': 'Unspecified',
        '28': 'Unspecified',
        '29': 'Unspecified',
        '32': 'Unspecified',
        '33': 'Unspecified',
        '34': 'Unspecified',
        '35': 'Unspecified',
        '36': 'Unspecified',
        '37': 'Unspecified',
        '38': 'Unspecified',
        '39': 'Unspecified',
        '40': 'Unspecified',
        '42': 'Unspecified',
        '43': 'Unspecified',
        '44': 'Unspecified',
        '45': 'Unspecified',
        '46': 'Unspecified',
        '47': 'Unspecified',
        '48': 'Unspecified',
        '49': 'Unspecified',
        '50': 'Unspecified',
        '51': 'Unspecified',
        '53': 'Unspecified',
        '54': [
            'Unspecified'
        ],
        '56': 'Unspecified',
        '57': 'Unspecified',
        '58': 'Unspecified',
        '59': 'Unspecified',
        '60': 'Unspecified',
        '61': 'Unspecified',
        '62': 'Unspecified',
        '64': 'Unspecified',
        '65': 'Unspecified',
        '66': 'Unspecified',
        '67': 'Unspecified',
        '68': 'Unspecified',
        '69': 'Unspecified',
        '70': 'Unspecified',
        '71': 'Unspecified',
        '72': 'Unspecified',
        '73': 'Unspecified',
        '74': 'Unspecified',
        '75': 'Unspecified',
        '76': 'Unspecified',
        '77': 'Unspecified',
        '78': 'Unspecified',
        '79': 'Unspecified',
        '80': 'Unspecified',
        '82': 'Unspecified',
        '83': 'Unspecified',
        '84': 'Unspecified',
        '85': 'Unspecified',
        '86': 'Unspecified',
        '87': 'Unspecified',
        '89': 'Unspecified',
        '90': 'Unspecified',
        '91': 'Unspecified',
        '92': 'Unspecified',
        '93': 'Unspecified',
        '94': 'Unspecified',
        '95': 'Unspecified',
        '96': 'Unspecified',
        '99': 'Unspecified',
        '104': 'Unspecified',
        '106': 'Unspecified',
        '108': 'Unspecified',
        '109': 'Unspecified',
        '110': 'Unspecified',
        '111': 'Unspecified',
        '112': 'Unspecified',
        '113': 'Unspecified',
        '115': 'Unspecified',
        '116': 'Unspecified',
        '124': 'Unspecified',
        '126': 'Unspecified',
        '146': 'Unspecified',
        '148': 'Unspecified',
        '149': 'Unspecified',
        '150': 'Unspecified',
        '156': 'Unspecified',
        '157': 'Unspecified',
        '162': [
            'Unspecified'
        ],
        '163': 'Unspecified',
        '236': 'Unspecified',
        '237': 'Unspecified'
    }

    empty_survey_10 = {
        '22': 'Unspecified',
        '108': 'Unspecified',
        '109': 'Unspecified',
        '110': 'Unspecified',
        '111': 'Unspecified',
        '112': 'Unspecified',
        '113': 'Unspecified',
        '115': 'Unspecified',
        '116': 'Unspecified',
        '148': 'Unspecified',
        '492': 'Unspecified',
        '493': 'Unspecified',
        '502': 'Unspecified'
    }

    filled_survey_10a = {'22': 'I am right handed',
                         '108': '["Free text - í.,ú!N):TfüQWä$ãZ-SQ"]',
                         '109': 'centimeters',
                         '110': 'United States',
                         '111': 'June',
                         '112': 'Unspecified',
                         '113': '["Free text - -,mV7Ä\t9xäMf\\è\n!¿x_ã"]',
                         '115': '["Free text - Js*äbéøx\'ó,çné\nSEQ8\t"]',
                         '116': '["Free text - Å|ī8W=A4K\rØø\t_Af3ÓÓ."]',
                         '148': 'Unspecified',
                         '492': 'Unspecified',
                         '493': 'Unspecified',
                         '502': 'Unspecified'}

    filled_survey_19a = {
        "485": "Unspecified",
        "486": "Unspecified",
        "487": "Unspecified",
        "488": "Unspecified",
        "489": "Unspecified",
        "490": "Unspecified"
    }


SURVEY_ANSWERS = {
    # Birth Month
    "111": "February",
    # Current ZIP code
    "115": "a free text field"
}
