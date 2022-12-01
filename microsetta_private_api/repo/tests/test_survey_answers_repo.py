import unittest
import datetime
from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo

from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.model.source import Source, HumanInfo
from json import dumps, loads


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
    # Birth Month
    "111": "February",
    # Current ZIP code
    "115": "a free text field"
}


class SurveyAnswersTests(unittest.TestCase):
    def setUp(self):
        with Transaction() as t:
            sr = SourceRepo(t)
            sar = SurveyAnswersRepo(t)

            sr.create_source(HUMAN_SOURCE)
            sar.submit_answered_survey(ACCOUNT_ID, HUMAN_SOURCE.id,
                                       'en_US', 10, SURVEY_ANSWERS,
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
            self.assertEqual(obs['111'], SURVEY_ANSWERS['111'])
            self.assertNotEqual(obs['115'], SURVEY_ANSWERS['115'])

    def test_unlocalize_bug(self):
        with Transaction() as t:
            tr = SurveyAnswersRepo(t)
            exp = 'Fair'
            obs = tr._unlocalize('Bajo', 210, 'es_MX')
            self.assertEqual(obs, exp)

            exp = 'Low'
            obs = tr._unlocalize('Bajo', 141, 'es_MX')
            self.assertEqual(obs, exp)

    def test_generate_empty_surveys(self):
        with Transaction() as t:
            sar = SurveyAnswersRepo(t)

            obs = sar._generate_empty_surveys()

            exp = loads(empty_surveys)

            self.assertDictEqual(obs, exp)

    def test_migrate_responses(self):
        with Transaction() as t:
            sar = SurveyAnswersRepo(t)

            # _migrate_responses() is a method used by migrate_responses()
            # to construct a set of filled survey_templates. It also returns
            # a dict of metadata associated w/each template like account_id,
            # survey creation_time, etc.
            obs, obs_meta = sar._migrate_responses('000001040')

            exp = loads(filled_surveys)

            self.assertDictEqual(obs, exp)

            # unfortunately, obs_meta only contains creation_time, source_id,
            # and account_id - three values that are generated dynamically.
            # test that the template_ids returned is as expected only.
            obs = set(obs_meta.keys())
            exp = {"10", "11", "12", "13", "14", "15", "16", "17", "18"}
            self.assertEqual(obs, exp)

            # construct the set of filled survey_templates (again) and submit
            # them to the system. What's returned is a list of (account_id,
            # survey_id) tuples that can be used to delete the surveys after.
            new_survey_ids = sar.migrate_responses('000001040')

            # delete the surveys now that they've been created successfully
            for account_id, survey_id in new_survey_ids:
                status = sar.delete_answered_survey(account_id, survey_id)
                self.assertTrue(status, msg=f"survey {survey_id} failed to delete")

            t.commit()

    def test_get_template_ids_from_survey_ids(self):
        with Transaction() as t:
            sar = SurveyAnswersRepo(t)

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
            obs = sar.get_template_ids_from_survey_ids(['6d16832b84358c93', '6d1682845c93'])
            exp = [('6d16832b84358c93', 1)]
            self.assertEqual(obs, exp)

            # this should just return two tuples.
            obs = sar.get_template_ids_from_survey_ids(['6d16832b84358c93', '001e19ab6ea2f7de'])
            print(obs)
            exp = [('6d16832b84358c93', 1), ('001e19ab6ea2f7de', 1)]
            self.assertEqual(obs, exp)

            with self.assertRaises(ValueError):
                # lone parameter is not a list
                sar.get_template_ids_from_survey_ids('6d16832b84358c93')

            with self.assertRaises(ValueError):
                # parameter is a list with just an empty string
                sar.get_template_ids_from_survey_ids([''])

            with self.assertRaises(ValueError):
                # parameter is an empty list
                sar.get_template_ids_from_survey_ids([])

            with self.assertRaises(ValueError):
                # parameter is None
                sar.get_template_ids_from_survey_ids(None)

            with self.assertRaises(ValueError):
                # parameter contains one valid and one invalid value
                sar.get_template_ids_from_survey_ids(['6d16832b84358c93', ''])

            with self.assertRaises(ValueError):
                # parameter contains one valid and one invalid value
                sar.get_template_ids_from_survey_ids(['6d16832b84358c93', None])

            #self.assertTrue(False)

empty_surveys = """
{
  "10": {
    "22": "Unspecified",
    "108": "Unspecified",
    "109": "Unspecified",
    "110": "Unspecified",
    "111": "Unspecified",
    "112": "Unspecified",
    "113": "Unspecified",
    "115": "Unspecified",
    "148": "Unspecified",
    "492": "Unspecified",
    "493": "Unspecified",
    "502": "Unspecified"
  },
  "11": {
    "15": "Unspecified",
    "17": "Unspecified",
    "18": "Unspecified",
    "19": "Unspecified",
    "20": "Unspecified",
    "21": "Unspecified",
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
    "16": "Unspecified",
    "24": "Unspecified",
    "25": "Unspecified",
    "26": "Unspecified",
    "27": "Unspecified",
    "28": "Unspecified",
    "29": "Unspecified",
    "32": "Unspecified",
    "33": "Unspecified",
    "34": "Unspecified",
    "35": "Unspecified",
    "36": "Unspecified",
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
    "37": "Unspecified",
    "38": "Unspecified",
    "78": "Unspecified",
    "79": "Unspecified",
    "83": "Unspecified",
    "95": "Unspecified",
    "360": "Unspecified",
    "362": "Unspecified",
    "363": "Unspecified",
    "364": "Unspecified",
    "365": "Unspecified"
  },
  "14": {
    "39": "Unspecified",
    "40": "Unspecified",
    "42": "Unspecified",
    "43": "Unspecified",
    "44": "Unspecified",
    "45": "Unspecified",
    "46": "Unspecified",
    "47": "Unspecified",
    "48": "Unspecified",
    "49": "Unspecified",
    "50": "Unspecified",
    "51": "Unspecified",
    "99": "Unspecified",
    "124": "Unspecified",
    "126": "Unspecified",
    "156": "Unspecified",
    "370": "Unspecified",
    "374": "Unspecified",
    "375": "Unspecified",
    "387": "Unspecified",
    "497": "Unspecified",
    "500": "Unspecified"
  },
  "15": {
    "60": "Unspecified",
    "77": "Unspecified",
    "80": "Unspecified",
    "82": "Unspecified",
    "84": "Unspecified",
    "85": "Unspecified",
    "86": "Unspecified",
    "87": "Unspecified",
    "89": "Unspecified",
    "90": "Unspecified",
    "92": "Unspecified",
    "93": "Unspecified",
    "94": "Unspecified",
    "96": "Unspecified",
    "106": "Unspecified",
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
    "7": "Unspecified",
    "8": "Unspecified",
    "9": [
      "Unspecified"
    ],
    "53": "Unspecified",
    "54": [
      "Unspecified"
    ],
    "415": "Unspecified"
  },
  "17": {
    "1": "Unspecified",
    "2": "Unspecified",
    "3": "Unspecified",
    "4": "Unspecified",
    "5": "Unspecified",
    "6": "Unspecified",
    "11": "Unspecified",
    "104": "Unspecified",
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
    "56": "Unspecified",
    "57": "Unspecified",
    "58": "Unspecified",
    "59": "Unspecified",
    "61": "Unspecified",
    "62": "Unspecified",
    "64": "Unspecified",
    "65": "Unspecified",
    "66": "Unspecified",
    "67": "Unspecified",
    "68": "Unspecified",
    "69": "Unspecified",
    "70": "Unspecified",
    "71": "Unspecified",
    "72": "Unspecified",
    "73": "Unspecified",
    "74": "Unspecified",
    "75": "Unspecified",
    "76": "Unspecified",
    "91": "Unspecified",
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
  },
  "19": {
    "485": "Unspecified",
    "486": "Unspecified",
    "487": "Unspecified",
    "488": "Unspecified",
    "489": "Unspecified",
    "490": "Unspecified"
  },
  "20": {
    "174": "Unspecified",
    "175": "Unspecified",
    "176": "Unspecified",
    "177": "Unspecified",
    "178": "Unspecified",
    "179": "Unspecified",
    "180": "Unspecified",
    "181": "Unspecified",
    "182": "Unspecified",
    "183": "Unspecified",
    "184": "Unspecified",
    "185": "Unspecified"
  },
  "21": {
    "209": "Unspecified",
    "210": "Unspecified",
    "211": [
      "Unspecified"
    ],
    "212": "Unspecified",
    "213": "Unspecified",
    "214": [
      "Unspecified"
    ],
    "215": "Unspecified",
    "216": "Unspecified",
    "217": [
      "Unspecified"
    ],
    "218": "Unspecified",
    "219": "Unspecified",
    "220": [
      "Unspecified"
    ],
    "221": "Unspecified",
    "222": "Unspecified",
    "223": "Unspecified",
    "224": "Unspecified",
    "225": "Unspecified",
    "226": "Unspecified",
    "227": "Unspecified",
    "228": "Unspecified",
    "229": "Unspecified",
    "230": "Unspecified",
    "231": "Unspecified",
    "232": "Unspecified",
    "233": "Unspecified",
    "234": "Unspecified",
    "235": "Unspecified",
    "238": [
      "Unspecified"
    ]
  }
}"""

filled_surveys = """
{
  "10": {
    "22": "I am right handed",
    "108": "Unspecified",
    "109": "inches",
    "110": "United States",
    "111": "February",
    "112": "1945",
    "113": "Unspecified",
    "115": "Unspecified",
    "148": "Unspecified",
    "492": "Unspecified",
    "493": "Unspecified",
    "502": "Unspecified",
    "41": "No",
    "52": "Yes",
    "114": "pounds",
    "107": "Female",
    "97": "I do not have this condition",
    "88": "Diagnosed by a medical professional (doctor, physician assistant)",
    "10": "Yes",
    "81": "Diagnosed by a medical professional (doctor, physician assistant)",
    "12": "Yes",
    "13": "Bottled",
    "14": "Caucasian",
    "23": "Graduate or Professional degree",
    "31": "Daily",
    "63": "Never",
    "55": "No"
  },
  "11": {
    "15": "I have lived in my current state of residence for more than a year.",
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
    "16": "I have not been outside of my country of residence in the past year.",
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
    "99": "Unspecified",
    "124": "Unspecified",
    "126": "Unspecified",
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
    "93": "Diagnosed by a medical professional (doctor, physician assistant)",
    "94": "I do not have this condition",
    "96": "I do not have this condition",
    "106": "Unspecified",
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
      "Drug (e.g. Penicillin)",
      "Pet dander",
      "Sun"
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
    "104": "Unspecified",
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
}"""


if __name__ == '__main__':
    unittest.main()
