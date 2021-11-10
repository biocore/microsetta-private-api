import unittest
import pandas as pd
import json
import pkg_resources
from microsetta_private_api.model.vioscreen import (
    VioscreenSession,
    VioscreenPercentEnergyComponent, VioscreenPercentEnergy,
    VioscreenDietaryScoreComponent, VioscreenDietaryScore,
    VioscreenSupplementsComponent, VioscreenSupplements,
    VioscreenFoodComponentsComponent, VioscreenFoodComponents,
    VioscreenEatingPatternsComponent, VioscreenEatingPatterns,
    VioscreenMPedsComponent, VioscreenMPeds,
    VioscreenFoodConsumptionComponent, VioscreenFoodConsumption,
    VioscreenComposite
)


package = 'microsetta_private_api'

def get_data_path(filename):
    return pkg_resources.resource_filename(package,
                                           'model/tests/data/%s' % filename)


class SessionsTestCase(unittest.TestCase):

    def test_from_vioscreen(self):
        # a little helper method to simplify expected object instantiation
        def norm(ts):
            return pd.to_datetime(ts).tz_localize('US/Pacific')

        exp = [
            VioscreenSession(sessionId="000ada854d4f45f5abda90ccade7f0a8",
                             username="80043f5209506497",
                             protocolId=344,
                             status="Finished",
                             startDate=norm("2014-10-08T18:55:12.747"),
                             endDate=norm("2014-10-08T18:57:07.503"),
                             cultureCode="en-US",
                             created=norm("2014-10-08T18:55:07.96"),
                             modified=norm("2017-07-29T03:56:04.22")),
            VioscreenSession(sessionId="01013a5b4fa243a3b94db37f41ab4589",
                             username="77db08e51211d7e3",
                             protocolId=344,
                             status="Finished",
                             startDate=norm("2014-11-09T01:06:57.237"),
                             endDate=norm("2014-11-09T01:18:22.65"),
                             cultureCode="en-US",
                             created=norm("2014-11-09T01:06:43.5"),
                             modified=norm("2017-07-29T03:44:07.817")),
            VioscreenSession(sessionId="010d7e02c6d242d29426992eb5be487f",
                             username="e67bb86b387953d4",
                             protocolId=344,
                             status="Finished",
                             startDate=norm("2015-01-10T06:39:35.19"),
                             endDate=norm("2015-01-10T7:25:52.607"),
                             cultureCode="en-US",
                             created=norm("2015-01-10T06:39:06.187"),
                             modified=norm("2017-07-29T02:38:41.857")),
            VioscreenSession(sessionId="00737d1b445547ffa180aac38c19e18b",
                             username="b81d9f26c289fe0f",
                             protocolId=344,
                             status="Started",
                             startDate=norm("2015-09-02T21:51:59.993"),
                             endDate=None,
                             cultureCode="en-US",
                             created=norm("2015-09-02T21:50:19.887"),
                             modified=norm("2016-06-16T7:17:57.86")),
            VioscreenSession(sessionId="0126a1104e434cd88bcff3e3ffb23c9a",
                             username="16a8d5d0834461fe",
                             protocolId=344,
                             status="Finished",
                             startDate=norm("2015-11-17T9:05:14.757"),
                             endDate=norm("2015-11-17T9:24:35.723"),
                             cultureCode="en-US",
                             created=norm("2015-11-17T9:04:53.623"),
                             modified=norm("2017-07-29T00:47:03.423"))
        ]

        USERS_DATA = []
        SESSIONS_DATA = []

        with open(get_data_path("users.data")) as data:
            USERS_DATA = json.load(data)

        with open(get_data_path("sessions.data")) as data:
            SESSIONS_DATA = json.load(data)

        for e, sessions_data in zip(exp, SESSIONS_DATA):
            users_data = [obj for obj in USERS_DATA if obj['username']
                          == sessions_data['username']][0]
            obs = VioscreenSession.from_vioscreen(sessions_data, users_data)
            self.assertEqual(e.__dict__, obs.__dict__)


class PercentEnergyTestCase(unittest.TestCase):

    def test_from_vioscreen(self):
        exp = [
            VioscreenPercentEnergy(
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
                ]),
            None,
            VioscreenPercentEnergy(
                sessionId="005eae45652f4aef9880502a08139155",
                energy_components=[
                    VioscreenPercentEnergyComponent(code="%protein",
                                                    description="Percent of calories from Protein",  # noqa
                                                    short_description="Protein",  # noqa
                                                    units="%",
                                                    amount=14.858749639268694),
                    VioscreenPercentEnergyComponent(code="%fat",
                                                    description="Percent of calories from Fat",  # noqa
                                                    short_description="Fat",
                                                    units="%",
                                                    amount=30.167126097771146),
                    VioscreenPercentEnergyComponent(code="%carbo",
                                                    description="Percent of calories from Carbohydrate",  # noqa
                                                    short_description="Carbohydrate",  # noqa
                                                    units="%",
                                                    amount=54.9666593467124),
                    VioscreenPercentEnergyComponent(code="%alcohol",
                                                    description="Percent of calories from Alcohol",  # noqa
                                                    short_description="Alcohol",  # noqa
                                                    units="%",
                                                    amount=0.007464916247760429),  # noqa
                    VioscreenPercentEnergyComponent(code="%sfatot",
                                                    description="Percent of calories from Saturated Fat",  # noqa
                                                    short_description="Saturated Fat",  # noqa
                                                    units="%",
                                                    amount=9.854668486202778),
                    VioscreenPercentEnergyComponent(code="%mfatot",
                                                    description="Percent of calories from Monounsaturated Fat",  # noqa
                                                    short_description="Monounsaturated Fat",  # noqa
                                                    units="%",
                                                    amount=10.408216625871315),
                    VioscreenPercentEnergyComponent(code="%pfatot",
                                                    description="Percent of calories from Polyunsaturated Fat",  # noqa
                                                    short_description="Polyunsaturated Fat",  # noqa
                                                    units="%",
                                                    amount=8.446574429213285),
                    VioscreenPercentEnergyComponent(code="%adsugtot",
                                                    description="Percent of calories from Added Sugar",  # noqa
                                                    short_description="Added Sugar",  # noqa
                                                    units="%",
                                                    amount=1.9479807882340903)
                ]),
            VioscreenPercentEnergy(
                sessionId="00d3616753e04a5bab52d972ad936251",
                energy_components=[
                    VioscreenPercentEnergyComponent(code="%protein",
                                                    description="Percent of calories from Protein",  # noqa
                                                    short_description="Protein",  # noqa
                                                    units="%",
                                                    amount=14.101114742737353),
                    VioscreenPercentEnergyComponent(code="%fat",
                                                    description="Percent of calories from Fat",  # noqa
                                                    short_description="Fat",
                                                    units="%",
                                                    amount=44.47945688205364),
                    VioscreenPercentEnergyComponent(code="%carbo",
                                                    description="Percent of calories from Carbohydrate",  # noqa
                                                    short_description="Carbohydrate",  # noqa
                                                    units="%",
                                                    amount=41.17906211247171),
                    VioscreenPercentEnergyComponent(code="%alcohol",
                                                    description="Percent of calories from Alcohol",  # noqa
                                                    short_description="Alcohol",  # noqa
                                                    units="%",
                                                    amount=0.24036626273729872),  # noqa
                    VioscreenPercentEnergyComponent(code="%sfatot",
                                                    description="Percent of calories from Saturated Fat",  # noqa
                                                    short_description="Saturated Fat",  # noqa
                                                    units="%",
                                                    amount=23.027133054230525),
                    VioscreenPercentEnergyComponent(code="%mfatot",
                                                    description="Percent of calories from Monounsaturated Fat",  # noqa
                                                    short_description="Monounsaturated Fat",  # noqa
                                                    units="%",
                                                    amount=13.51630871254169),
                    VioscreenPercentEnergyComponent(code="%pfatot",
                                                    description="Percent of calories from Polyunsaturated Fat",  # noqa
                                                    short_description="Polyunsaturated Fat",  # noqa
                                                    units="%",
                                                    amount=5.9299567345449065),
                    VioscreenPercentEnergyComponent(code="%adsugtot",
                                                    description="Percent of calories from Added Sugar",  # noqa
                                                    short_description="Added Sugar",  # noqa
                                                    units="%",
                                                    amount=3.822618465270744)
                ]),
            VioscreenPercentEnergy(
                sessionId="00c41c34403c4899a9e01d455403114b",
                energy_components=[
                    VioscreenPercentEnergyComponent(code="%protein",
                                                    description="Percent of calories from Protein",  # noqa
                                                    short_description="Protein",  # noqa
                                                    units="%",
                                                    amount=11.819810934852827),
                    VioscreenPercentEnergyComponent(code="%fat",
                                                    description="Percent of calories from Fat",  # noqa
                                                    short_description="Fat",
                                                    units="%",
                                                    amount=24.245658148606022),
                    VioscreenPercentEnergyComponent(code="%carbo",
                                                    description="Percent of calories from Carbohydrate",  # noqa
                                                    short_description="Carbohydrate",  # noqa
                                                    units="%",
                                                    amount=63.93251457857734),
                    VioscreenPercentEnergyComponent(code="%alcohol",
                                                    description="Percent of calories from Alcohol",  # noqa
                                                    short_description="Alcohol",  # noqa
                                                    units="%",
                                                    amount=0.002016337963813013),  # noqa
                    VioscreenPercentEnergyComponent(code="%sfatot",
                                                    description="Percent of calories from Saturated Fat",  # noqa
                                                    short_description="Saturated Fat",  # noqa
                                                    units="%",
                                                    amount=6.376076974314159),
                    VioscreenPercentEnergyComponent(code="%mfatot",
                                                    description="Percent of calories from Monounsaturated Fat",  # noqa
                                                    short_description="Monounsaturated Fat",  # noqa
                                                    units="%",
                                                    amount=8.978058847621535),
                    VioscreenPercentEnergyComponent(code="%pfatot",
                                                    description="Percent of calories from Polyunsaturated Fat",  # noqa
                                                    short_description="Polyunsaturated Fat",  # noqa
                                                    units="%",
                                                    amount=8.05870871265928),
                    VioscreenPercentEnergyComponent(code="%adsugtot",
                                                    description="Percent of calories from Added Sugar",  # noqa
                                                    short_description="Added Sugar",  # noqa
                                                    units="%",
                                                    amount=3.8946426170304487)
                ])
        ]

        PE_DATA = []

        with open(get_data_path("percentenergy.data")) as data:
            PE_DATA = json.load(data)

        for e, pe_data in zip(exp, PE_DATA):
            if not pe_data:
                continue

            obs = VioscreenPercentEnergy.from_vioscreen(pe_data)
            self.assertEqual(e.sessionId, obs.sessionId)
            for e_obj, obs_obj in zip(e.energy_components,
                                      obs.energy_components):
                self.assertEqual(e_obj.__dict__, obs_obj.__dict__)


class DietaryScoreTestCase(unittest.TestCase):
    # flake8: noqa: E501
    def test_from_vioscreen(self):
        exp = VioscreenDietaryScore(sessionId="0087da64cdcb41ad800c23531d1198f2",
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

        DS_DATA = []

        with open(get_data_path("dietaryscores.data")) as data:
            DS_DATA = json.load(data)

        obs = VioscreenDietaryScore.from_vioscreen(DS_DATA[0])
        self.assertEqual(exp.sessionId, obs.sessionId)
        self.assertEqual(exp.scoresType, obs.scoresType)
        for exp_obj, obs_obj in zip(exp.scores,
                                    obs.scores):
            self.assertEqual(exp_obj.code, obs_obj.code)


class SupplementsTestCase(unittest.TestCase):
    def test_from_vioscreen(self):
        exp = VioscreenSupplements(
            sessionId="005eae45652f4aef9880502a08139155",
            supplements_components=[
                VioscreenSupplementsComponent(
                    supplement="MultiVitamin",
                    frequency="7",
                    amount="200",
                    average="200"),
                VioscreenSupplementsComponent(
                    supplement="Calcium",
                    frequency="",
                    amount="",
                    average="")])

        SUPPLEMENTS_DATA = []

        with open(get_data_path("supplements.data")) as data:
            SUPPLEMENTS_DATA = json.load(data)

        obs = VioscreenSupplements.from_vioscreen(SUPPLEMENTS_DATA[2])
        self.assertEqual(exp.sessionId, obs.sessionId)
        for exp_obj, obs_obj in zip(exp.supplements_components,
                                    obs.supplements_components):
            self.assertEqual(exp_obj.__dict__, obs_obj.__dict__)


class FoodComponentsTestCase(unittest.TestCase):
    def test_from_vioscreen(self):
        exp = VioscreenFoodComponents(
            sessionId="0087da64cdcb41ad800c23531d1198f2",
            components=[
                VioscreenFoodComponentsComponent(code="acesupot",
                                                 description="Acesulfame Potassium",
                                                 units="mg",
                                                 amount=0.0,
                                                 valueType="Amount")
            ]
        )

        FC_DATA = []

        with open(get_data_path("foodcomponents.data")) as data:
            FC_DATA = json.load(data)

        obs = VioscreenFoodComponents.from_vioscreen(FC_DATA[0])
        self.assertEqual(exp.sessionId, obs.sessionId)
        exp_obj = exp.components[0]
        obs_obj = obs.components[0]
        self.assertEqual(exp_obj.__dict__, obs_obj.__dict__)


class EatingPatternsTestCase(unittest.TestCase):
    def test_from_vioscreen(self):
        exp = VioscreenEatingPatterns(
            sessionId="0087da64cdcb41ad800c23531d1198f2",
            components=[
                VioscreenEatingPatternsComponent(code="ADDEDFATS",
                                                 description="Eating Pattern",
                                                 units="PerDay",
                                                 amount=8.07030444201639,
                                                 valueType="Amount")
            ]
        )

        EP_DATA = []

        with open(get_data_path("eatingpatterns.data")) as data:
            EP_DATA = json.load(data)

        obs = VioscreenEatingPatterns.from_vioscreen(EP_DATA[0])
        self.assertEqual(exp.sessionId, obs.sessionId)
        exp_obj = exp.components[0]
        obs_obj = obs.components[0]
        self.assertEqual(exp_obj.__dict__, obs_obj.__dict__)


class MPedsTestCase(unittest.TestCase):
    def test_from_vioscreen(self):
        exp = VioscreenMPeds(
            sessionId="0087da64cdcb41ad800c23531d1198f2",
            components=[
                VioscreenMPedsComponent(code="A_BEV",
                                        description="MPED: Total drinks of alcohol",
                                        units="alc_drinks",
                                        amount=1.30647563412786,
                                        valueType="Amount")
            ]
        )

        MPEDS_DATA = []

        with open(get_data_path("mpeds.data")) as data:
            MPEDS_DATA = json.load(data)

        obs = VioscreenMPeds.from_vioscreen(MPEDS_DATA[0])
        self.assertEqual(exp.sessionId, obs.sessionId)
        exp_obj = exp.components[0]
        obs_obj = obs.components[0]
        self.assertEqual(exp_obj.__dict__, obs_obj.__dict__)


class FoodConsumptionTestCase(unittest.TestCase):
    def test_from_vioscreen(self):
        exp = VioscreenFoodConsumption(
            sessionId="0087da64cdcb41ad800c23531d1198f2",
            components=[
                VioscreenFoodConsumptionComponent(
                    foodCode="20001",
                    description="Apples, applesauce and pears",
                    foodGroup="Fruits",
                    amount=1.0,
                    frequency=28,
                    consumptionAdjustment=1.58695652173913,
                    servingSizeText="1 apple or pear, 1/2 cup",
                    servingFrequencyText="2-3 per month",
                    created="2017-07-29T02:02:54.72",
                    data=[
                        VioscreenFoodComponentsComponent(code="acesupot",
                                                         description="Acesulfame Potassium",
                                                         units="mg",
                                                         amount=0.0,
                                                         valueType="Amount")
                    ]
                )
            ]
        )

        CONS_DATA = []

        with open(get_data_path("foodconsumption.data")) as data:
            CONS_DATA = json.load(data)

        obs = VioscreenFoodConsumption.from_vioscreen(CONS_DATA)
        self.assertEqual(exp.sessionId, obs.sessionId)
        exp_obj = exp.components[0].data[0]
        obs_obj = obs.components[0].data[0]
        self.assertEqual(exp_obj.__dict__, obs_obj.__dict__)


if __name__ == '__main__':
    unittest.main()
