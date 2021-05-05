import unittest
from microsetta_private_api.model.vioscreen import (
    VioscreenSession, VioscreenDietaryScore, 
    VioscreenDietaryScoreComponent)
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import (
    VioscreenSessionRepo, VioscreenDietaryScoreRepo)
from datetime import datetime

def _to_dt(mon, day, year):
    return datetime(month=mon, day=day, year=year)

VIOSCREEN_SESSION = VioscreenSession(sessionId='0087da64cdcb41ad800c23531d1198f2',
                                     username='a user',
                                     protocolId=1234,
                                     status='something',
                                     startDate=_to_dt(1, 1, 1970),
                                     endDate=None,
                                     cultureCode='foo',
                                     created=_to_dt(1, 1, 1970),
                                     modified=_to_dt(1, 1, 1970))

VIOSCREEN_DIETARY_SCORE = exp = VioscreenDietaryScore(sessionId="0087da64cdcb41ad800c23531d1198f2",
                                    scoresType="Hei2010",
                                    scores=[VioscreenDietaryScoreComponent(code="TotalVegetables",
                                                                           name="",
                                                                           score=0,
                                                                           lowerLimit=0,
                                                                           upperLimit=0),
                                            VioscreenDietaryScoreComponent(code="GreensAndBeans",
                                                                           name="",
                                                                           score=0,
                                                                           lowerLimit=0,
                                                                           upperLimit=0),
                                            VioscreenDietaryScoreComponent(code="TotalFruit",
                                                                           name="",
                                                                           score=0,
                                                                           lowerLimit=0,
                                                                           upperLimit=0),
                                            VioscreenDietaryScoreComponent(code="WholeFruit",
                                                                           name="",
                                                                           score=0,
                                                                           lowerLimit=0,
                                                                           upperLimit=0),
                                            VioscreenDietaryScoreComponent(code="WholeGrains",
                                                                           name="",
                                                                           score=0,
                                                                           lowerLimit=0,
                                                                           upperLimit=0),
                                            VioscreenDietaryScoreComponent(code="Dairy",
                                                                           name="",
                                                                           score=0,
                                                                           lowerLimit=0,
                                                                           upperLimit=0),
                                            VioscreenDietaryScoreComponent(code="TotalProteins",
                                                                           name="",
                                                                           score=0,
                                                                           lowerLimit=0,
                                                                           upperLimit=0),
                                            VioscreenDietaryScoreComponent(code="SeafoodAndPlantProteins",
                                                                           name="",
                                                                           score=0,
                                                                           lowerLimit=0,
                                                                           upperLimit=0),
                                            VioscreenDietaryScoreComponent(code="FattyAcids",
                                                                           name="",
                                                                           score=0,
                                                                           lowerLimit=0,
                                                                           upperLimit=0),
                                            VioscreenDietaryScoreComponent(code="RefinedGrains",
                                                                           name="",
                                                                           score=0,
                                                                           lowerLimit=0,
                                                                           upperLimit=0),
                                            VioscreenDietaryScoreComponent(code="Sodium",
                                                                           name="",
                                                                           score=0,
                                                                           lowerLimit=0,
                                                                           upperLimit=0),
                                            VioscreenDietaryScoreComponent(code="EmptyCalories",
                                                                           name="",
                                                                           score=0,
                                                                           lowerLimit=0,
                                                                           upperLimit=0),
                                            VioscreenDietaryScoreComponent(code="TotalScore",
                                                                           name="",
                                                                           score=0,
                                                                           lowerLimit=0,
                                                                           upperLimit=0)
                                            ])

class TestDietaryScoreRepo(unittest.TestCase):
    def test_insert_dietary_score_exists(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenDietaryScoreRepo(t)
            r.insert_dietary_score(VIOSCREEN_DIETARY_SCORE)
            obs = r.insert_dietary_score(VIOSCREEN_DIETARY_SCORE)
            self.assertEqual(obs, 0)

    def test_insert_dietary_score_does_not_exist(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenDietaryScoreRepo(t)
            obs = r.insert_dietary_score(VIOSCREEN_DIETARY_SCORE)
            self.assertEqual(obs, 8)

    def test_get_dietary_score_exists(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenDietaryScoreRepo(t)
            r.insert_dietary_score(VIOSCREEN_DIETARY_SCORE)
            obs = r.get_dietary_score(VIOSCREEN_DIETARY_SCORE.sessionId)
            self.assertEqual(obs, VIOSCREEN_DIETARY_SCORE)

    def test_get_dietary_score_does_not_exist(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenDietaryScoreRepo(t)
            obs = r.get_dietary_score('does not exist')
            self.assertEqual(obs, None)

if __name__ == '__main__':
    unittest.main()