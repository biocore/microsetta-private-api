import unittest
import json

from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import (
    VioscreenRepo, VioscreenSupplementsRepo)
from microsetta_private_api.repo.tests.test_vioscreen_dietaryscore import (
    VIOSCREEN_SESSION, VIOSCREEN_DIETARY_SCORE)
from microsetta_private_api.repo.tests.test_vioscreen_supplements import (
    VIOSCREEN_SUPPLEMENTS
    )
from microsetta_private_api.model.vioscreen import (
    VioscreenFoodConsumption, VioscreenPercentEnergy, VioscreenFoodComponents,
    VioscreenMPeds, VioscreenEatingPatterns, VioscreenComposite)


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


if __name__ == '__main__':
    unittest.main()
