import unittest
import uuid
from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo
from microsetta_private_api.repo.transaction import Transaction
from psycopg2.errors import ForeignKeyViolation


# test identifiers with a vio ID
TEST1_ACCOUNT_ID = "80c327ca-a5c7-4c7f-b64b-b219d9ff0b47"
TEST1_SOURCE_ID = None
TEST1_SAMPLE_ID = "125a7cc5-41ae-44ef-983c-6f1a5213f668"
TEST1_SURVEY_ID = None
TEST1_VIO_ID = "1c689634cea0d11b"


# not in registry
TEST2_ACCOUNT_ID = "735e1689-6976-4d96-9a33-7a19f06602bf"
TEST2_SOURCE_ID = None
TEST2_SAMPLE_ID = "7380bb81-7401-45bd-85a0-51001f5f5cf1"


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

    def test_create_vioscreen_id_valid(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs = template_repo.create_vioscreen_id(TEST2_ACCOUNT_ID,
                                                    TEST2_SOURCE_ID,
                                                    TEST2_SAMPLE_ID)
            self.assertTrue(obs is not None)
            t.rollback()

    def test_create_vioscreen_id_idempotent(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs1 = template_repo.create_vioscreen_id(TEST2_ACCOUNT_ID,
                                                     TEST2_SOURCE_ID,
                                                     TEST2_SAMPLE_ID)
            obs2 = template_repo.create_vioscreen_id(TEST2_ACCOUNT_ID,
                                                     TEST2_SOURCE_ID,
                                                     TEST2_SAMPLE_ID)
            self.assertEqual(obs1, obs2)

            obs = template_repo.create_vioscreen_id(TEST1_ACCOUNT_ID,
                                                    TEST1_SOURCE_ID,
                                                    TEST1_SAMPLE_ID)
            self.assertEqual(obs, TEST1_VIO_ID)
            t.rollback()

    def test_create_vioscreen_id_bad_source_or_account(self):
        # transaction needs to be created each time as the FK violation
        # disrupts the active transaction
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            with self.assertRaises(ForeignKeyViolation):
                template_repo.create_vioscreen_id(str(uuid.uuid4()),
                                                  TEST2_SOURCE_ID,
                                                  TEST2_SAMPLE_ID)

        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            with self.assertRaises(ForeignKeyViolation):
                template_repo.create_vioscreen_id(TEST2_ACCOUNT_ID,
                                                  str(uuid.uuid4()),
                                                  TEST2_SAMPLE_ID)

        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            with self.assertRaises(KeyError):
                template_repo.create_vioscreen_id(TEST2_ACCOUNT_ID,
                                                  TEST2_SOURCE_ID,
                                                  str(uuid.uuid4()))

    def test_get_vioscreen_id_if_exists_valid(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs = template_repo.get_vioscreen_id_if_exists(TEST1_ACCOUNT_ID,
                                                           TEST1_SOURCE_ID,
                                                           TEST1_SAMPLE_ID)
            self.assertEqual(obs, TEST1_VIO_ID)

    def test_get_vioscreen_id_if_exists_invalid(self):
        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            obs = template_repo.get_vioscreen_id_if_exists(TEST2_ACCOUNT_ID,
                                                           TEST2_SOURCE_ID,
                                                           TEST2_SAMPLE_ID)
            self.assertEqual(obs, None)
