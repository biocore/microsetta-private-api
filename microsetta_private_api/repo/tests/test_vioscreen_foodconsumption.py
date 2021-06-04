import unittest
from microsetta_private_api.model.vioscreen import (
    VioscreenSession, VioscreenFoodConsumption,
    VioscreenFoodConsumptionComponent,
    VioscreenFoodComponentsComponent)
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import (
    VioscreenSessionRepo, VioscreenFoodConsumptionRepo)
from datetime import datetime
import json
import pkg_resources


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

CONS_DATA = {"sessionId": "0087da64cdcb41ad800c23531d1198f2", 
                "foodConsumption": [
                    {"foodCode": "20001", 
                     "description": "Apples, applesauce and pears", 
                     "foodGroup": "Fruits", 
                     "amount": 1.0, 
                     "frequency": 28, 
                     "consumptionAdjustment": 1.58695652173913, 
                     "servingSizeText": "1 apple or pear, 1/2 cup", 
                     "servingFrequencyText": "2-3 per month", 
                     "created": "2017-07-29T02:02:54.72", 
                        "data": [
                            {"code": "acesupot", "description": "Acesulfame Potassium", "units": "mg", "amount": 0.0, "valueType": "Amount"}, 
                            {"code": "addsugar", "description": "Added Sugar", "units": "g", "amount": 0.37180348271909, "valueType": "Amount"}, 
                            {"code": "adsugtot", "description": "Added Sugars (by Total Sugars)", "units": "g", "amount": 0.258159998188848, "valueType": "Amount"}
                        ]
                    }, 
                    {"foodCode": "20018", 
                     "description": "Apricots - dried", 
                     "foodGroup": "Fruits", 
                     "amount": 1.5, 
                     "frequency": 12, 
                     "consumptionAdjustment": 1.58695652173913, 
                     "servingSizeText": "6 dried halves", 
                     "servingFrequencyText": "1 per month", 
                     "created": "2017-07-29T02:02:54.72", 
                        "data": [
                            {"code": "acesupot", "description": "Acesulfame Potassium", "units": "mg", "amount": 0.0, "valueType": "Amount"}, 
                            {"code": "addsugar", "description": "Added Sugar", "units": "g", "amount": 0.0, "valueType": "Amount"}, 
                            {"code": "adsugtot", "description": "Added Sugars (by Total Sugars)", "units": "g", "amount": 0.0, "valueType": "Amount"}
                        ]
                    }
                ]
            }


class TestFoodConsumptionRepo(unittest.TestCase):
    package = 'microsetta_private_api.repo.tests'

    def get_data_path(self, filename):
        # adapted from qiime2.plugin.testing.TestPluginBase
        return pkg_resources.resource_filename(self.package,
                                               'data/%s' % filename)

    def test_insert_food_consumption_does_not_exist(self):
        with Transaction() as t:
            with open(self.get_data_path("foodconsumption.data")) as fp:
                FULL_DATA = json.load(fp)
            VIOSCREEN_FOOD_CONSUMPTION = VioscreenFoodConsumption.from_vioscreen(FULL_DATA)
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenFoodConsumptionRepo(t)
            obs = r.insert_food_consumption(VIOSCREEN_FOOD_CONSUMPTION)
            self.assertEqual(obs, 14742)

    def test_get_food_consumption_exists(self):
        with Transaction() as t:
            with open(self.get_data_path("foodconsumption.data")) as fp:
                FULL_DATA = json.load(fp)
            VIOSCREEN_FOOD_CONSUMPTION = VioscreenFoodConsumption.from_vioscreen(FULL_DATA)
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenFoodConsumptionRepo(t)
            r.insert_food_consumption(VIOSCREEN_FOOD_CONSUMPTION)
            obs = r.get_food_consumption(VIOSCREEN_FOOD_CONSUMPTION.sessionId)
            self.assertEqual(obs.sessionId, VIOSCREEN_FOOD_CONSUMPTION.sessionId)          
            obs_comps = sorted(obs.components, key=lambda x: x.description)
            exp_comps = sorted(VIOSCREEN_FOOD_CONSUMPTION.components, key=lambda x: x.description)
            for obs_comp, exp_comp in zip(obs_comps, exp_comps):
                obs_cs = sorted(obs_comp.data, key=lambda x: x.code)
                exp_cs = sorted(obs_comp.data, key=lambda x: x.code)
                for obs_c, exp_c in zip(obs_cs, exp_cs):
                    self.assertEqual(obs_c, exp_c)

    def test_get_food_consumption_does_not_exist(self):
        with Transaction() as t:
            with open(self.get_data_path("foodconsumption.data")) as fp:
                FULL_DATA = json.load(fp)
            VIOSCREEN_FOOD_CONSUMPTION = VioscreenFoodConsumption.from_vioscreen(FULL_DATA)
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenFoodConsumptionRepo(t)
            obs = r.get_food_consumption('does not exist')
            self.assertEqual(obs, None)


if __name__ == '__main__':
    unittest.main()
