import unittest
import json
from microsetta_private_api.api.tests.test_api import (
    ACCT_MOCK_ISS_3,
    ACCT_MOCK_SUB_3,
    FAKE_TOKEN_ADMIN,
    create_dummy_acct,
    make_headers)

from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import (
    VioscreenRepo, VioscreenSessionRepo, VioscreenSupplementsRepo)
from microsetta_private_api.repo.tests.test_vioscreen_dietaryscore import (
    VIOSCREEN_SESSION, VIOSCREEN_DIETARY_SCORE)
from microsetta_private_api.repo.tests.test_vioscreen_supplements import (
    VIOSCREEN_SUPPLEMENTS
    )
from microsetta_private_api.model.vioscreen import (
    VioscreenFoodConsumption, VioscreenPercentEnergy,
    VioscreenFoodComponents,
    VioscreenMPeds, VioscreenEatingPatterns,
    VioscreenComposite, VioscreenSession)


def get_data_path(filename):
    package = 'microsetta_private_api/model/tests'
    return package + '/data/%s' % filename


class VioscreenRepoTests(unittest.TestCase):
    def setUp(self):
        # reusing as much as we can, but there are some differences in
        # hwo the raw data were used
        def loader(model, name):
            with open(get_data_path(f"{name}.data")) as data:
                loaded_data = json.load(data)
                if isinstance(loaded_data, list):
                    return model.from_vioscreen(loaded_data[0])
                else:
                    return model.from_vioscreen(loaded_data)

        fc = loader(VioscreenFoodConsumption, 'foodconsumption')
        fcom = loader(VioscreenFoodComponents, 'foodcomponents')
        pe = loader(VioscreenPercentEnergy, 'percentenergy')
        m = loader(VioscreenMPeds, 'mpeds')
        ep = loader(VioscreenEatingPatterns, 'eatingpatterns')

        self.supp = VIOSCREEN_SUPPLEMENTS
        self.FFQ = VioscreenComposite(VIOSCREEN_SESSION, pe,
                                      [VIOSCREEN_DIETARY_SCORE, ],
                                      VIOSCREEN_SUPPLEMENTS, fcom,
                                      ep, m, fc)

    def test_insert_ffq(self):
        with Transaction() as t:
            vr = VioscreenRepo(t)
            vr.insert_ffq(self.FFQ)

            # if we've successfully inserted, we should be able to use
            # another repo to get a subset of data

            vs = VioscreenSupplementsRepo(t)
            supp = vs.get_supplements(VIOSCREEN_SESSION.sessionId)
            self.assertEqual(self.supp, supp)

    def test_get_ffq(self):
        with Transaction() as t:
            vr = VioscreenRepo(t)
            vr.insert_ffq(self.FFQ)
            obs = vr.get_ffq(VIOSCREEN_SESSION.sessionId)
            self.assertEqual(obs, self.FFQ)

    def test_get_vioscreen_sessions_404(self):
        src_id = self.src_id + '1'
        url = (f'/api/accounts/{self.acct_id}'
               f'/sources/{src_id}') + '/vioscreen_sessions'
        _ = create_dummy_acct(create_dummy_1=True,
                              iss=ACCT_MOCK_ISS_3,
                              sub=ACCT_MOCK_SUB_3,
                              dummy_is_admin=True)
        get_response = self.client.get(url,
                                       headers=make_headers(FAKE_TOKEN_ADMIN))
        self.assertEqual(get_response.status_code, 404)

    def test_get_vioscreen_sessions_200(self):
        vioscreen_session = VioscreenSession(
            sessionId="000ada854d4f45f5abda90ccade7f0a8",
            username="674533d367f222d2",
            protocolId=344,
            status="Finished",
            startDate="2014-10-08T18:55:12.747",
            endDate="2014-10-08T18:57:07.503",
            cultureCode="en-US",
            created="2014-10-08T18:55:07.96",
            modified="2017-07-29T03:56:04.22"
        )

        with Transaction() as t:
            vio_sess = VioscreenSessionRepo(t)
            vio_sess.upsert_session(vioscreen_session)
            t.commit()

        url = self._url_constructor() + '/vioscreen/session'
        _ = create_dummy_acct(create_dummy_1=True,
                              iss=ACCT_MOCK_ISS_3,
                              sub=ACCT_MOCK_SUB_3,
                              dummy_is_admin=True)
        get_response = self.client.get(url,
                                       headers=make_headers(FAKE_TOKEN_ADMIN))
        self.assertEqual(get_response.status_code, 200)

        response_obj = json.loads(get_response.data)
        self.assertEqual(response_obj['username'], vioscreen_session.username)
        self.assertEqual(response_obj['sessionId'],
                         vioscreen_session.sessionId)
        self.assertEqual(response_obj['status'], vioscreen_session.status)


if __name__ == '__main__':
    unittest.main()
