import unittest
from microsetta_private_api.model.vioscreen import VioscreenSession
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import VioscreenSessionRepo
from datetime import datetime
from copy import copy


def _to_dt(mon, day, year):
    return datetime(month=mon, day=day, year=year)


VIOSCREEN_SESSION = VioscreenSession(sessionId='a session',
                                     username='a user',
                                     protocolId=1234,
                                     status='something',
                                     startDate=_to_dt(1, 1, 1970),
                                     endDate=None,
                                     cultureCode='foo',
                                     created=_to_dt(1, 1, 1970),
                                     modified=_to_dt(1, 1, 1970))


class VioscreenSessions(unittest.TestCase):
    def test_upsert_session_does_not_exist(self):
        with Transaction() as t:
            r = VioscreenSessionRepo(t)
            obs = r.upsert_session(VIOSCREEN_SESSION)
            self.assertEqual(obs, True)

    def test_upsert_session_exists(self):
        with Transaction() as t:
            r = VioscreenSessionRepo(t)
            obs = r.upsert_session(VIOSCREEN_SESSION)
            self.assertEqual(obs, True)

            # upsert of unmodified should have no change
            obs = r.upsert_session(VIOSCREEN_SESSION)
            # ...however the ON CONFLICT won't realize nothing
            # is different and still report something changed
            self.assertEqual(obs, True)

            session_modified = copy(VIOSCREEN_SESSION)
            session_modified.endDate = _to_dt(2, 1, 1970)
            obs = r.upsert_session(session_modified)
            self.assertEqual(obs, True)

            obs = r.get_session(VIOSCREEN_SESSION.sessionId)
            self.assertEqual(obs, session_modified)

    def test_get_session_exists(self):
        with Transaction() as t:
            r = VioscreenSessionRepo(t)
            r.upsert_session(VIOSCREEN_SESSION)
            obs = r.get_session(VIOSCREEN_SESSION.sessionId)
            self.assertEqual(obs, VIOSCREEN_SESSION)

    def test_get_session_does_not_exist(self):
        with Transaction() as t:
            r = VioscreenSessionRepo(t)
            obs = r.get_session('does not exist')
            self.assertEqual(obs, None)


if __name__ == '__main__':
    unittest.main()

