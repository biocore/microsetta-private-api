import unittest
from microsetta_private_api.model.vioscreen import (
    VioscreenSession, VioscreenFoodComponents,
    VioscreenFoodComponentsComponent)
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import (
    VioscreenSessionRepo, VioscreenFoodComponentsRepo)
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

package = 'microsetta_private_api/model/tests'
# package where data is stored

def get_data_path(filename):
    return package + '/data/%s' % filename


class TestFoodComponentsRepo(unittest.TestCase):

    def test_insert_food_components_does_not_exist(self):
        with Transaction() as t:
            with open(get_data_path("foodcomponents.data")) as data:
                FC_DATA = json.load(data)
            VIOSCREEN_FOOD_COMPONENTS = VioscreenFoodComponents.from_vioscreen(FC_DATA[0])
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenFoodComponentsRepo(t)
            obs = r.insert_food_components(VIOSCREEN_FOOD_COMPONENTS)
            self.assertEqual(obs, 156)

    def test_get_food_components_exists(self):
        with Transaction() as t:
            with open(get_data_path("foodcomponents.data")) as data:
                FC_DATA = json.load(data)
            VIOSCREEN_FOOD_COMPONENTS = VioscreenFoodComponents.from_vioscreen(FC_DATA[0])
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenFoodComponentsRepo(t)
            r.insert_food_components(VIOSCREEN_FOOD_COMPONENTS)
            obs = r.get_food_components(VIOSCREEN_FOOD_COMPONENTS.sessionId)
            self.assertEqual(obs, VIOSCREEN_FOOD_COMPONENTS)

    def test_get_food_components_does_not_exist(self):
        with Transaction() as t:
            with open(get_data_path("foodcomponents.data")) as data:
                FC_DATA = json.load(data)
            VIOSCREEN_FOOD_COMPONENTS = VioscreenFoodComponents.from_vioscreen(FC_DATA[0])
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenFoodComponentsRepo(t)
            obs = r.get_food_components('does not exist')
            self.assertEqual(obs, None)


if __name__ == '__main__':
    unittest.main()
