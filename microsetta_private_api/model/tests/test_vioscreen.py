import unittest
import pandas as pd
from microsetta_private_api.model.vioscreen import VioscreenSession, VioscreenPercentEnergy, VioscreenPercentEnergyComponent

USERS_DATA = [
    {"id": 14129, "guid": "E4A6C3CA-6BDE-4497-B8CE-182E5EA2FAF3", "username": "80043f5209506497", "email": "", "subjectId": "", "firstname": "NOT", "middlename": "", "lastname": "IDENTIFIED",
        "dateOfBirth": "1/1/1800", "activityLevel": "Unknown", "gender": "Female", "height": None, "weight": None, "displayUnits": "Standard", "timeZone": "Eastern Standard Time", "created": "2014-10-08T21:55:07.687"},
    {"id": 14488, "guid": "482DCB5D-4D50-4D77-981B-C4EF590945E4", "username": "77db08e51211d7e3", "email": "", "subjectId": "", "firstname": "NOT", "middlename": "", "lastname": "IDENTIFIED",
        "dateOfBirth": "1/1/1800", "activityLevel": "Unknown", "gender": "Female", "height": None, "weight": None, "displayUnits": "Standard", "timeZone": "Eastern Standard Time", "created": "2014-11-09T04:06:43.287"},
    {"id": 16820, "guid": "546A78A2-D90E-489F-91A4-851CA28F7BA2", "username": "e67bb86b387953d4", "email": "", "subjectId": "", "firstname": "NOT", "middlename": "", "lastname": "IDENTIFIED",
        "dateOfBirth": "1/1/1800", "activityLevel": "Unknown", "gender": "Female", "height": None, "weight": None, "displayUnits": "Standard", "timeZone": "Eastern Standard Time", "created": "2015-01-10T09:39:05.493"},
    {"id": 20599, "guid": "1A31DB14-5B5D-4AE7-9FA2-315DE6BEE9B8", "username": "b81d9f26c289fe0f", "email": "", "subjectId": "", "firstname": "NOT", "middlename": "", "lastname": "IDENTIFIED",
        "dateOfBirth": "1/1/1800", "activityLevel": "Unknown", "gender": "Female", "height": None, "weight": None, "displayUnits": "Standard", "timeZone": "Eastern Standard Time", "created": "2015-09-03T00:50:19.797"},
    {"id": 22352, "guid": "2E5D275B-B9A1-406C-A146-27C97DE54F85", "username": "16a8d5d0834461fe", "email": "", "subjectId": "", "firstname": "NOT", "middlename": "", "lastname": "IDENTIFIED",
        "dateOfBirth": "1/1/1800", "activityLevel": "Unknown", "gender": "Female", "height": None, "weight": None, "displayUnits": "Standard", "timeZone": "Eastern Standard Time", "created": "2015-11-17T12:04:53.56"},
]

SESSIONS_DATA = [
    {"id": 22352, "sessionId": "000ada854d4f45f5abda90ccade7f0a8", "userId": 14129, "username": "80043f5209506497", "userGuid": "E4A6C3CA-6BDE-4497-B8CE-182E5EA2FAF3", "organizationId": 160, "protocolId": 344, "description": "Knight Lab, University of Colorado Boulder", "visitNumber": 1, "status": "Finished",
        "startDate": "2014-10-08T21:55:12.747", "endDate": "2014-10-08T21:57:07.503", "age": 214, "height": None, "weight": None, "gender": "Female", "plStatus": "NotSet", "activityLevel": "Unknown", "displayUnits": "Standard", "cultureCode": "en-US", "created": "2014-10-08T21:55:07.96", "modified": "2017-07-29T06:56:04.22"},
    {"id": 22747, "sessionId": "01013a5b4fa243a3b94db37f41ab4589", "userId": 14488, "username": "77db08e51211d7e3", "userGuid": "482DCB5D-4D50-4D77-981B-C4EF590945E4", "organizationId": 160, "protocolId": 344, "description": "Knight Lab, University of Colorado Boulder", "visitNumber": 1, "status": "Finished",
        "startDate": "2014-11-09T04:06:57.237", "endDate": "2014-11-09T04:18:22.65", "age": 214, "height": None, "weight": None, "gender": "Female", "plStatus": "NotSet", "activityLevel": "Unknown", "displayUnits": "Standard", "cultureCode": "en-US", "created": "2014-11-09T04:06:43.5", "modified": "2017-07-29T06:44:07.817"},
    {"id": 25201, "sessionId": "010d7e02c6d242d29426992eb5be487f", "userId": 16820, "username": "e67bb86b387953d4", "userGuid": "546A78A2-D90E-489F-91A4-851CA28F7BA2", "organizationId": 160, "protocolId": 344, "description": "Knight Lab, University of Colorado Boulder", "visitNumber": 1, "status": "Finished",
        "startDate": "2015-01-10T09:39:35.19", "endDate": "2015-01-10T10:25:52.607", "age": 215, "height": None, "weight": None, "gender": "Female", "plStatus": "NotSet", "activityLevel": "Unknown", "displayUnits": "Standard", "cultureCode": "en-US", "created": "2015-01-10T09:39:06.187", "modified": "2017-07-29T05:38:41.857"},
    {"id": 29506, "sessionId": "00737d1b445547ffa180aac38c19e18b", "userId": 20599, "username": "b81d9f26c289fe0f", "userGuid": "1A31DB14-5B5D-4AE7-9FA2-315DE6BEE9B8", "organizationId": 160, "protocolId": 344, "description": "Knight Lab, University of Colorado Boulder", "visitNumber": 1, "status": "Started",
        "startDate": "2015-09-03T00:51:59.993", "endDate": None, "age": 215, "height": None, "weight": None, "gender": "Female", "plStatus": "NotSet", "activityLevel": "Unknown", "displayUnits": "Standard", "cultureCode": "en-US", "created": "2015-09-03T00:50:19.887", "modified": "2016-06-16T10:17:57.86"},
    {"id": 31381, "sessionId": "0126a1104e434cd88bcff3e3ffb23c9a", "userId": 22352, "username": "16a8d5d0834461fe", "userGuid": "2E5D275B-B9A1-406C-A146-27C97DE54F85", "organizationId": 160, "protocolId": 344, "description": "Knight Lab, University of Colorado Boulder", "visitNumber": 1, "status": "Finished",
        "startDate": "2015-11-17T12:05:14.757", "endDate": "2015-11-17T12:24:35.723", "age": 215, "height": None, "weight": None, "gender": "Female", "plStatus": "NotSet", "activityLevel": "Unknown", "displayUnits": "Standard", "cultureCode": "en-US", "created": "2015-11-17T12:04:53.623", "modified": "2017-07-29T03:47:03.423"},
]


class SessionsTestCase(unittest.TestCase):

    def test_from_vioscreen(self):
        exp = [
            VioscreenSession(sessionId="000ada854d4f45f5abda90ccade7f0a8", username="80043f5209506497", protocolId=344, status="Finished", startDate=pd.to_datetime("2014-10-08T18:55:12.747").tz_localize('US/Pacific'), endDate=pd.to_datetime(
                "2014-10-08T18:57:07.503").tz_localize('US/Pacific'), cultureCode="en-US", created=pd.to_datetime("2014-10-08T18:55:07.96").tz_localize('US/Pacific'), modified=pd.to_datetime("2017-07-29T03:56:04.22").tz_localize('US/Pacific')),
            VioscreenSession(sessionId="01013a5b4fa243a3b94db37f41ab4589", username="77db08e51211d7e3", protocolId=344, status="Finished", startDate=pd.to_datetime("2014-11-09T01:06:57.237").tz_localize('US/Pacific'), endDate=pd.to_datetime(
                "2014-11-09T01:18:22.65").tz_localize('US/Pacific'), cultureCode="en-US", created=pd.to_datetime("2014-11-09T01:06:43.5").tz_localize('US/Pacific'), modified=pd.to_datetime("2017-07-29T03:44:07.817").tz_localize('US/Pacific')),
            VioscreenSession(sessionId="010d7e02c6d242d29426992eb5be487f", username="e67bb86b387953d4", protocolId=344, status="Finished", startDate=pd.to_datetime("2015-01-10T06:39:35.19").tz_localize('US/Pacific'), endDate=pd.to_datetime(
                "2015-01-10T7:25:52.607").tz_localize('US/Pacific'), cultureCode="en-US", created=pd.to_datetime("2015-01-10T06:39:06.187").tz_localize('US/Pacific'), modified=pd.to_datetime("2017-07-29T02:38:41.857").tz_localize('US/Pacific')),
            VioscreenSession(sessionId="00737d1b445547ffa180aac38c19e18b", username="b81d9f26c289fe0f", protocolId=344, status="Started", startDate=pd.to_datetime("2015-09-02T21:51:59.993").tz_localize(
                'US/Pacific'), endDate=None, cultureCode="en-US", created=pd.to_datetime("2015-09-02T21:50:19.887").tz_localize('US/Pacific'), modified=pd.to_datetime("2016-06-16T7:17:57.86").tz_localize('US/Pacific')),
            VioscreenSession(sessionId="0126a1104e434cd88bcff3e3ffb23c9a", username="16a8d5d0834461fe", protocolId=344, status="Finished", startDate=pd.to_datetime("2015-11-17T9:05:14.757").tz_localize('US/Pacific'), endDate=pd.to_datetime(
                "2015-11-17T9:24:35.723").tz_localize('US/Pacific'), cultureCode="en-US", created=pd.to_datetime("2015-11-17T9:04:53.623").tz_localize('US/Pacific'), modified=pd.to_datetime("2017-07-29T00:47:03.423").tz_localize('US/Pacific'))
        ]
        for e, sessions_data in zip(exp, SESSIONS_DATA):
            users_data = [obj for obj in USERS_DATA if obj['username']
                          == sessions_data['username']][0]
            obs = VioscreenSession.from_vioscreen(sessions_data, users_data)
            self.assertEqual(e.__dict__, obs.__dict__)

            
PE_DATA = [
    {"sessionId": "0087da64cdcb41ad800c23531d1198f2", "calculations": [
        {"code": "%protein", "description": "Percent of calories from Protein", "shortDescription": "Protein",
            "units": "%", "amount": 14.50362489752287, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%fat", "description": "Percent of calories from Fat", "shortDescription": "Fat", "units": "%",
         "amount": 35.5233111996746, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%carbo", "description": "Percent of calories from Carbohydrate", "shortDescription": "Carbohydrate",
         "units": "%", "amount": 42.67319895276668, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%alcohol", "description": "Percent of calories from Alcohol", "shortDescription": "Alcohol",
         "units": "%", "amount": 7.299864950035845, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%sfatot", "description": "Percent of calories from Saturated Fat", "shortDescription": "Saturated Fat",
         "units": "%", "amount": 8.953245015317886, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%mfatot", "description": "Percent of calories from Monounsaturated Fat", "shortDescription": "Monounsaturated Fat",
         "units": "%", "amount": 16.04143105742606, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%pfatot", "description": "Percent of calories from Polyunsaturated Fat", "shortDescription": "Polyunsaturated Fat",
         "units": "%", "amount": 9.3864628707637, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%adsugtot", "description": "Percent of calories from Added Sugar", "shortDescription": "Added Sugar",
         "units": "%", "amount": 5.59094160186449, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None}
    ]},
    {},
    {"sessionId": "005eae45652f4aef9880502a08139155", "calculations": [
        {"code": "%protein", "description": "Percent of calories from Protein", "shortDescription": "Protein",
            "units": "%", "amount": 14.858749639268694, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%fat", "description": "Percent of calories from Fat", "shortDescription": "Fat", "units": "%",
         "amount": 30.167126097771146, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%carbo", "description": "Percent of calories from Carbohydrate", "shortDescription": "Carbohydrate",
         "units": "%", "amount": 54.9666593467124, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%alcohol", "description": "Percent of calories from Alcohol", "shortDescription": "Alcohol",
         "units": "%", "amount": 0.007464916247760429, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%sfatot", "description": "Percent of calories from Saturated Fat", "shortDescription": "Saturated Fat",
         "units": "%", "amount": 9.854668486202778, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%mfatot", "description": "Percent of calories from Monounsaturated Fat", "shortDescription": "Monounsaturated Fat",
         "units": "%", "amount": 10.408216625871315, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%pfatot", "description": "Percent of calories from Polyunsaturated Fat", "shortDescription": "Polyunsaturated Fat",
         "units": "%", "amount": 8.446574429213285, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%adsugtot", "description": "Percent of calories from Added Sugar", "shortDescription": "Added Sugar",
         "units": "%", "amount": 1.9479807882340903, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None}
    ]},
    {"sessionId": "00d3616753e04a5bab52d972ad936251", "calculations": [
        {"code": "%protein", "description": "Percent of calories from Protein", "shortDescription": "Protein",
            "units": "%", "amount": 14.101114742737353, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%fat", "description": "Percent of calories from Fat", "shortDescription": "Fat", "units": "%",
         "amount": 44.47945688205364, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%carbo", "description": "Percent of calories from Carbohydrate", "shortDescription": "Carbohydrate",
         "units": "%", "amount": 41.17906211247171, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%alcohol", "description": "Percent of calories from Alcohol", "shortDescription": "Alcohol",
         "units": "%", "amount": 0.24036626273729872, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%sfatot", "description": "Percent of calories from Saturated Fat", "shortDescription": "Saturated Fat",
         "units": "%", "amount": 23.027133054230525, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%mfatot", "description": "Percent of calories from Monounsaturated Fat", "shortDescription": "Monounsaturated Fat",
         "units": "%", "amount": 13.51630871254169, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%pfatot", "description": "Percent of calories from Polyunsaturated Fat", "shortDescription": "Polyunsaturated Fat",
         "units": "%", "amount": 5.9299567345449065, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%adsugtot", "description": "Percent of calories from Added Sugar", "shortDescription": "Added Sugar",
         "units": "%", "amount": 3.822618465270744, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None}
    ]},
    {"sessionId": "00c41c34403c4899a9e01d455403114b", "calculations": [
        {"code": "%protein", "description": "Percent of calories from Protein", "shortDescription": "Protein",
            "units": "%", "amount": 11.819810934852827, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%fat", "description": "Percent of calories from Fat", "shortDescription": "Fat", "units": "%",
         "amount": 24.245658148606022, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%carbo", "description": "Percent of calories from Carbohydrate", "shortDescription": "Carbohydrate",
         "units": "%", "amount": 63.93251457857734, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%alcohol", "description": "Percent of calories from Alcohol", "shortDescription": "Alcohol",
         "units": "%", "amount": 0.002016337963813013, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%sfatot", "description": "Percent of calories from Saturated Fat", "shortDescription": "Saturated Fat",
         "units": "%", "amount": 6.376076974314159, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%mfatot", "description": "Percent of calories from Monounsaturated Fat", "shortDescription": "Monounsaturated Fat",
         "units": "%", "amount": 8.978058847621535, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%pfatot", "description": "Percent of calories from Polyunsaturated Fat", "shortDescription": "Polyunsaturated Fat",
         "units": "%", "amount": 8.05870871265928, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None},
        {"code": "%adsugtot", "description": "Percent of calories from Added Sugar", "shortDescription": "Added Sugar", 
         "units": "%", "amount": 3.8946426170304487, "precision": 0, "foodComponentType": 1, "foodDataDefinition": None}]}
]


class PercentEnergyTestCase(unittest.TestCase):

    def test_from_vioscreen(self):
        PE_DATA2 = [obj for obj in PE_DATA if bool(obj) == True]

        exp = [
            VioscreenPercentEnergy(sessionId="0087da64cdcb41ad800c23531d1198f2", energy_components=[
                VioscreenPercentEnergyComponent(code="%protein", description="Percent of calories from Protein",
                                                short_description="Protein", units="%", amount=14.50362489752287),
                VioscreenPercentEnergyComponent(code="%fat", description="Percent of calories from Fat",
                                                short_description="Fat", units="%", amount=35.5233111996746),
                VioscreenPercentEnergyComponent(code="%carbo", description="Percent of calories from Carbohydrate",
                                                short_description="Carbohydrate", units="%", amount=42.67319895276668),
                VioscreenPercentEnergyComponent(code="%alcohol", description="Percent of calories from Alcohol",
                                                short_description="Alcohol", units="%", amount=7.299864950035845),
                VioscreenPercentEnergyComponent(code="%sfatot", description="Percent of calories from Saturated Fat",
                                                short_description="Saturated Fat", units="%", amount=8.953245015317886),
                VioscreenPercentEnergyComponent(code="%mfatot", description="Percent of calories from Monounsaturated Fat",
                                                short_description="Monounsaturated Fat", units="%", amount=16.04143105742606),
                VioscreenPercentEnergyComponent(code="%pfatot", description="Percent of calories from Polyunsaturated Fat",
                                                short_description="Polyunsaturated Fat", units="%", amount=9.3864628707637),
                VioscreenPercentEnergyComponent(code="%adsugtot", description="Percent of calories from Added Sugar",
                                                short_description="Added Sugar", units="%", amount=5.59094160186449)
            ]),
            VioscreenPercentEnergy(sessionId="005eae45652f4aef9880502a08139155", energy_components=[
                VioscreenPercentEnergyComponent(code="%protein", description="Percent of calories from Protein",
                                                short_description="Protein", units="%", amount=14.858749639268694),
                VioscreenPercentEnergyComponent(code="%fat", description="Percent of calories from Fat",
                                                short_description="Fat", units="%", amount=30.167126097771146),
                VioscreenPercentEnergyComponent(code="%carbo", description="Percent of calories from Carbohydrate",
                                                short_description="Carbohydrate", units="%", amount=54.9666593467124),
                VioscreenPercentEnergyComponent(code="%alcohol", description="Percent of calories from Alcohol",
                                                short_description="Alcohol", units="%", amount=0.007464916247760429),
                VioscreenPercentEnergyComponent(code="%sfatot", description="Percent of calories from Saturated Fat",
                                                short_description="Saturated Fat", units="%", amount=9.854668486202778),
                VioscreenPercentEnergyComponent(code="%mfatot", description="Percent of calories from Monounsaturated Fat",
                                                short_description="Monounsaturated Fat", units="%", amount=10.408216625871315),
                VioscreenPercentEnergyComponent(code="%pfatot", description="Percent of calories from Polyunsaturated Fat",
                                                short_description="Polyunsaturated Fat", units="%", amount=8.446574429213285),
                VioscreenPercentEnergyComponent(code="%adsugtot", description="Percent of calories from Added Sugar",
                                                short_description="Added Sugar", units="%", amount=1.9479807882340903)
            ]),
            VioscreenPercentEnergy(sessionId="00d3616753e04a5bab52d972ad936251", energy_components=[
                VioscreenPercentEnergyComponent(code="%protein", description="Percent of calories from Protein",
                                                short_description="Protein", units="%", amount=14.101114742737353),
                VioscreenPercentEnergyComponent(code="%fat", description="Percent of calories from Fat",
                                                short_description="Fat", units="%", amount=44.47945688205364),
                VioscreenPercentEnergyComponent(code="%carbo", description="Percent of calories from Carbohydrate",
                                                short_description="Carbohydrate", units="%", amount=41.17906211247171),
                VioscreenPercentEnergyComponent(code="%alcohol", description="Percent of calories from Alcohol",
                                                short_description="Alcohol", units="%", amount=0.24036626273729872),
                VioscreenPercentEnergyComponent(code="%sfatot", description="Percent of calories from Saturated Fat",
                                                short_description="Saturated Fat", units="%", amount=23.027133054230525),
                VioscreenPercentEnergyComponent(code="%mfatot", description="Percent of calories from Monounsaturated Fat",
                                                short_description="Monounsaturated Fat", units="%", amount=13.51630871254169),
                VioscreenPercentEnergyComponent(code="%pfatot", description="Percent of calories from Polyunsaturated Fat",
                                                short_description="Polyunsaturated Fat", units="%", amount=5.9299567345449065),
                VioscreenPercentEnergyComponent(code="%adsugtot", description="Percent of calories from Added Sugar",
                                                short_description="Added Sugar", units="%", amount=3.822618465270744)
            ]),
            VioscreenPercentEnergy(sessionId="00c41c34403c4899a9e01d455403114b", energy_components=[
                VioscreenPercentEnergyComponent(code="%protein", description="Percent of calories from Protein",
                                                short_description="Protein", units="%", amount=11.819810934852827),
                VioscreenPercentEnergyComponent(code="%fat", description="Percent of calories from Fat",
                                                short_description="Fat", units="%", amount=24.245658148606022),
                VioscreenPercentEnergyComponent(code="%carbo", description="Percent of calories from Carbohydrate",
                                                short_description="Carbohydrate", units="%", amount=63.93251457857734),
                VioscreenPercentEnergyComponent(code="%alcohol", description="Percent of calories from Alcohol",
                                                short_description="Alcohol", units="%", amount=0.002016337963813013),
                VioscreenPercentEnergyComponent(code="%sfatot", description="Percent of calories from Saturated Fat",
                                                short_description="Saturated Fat", units="%", amount=6.376076974314159),
                VioscreenPercentEnergyComponent(code="%mfatot", description="Percent of calories from Monounsaturated Fat",
                                                short_description="Monounsaturated Fat", units="%", amount=8.978058847621535),
                VioscreenPercentEnergyComponent(code="%pfatot", description="Percent of calories from Polyunsaturated Fat",
                                                short_description="Polyunsaturated Fat", units="%", amount=8.05870871265928),
                VioscreenPercentEnergyComponent(code="%adsugtot", description="Percent of calories from Added Sugar",
                                                short_description="Added Sugar", units="%", amount=3.8946426170304487)
            ])
        ]

        for e, pe_data in zip(exp, PE_DATA2):
            obs = VioscreenPercentEnergy.from_vioscreen(pe_data)
            self.assertEqual(e.sessionId, obs.sessionId)
            for e_obj, obs_obj in zip(e.energy_components, obs.energy_components):
                self.assertEqual(e_obj.__dict__, obs_obj.__dict__)


if __name__ == '__main__':
    unittest.main()
