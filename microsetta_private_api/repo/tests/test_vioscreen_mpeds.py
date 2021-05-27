import unittest
from microsetta_private_api.model.vioscreen import (
    VioscreenSession, VioscreenMPeds,
    VioscreenMPedsComponent)
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import (
    VioscreenSessionRepo, VioscreenMPedsRepo)
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

MP_DATA = {"sessionId": "0087da64cdcb41ad800c23531d1198f2", 
            "data": [
                {"code": "A_BEV", "description": "MPED: Total drinks of alcohol", "units": "alc_drinks", "amount": 1.30647563412786, "valueType": "Amount"}, 
                {"code": "A_CAL", "description": "MPED: Calories from alcoholic beverages", "units": "kcal", "amount": 153.256682095462, "valueType": "Amount"}, 
                {"code": "ADD_SUG", "description": "MPED: Teaspoon equivalents of added sugars", "units": "tsp_eq", "amount": 6.17650766372946, "valueType": "Amount"}, 
                {"code": "D_CHEESE", "description": "MPED: Number of cheese cup equivalents", "units": "cup_eq", "amount": 0.273545909382097, "valueType": "Amount"}, 
                {"code": "D_MILK", "description": "MPED: Number of milk cup equivalents", "units": "cup_eq", "amount": 0.0908870641392104, "valueType": "Amount"}, 
                {"code": "D_TOT_SOYM", "description": "MPED: Total number of milk group (milk, yogurt & cheese) cup equivalents PLUS soy milk", "units": "cup_eq", "amount": 0.364432970091999, "valueType": "Amount"}, 
                {"code": "D_TOTAL", "description": "MPED: Total number of milk group (milk, yogurt & cheese) cup equivalents", "units": "cup_eq", "amount": 0.364432970091999, "valueType": "Amount"}, 
                {"code": "D_YOGURT", "description": "MPED: Number of yogurt cup equivalents", "units": "cup_eq", "amount": 0.0, "valueType": "Amount"}, 
                {"code": "DISCFAT_OIL", "description": "MPED: Grams of discretionary Oil", "units": "g", "amount": 37.5229036217325, "valueType": "Amount"}, 
                {"code": "DISCFAT_SOL", "description": "MPED: Grams of discretionary Solid fat", "units": "g", "amount": 16.613760767425, "valueType": "Amount"}, 
                {"code": "F_CITMLB", "description": "MPED: Number of citrus, melon, berry cup equivalents", "units": "cup_eq", "amount": 0.689545236924411, "valueType": "Amount"}, 
                {"code": "F_NJ_CITMLB", "description": "MPED: Number of non-juice citrus, melon, berry cup equivalents", "units": "cup_eq", "amount": 0.632059715135536, "valueType": "Amount"}, 
                {"code": "F_NJ_OTHER", "description": "MPED: Number of other non-juice fruit cup equivalents", "units": "cup_eq", "amount": 1.54948829578895, "valueType": "Amount"}, 
                {"code": "F_NJ_TOTAL", "description": "MPED: Total number of non-juice fruit cup equivalents", "units": "cup_eq", "amount": 2.18154900059084, "valueType": "Amount"}, 
                {"code": "F_OTHER", "description": "MPED: Number of other fruit cup equivalents", "units": "cup_eq", "amount": 1.54948829578895, "valueType": "Amount"}, 
                {"code": "F_TOTAL", "description": "MPED: Total number of fruit cup equivalents", "units": "cup_eq", "amount": 2.23903451216323, "valueType": "Amount"}, 
                {"code": "G_NWHL", "description": "MPED: Number of non-whole grain ounce equivalents", "units": "oz_eq", "amount": 1.9729872302956, "valueType": "Amount"}, 
                {"code": "G_TOTAL", "description": "MPED: Total number of grain ounce equivalents", "units": "oz_eq", "amount": 2.85032356921448, "valueType": "Amount"}, 
                {"code": "G_WHL", "description": "MPED: Number of whole grain ounce equivalents", "units": "oz_eq", "amount": 0.877350918337469, "valueType": "Amount"}, 
                {"code": "LEGUMES", "description": "MPED: Number of cooked dry beans and peas cup equivalents", "units": "cup_eq", "amount": 0.16504833187959, "valueType": "Amount"}, 
                {"code": "M_EGG", "description": "MPED: Oz equivalents of lean meat from eggs", "units": "oz_eq", "amount": 0.596116072112962, "valueType": "Amount"}, 
                {"code": "M_FISH_HI", "description": "MPED: Oz cooked lean meat from fish, other seafood high in Omega-3", "units": "oz_eq", "amount": 1.25571989817162, "valueType": "Amount"}, 
                {"code": "M_FISH_LO", "description": "MPED: Oz cooked lean meat from fish, other seafood low in Omega-3", "units": "oz_eq", "amount": 0.315646376021921, "valueType": "Amount"}, 
                {"code": "M_FRANK", "description": "MPED: Oz cooked lean meat from franks, sausages, luncheon meats", "units": "oz_eq", "amount": 0.0213110342417678, "valueType": "Amount"}, 
                {"code": "M_MEAT", "description": "MPED: Oz cooked lean meat from beef, pork, veal, lamb, and game", "units": "oz_eq", "amount": 1.22173228394495, "valueType": "Amount"}, 
                {"code": "M_MPF", "description": "MPED: Oz cooked lean meat from meat, poultry, fish", "units": "oz_eq", "amount": 3.38365950453771, "valueType": "Amount"}, 
                {"code": "M_NUTSD", "description": "MPED: Oz equivalents of lean meat from nuts and seeds", "units": "oz_eq", "amount": 1.17397021879419, "valueType": "Amount"}, 
                {"code": "M_ORGAN", "description": "MPED: Oz cooked lean meat from organ meats", "units": "oz_eq", "amount": 0.0, "valueType": "Amount"}, 
                {"code": "M_POULT", "description": "MPED: Oz cooked lean meat from chicken, poultry, and other poultry", "units": "oz_eq", "amount": 0.569249912810652, "valueType": "Amount"}, 
                {"code": "M_SOY", "description": "MPED: Oz equivalents of lean meat from soy product", "units": "oz_eq", "amount": 0.412878942543725, "valueType": "Amount"}, 
                {"code": "rgrain", "description": "Refined Grains (ounce equivalents)", "units": "oz_eq", "amount": 0.793014689448736, "valueType": "Amount"}, 
                {"code": "tgrain", "description": "Total Grains (ounce equivalents)", "units": "oz_eq", "amount": 2.88646006412213, "valueType": "Amount"}, 
                {"code": "V_DRKGR", "description": "MPED: Number of dark-green vegetable cup equivalents", "units": "cup_eq", "amount": 1.66142555338475, "valueType": "Amount"}, 
                {"code": "V_ORANGE", "description": "MPED: Number of orange vegetable cup equivalents", "units": "cup_eq", "amount": 0.689578429247855, "valueType": "Amount"}, 
                {"code": "V_OTHER", "description": "MPED: Number of other vegetable cup equivalents", "units": "cup_eq", "amount": 3.63489287499842, "valueType": "Amount"}, 
                {"code": "V_POTATO", "description": "MPED: Number of white potato cup equivalents", "units": "cup_eq", "amount": 0.234652293218325, "valueType": "Amount"}, 
                {"code": "V_STARCY", "description": "MPED: Number of other starchy vegetable cup equivalents", "units": "cup_eq", "amount": 0.149456552349425, "valueType": "Amount"}, 
                {"code": "V_TOMATO", "description": "MPED: Number of tomato cup equivalents", "units": "cup_eq", "amount": 0.564382738025058, "valueType": "Amount"}, 
                {"code": "V_TOTAL", "description": "MPED: Total number of vegetable cup equivalents, excl legumes", "units": "cup_eq", "amount": 6.93453592066051, "valueType": "Amount"}, 
                {"code": "wgrain", "description": "Whole Grains (ounce equivalents)", "units": "oz_eq", "amount": 2.09344536626343, "valueType": "Amount"}
            ]
} 

VIOSCREEN_MPEDS = VioscreenMPeds.from_vioscreen(MP_DATA)



class TestMPedsRepo(unittest.TestCase):

    def test_insert_mpeds_does_not_exist(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenMPedsRepo(t)
            obs = r.insert_mpeds(VIOSCREEN_MPEDS)
            self.assertEqual(obs, 40)

    def test_get_mpeds_exists(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenMPedsRepo(t)
            r.insert_mpeds(VIOSCREEN_MPEDS)
            obs = r.get_mpeds(VIOSCREEN_MPEDS.sessionId)
            self.assertEqual(obs, VIOSCREEN_MPEDS)

    def test_get_mpeds_does_not_exist(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenMPedsRepo(t)
            obs = r.get_mpeds('does not exist')
            self.assertEqual(obs, None)


if __name__ == '__main__':
    unittest.main()
