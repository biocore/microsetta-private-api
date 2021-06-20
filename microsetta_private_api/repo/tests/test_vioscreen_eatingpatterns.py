import unittest
from microsetta_private_api.model.vioscreen import (
    VioscreenSession, VioscreenEatingPatterns,
    VioscreenEatingPatternsComponent)
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import (
    VioscreenSessionRepo, VioscreenEatingPatternsRepo)
from datetime import datetime
import json


def _to_dt(mon, day, year):
    return datetime(month=mon, day=day, year=year)


VIOSCREEN_SESSION = VioscreenSession(sessionId='0087da64cdcb41ad800c23531d1198f2',  # noqa
                                     username='a user',
                                     protocolId=1234,
                                     status='something',
                                     startDate=_to_dt(1, 1, 1970),
                                     endDate=None,
                                     cultureCode='foo',
                                     created=_to_dt(1, 1, 1970),
                                     modified=_to_dt(1, 1, 1970))

package = 'microsetta_private_api/model/tests'
# package where data is stored

def get_data_path(filename):
    return package + '/data/%s' % filename


class TestEatingPatternsRepo(unittest.TestCase):

    def test_insert_eating_patterns_does_not_exist(self):
        with Transaction() as t:
            with open(get_data_path("eatingpatterns.data")) as data:
                EP_DATA = json.load(data)
            VIOSCREEN_EATING_PATTERNS = VioscreenEatingPatterns.from_vioscreen(EP_DATA[0])
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenEatingPatternsRepo(t)
            obs = r.insert_eating_patterns(VIOSCREEN_EATING_PATTERNS)
            self.assertEqual(obs, 17)

    def test_get_eating_patterns_exists(self):
        with Transaction() as t:
            with open(get_data_path("eatingpatterns.data")) as data:
                EP_DATA = json.load(data)
            VIOSCREEN_EATING_PATTERNS = VioscreenEatingPatterns.from_vioscreen(EP_DATA[0])
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenEatingPatternsRepo(t)
            r.insert_eating_patterns(VIOSCREEN_EATING_PATTERNS)
            obs = r.get_eating_patterns(VIOSCREEN_EATING_PATTERNS.sessionId)
            self.assertEqual(obs, VIOSCREEN_EATING_PATTERNS)

    def test_get_eating_patterns_does_not_exist(self):
        with Transaction() as t:
            with open(get_data_path("eatingpatterns.data")) as data:
                EP_DATA = json.load(data)
            VIOSCREEN_EATING_PATTERNS = VioscreenEatingPatterns.from_vioscreen(EP_DATA[0])
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenEatingPatternsRepo(t)
            obs = r.get_eating_patterns('does not exist')
            self.assertEqual(obs, None)


if __name__ == '__main__':
    unittest.main()
