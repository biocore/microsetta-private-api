import unittest
from microsetta_private_api.model.vioscreen import (VioscreenSession,
                                                    VioscreenPercentEnergy,
                                                    VioscreenPercentEnergyComponent)  # noqa
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import (VioscreenSessionRepo,
                                                        VioscreenPercentEnergyRepo)  # noqa
from datetime import datetime
from copy import copy


def _to_dt(mon, day, year):
    return datetime(month=mon, day=day, year=year)


VIOSCREEN_USERNAME1 = '3379e14164fac0ed'

# in ag_test db, this uuid corresponds to VIOSCREEN_USERNAME1
BARCODE_UUID_FOR_VIOSESSION = '66ec7d9a-400d-4d71-bce8-fdf79d2be554'
BARCODE_UUID_NOTIN_REGISTRY = 'edee4af9-65b2-4ed1-ba66-5bf58383005e'

VIOSCREEN_SESSION = VioscreenSession(sessionId='a session',
                                     username='a user',
                                     protocolId=1234,
                                     status='something',
                                     startDate=_to_dt(1, 1, 1970),
                                     endDate=None,
                                     cultureCode='foo',
                                     created=_to_dt(1, 1, 1970),
                                     modified=_to_dt(1, 1, 1970))

VIOSCREEN_PERCENT_ENERGY_COMPONENTS = [
    VioscreenPercentEnergyComponent('%mfatot',
                                    'foo', 'bar', '%', 10),
]
VIOSCREEN_PERCENT_ENERGY = \
    VioscreenPercentEnergy(sessionId='a session',
                           energy_components=VIOSCREEN_PERCENT_ENERGY_COMPONENTS)  # noqa


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

    def test_get_sessions_by_username_exists(self):
        with Transaction() as t:
            r = VioscreenSessionRepo(t)
            obs = r.upsert_session(VIOSCREEN_SESSION)
            self.assertEqual(obs, True)

            obs = r.get_sessions_by_username(VIOSCREEN_SESSION.username)
            self.assertEqual(obs, [VIOSCREEN_SESSION, ])

    def test_get_sessions_by_username_multiple(self):
        to_insert = [VIOSCREEN_SESSION.copy(),
                     VIOSCREEN_SESSION.copy(),
                     VIOSCREEN_SESSION.copy()]

        # NOTE: the username is held constant across these records. This
        # emulates a user haveing multiple FFQ sessions
        to_insert[0].sessionId = 'session1'
        to_insert[1].sessionId = 'session2'
        to_insert[2].sessionId = 'session3'

        to_insert[0].created = _to_dt(1, 1, 1970)
        to_insert[1].created = _to_dt(1, 1, 1980)
        to_insert[2].created = _to_dt(1, 1, 1990)

        # the third entry, while started the latest, does not have an enddate
        # so cannot be complete
        to_insert[0].endDate = _to_dt(1, 1, 1971)
        to_insert[1].endDate = _to_dt(1, 1, 1981)
        to_insert[2].endDate = None

        with Transaction() as t:
            r = VioscreenSessionRepo(t)
            for record in to_insert:
                obs = r.upsert_session(record)
                self.assertEqual(obs, True)

            obs = r.get_sessions_by_username(VIOSCREEN_SESSION.username)
            self.assertEqual(obs, to_insert)

    def test_get_sessions_by_username_does_not_exist(self):
        with Transaction() as t:
            r = VioscreenSessionRepo(t)
            obs = r.get_sessions_by_username('does not exist')
            self.assertEqual(obs, None)

    def test_get_unfinished_sessions(self):
        with Transaction() as t:
            r = VioscreenSessionRepo(t)
            cur = t.cursor()
            cur.execute("SELECT vio_id FROM ag.vioscreen_registry")
            exp = {r[0] for r in cur.fetchall()}
            obs = r.get_unfinished_sessions()
            self.assertEqual({r.username for r in obs}, exp)

            user1 = VIOSCREEN_SESSION.copy()
            user1.username = VIOSCREEN_USERNAME1
            obs = r.upsert_session(user1)
            self.assertTrue(obs)

            # our base session is still unfinished (no end date)
            cur.execute("SELECT vio_id FROM ag.vioscreen_registry")
            exp = {r[0] for r in cur.fetchall()}
            obs = r.get_unfinished_sessions()
            self.assertEqual({r.username for r in obs}, exp)

            # set a finished status
            user1.status = 'Finished'
            user1.endDate = _to_dt(1, 1, 1971)
            obs = r.upsert_session(user1)
            self.assertTrue(obs)

            # our users record is finished so we shouldn't get it back
            cur.execute("SELECT vio_id FROM ag.vioscreen_registry")
            exp = {r[0] for r in cur.fetchall()}
            obs = r.get_unfinished_sessions()
            self.assertEqual({r.username for r in obs},
                             exp - {VIOSCREEN_USERNAME1, })

    def test_get_unfinished_sessions_multiple(self):
        with Transaction() as t:
            r = VioscreenSessionRepo(t)
            cur = t.cursor()
            cur.execute("SELECT vio_id FROM ag.vioscreen_registry")
            exp = {r[0] for r in cur.fetchall()}
            obs = r.get_unfinished_sessions()
            self.assertEqual({r.username for r in obs}, exp)

            sess1 = VIOSCREEN_SESSION.copy()
            sess1.username = VIOSCREEN_USERNAME1
            sess2 = VIOSCREEN_SESSION.copy()
            sess2.username = VIOSCREEN_USERNAME1
            sess2.sessionId = 'a different sessionid'

            obs = r.upsert_session(sess1)
            self.assertTrue(obs)
            obs = r.upsert_session(sess2)
            self.assertTrue(obs)

            # our sessions are unfinished
            cur.execute("SELECT vio_id FROM ag.vioscreen_registry")
            exp = {r[0] for r in cur.fetchall()}
            obs = r.get_unfinished_sessions()
            self.assertEqual({r.username for r in obs}, exp)

            # set a finished status
            sess1.status = 'Finished'
            sess1.endDate = _to_dt(1, 1, 1971)
            obs = r.upsert_session(sess1)
            self.assertTrue(obs)

            # one session is finished, and we only actually understand the
            # sematics of a single session anyway, so under our current
            # operating assumptions, this users FFQ is now complete
            cur.execute("SELECT vio_id FROM ag.vioscreen_registry")
            exp = {r[0] for r in cur.fetchall()}
            obs = r.get_unfinished_sessions()
            self.assertEqual({r.username for r in obs},
                             exp - {VIOSCREEN_USERNAME1, })

    def test_get_missing_ffqs(self):
        with Transaction() as t:
            cur = t.cursor()
            r = VioscreenSessionRepo(t)
            pr = VioscreenPercentEnergyRepo(t)

            user1 = VIOSCREEN_SESSION.copy()
            user1.username = VIOSCREEN_USERNAME1
            r.upsert_session(user1)

            # our user is not present as they do not have an enddate or
            # finished status
            obs = r.get_missing_ffqs()
            self.assertNotIn(VIOSCREEN_USERNAME1, {o.username for o in obs})

            user1.status = 'Finished'
            user1.endDate = _to_dt(1, 1, 1971)
            r.upsert_session(user1)

            # our finished session does not have ffq data
            obs = r.get_missing_ffqs()
            self.assertIn(VIOSCREEN_USERNAME1, {o.username for o in obs})

            # give our user a "completed" ffq
            user1_pe = VIOSCREEN_PERCENT_ENERGY
            pr.insert_percent_energy(user1_pe)
            obs = r.get_missing_ffqs()
            self.assertNotIn(VIOSCREEN_USERNAME1, {o.username for o in obs})

            # our users record is finished so we shouldn't get it back
            cur.execute("SELECT vio_id FROM ag.vioscreen_registry")
            exp = {r[0] for r in cur.fetchall()}
            obs = r.get_unfinished_sessions()
            self.assertEqual({r.username for r in obs},
                             exp - {VIOSCREEN_USERNAME1, })

    def test_get_ffq_status_by_sample(self):

        session_copy = VIOSCREEN_SESSION.copy()
        session_copy.username = VIOSCREEN_USERNAME1
        with Transaction() as t:
            r = VioscreenSessionRepo(t)
            r.upsert_session(session_copy)
            session = r.get_sessions_by_username(VIOSCREEN_USERNAME1)[0]

            obs = r.get_ffq_status_by_sample(BARCODE_UUID_NOTIN_REGISTRY)
            self.assertEqual(obs, (False, False, None))

            session.status = 'Finished'
            session.endDate = _to_dt(2, 1, 1970)
            r.upsert_session(session)

            # enumerate the empirically observed states from vioscreen
            # (is_complete, has_taken, exact_status)
            obs = r.get_ffq_status_by_sample(BARCODE_UUID_FOR_VIOSESSION)
            self.assertEqual(obs, (True, True, 'Finished'))

            session.status = 'Started'
            session.endDate = None
            r.upsert_session(session)

            obs = r.get_ffq_status_by_sample(BARCODE_UUID_FOR_VIOSESSION)
            self.assertEqual(obs, (False, True, 'Started'))

            session.status = 'New'
            r.upsert_session(session)
            obs = r.get_ffq_status_by_sample(BARCODE_UUID_FOR_VIOSESSION)
            self.assertEqual(obs, (False, False, 'New'))

            session.status = 'Review'
            r.upsert_session(session)
            obs = r.get_ffq_status_by_sample(BARCODE_UUID_FOR_VIOSESSION)
            self.assertEqual(obs, (False, True, 'Review'))


if __name__ == '__main__':
    unittest.main()
