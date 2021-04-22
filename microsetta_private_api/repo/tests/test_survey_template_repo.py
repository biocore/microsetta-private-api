import unittest
import uuid
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo
from microsetta_private_api.repo.transaction import Transaction
from psycopg2.errors import ForeignKeyViolation


# test identifiers with a vio ID
TEST1_ACCOUNT_ID = "80c327ca-a5c7-4c7f-b64b-b219d9ff0b47"
TEST1_SAMPLE_ID = "125a7cc5-41ae-44ef-983c-6f1a5213f668"
TEST1_VIO_ID = "1c689634cea0d11b"


# not in registry
TEST2_ACCOUNT_ID = "735e1689-6976-4d96-9a33-7a19f06602bf"
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


class SurveyTemplateTests(unittest.TestCase):
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