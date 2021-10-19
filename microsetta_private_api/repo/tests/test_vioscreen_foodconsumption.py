import unittest
from microsetta_private_api.model.vioscreen import (
    VioscreenSession, VioscreenFoodConsumption)
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import (
    VioscreenSessionRepo, VioscreenFoodConsumptionRepo)
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


class TestFoodConsumptionRepo(unittest.TestCase):
    def test_insert_food_consumption_does_not_exist(self):
        with Transaction() as t:
            with open(get_data_path("foodconsumption.data")) as data:
                CONS_DATA = json.load(data)
            VIOSCREEN_FOOD_CONSUMPTION = \
                VioscreenFoodConsumption.from_vioscreen(CONS_DATA)
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenFoodConsumptionRepo(t)
            obs = r.insert_food_consumption(VIOSCREEN_FOOD_CONSUMPTION)
            self.assertEqual(obs, 14742)

    def test_get_food_consumption_exists(self):
        with Transaction() as t:
            with open(get_data_path("foodconsumption.data")) as data:
                CONS_DATA = json.load(data)
            VIOSCREEN_FOOD_CONSUMPTION = \
                VioscreenFoodConsumption.from_vioscreen(CONS_DATA)
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenFoodConsumptionRepo(t)
            r.insert_food_consumption(VIOSCREEN_FOOD_CONSUMPTION)
            obs = r.get_food_consumption(VIOSCREEN_FOOD_CONSUMPTION.sessionId)
            self.assertEqual(obs.sessionId,
                             VIOSCREEN_FOOD_CONSUMPTION.sessionId)
            obs_comps = sorted(obs.components, key=lambda x: x.description)
            exp_comps = sorted(VIOSCREEN_FOOD_CONSUMPTION.components,
                               key=lambda x: x.description)
            for obs_comp, exp_comp in zip(obs_comps, exp_comps):
                obs_cs = sorted(obs_comp.data, key=lambda x: x.code)
                exp_cs = sorted(obs_comp.data, key=lambda x: x.code)
                for obs_c, exp_c in zip(obs_cs, exp_cs):
                    self.assertEqual(obs_c, exp_c)

    def test_get_food_consumption_does_not_exist(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenFoodConsumptionRepo(t)
            obs = r.get_food_consumption('does not exist')
            self.assertEqual(obs, None)


if __name__ == '__main__':
    unittest.main()
