import unittest
from microsetta_private_api.model.vioscreen import (
    VioscreenSession, VioscreenPercentEnergy,
    VioscreenPercentEnergyComponent)
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import (
    VioscreenSessionRepo, VioscreenPercentEnergyRepo)
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

VIOSCREEN_PERCENT_ENERGY = VioscreenPercentEnergy(
                sessionId="0087da64cdcb41ad800c23531d1198f2",
                energy_components=[
                    VioscreenPercentEnergyComponent(code="%protein",
                                                    description="Percent of calories from Protein",  # noqa
                                                    short_description="Protein",  # noqa
                                                    units="%",
                                                    amount=14.50362489752287),
                    VioscreenPercentEnergyComponent(code="%fat",
                                                    description="Percent of calories from Fat",  # noqa
                                                    short_description="Fat",
                                                    units="%",
                                                    amount=35.5233111996746),
                    VioscreenPercentEnergyComponent(code="%carbo",
                                                    description="Percent of calories from Carbohydrate",  # noqa
                                                    short_description="Carbohydrate",  # noqa
                                                    units="%",
                                                    amount=42.67319895276668),
                    VioscreenPercentEnergyComponent(code="%alcohol",
                                                    description="Percent of calories from Alcohol",  # noqa
                                                    short_description="Alcohol",  # noqa
                                                    units="%",
                                                    amount=7.299864950035845),
                    VioscreenPercentEnergyComponent(code="%sfatot",
                                                    description="Percent of calories from Saturated Fat",  # noqa
                                                    short_description="Saturated Fat",  # noqa
                                                    units="%",
                                                    amount=8.953245015317886),
                    VioscreenPercentEnergyComponent(code="%mfatot",
                                                    description="Percent of calories from Monounsaturated Fat",  # noqa
                                                    short_description="Monounsaturated Fat",  # noqa
                                                    units="%",
                                                    amount=16.04143105742606),
                    VioscreenPercentEnergyComponent(code="%pfatot",
                                                    description="Percent of calories from Polyunsaturated Fat",  # noqa
                                                    short_description="Polyunsaturated Fat",  # noqa
                                                    units="%",
                                                    amount=9.3864628707637),
                    VioscreenPercentEnergyComponent(code="%adsugtot",
                                                    description="Percent of calories from Added Sugar",  # noqa
                                                    short_description="Added Sugar",  # noqa
                                                    units="%",
                                                    amount=5.59094160186449)
                ])


class TestPercentEnergyRepo(unittest.TestCase):
    def _assert_unordered_components(self, obs, exp):
        self.assertEqual(obs.sessionId, exp.sessionId)
        obs_comp = {c.code: c for c in obs.energy_components}
        exp_comp = {c.code: c for c in exp.energy_components}

        # make sure the keys (codes) are the same
        self.assertEqual(set(obs_comp), set(exp_comp))

        # there are small numeric differences going in/out of the database
        for k in obs_comp:
            self.assertAlmostEqual(obs_comp[k].amount,
                                   exp_comp[k].amount)

    def test_insert_percent_energy_exists(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenPercentEnergyRepo(t)
            r.insert_percent_energy(VIOSCREEN_PERCENT_ENERGY)
            obs = r.insert_percent_energy(VIOSCREEN_PERCENT_ENERGY)
            self.assertEqual(obs, 0)

    def test_insert_percent_energy_does_not_exist(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenPercentEnergyRepo(t)
            obs = r.insert_percent_energy(VIOSCREEN_PERCENT_ENERGY)
            self.assertEqual(obs, 8)

    def test_get_percent_energy_exists(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenPercentEnergyRepo(t)
            r.insert_percent_energy(VIOSCREEN_PERCENT_ENERGY)
            obs = r.get_percent_energy(VIOSCREEN_PERCENT_ENERGY.sessionId)
            self._assert_unordered_components(obs, VIOSCREEN_PERCENT_ENERGY)

    def test_get_percent_energy_does_not_exist(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenPercentEnergyRepo(t)
            obs = r.get_percent_energy('does not exist')
            self.assertEqual(obs, None)


if __name__ == '__main__':
    unittest.main()
