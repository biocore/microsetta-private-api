import unittest
from unittest import skipIf
from dateutil import parser
import pytz
import datetime

from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.util.myfoodrepo import create_subj
from microsetta_private_api.client.myfoodrepo import MFRClient


class MyFoodRepoTests(unittest.TestCase):
    @skipIf(SERVER_CONFIG['myfoodrepo_url'] in ('', 'mfr_url_placeholder'),
            "MFR secrets not provided")
    def test_create_subj(self):
        client = MFRClient(SERVER_CONFIG["myfoodrepo_study"])
        exp_delta = SERVER_CONFIG["myfoodrepo_participation_days"]

        subj_id = create_subj()

        cohort = SERVER_CONFIG['myfoodrepo_cohort']
        obs = client.read_subj(cohort, subj_id)

        obs_date = obs.data.subject.expired_at
        obs_date = parser.parse(obs_date)

        now = datetime.datetime.now(pytz.utc)

        # allow for a 1 minute time between when we set expiration and our test
        self.assertEqual((obs_date - now).days, exp_delta - 1)
        self.assertGreater((obs_date - now).seconds, 24 * 59 * 60)


if __name__ == '__main__':
    unittest.main()
