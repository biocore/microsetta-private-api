import unittest
from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo
from microsetta_private_api.repo.transaction import Transaction


class SurveyAnswersTests(unittest.TestCase):
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
