import unittest
import pandas as pd
from microsetta_private_api.model.vioscreen import (
    VioscreenSession,
    VioscreenPercentEnergyComponent, VioscreenPercentEnergy,
    VioscreenDietaryScoreComponent, VioscreenDietaryScore,
    VioscreenSupplementsComponent, VioscreenSupplements,
    VioscreenComposite
)

USERS_DATA = [
    {
        "id": 14129,
        "guid": "E4A6C3CA-6BDE-4497-B8CE-182E5EA2FAF3",
        "username": "80043f5209506497",
        "email": "",
        "subjectId": "",
        "firstname": "NOT",
        "middlename": "",
        "lastname": "IDENTIFIED",
        "dateOfBirth": "1/1/1800",
        "activityLevel": "Unknown",
        "gender": "Female",
        "height": None,
        "weight": None,
        "displayUnits": "Standard",
        "timeZone": "Eastern Standard Time",
        "created": "2014-10-08T21:55:07.687"
    },
    {
        "id": 14488,
        "guid": "482DCB5D-4D50-4D77-981B-C4EF590945E4",
        "username": "77db08e51211d7e3",
        "email": "",
        "subjectId": "",
        "firstname": "NOT",
        "middlename": "",
        "lastname": "IDENTIFIED",
        "dateOfBirth": "1/1/1800",
        "activityLevel": "Unknown",
        "gender": "Female",
        "height": None,
        "weight": None,
        "displayUnits": "Standard",
        "timeZone": "Eastern Standard Time",
        "created": "2014-11-09T04:06:43.287"
    },
    {
        "id": 16820,
        "guid": "546A78A2-D90E-489F-91A4-851CA28F7BA2",
        "username": "e67bb86b387953d4",
        "email": "",
        "subjectId": "",
        "firstname": "NOT",
        "middlename": "",
        "lastname": "IDENTIFIED",
        "dateOfBirth": "1/1/1800",
        "activityLevel": "Unknown",
        "gender": "Female",
        "height": None,
        "weight": None,
        "displayUnits": "Standard",
        "timeZone": "Eastern Standard Time",
        "created": "2015-01-10T09:39:05.493"
    },
    {
        "id": 20599,
        "guid": "1A31DB14-5B5D-4AE7-9FA2-315DE6BEE9B8",
        "username": "b81d9f26c289fe0f",
        "email": "",
        "subjectId": "",
        "firstname": "NOT",
        "middlename": "",
        "lastname": "IDENTIFIED",
        "dateOfBirth": "1/1/1800",
        "activityLevel": "Unknown",
        "gender": "Female",
        "height": None,
        "weight": None,
        "displayUnits": "Standard",
        "timeZone": "Eastern Standard Time",
        "created": "2015-09-03T00:50:19.797"
    },
    {
        "id": 22352,
        "guid": "2E5D275B-B9A1-406C-A146-27C97DE54F85",
        "username": "16a8d5d0834461fe",
        "email": "",
        "subjectId": "",
        "firstname": "NOT",
        "middlename": "",
        "lastname": "IDENTIFIED",
        "dateOfBirth": "1/1/1800",
        "activityLevel": "Unknown",
        "gender": "Female",
        "height": None,
        "weight": None,
        "displayUnits": "Standard",
        "timeZone": "Eastern Standard Time",
        "created": "2015-11-17T12:04:53.56"
    }
]


SESSIONS_DATA = [
    {
        "id": 22352,
        "sessionId": "000ada854d4f45f5abda90ccade7f0a8",
        "userId": 14129,
        "username": "80043f5209506497",
        "userGuid": "E4A6C3CA-6BDE-4497-B8CE-182E5EA2FAF3",
        "organizationId": 160,
        "protocolId": 344,
        "description": "Knight Lab, University of Colorado Boulder",
        "visitNumber": 1,
        "status": "Finished",
        "startDate": "2014-10-08T21:55:12.747",
        "endDate": "2014-10-08T21:57:07.503",
        "age": 214,
        "height": None,
        "weight": None,
        "gender": "Female",
        "plStatus": "NotSet",
        "activityLevel": "Unknown",
        "displayUnits": "Standard",
        "cultureCode": "en-US",
        "created": "2014-10-08T21:55:07.96",
        "modified": "2017-07-29T06:56:04.22"
    },
    {
        "id": 22747,
        "sessionId": "01013a5b4fa243a3b94db37f41ab4589",
        "userId": 14488,
        "username": "77db08e51211d7e3",
        "userGuid": "482DCB5D-4D50-4D77-981B-C4EF590945E4",
        "organizationId": 160,
        "protocolId": 344,
        "description": "Knight Lab, University of Colorado Boulder",
        "visitNumber": 1,
        "status": "Finished",
        "startDate": "2014-11-09T04:06:57.237",
        "endDate": "2014-11-09T04:18:22.65",
        "age": 214,
        "height": None,
        "weight": None,
        "gender": "Female",
        "plStatus": "NotSet",
        "activityLevel": "Unknown",
        "displayUnits": "Standard",
        "cultureCode": "en-US",
        "created": "2014-11-09T04:06:43.5",
        "modified": "2017-07-29T06:44:07.817"
    },
    {
        "id": 25201,
        "sessionId": "010d7e02c6d242d29426992eb5be487f",
        "userId": 16820,
        "username": "e67bb86b387953d4",
        "userGuid": "546A78A2-D90E-489F-91A4-851CA28F7BA2",
        "organizationId": 160,
        "protocolId": 344,
        "description": "Knight Lab, University of Colorado Boulder",
        "visitNumber": 1,
        "status": "Finished",
        "startDate": "2015-01-10T09:39:35.19",
        "endDate": "2015-01-10T10:25:52.607",
        "age": 215,
        "height": None,
        "weight": None,
        "gender": "Female",
        "plStatus": "NotSet",
        "activityLevel": "Unknown",
        "displayUnits": "Standard",
        "cultureCode": "en-US",
        "created": "2015-01-10T09:39:06.187",
        "modified": "2017-07-29T05:38:41.857"
    },
    {
        "id": 29506,
        "sessionId": "00737d1b445547ffa180aac38c19e18b",
        "userId": 20599,
        "username": "b81d9f26c289fe0f",
        "userGuid": "1A31DB14-5B5D-4AE7-9FA2-315DE6BEE9B8",
        "organizationId": 160,
        "protocolId": 344,
        "description": "Knight Lab, University of Colorado Boulder",
        "visitNumber": 1,
        "status": "Started",
        "startDate": "2015-09-03T00:51:59.993",
        "endDate": None,
        "age": 215,
        "height": None,
        "weight": None,
        "gender": "Female",
        "plStatus": "NotSet",
        "activityLevel": "Unknown",
        "displayUnits": "Standard",
        "cultureCode": "en-US",
        "created": "2015-09-03T00:50:19.887",
        "modified": "2016-06-16T10:17:57.86"
    },
    {
        "id": 31381,
        "sessionId": "0126a1104e434cd88bcff3e3ffb23c9a",
        "userId": 22352,
        "username": "16a8d5d0834461fe",
        "userGuid": "2E5D275B-B9A1-406C-A146-27C97DE54F85",
        "organizationId": 160,
        "protocolId": 344,
        "description": "Knight Lab, University of Colorado Boulder",
        "visitNumber": 1,
        "status": "Finished",
        "startDate": "2015-11-17T12:05:14.757",
        "endDate": "2015-11-17T12:24:35.723",
        "age": 215,
        "height": None,
        "weight": None,
        "gender": "Female",
        "plStatus": "NotSet",
        "activityLevel": "Unknown",
        "displayUnits": "Standard",
        "cultureCode": "en-US",
        "created": "2015-11-17T12:04:53.623",
        "modified": "2017-07-29T03:47:03.423"
    }
]


PE_DATA = [
    {
        "sessionId": "0087da64cdcb41ad800c23531d1198f2",
        "calculations": [
            {
                "code": "%protein",
                "description": "Percent of calories from Protein",
                "shortDescription": "Protein",
                "units": "%",
                "amount": 14.50362489752287,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%fat",
                "description": "Percent of calories from Fat",
                "shortDescription": "Fat",
                "units": "%",
                "amount": 35.5233111996746,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%carbo",
                "description": "Percent of calories from Carbohydrate",
                "shortDescription": "Carbohydrate",
                "units": "%",
                "amount": 42.67319895276668,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%alcohol",
                "description": "Percent of calories from Alcohol",
                "shortDescription": "Alcohol",
                "units": "%",
                "amount": 7.299864950035845,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%sfatot",
                "description": "Percent of calories from Saturated Fat",
                "shortDescription": "Saturated Fat",
                "units": "%",
                "amount": 8.953245015317886,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%mfatot",
                "description": "Percent of calories from Monounsaturated Fat",
                "shortDescription": "Monounsaturated Fat",
                "units": "%",
                "amount": 16.04143105742606,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%pfatot",
                "description": "Percent of calories from Polyunsaturated Fat",
                "shortDescription": "Polyunsaturated Fat",
                "units": "%",
                "amount": 9.3864628707637,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%adsugtot",
                "description": "Percent of calories from Added Sugar",
                "shortDescription": "Added Sugar",
                "units": "%",
                "amount": 5.59094160186449,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            }
        ]
    },
    {},
    {
        "sessionId": "005eae45652f4aef9880502a08139155",
        "calculations": [
            {
                "code": "%protein",
                "description": "Percent of calories from Protein",
                "shortDescription": "Protein",
                "units": "%",
                "amount": 14.858749639268694,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%fat",
                "description": "Percent of calories from Fat",
                "shortDescription": "Fat",
                "units": "%",
                "amount": 30.167126097771146,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%carbo",
                "description": "Percent of calories from Carbohydrate",
                "shortDescription": "Carbohydrate",
                "units": "%",
                "amount": 54.9666593467124,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%alcohol",
                "description": "Percent of calories from Alcohol",
                "shortDescription": "Alcohol",
                "units": "%",
                "amount": 0.007464916247760429,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%sfatot",
                "description": "Percent of calories from Saturated Fat",
                "shortDescription": "Saturated Fat",
                "units": "%",
                "amount": 9.854668486202778,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%mfatot",
                "description": "Percent of calories from Monounsaturated Fat",
                "shortDescription": "Monounsaturated Fat",
                "units": "%",
                "amount": 10.408216625871315,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%pfatot",
                "description": "Percent of calories from Polyunsaturated Fat",
                "shortDescription": "Polyunsaturated Fat",
                "units": "%",
                "amount": 8.446574429213285,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%adsugtot",
                "description": "Percent of calories from Added Sugar",
                "shortDescription": "Added Sugar",
                "units": "%",
                "amount": 1.9479807882340903,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            }
        ]
    },
    {
        "sessionId": "00d3616753e04a5bab52d972ad936251",
        "calculations": [
            {
                "code": "%protein",
                "description": "Percent of calories from Protein",
                "shortDescription": "Protein",
                "units": "%",
                "amount": 14.101114742737353,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%fat",
                "description": "Percent of calories from Fat",
                "shortDescription": "Fat",
                "units": "%",
                "amount": 44.47945688205364,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%carbo",
                "description": "Percent of calories from Carbohydrate",
                "shortDescription": "Carbohydrate",
                "units": "%",
                "amount": 41.17906211247171,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%alcohol",
                "description": "Percent of calories from Alcohol",
                "shortDescription": "Alcohol",
                "units": "%",
                "amount": 0.24036626273729872,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%sfatot",
                "description": "Percent of calories from Saturated Fat",
                "shortDescription": "Saturated Fat",
                "units": "%",
                "amount": 23.027133054230525,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%mfatot",
                "description": "Percent of calories from Monounsaturated Fat",
                "shortDescription": "Monounsaturated Fat",
                "units": "%",
                "amount": 13.51630871254169,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%pfatot",
                "description": "Percent of calories from Polyunsaturated Fat",
                "shortDescription": "Polyunsaturated Fat",
                "units": "%",
                "amount": 5.9299567345449065,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%adsugtot",
                "description": "Percent of calories from Added Sugar",
                "shortDescription": "Added Sugar",
                "units": "%",
                "amount": 3.822618465270744,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            }
        ]
    },
    {
        "sessionId": "00c41c34403c4899a9e01d455403114b",
        "calculations": [
            {
                "code": "%protein",
                "description": "Percent of calories from Protein",
                "shortDescription": "Protein",
                "units": "%",
                "amount": 11.819810934852827,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%fat",
                "description": "Percent of calories from Fat",
                "shortDescription": "Fat",
                "units": "%",
                "amount": 24.245658148606022,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%carbo",
                "description": "Percent of calories from Carbohydrate",
                "shortDescription": "Carbohydrate",
                "units": "%",
                "amount": 63.93251457857734,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%alcohol",
                "description": "Percent of calories from Alcohol",
                "shortDescription": "Alcohol",
                "units": "%",
                "amount": 0.002016337963813013,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%sfatot",
                "description": "Percent of calories from Saturated Fat",
                "shortDescription": "Saturated Fat",
                "units": "%",
                "amount": 6.376076974314159,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%mfatot",
                "description": "Percent of calories from Monounsaturated Fat",
                "shortDescription": "Monounsaturated Fat",
                "units": "%",
                "amount": 8.978058847621535,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%pfatot",
                "description": "Percent of calories from Polyunsaturated Fat",
                "shortDescription": "Polyunsaturated Fat",
                "units": "%",
                "amount": 8.05870871265928,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            },
            {
                "code": "%adsugtot",
                "description": "Percent of calories from Added Sugar",
                "shortDescription": "Added Sugar",
                "units": "%",
                "amount": 3.8946426170304487,
                "precision": 0,
                "foodComponentType": 1,
                "foodDataDefinition": None
            }
        ]
    }
]

DS_DATA = [
    {"sessionId": "0087da64cdcb41ad800c23531d1198f2",
        "dietaryScore": {
            "type": "Hei2010",
            "scores": [
                {"type": "TotalVegetables",
                 "name": "Total Vegetables", "score": 5.0,
                 "lowerLimit": 0.0, "upperLimit": 5.0},
                {"type": "GreensAndBeans", "name": "Greens and Beans",
                 "score": 5.0, "lowerLimit": 0.0, "upperLimit": 5.0},
                {"type": "TotalFruit", "name": "Total Fruit",
                 "score": 5.0, "lowerLimit": 0.0, "upperLimit": 5.0},
                {"type": "WholeFruit", "name": "Whole Fruit",
                 "score": 5.0, "lowerLimit": 0.0, "upperLimit": 5.0},
                {"type": "WholeGrains", "name": "Whole Grains",
                 "score": 3.235287086290936, "lowerLimit": 0.0,
                 "upperLimit": 10.0},
                {"type": "Dairy", "name": "Dairy",
                 "score": 1.5506188406057975, "lowerLimit": 0.0,
                 "upperLimit": 10.0},
                {"type": "TotalProteins", "name": "Total Protein Foods",
                 "score": 5.0, "lowerLimit": 0.0, "upperLimit": 5.0},
                {"type": "SeafoodAndPlantProteins",
                 "name": "Seafood and Plant Proteins", "score": 5.0,
                 "lowerLimit": 0.0, "upperLimit": 5.0},
                {"type": "FattyAcids", "name": "Fatty Acids",
                 "score": 10.0, "lowerLimit": 0.0, "upperLimit": 10.0},
                {"type": "RefinedGrains", "name": "Refined Grains",
                 "score": 10.0, "lowerLimit": 0.0, "upperLimit": 10.0},
                {"type": "Sodium", "name": "Sodium",
                 "score": 1.5957926627133845, "lowerLimit": 0.0,
                 "upperLimit": 10.0},
                {"type": "EmptyCalories", "name": "Empty Calories",
                 "score": 20.0, "lowerLimit": 0.0, "upperLimit": 20.0},
                {"type": "TotalScore", "name": "Total HEI Score",
                 "score": 76.38169858961012, "lowerLimit": 0.0,
                 "upperLimit": 100.0}
            ]}},
    {"sessionId": "00e381e946a04693bbc7ab8b830700e9",
        "dietaryScore": {"type": "Hei2010",
                         "scores": []}},
    {"sessionId": "005eae45652f4aef9880502a08139155",
        "dietaryScore": {"type": "Hei2010",
                         "scores": []}},
    {"sessionId": "00d3616753e04a5bab52d972ad936251",
        "dietaryScore": {
            "type": "Hei2010",
            "scores": [
                {"type": "TotalVegetables", "name": "Total Vegetables",
                 "score": 5.0, "lowerLimit": 0.0, "upperLimit": 5.0},
                {"type": "GreensAndBeans", "name": "Greens and Beans",
                 "score": 5.0, "lowerLimit": 0.0, "upperLimit": 5.0},
                {"type": "TotalFruit", "name": "Total Fruit",
                 "score": 4.514409456498512, "lowerLimit": 0.0,
                 "upperLimit": 5.0},
                {"type": "WholeFruit", "name": "Whole Fruit",
                 "score": 5.0, "lowerLimit": 0.0, "upperLimit": 5.0},
                {"type": "WholeGrains", "name": "Whole Grains",
                 "score": 2.536107209734357, "lowerLimit": 0.0,
                 "upperLimit": 10.0},
                {"type": "Dairy", "name": "Dairy",
                 "score": 8.324808489520159, "lowerLimit": 0.0,
                 "upperLimit": 10.0},
                {"type": "TotalProteins", "name": "Total Protein Foods",
                 "score": 4.0614596268108425, "lowerLimit": 0.0,
                 "upperLimit": 5.0},
                {"type": "SeafoodAndPlantProteins",
                 "name": "Seafood and Plant Proteins",
                 "score": 3.823510929287682, "lowerLimit": 0.0,
                 "upperLimit": 5.0},
                {"type": "FattyAcids", "name": "Fatty Acids",
                 "score": 0.0, "lowerLimit": 0.0, "upperLimit": 10.0},
                {"type": "RefinedGrains", "name": "Refined Grains",
                 "score": 10.0, "lowerLimit": 0.0, "upperLimit": 10.0},
                {"type": "Sodium", "name": "Sodium",
                 "score": 3.45530630018148, "lowerLimit": 0.0,
                 "upperLimit": 10.0},
                {"type": "EmptyCalories", "name": "Empty Calories",
                 "score": 8.01530811516409, "lowerLimit": 0.0,
                 "upperLimit": 20.0},
                {"type": "TotalScore", "name": "Total HEI Score",
                 "score": 59.73091012719712, "lowerLimit": 0.0,
                 "upperLimit": 100.0}
            ]
        }
     },
    {"sessionId": "004c7bec8c904a76bfc5c2f65a33637b",
        "dietaryScore": {"type": "Hei2010",
                         "scores": [

                         ]
                         }
     },
    {"sessionId": "00c41c34403c4899a9e01d455403114b",
        "dietaryScore": {"type": "Hei2010",
                         "scores": [
                             {"type": "TotalVegetables",
                                 "name": "Total Vegetables", "score": 5.0,
                              "lowerLimit": 0.0, "upperLimit": 5.0},
                             {"type": "GreensAndBeans",
                                 "name": "Greens and Beans", "score": 5.0,
                                 "lowerLimit": 0.0, "upperLimit": 5.0},
                             {"type": "TotalFruit", "name": "Total Fruit",
                                 "score": 5.0, "lowerLimit": 0.0,
                                 "upperLimit": 5.0},
                             {"type": "WholeFruit", "name": "Whole Fruit",
                                 "score": 5.0, "lowerLimit": 0.0,
                                 "upperLimit": 5.0},
                             {"type": "WholeGrains", "name": "Whole Grains",
                                 "score": 2.6106043404217867,
                                 "lowerLimit": 0.0,
                                 "upperLimit": 10.0},
                             {"type": "Dairy", "name": "Dairy",
                                 "score": 0.8732242861213225,
                                 "lowerLimit": 0.0,
                                 "upperLimit": 10.0},
                             {"type": "TotalProteins",
                                 "name": "Total Protein Foods", "score": 5.0,
                                 "lowerLimit": 0.0, "upperLimit": 5.0},
                             {"type": "SeafoodAndPlantProteins",
                                 "name": "Seafood and Plant Proteins",
                                 "score": 5.0, "lowerLimit": 0.0,
                                 "upperLimit": 5.0},
                             {"type": "FattyAcids", "name": "Fatty Acids",
                                 "score": 10.0, "lowerLimit": 0.0,
                                 "upperLimit": 10.0},
                             {"type": "RefinedGrains",
                                 "name": "Refined Grains",
                                 "score": 10.0, "lowerLimit": 0.0,
                                 "upperLimit": 10.0},
                             {"type": "Sodium", "name": "Sodium",
                                 "score": 0.0, "lowerLimit": 0.0,
                                 "upperLimit": 10.0},
                             {"type": "EmptyCalories",
                                 "name": "Empty Calories", "score": 20.0,
                                 "lowerLimit": 0.0, "upperLimit": 20.0},
                             {"type": "TotalScore",
                                 "name": "Total HEI Score",
                                 "score": 73.4838286265431, "lowerLimit": 0.0,
                                 "upperLimit": 100.0}
                         ]
                         }
     },
    {"sessionId": "0003765db07940849b2461b3a058ffba",
        "dietaryScore": {"type": "Hei2010",
                         "scores": [
                             {"type": "TotalVegetables",
                                 "name": "Total Vegetables",
                                 "score": 5.0, "lowerLimit": 0.0,
                                 "upperLimit": 5.0},
                             {"type": "GreensAndBeans",
                                 "name": "Greens and Beans",
                                 "score": 5.0, "lowerLimit": 0.0,
                                 "upperLimit": 5.0},
                             {"type": "TotalFruit", "name": "Total Fruit",
                                 "score": 5.0, "lowerLimit": 0.0,
                                 "upperLimit": 5.0},
                             {"type": "WholeFruit", "name": "Whole Fruit",
                                 "score": 5.0, "lowerLimit": 0.0,
                                 "upperLimit": 5.0},
                             {"type": "WholeGrains", "name": "Whole Grains",
                                 "score": 10.0, "lowerLimit": 0.0,
                                 "upperLimit": 10.0},
                             {"type": "Dairy", "name": "Dairy",
                                 "score": 8.172197818970483, "lowerLimit": 0.0,
                                 "upperLimit": 10.0},
                             {"type": "TotalProteins",
                                 "name": "Total Protein Foods", "score": 5.0,
                                 "lowerLimit": 0.0, "upperLimit": 5.0},
                             {"type": "SeafoodAndPlantProteins",
                                 "name": "Seafood and Plant Proteins",
                                 "score": 5.0, "lowerLimit": 0.0,
                                 "upperLimit": 5.0},
                             {"type": "FattyAcids", "name": "Fatty Acids",
                                 "score": 4.1785984635140165,
                                 "lowerLimit": 0.0,
                                 "upperLimit": 10.0},
                             {"type": "RefinedGrains",
                                 "name": "Refined Grains",
                                 "score": 10.0, "lowerLimit": 0.0,
                                 "upperLimit": 10.0},
                             {"type": "Sodium", "name": "Sodium",
                                 "score": 2.1833892942459188,
                                 "lowerLimit": 0.0,
                                 "upperLimit": 10.0},
                             {"type": "EmptyCalories",
                                 "name": "Empty Calories",
                                 "score": 18.281526358473315,
                                 "lowerLimit": 0.0,
                                 "upperLimit": 20.0},
                             {"type": "TotalScore", "name": "Total HEI Score",
                                 "score": 82.81571193520372, "lowerLimit": 0.0,
                                 "upperLimit": 100.0}
                         ]
                         }
     },
    {"sessionId": "005e14983cc646ca8707c2984ed88930",
        "dietaryScore": {"type": "Hei2010",
                         "scores": [
                             {"type": "TotalVegetables",
                                 "name": "Total Vegetables", "score": 5.0,
                                 "lowerLimit": 0.0, "upperLimit": 5.0},
                             {"type": "GreensAndBeans",
                                 "name": "Greens and Beans", "score": 5.0,
                                 "lowerLimit": 0.0, "upperLimit": 5.0},
                             {"type": "TotalFruit", "name": "Total Fruit",
                                 "score": 5.0, "lowerLimit": 0.0,
                                 "upperLimit": 5.0},
                             {"type": "WholeFruit", "name": "Whole Fruit",
                                 "score": 5.0, "lowerLimit": 0.0,
                                 "upperLimit": 5.0},
                             {"type": "WholeGrains", "name": "Whole Grains",
                                 "score": 4.179046594884575, "lowerLimit": 0.0,
                                 "upperLimit": 10.0},
                             {"type": "Dairy", "name": "Dairy",
                                 "score": 9.087068693664271, "lowerLimit": 0.0,
                                 "upperLimit": 10.0},
                             {"type": "TotalProteins",
                                 "name": "Total Protein Foods", "score": 5.0,
                                 "lowerLimit": 0.0, "upperLimit": 5.0},
                             {"type": "SeafoodAndPlantProteins",
                                 "name": "Seafood and Plant Proteins",
                                 "score": 4.8355282284562, "lowerLimit": 0.0,
                                 "upperLimit": 5.0},
                             {"type": "FattyAcids", "name": "Fatty Acids",
                                 "score": 0.17405159461471115,
                                 "lowerLimit": 0.0,
                                 "upperLimit": 10.0},
                             {"type": "RefinedGrains",
                                 "name": "Refined Grains",
                                 "score": 9.375886827256924, "lowerLimit": 0.0,
                                 "upperLimit": 10.0},
                             {"type": "Sodium", "name": "Sodium",
                                 "score": 4.304162622077493, "lowerLimit": 0.0,
                                 "upperLimit": 10.0},
                             {"type": "EmptyCalories",
                                 "name": "Empty Calories",
                                 "score": 16.48636959393508, "lowerLimit": 0.0,
                                 "upperLimit": 20.0},
                             {"type": "TotalScore", "name": "Total HEI Score",
                                 "score": 73.44211415488925, "lowerLimit": 0.0,
                                 "upperLimit": 100.0}
                         ]
                         }
     },
    {"sessionId": "00d5c51ef24e410286057f49bd3f36b2",
        "dietaryScore": {"type": "Hei2010",
                         "scores": [

                         ]
                         }
     },
    {"sessionId": "006392a3ce1f419ebbaa12b6a5aaaf49",
        "dietaryScore": {"type": "Hei2010",
                         "scores": [
                             {"type": "TotalVegetables",
                                 "name": "Total Vegetables", "score": 5.0,
                                 "lowerLimit": 0.0, "upperLimit": 5.0},
                             {"type": "GreensAndBeans",
                                 "name": "Greens and Beans", "score": 5.0,
                                 "lowerLimit": 0.0, "upperLimit": 5.0},
                             {"type": "TotalFruit", "name": "Total Fruit",
                                 "score": 1.4283556080637814,
                                 "lowerLimit": 0.0, "upperLimit": 5.0},
                             {"type": "WholeFruit", "name": "Whole Fruit",
                                 "score": 2.8067613352425202,
                                 "lowerLimit": 0.0, "upperLimit": 5.0},
                             {"type": "WholeGrains", "name": "Whole Grains",
                                 "score": 1.8573401523909128,
                                 "lowerLimit": 0.0, "upperLimit": 10.0},
                             {"type": "Dairy", "name": "Dairy",
                                 "score": 7.27077857086018,
                                 "lowerLimit": 0.0, "upperLimit": 10.0},
                             {"type": "TotalProteins",
                                 "name": "Total Protein Foods", "score": 5.0,
                                 "lowerLimit": 0.0, "upperLimit": 5.0},
                             {"type": "SeafoodAndPlantProteins",
                                 "name": "Seafood and Plant Proteins",
                                 "score": 5.0, "lowerLimit": 0.0,
                                 "upperLimit": 5.0},
                             {"type": "FattyAcids", "name": "Fatty Acids",
                                 "score": 4.0905309501780875,
                                 "lowerLimit": 0.0, "upperLimit": 10.0},
                             {"type": "RefinedGrains",
                                 "name": "Refined Grains",
                                 "score": 8.615641107012927,
                                 "lowerLimit": 0.0, "upperLimit": 10.0},
                             {"type": "Sodium", "name": "Sodium",
                                 "score": 4.753580824270443, "lowerLimit": 0.0,
                                 "upperLimit": 10.0},
                             {"type": "EmptyCalories",
                                 "name": "Empty Calories",
                                 "score": 15.394915641340159,
                                 "lowerLimit": 0.0, "upperLimit": 20.0},
                             {"type": "TotalScore", "name": "Total HEI Score",
                                 "score": 66.217904189359, "lowerLimit": 0.0,
                                 "upperLimit": 100.0}
                         ]
                         }
     }
]

SUPPLEMENTS_DATA = [
    {"sessionId": "0087da64cdcb41ad800c23531d1198f2",
        "data": [
            {"supplement": "MultiVitamin", "frequency": "", "amount": "",
                "average": ""},
            {"supplement": "Calcium", "frequency": "", "amount": "",
                "average": ""}
        ]
     },
    {"sessionId": "00e381e946a04693bbc7ab8b830700e9",
        "data": [
            {"supplement": "MultiVitamin", "frequency": "", "amount": "",
                "average": ""},
            {"supplement": "Calcium", "frequency": "", "amount": "",
                "average": ""}
        ]
     },
    {"sessionId": "005eae45652f4aef9880502a08139155",
        "data": [
            {"supplement": "MultiVitamin", "frequency": "7",
                "amount": "200", "average": "200"},
            {"supplement": "Calcium", "frequency": "", "amount": "",
                "average": ""}
        ]
     },
    {"sessionId": "00d3616753e04a5bab52d972ad936251",
        "data": [
            {"supplement": "MultiVitamin", "frequency": "7", "amount": "200",
                "average": "200"},
            {"supplement": "Calcium", "frequency": "", "amount": "",
                "average": ""}
        ]
     },
    {"sessionId": "004c7bec8c904a76bfc5c2f65a33637b",
        "data": [
            {"supplement": "MultiVitamin", "frequency": "", "amount": "",
                "average": ""},
            {"supplement": "Calcium", "frequency": "", "amount": "",
                "average": ""}
        ]
     },
    {"sessionId": "00c41c34403c4899a9e01d455403114b",
        "data": [
            {"supplement": "MultiVitamin", "frequency": "7", "amount": "200",
                "average": "200"},
            {"supplement": "Calcium", "frequency": "", "amount": "",
                "average": ""}
        ]
     },
    {"sessionId": "0003765db07940849b2461b3a058ffba",
        "data": [
            {"supplement": "MultiVitamin",
                "frequency": "Less than once per week",
                "amount": "200", "average": ""},
            {"supplement": "Calcium", "frequency": "", "amount": "",
                "average": ""}
        ]
     },
    {"sessionId": "005e14983cc646ca8707c2984ed88930",
        "data": [
            {"supplement": "MultiVitamin", "frequency": "", "amount": "",
                "average": ""},
            {"supplement": "Calcium", "frequency": "", "amount": "",
                "average": ""}
        ]
     },
    {"sessionId": "00d5c51ef24e410286057f49bd3f36b2",
        "data": [
            {"supplement": "MultiVitamin", "frequency": "", "amount": "",
                "average": ""},
            {"supplement": "Calcium", "frequency": "", "amount": "",
                "average": ""}
        ]
     },
    {"sessionId": "006392a3ce1f419ebbaa12b6a5aaaf49",
        "data": [
            {"supplement": "MultiVitamin", "frequency": "2", "amount": "200",
                "average": "57"},
            {"supplement": "Calcium", "frequency": "", "amount": "",
                "average": ""}
        ]
     }
]


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

        obs = VioscreenSupplements.from_vioscreen(SUPPLEMENTS_DATA[2])
        self.assertEqual(exp.sessionId, obs.sessionId)
        for exp_obj, obs_obj in zip(exp.supplements_components,
                                    obs.supplements_components):
            self.assertEqual(exp_obj.__dict__, obs_obj.__dict__)


class CompositeTestCase(unittest.TestCase):
    def test_constructor(self):
        # fake a cross link in the test data
        session = SESSIONS_DATA[0]
        user = USERS_DATA[0]
        pe_data = PE_DATA[0].copy()
        pe_data["sessionId"] = session["sessionId"]

        vs_session = VioscreenSession.from_vioscreen(session, user)
        vs_pe = VioscreenPercentEnergy.from_vioscreen(pe_data)

        # just exercise the constructor
        VioscreenComposite(vs_session, vs_pe)


if __name__ == '__main__':
    unittest.main()
