import unittest
from microsetta_private_api.model.vioscreen import (
    VioscreenSession, VioscreenSupplements, 
    VioscreenSupplementsComponent)
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import (
    VioscreenSessionRepo, VioscreenSupplementsRepo)
from datetime import datetime

def _to_dt(mon, day, year):
    return datetime(month=mon, day=day, year=year)

VIOSCREEN_SESSION = VioscreenSession(sessionId='0087da64cdcb41ad800c23531d1198f2',
                                     username='a user',
                                     protocolId=1234,
                                     status='something',
                                     startDate=_to_dt(1, 1, 1970),
                                     endDate=None,
                                     cultureCode='foo',
                                     created=_to_dt(1, 1, 1970),
                                     modified=_to_dt(1, 1, 1970))

VIOSCREEN_SUPPLEMENTS = VioscreenSupplements(sessionId="005eae45652f4aef9880502a08139155",
                                   supplements_components=[VioscreenSupplementsComponent(supplement="MultiVitamin",
                                                                                         frequency="7",
                                                                                         amount="200",
                                                                                         average="200"),
                                                           VioscreenSupplementsComponent(supplement="Calcium",
                                                                                         frequency="",
                                                                                         amount="",
                                                                                         average="")
                                    ])

class TestSupplementsRepo(unittest.TestCase):
    def test_insert_supplements_exists(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenSupplementsRepo(t)
            r.insert_supplements(VIOSCREEN_SUPPLEMENTS)
            obs = r.insert_supplements(VIOSCREEN_SUPPLEMENTS)
            self.assertEqual(obs, 0)

    def test_insert_supplements_does_not_exist(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenSupplementsRepo(t)
            obs = r.insert_supplements(VIOSCREEN_SUPPLEMENTS)
            self.assertEqual(obs, 8)

    def test_get_supplements_exists(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenSupplementsRepo(t)
            r.insert_supplements(VIOSCREEN_SUPPLEMENTS)
            obs = r.get_supplements(VIOSCREEN_SUPPLEMENTS.sessionId)
            self.assertEqual(obs, VIOSCREEN_SUPPLEMENTS)

    def test_get_supplements_does_not_exist(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenSupplementsRepo(t)
            obs = r.get_supplements('does not exist')
            self.assertEqual(obs, None)

if __name__ == '__main__':
    unittest.main()