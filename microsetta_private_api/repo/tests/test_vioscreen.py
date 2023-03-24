import unittest
import json
from microsetta_private_api.api.tests.test_api import (
    ACCT_MOCK_ISS_3,
    ACCT_MOCK_SUB_3,
    create_dummy_acct)

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
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo


def get_data_path(filename):
    package = 'microsetta_private_api/model/tests'
    return package + '/data/%s' % filename


class VioscreenRepoTests(unittest.TestCase):
    def setUp(self):
        with Transaction() as t:
            cur = t.cursor()
            cur.execute("""SELECT DISTINCT ag_login_id as account_id,
                                           source_id
                           FROM ag.ag_kit_barcodes
                           JOIN ag.ag_login_surveys using (source_id)
                           WHERE barcode='000004216'""")
            acct_id, src_id = cur.fetchone()
            self.acct_id = acct_id
            self.src_id = src_id

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

    def test_is_code_unused_false(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            vr = VioscreenRepo(t)
            ffq_code = admin_repo.create_ffq_code()

            with t.dict_cursor() as cur:
                cur.execute(
                    "UPDATE campaign.ffq_registration_codes "
                    "SET registration_code_used = NOW()"
                    "WHERE ffq_registration_code = %s",
                    (ffq_code,)
                )

            code_used = vr.is_code_unused(ffq_code)
            self.assertFalse(code_used)

    def test_is_code_unused_true(self):
        with Transaction() as t:
            admin_repo = AdminRepo(t)
            vr = VioscreenRepo(t)
            ffq_code = admin_repo.create_ffq_code()

            code_used = vr.is_code_unused(ffq_code)
            self.assertTrue(code_used)

    def test_get_registry_entries_by_source(self):
        with Transaction() as t:
            # First, we'll set up an FFQ code
            admin_repo = AdminRepo(t)
            ffq_code = admin_repo.create_ffq_code()

            # Next, we'll have our source 'take' the FFQ
            s_t_repo = SurveyTemplateRepo(t)
            vio_id = s_t_repo.create_vioscreen_id(
                self.acct_id,
                self.src_id,
                None,
                ffq_code
            )

            # Now let's verify that we can retrieve the registry entry
            vio_repo = VioscreenRepo(t)
            reg_entries = vio_repo.get_registry_entries_by_source(
                self.acct_id,
                self.src_id
            )
            retrieved_entry = reg_entries[0]

            self.assertEqual(retrieved_entry.registration_code, ffq_code)
            self.assertEqual(retrieved_entry.survey_id, vio_id)


class VioscreenSessions(unittest.TestCase):
    def setUp(self):
        super().setUp()

        with Transaction() as t:
            cur = t.cursor()
            cur.execute("""SELECT DISTINCT ag_login_id as account_id,
                                           source_id,
                                           ag_kit_barcode_id as sample_id
                           FROM ag.ag_kit_barcodes
                           JOIN ag.ag_login_surveys using (source_id)
                           WHERE barcode='000004216'""")
            acct_id, src_id, samp_id = cur.fetchone()
            self.acct_id = acct_id
            self.src_id = src_id
            self.samp_id = samp_id
            self.vio_id = '674533d367f222d2'
            cur.execute("""INSERT INTO ag.vioscreen_registry
                           (account_id, source_id, sample_id, vio_id)
                           VALUES (%s, %s, %s, %s)""",
                        (self.acct_id, self.src_id, self.samp_id, self.vio_id))
            t.commit()

    def tearDown(self):
        with Transaction() as t:
            cur = t.cursor()
            cur.execute("""DELETE FROM ag.vioscreen_registry
                           WHERE account_id=%s
                               AND source_id=%s
                               AND sample_id=%s
                               AND vio_id=%s""",
                        (self.acct_id, self.src_id, self.samp_id, self.vio_id))

            sessionId = "000ada854d4f45f5abda90ccade7f0a8"
            cur.execute("""DELETE FROM ag.vioscreen_sessions
                           WHERE sessionId = %s""",
                        (sessionId,))

            sessionId2 = "000ada854d4f45f5abda90ccade7f0a9"
            cur.execute("""DELETE FROM ag.vioscreen_sessions
                           WHERE sessionId = %s""",
                        (sessionId2,))
            t.commit()

        super().tearDown()

    def test_get_vioscreen_sessions_404(self):
        _ = create_dummy_acct(create_dummy_1=True,
                              iss=ACCT_MOCK_ISS_3,
                              sub=ACCT_MOCK_SUB_3,
                              dummy_is_admin=True)
        with Transaction() as t:
            vio_session = VioscreenRepo(t)
            sessions = vio_session.get_vioscreen_sessions(self.acct_id,
                                                          self.src_id)
            self.assertEqual(sessions, None)

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
        with Transaction() as t:
            vio_session = VioscreenRepo(t)
            sessions = vio_session.get_vioscreen_sessions(self.acct_id,
                                                          self.src_id)
            self.assertEqual(len(sessions), 1)


if __name__ == '__main__':
    unittest.main()
