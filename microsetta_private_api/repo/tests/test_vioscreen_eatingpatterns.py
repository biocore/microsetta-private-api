import unittest
from microsetta_private_api.model.vioscreen import (
    VioscreenSession, VioscreenEatingPatterns,
    VioscreenEatingPatternsComponent)
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import (
    VioscreenSessionRepo, VioscreenEatingPatternsRepo)
from datetime import datetime


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

EP_DATA = {"sessionId": "0087da64cdcb41ad800c23531d1198f2",
            "data": [
                {"code": "ADDEDFATS", "description": "Eating Pattern", "units": "PerDay", "amount": 8.07030444201639, "valueType": "Amount"},
                {"code": "ALCOHOLSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 1.30647563412786, "valueType": "Amount"},
                {"code": "ANIMALPROTEIN", "description": "Eating Pattern", "units": "PerDay", "amount": 1.96556496716603, "valueType": "Amount"},
                {"code": "CALCDAIRYSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 0.364432970091999, "valueType": "Amount"},
                {"code": "CALCSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 2.62447202541388, "valueType": "Amount"},
                {"code": "FISHSERV", "description": "Eating Pattern", "units": "PerWeek", "amount": 0.392841568548386, "valueType": "Amount"},
                {"code": "FRIEDFISH", "description": "Eating Pattern", "units": "PerWeek", "amount": 0.0, "valueType": "Amount"},
                {"code": "FRTSUMM", "description": "Eating Pattern", "units": "PerDay", "amount": 4.47806902432647, "valueType": "Amount"},
                {"code": "GRAINSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 0.877350918337469, "valueType": "Amount"},
                {"code": "JUICESERV", "description": "Eating Pattern", "units": "PerDay", "amount": 0.098804910215613, "valueType": "Amount"},
                {"code": "LOWFATDAIRYSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 0.0, "valueType": "Amount"},
                {"code": "NOFRYFISHSERV", "description": "Eating Pattern", "units": "PerWeek", "amount": 0.392841568548386, "valueType": "Amount"},
                {"code": "NONFATDAIRY", "description": "Eating Pattern", "units": "PerDay", "amount": 0.0, "valueType": "Amount"},
                {"code": "PLANTPROTEIN", "description": "Eating Pattern", "units": "PerDay", "amount": 0.200006679966025, "valueType": "Amount"},
                {"code": "SALADSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 5.85226950661777, "valueType": "Amount"},
                {"code": "SOYFOODS", "description": "Eating Pattern", "units": "PerDay", "amount": 0.205479452054794, "valueType": "Amount"},
                {"code": "VEGSUMM", "description": "Eating Pattern", "units": "PerDay", "amount": 13.8556749715375, "valueType": "Amount"}
            ]
        }

VIOSCREEN_EATING_PATTERNS = VioscreenEatingPatterns.from_vioscreen(EP_DATA)



class TestEatingPatternsRepo(unittest.TestCase):

    def test_insert_eating_patterns_does_not_exist(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenEatingPatternsRepo(t)
            obs = r.insert_eating_patterns(VIOSCREEN_EATING_PATTERNS)
            self.assertEqual(obs, 17)

    def test_get_eating_patterns_exists(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenEatingPatternsRepo(t)
            r.insert_eating_patterns(VIOSCREEN_EATING_PATTERNS)
            obs = r.get_eating_patterns(VIOSCREEN_EATING_PATTERNS.sessionId)
            self.assertEqual(obs, VIOSCREEN_EATING_PATTERNS)

    def test_get_eating_patterns_does_not_exist(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenEatingPatternsRepo(t)
            obs = r.get_eating_patterns('does not exist')
            self.assertEqual(obs, None)


if __name__ == '__main__':
    unittest.main()
