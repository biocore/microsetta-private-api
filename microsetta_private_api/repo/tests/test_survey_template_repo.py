import unittest
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo
from microsetta_private_api.repo.transaction import Transaction
from psycopg2.errors import ForeignKeyViolation


# test identifiers with a vio ID
TEST1_ACCOUNT_ID = "80c327ca-a5c7-4c7f-b64b-b219d9ff0b47"
TEST1_SOURCE_ID = "19f1550d-893f-48a1-81eb-3ecc70c8d86a"
TEST1_SAMPLE_ID = "125a7cc5-41ae-44ef-983c-6f1a5213f668"
TEST1_VIO_ID = "1c689634cea0d11b"

# not in registry
TEST2_ACCOUNT_ID = "5d120344-70e0-46a6-a98b-827a06c1a895"
TEST2_SOURCE_ID = "cdb4255e-6e90-4c5b-9b80-ef750b61a318"
TEST2_SAMPLE_ID = "dd633659-2924-4ee6-8771-3a156c7a74a5"


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
                template_repo.create_vioscreen_id(TEST2_ACCOUNT_ID[::-1],
                                                  TEST2_SOURCE_ID,
                                                  TEST2_SAMPLE_ID)

        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            with self.assertRaises(ForeignKeyViolation):
                template_repo.create_vioscreen_id(TEST2_ACCOUNT_ID,
                                                  TEST2_SOURCE_ID[::-1],
                                                  TEST2_SAMPLE_ID)

        with Transaction() as t:
            template_repo = SurveyTemplateRepo(t)
            with self.assertRaises(KeyError):
                template_repo.create_vioscreen_id(TEST2_ACCOUNT_ID,
                                                  TEST2_SOURCE_ID,
                                                  TEST2_SAMPLE_ID[::-1])

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