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


VIOSCREEN_SESSION = VioscreenSession(sessionId='0087da64cdcb41ad800c23531d1198f2',  # noqa
                                     username='a user',
                                     protocolId=1234,
                                     status='something',
                                     startDate=_to_dt(1, 1, 1970),
                                     endDate=None,
                                     cultureCode='foo',
                                     created=_to_dt(1, 1, 1970),
                                     modified=_to_dt(1, 1, 1970))

VIOSCREEN_DIETARY_SCORE = VioscreenDietaryScore(
    sessionId="0087da64cdcb41ad800c23531d1198f2",
    scoresType="Hei2010",
    scores=[VioscreenDietaryScoreComponent(code="TotalVegetables",
                                           name="Total Vegetables",
                                           score=1,
                                           lowerLimit=0.0,
                                           upperLimit=5.0),
            VioscreenDietaryScoreComponent(code="GreensAndBeans",
                                           name="Greens and Beans",
                                           score=2,
                                           lowerLimit=0.0,
                                           upperLimit=5.0),
            VioscreenDietaryScoreComponent(code="TotalFruit",
                                           name="Total Fruit",
                                           score=3,
                                           lowerLimit=0.0,
                                           upperLimit=5.0),
            VioscreenDietaryScoreComponent(code="WholeFruit",
                                           name="Whole Fruit",
                                           score=4,
                                           lowerLimit=0.0,
                                           upperLimit=5.0),
            VioscreenDietaryScoreComponent(code="WholeGrains",
                                           name="Whole Grains",
                                           score=5,
                                           lowerLimit=0.0,
                                           upperLimit=10.0),
            VioscreenDietaryScoreComponent(code="Dairy",
                                           name="Dairy",
                                           score=6,
                                           lowerLimit=0.0,
                                           upperLimit=10.0),
            VioscreenDietaryScoreComponent(code="TotalProteins",
                                           name="Total Protein Foods",
                                           score=7,
                                           lowerLimit=0.0,
                                           upperLimit=5.0),
            VioscreenDietaryScoreComponent(code="SeafoodAndPlantProteins",
                                           name="Seafood and Plant Proteins",
                                           score=8,
                                           lowerLimit=0.0,
                                           upperLimit=5.0),
            VioscreenDietaryScoreComponent(code="FattyAcids",
                                           name="Fatty Acids",
                                           score=9,
                                           lowerLimit=0.0,
                                           upperLimit=10.0),
            VioscreenDietaryScoreComponent(code="RefinedGrains",
                                           name="Refined Grains",
                                           score=10,
                                           lowerLimit=0.0,
                                           upperLimit=10.0),
            VioscreenDietaryScoreComponent(code="Sodium",
                                           name="Sodium",
                                           score=11,
                                           lowerLimit=0.0,
                                           upperLimit=10.0),
            VioscreenDietaryScoreComponent(code="EmptyCalories",
                                           name="Empty Calories",
                                           score=12,
                                           lowerLimit=0.0,
                                           upperLimit=20.0),
            VioscreenDietaryScoreComponent(code="TotalScore",
                                           name="Total HEI Score",
                                           score=13,
                                           lowerLimit=0.0,
                                           upperLimit=100.0)
            ]
)


class TestDietaryScoreRepo(unittest.TestCase):
    def test_insert_dietary_score_does_not_exist(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenDietaryScoreRepo(t)
            obs = r.insert_dietary_scores([VIOSCREEN_DIETARY_SCORE, ])
            self.assertEqual(obs, 13)

    def test_get_dietary_scores_exists(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenDietaryScoreRepo(t)
            r.insert_dietary_scores([VIOSCREEN_DIETARY_SCORE, ])
            obs = r.get_dietary_scores(VIOSCREEN_DIETARY_SCORE.sessionId)
            self.assertEqual(obs, [VIOSCREEN_DIETARY_SCORE, ])

    def test_get_dietary_scores_does_not_exist(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenDietaryScoreRepo(t)
            obs = r.get_dietary_scores('does not exist')
            self.assertEqual(obs, None)


if __name__ == '__main__':
    unittest.main()
