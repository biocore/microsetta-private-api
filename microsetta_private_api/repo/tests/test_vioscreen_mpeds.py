import unittest
from microsetta_private_api.model.vioscreen import (
    VioscreenSession, VioscreenMPeds)
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import (
    VioscreenSessionRepo, VioscreenMPedsRepo)
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


def get_data_path(filename):
    package = 'microsetta_private_api/model/tests'
    return package + '/data/%s' % filename


class TestMPedsRepo(unittest.TestCase):

    def test_insert_mpeds_does_not_exist(self):
        with Transaction() as t:
            with open(get_data_path("mpeds.data")) as data:
                MPEDS_DATA = json.load(data)
            VIOSCREEN_MPEDS = VioscreenMPeds.from_vioscreen(MPEDS_DATA[0])
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenMPedsRepo(t)
            obs = r.insert_mpeds(VIOSCREEN_MPEDS)
            self.assertEqual(obs, 40)

    def test_get_mpeds_exists(self):
        with Transaction() as t:
            with open(get_data_path("mpeds.data")) as data:
                MPEDS_DATA = json.load(data)
            VIOSCREEN_MPEDS = VioscreenMPeds.from_vioscreen(MPEDS_DATA[0])
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenMPedsRepo(t)
            r.insert_mpeds(VIOSCREEN_MPEDS)
            obs = r.get_mpeds(VIOSCREEN_MPEDS.sessionId)
            self.assertEqual(obs, VIOSCREEN_MPEDS)

    def test_get_mpeds_does_not_exist(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenMPedsRepo(t)
            obs = r.get_mpeds('does not exist')
            self.assertEqual(obs, None)


if __name__ == '__main__':
    unittest.main()
