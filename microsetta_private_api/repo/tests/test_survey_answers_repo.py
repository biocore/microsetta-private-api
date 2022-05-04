import unittest
import datetime
from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo

from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.model.source import Source, HumanInfo


SURVEY_ID = 'abcdef01-aaaa-bbbb-cccc-dddddddddddd'
ACCOUNT_ID = '607f6723-c704-4b52-bc26-556a9aec85f6'
HUMAN_SOURCE = Source('ffffffff-ffff-ffff-aaaa-aaaaaaaaaaaa',
                      ACCOUNT_ID,
                      Source.SOURCE_TYPE_HUMAN,
                      'test person',
                      HumanInfo('foo@bar.com', False,
                                None, None, None,
                                datetime.datetime.now(),
                                None, None, '18-plus'))

SURVEY_ANSWERS = {
    "3": "Never",  # non-free text
    "116": "a free text field",
}


class SurveyAnswersTests(unittest.TestCase):
    def setUp(self):
        with Transaction() as t:
            sr = SourceRepo(t)
            sar = SurveyAnswersRepo(t)

            sr.create_source(HUMAN_SOURCE)
            sar.submit_answered_survey(ACCOUNT_ID, HUMAN_SOURCE.id,
                                       'en_US', 1, SURVEY_ANSWERS,
                                       SURVEY_ID)
            t.commit()

    def tearDown(self):
        with Transaction() as t:
            sr = SourceRepo(t)
            sar = SurveyAnswersRepo(t)
            sar.delete_answered_survey(ACCOUNT_ID, SURVEY_ID)

            sr.delete_source(HUMAN_SOURCE.account_id,
                             HUMAN_SOURCE.id)
            t.commit()

    def test_scrub_bad_survey_id(self):
        with Transaction() as t:
            sar = SurveyAnswersRepo(t)

            with self.assertRaises(RepoException):
                sar.scrub(HUMAN_SOURCE.account_id, HUMAN_SOURCE.id,
                          HUMAN_SOURCE.id)

    def test_scrub_bad_source(self):
        with Transaction() as t:
            sar = SurveyAnswersRepo(t)

            with self.assertRaises(RepoException):
                sar.scrub(HUMAN_SOURCE.account_id, HUMAN_SOURCE.account_id,
                          SURVEY_ID)

    def test_scrub(self):
        with Transaction() as t:
            sar = SurveyAnswersRepo(t)
            sar.scrub(HUMAN_SOURCE.account_id, HUMAN_SOURCE.id,
                      SURVEY_ID)
            obs = sar.get_answered_survey(HUMAN_SOURCE.account_id,
                                          HUMAN_SOURCE.id,
                                          SURVEY_ID,
                                          'en_US')
            self.assertEqual(obs['3'], SURVEY_ANSWERS['3'])
            self.assertNotEqual(obs['116'], SURVEY_ANSWERS['116'])

    def test_unlocalize_bug(self):
        with Transaction() as t:
            tr = SurveyAnswersRepo(t)
            exp = 'Fair'
            obs = tr._unlocalize('Bajo', 210, 'es_MX')
            self.assertEqual(obs, exp)

            exp = 'Low'
            obs = tr._unlocalize('Bajo', 141, 'es_MX')
            self.assertEqual(obs, exp)


if __name__ == '__main__':
    unittest.main()
