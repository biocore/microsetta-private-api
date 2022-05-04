import unittest
from unittest.mock import patch

from microsetta_private_api.util.vioscreen import (VioscreenAdminAPI,
                                                   update_session_detail,
                                                   fetch_ffqs,
                                                   EN_US)
from microsetta_private_api.config_manager import SERVER_CONFIG


APIUSER = SERVER_CONFIG['vioscreen_admin_username']
RUN_API_TESTS = APIUSER not in ('', 'vioscreen_user_placeholder')
SID = '4bb9d8eba87a4ee58b535c65bf80b8b1'
UID = 'a5a9fb9775ccebe5'
SID2 = '520f3650623b43acaa230ba31ac6c981'  # incomplete


if RUN_API_TESTS:
    client = VioscreenAdminAPI(perform_async=False)
else:
    client = None


@unittest.skipIf(not RUN_API_TESTS,
                 "vioscreen secrets not provided")
class VioscreenAPITests(unittest.TestCase):
    def setUp(self):
        self.client = client

    def test_foodcomponents(self):
        obs = self.client.foodcomponents(SID)
        self.assertEqual(obs.sessionId, SID)

    def test_percentenergy(self):
        obs = self.client.percentenergy(SID)
        self.assertEqual(obs.sessionId, SID)

    def test_mpeds(self):
        obs = self.client.mpeds(SID)
        self.assertEqual(obs.sessionId, SID)

    def test_eatingpatterns(self):
        obs = self.client.eatingpatterns(SID)
        self.assertEqual(obs.sessionId, SID)

    def test_foodconsumption(self):
        obs = self.client.foodconsumption(SID)
        self.assertEqual(obs.sessionId, SID)

    def test_dietaryscore(self):
        obs = self.client.dietaryscore(SID)
        self.assertEqual(obs[0].sessionId, SID)

    def test_supplements(self):
        obs = self.client.supplements(SID)
        self.assertEqual(obs.sessionId, SID)

    def test_users(self):
        obs = self.client.users()
        self.assertTrue(any([d['username'] == UID for d in obs]))

    def test_user(self):
        obs = self.client.user(UID)
        self.assertEqual(obs['username'], UID)

    def test_sessions(self):
        obs = self.client.sessions(UID)
        self.assertEqual([s['sessionId'] for s in obs], [SID, ])

    def test_session_detail(self):
        obs = self.client.session_detail(SID)
        self.assertEqual(obs.sessionId, SID)

    def test_get_ffq(self):
        obs_err, obs = self.client.get_ffq(SID)
        self.assertEqual(obs.session.sessionId, SID)
        self.assertEqual(obs_err, [])

    def test_get_ffq_incomplete(self):
        obs_err, obs = self.client.get_ffq(SID2)
        self.assertEqual(obs, None)
        self.assertEqual(obs_err, ["FFQ appears incomplete or not taken", ])

    def test_top_food_report(self):
        obs = self.client.top_food_report(SID)
        self.assertTrue(obs.startswith(b'%PDF'))


class MockSession:
    def __init__(self, sid, uid):
        self.sessionId = sid
        self.username = uid
        self.status = 'Started'

    def update_from_vioscreen(self, other):
        pass


@unittest.skipIf(not RUN_API_TESTS,
                 "vioscreen secrets not provided")
class VioscreenGeneralTests(unittest.TestCase):
    @patch('microsetta_private_api.util.vioscreen.send_email')
    @patch('microsetta_private_api.util.vioscreen.current_task')
    @patch('microsetta_private_api.util.vioscreen.VioscreenSessionRepo')
    def test_update_session_detail(self, vs_session_repo, current_task,
                                   send_email):
        instance = vs_session_repo.return_value
        instance.get_unfinished_sessions.return_value = [
            MockSession(SID, UID),
            MockSession('foo', 'bar'),
            MockSession(None, UID),
        ]

        update_session_detail()
        exp = {'state': "SUCCESS",
               'meta': {"completion": 3,
                        "status": "SUCCESS",
                        "message": "2 sessions updated"}}
        current_task.update_state.assert_called_with(**exp)

        content = {"what": "Vioscreen sessions failed",
                   "content": ('\'foo\' : 404 ::: b\'{"Code":1021,"Message":'
                               '"Session not found.","InnerMessages":'
                               '["Session with id = [foo] was not '
                               'found."]}\'\n')}
        send_email.assert_called_once_with("pester@email.com",
                                           "pester_daniel",
                                           content,
                                           EN_US)

    @patch('microsetta_private_api.util.vioscreen.send_email')
    @patch('microsetta_private_api.util.vioscreen.VioscreenSessionRepo')
    @patch('microsetta_private_api.util.vioscreen.VioscreenRepo')
    def test_fetch_ffqs(self, vs_repo, vs_session_repo, send_email):
        instance = vs_session_repo.return_value
        instance.get_unfinished_sessions.return_value = [
            MockSession(SID, UID),
            MockSession('foo', None)
        ]

        vs_instance = vs_repo.return_value
        fetch_ffqs()

        vs_instance.insert_ffq.assert_called_once()
        content = {"what": "Vioscreen ffq insert failed",
                   "content": ('\'foo\' : 404 ::: b\'{"Code":1021,"Message":'
                               '"Session not found.","InnerMessages":'
                               '["Session with id = [foo] was not '
                               'found."]}\'\n')}
        send_email.assert_called_once_with("danielmcdonald@ucsd.edu",
                                           "pester_daniel",
                                           content,
                                           EN_US)


if __name__ == '__main__':
    unittest.main()
