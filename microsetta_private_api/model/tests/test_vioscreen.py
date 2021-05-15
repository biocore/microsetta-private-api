import unittest
import pandas as pd
from microsetta_private_api.model.vioscreen import (
    VioscreenSession,
    VioscreenPercentEnergyComponent, VioscreenPercentEnergy,
    VioscreenDietaryScoreComponent, VioscreenDietaryScore,
    VioscreenSupplementsComponent, VioscreenSupplements,
    VioscreenFoodComponentsComponent, VioscreenFoodComponents, 
    VioscreenEatingPatternsComponent, VioscreenEatingPatterns,
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

FC_DATA = [
    {"sessionId": "0087da64cdcb41ad800c23531d1198f2", 
        "data": [
            {"code": "acesupot", "description": "Acesulfame Potassium", "units": "mg", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "addsugar", "description": "Added Sugars (by Available Carbohydrate)", "units": "g", "amount": 29.1398999278022, "valueType": "Amount"}, 
            {"code": "adsugtot", "description": "Added Sugars (by Total Sugars)", "units": "g", "amount": 26.4238145115152, "valueType": "Amount"}, 
            {"code": "alanine", "description": "Alanine", "units": "g", "amount": 3.46104576644763, "valueType": "Amount"}, 
            {"code": "alcohol", "description": "Alcohol", "units": "g", "amount": 19.7145710875844, "valueType": "Amount"}, 
            {"code": "alphacar", "description": "Alpha-Carotene (provitamin A carotenoid)", "units": "mcg", "amount": 2017.53612640666, "valueType": "Amount"}, 
            {"code": "alphtoce", "description": "Total Vitamin E Activity (total alpha-tocopherol equivalents)", "units": "mg", "amount": 15.0707732661311, "valueType": "Amount"}, 
            {"code": "alphtoco", "description": "Alpha-Tocopherol", "units": "mg", "amount": 13.8272044723449, "valueType": "Amount"}, 
            {"code": "arginine", "description": "Arginine", "units": "g", "amount": 4.14062661445974, "valueType": "Amount"}, 
            {"code": "ash", "description": "Ash", "units": "g", "amount": 23.0771349098181, "valueType": "Amount"}, 
            {"code": "aspartam", "description": "Aspartame", "units": "mg", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "aspartic", "description": "Aspartic Acid", "units": "g", "amount": 7.27667761741976, "valueType": "Amount"}, 
            {"code": "avcarb", "description": "Available Carbohydrate", "units": "g", "amount": 165.04306093598, "valueType": "Amount"}, 
            {"code": "betacar", "description": "Beta-Carotene (provitamin A carotenoid)", "units": "mcg", "amount": 20306.1649748484, "valueType": "Amount"}, 
            {"code": "betacryp", "description": "Beta-Cryptoxanthin (provitamin A carotenoid)", "units": "mcg", "amount": 224.279496298639, "valueType": "Amount"}, 
            {"code": "betaine", "description": "Betaine", "units": "mg", "amount": 89.9817930861984, "valueType": "Amount"}, 
            {"code": "betatoco", "description": "Beta-Tocopherol", "units": "mg", "amount": 0.401608555584594, "valueType": "Amount"}, 
            {"code": "biochana", "description": "Biochanin A", "units": "mg", "amount": 0.0179590229570418, "valueType": "Amount"}, 
            {"code": "caffeine", "description": "Caffeine", "units": "mg", "amount": 155.634647911895, "valueType": "Amount"}, 
            {"code": "calcium", "description": "Calcium", "units": "mg", "amount": 787.341607624165, "valueType": "Amount"}, 
            {"code": "calories", "description": "Energy", "units": "kcal", "amount": 1807.87854871802, "valueType": "Amount"}, 
            {"code": "carbo", "description": "Total Carbohydrate", "units": "g", "amount": 201.681357817234, "valueType": "Amount"}, 
            {"code": "cholest", "description": "Cholesterol", "units": "mg", "amount": 216.56098480222, "valueType": "Amount"}, 
            {"code": "choline", "description": "Choline", "units": "g", "amount": 406.767310184525, "valueType": "Amount"}, 
            {"code": "clac9t11", "description": "CLA cis-9, trans-11", "units": "g", "amount": 0.0389142187265189, "valueType": "Amount"}, 
            {"code": "clat10c12", "description": "CLA trans-10, cis-12", "units": "g", "amount": 0.010277897103255, "valueType": "Amount"}, 
            {"code": "copper", "description": "Copper", "units": "mg", "amount": 1.78272620537979, "valueType": "Amount"}, 
            {"code": "coumest", "description": "Coumestrol", "units": "mg", "amount": 0.145742981532413, "valueType": "Amount"}, 
            {"code": "cystine", "description": "Cystine", "units": "g", "amount": 0.86202864047932, "valueType": "Amount"}, 
            {"code": "daidzein", "description": "Daidzein", "units": "mg", "amount": 5.18659457977212, "valueType": "Amount"}, 
            {"code": "delttoco", "description": "Delta-Tocopherol", "units": "mg", "amount": 2.37200624592061, "valueType": "Amount"}, 
            {"code": "erythr", "description": "Erythritol", "units": "g", "amount": 0.00224000001933588, "valueType": "Amount"}, 
            {"code": "fat", "description": "Total Fat", "units": "g", "amount": 74.6176347239974, "valueType": "Amount"}, 
            {"code": "fiber", "description": "Total Dietary Fiber", "units": "g", "amount": 36.6400854150717, "valueType": "Amount"}, 
            {"code": "fibh2o", "description": "Soluble Dietary Fiber", "units": "g", "amount": 9.31264086776921, "valueType": "Amount"}, 
            {"code": "fibinso", "description": "Insoluble Dietary Fiber", "units": "g", "amount": 27.3937417468301, "valueType": "Amount"}, 
            {"code": "fol_deqv", "description": "Dietary Folate Equivalents", "units": "mcg", "amount": 535.358027279696, "valueType": "Amount"}, 
            {"code": "fol_nat", "description": "Natural Folate (food folate)", "units": "mcg", "amount": 495.941020920334, "valueType": "Amount"}, 
            {"code": "fol_syn", "description": "Synthetic Folate (folic acid)", "units": "mcg", "amount": 23.2026128608886, "valueType": "Amount"}, 
            {"code": "formontn", "description": "Formononetin", "units": "mg", "amount": 0.0039347201005423, "valueType": "Amount"}, 
            {"code": "fructose", "description": "Fructose", "units": "g", "amount": 23.8118065366292, "valueType": "Amount"}, 
            {"code": "galactos", "description": "Galactose", "units": "g", "amount": 0.325095909073796, "valueType": "Amount"}, 
            {"code": "gammtoco", "description": "Gamma-Tocopherol", "units": "mg", "amount": 10.5817960101368, "valueType": "Amount"}, 
            {"code": "genistn", "description": "Genistein", "units": "mg", "amount": 6.67551536491055, "valueType": "Amount"}, 
            {"code": "glucose", "description": "Glucose", "units": "g", "amount": 24.7962641559998, "valueType": "Amount"}, 
            {"code": "glutamic", "description": "Glutamic Acid", "units": "g", "amount": 11.7082329977362, "valueType": "Amount"}, 
            {"code": "glycine", "description": "Glycine", "units": "g", "amount": 3.02835606129976, "valueType": "Amount"}, 
            {"code": "glycitn", "description": "Glycitein", "units": "mg", "amount": 1.15847124815855, "valueType": "Amount"}, 
            {"code": "grams", "description": "Total Grams", "units": "g", "amount": 4461.64073065229, "valueType": "Amount"}, 
            {"code": "histidin", "description": "Histidine", "units": "g", "amount": 1.79108003586935, "valueType": "Amount"}, 
            {"code": "inositol", "description": "Inositol", "units": "g", "amount": 0.239942736975281, "valueType": "Amount"}, 
            {"code": "iron", "description": "Iron", "units": "mg", "amount": 13.4234126963621, "valueType": "Amount"}, 
            {"code": "isoleuc", "description": "Isoleucine", "units": "g", "amount": 2.88311577827, "valueType": "Amount"}, 
            {"code": "isomalt", "description": "Isomalt", "units": "g", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "joules", "description": "Energy", "units": "kj", "amount": 7564.15947718781, "valueType": "Amount"}, 
            {"code": "lactitol", "description": "Lactitol", "units": "g", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "lactose", "description": "Lactose", "units": "g", "amount": 1.40077199349452, "valueType": "Amount"}, 
            {"code": "leucine", "description": "Leucine", "units": "g", "amount": 4.96326309285184, "valueType": "Amount"}, 
            {"code": "lutzeax", "description": "Lutein + Zeaxanthin", "units": "mcg", "amount": 14210.5886855697, "valueType": "Amount"}, 
            {"code": "lycopene", "description": "Lycopene", "units": "mcg", "amount": 5803.7247754124, "valueType": "Amount"}, 
            {"code": "lysine", "description": "Lysine", "units": "g", "amount": 4.4578740476423, "valueType": "Amount"}, 
            {"code": "magnes", "description": "Magnesium", "units": "mg", "amount": 418.784210838009, "valueType": "Amount"}, 
            {"code": "maltitol", "description": "Maltitol", "units": "g", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "maltose", "description": "Maltose", "units": "g", "amount": 3.93178534886411, "valueType": "Amount"}, 
            {"code": "mangan", "description": "Manganese", "units": "mg", "amount": 5.11558237307998, "valueType": "Amount"}, 
            {"code": "mannitol", "description": "Mannitol", "units": "g", "amount": 0.3741515674034, "valueType": "Amount"}, 
            {"code": "methhis3", "description": "3-Methylhistidine", "units": "mg", "amount": 12.7892253256824, "valueType": "Amount"}, 
            {"code": "methion", "description": "Methionine", "units": "g", "amount": 1.39970760273343, "valueType": "Amount"}, 
            {"code": "mfa141", "description": "MUFA 14:1 (myristoleic acid)", "units": "g", "amount": 0.0521369976619411, "valueType": "Amount"}, 
            {"code": "mfa161", "description": "MUFA 16:1 (palmitoleic acid)", "units": "g", "amount": 1.1097938595457, "valueType": "Amount"}, 
            {"code": "mfa181", "description": "MUFA 18:1 (oleic acid)", "units": "g", "amount": 29.9184222159848, "valueType": "Amount"}, 
            {"code": "mfa201", "description": "MUFA 20:1 (gadoleic acid)", "units": "g", "amount": 0.467779993166764, "valueType": "Amount"}, 
            {"code": "mfa221", "description": "MUFA 22:1 (erucic acid)", "units": "g", "amount": 0.250076280671428, "valueType": "Amount"}, 
            {"code": "mfatot", "description": "Total Monounsaturated Fatty Acids (MUFA)", "units": "g", "amount": 32.0908963631309, "valueType": "Amount"}, 
            {"code": "natoco", "description": "Natural Alpha-Tocopherol (RRR-alpha-tocopherol or d-alpha-tocopherol)", "units": "mg", "amount": 13.8272044723449, "valueType": "Amount"}, 
            {"code": "niacin", "description": "Niacin (vitamin B3)", "units": "mg", "amount": 19.3541332766736, "valueType": "Amount"}, 
            {"code": "niacineq", "description": "Niacin Equivalents", "units": "mg", "amount": 31.469031012723, "valueType": "Amount"}, 
            {"code": "nitrogen", "description": "Nitrogen", "units": "g", "amount": 11.1572792577067, "valueType": "Amount"}, 
            {"code": "omega3", "description": "Omega-3 Fatty Acids", "units": "g", "amount": 2.48016804796328, "valueType": "Amount"}, 
            {"code": "oxalic", "description": "Oxalic Acid", "units": "mg", "amount": 520.221114483978, "valueType": "Amount"}, 
            {"code": "pantothe", "description": "Pantothenic acid", "units": "mg", "amount": 6.03607144145405, "valueType": "Amount"}, 
            {"code": "pectins", "description": "Pectins", "units": "g", "amount": 7.45956819618311, "valueType": "Amount"}, 
            {"code": "pfa182", "description": "PUFA 18:2 (linoleic acid)", "units": "g", "amount": 16.0465876606774, "valueType": "Amount"}, 
            {"code": "pfa183", "description": "PUFA 18:3 (linolenic acid)", "units": "g", "amount": 1.87140724424294, "valueType": "Amount"}, 
            {"code": "pfa183n3", "description": "PUFA 18:3 n-3 (alpha-linolenic acid [ALA])", "units": "g", "amount": 1.82059571458515, "valueType": "Amount"}, 
            {"code": "pfa184", "description": "PUFA 18:4 (parinaric acid)", "units": "g", "amount": 0.0540339710336013, "valueType": "Amount"}, 
            {"code": "pfa204", "description": "PUFA 20:4 (arachidonic acid)", "units": "g", "amount": 0.112993556250618, "valueType": "Amount"}, 
            {"code": "pfa205", "description": "PUFA 20:5 (eicosapentaenoic acid [EPA])", "units": "g", "amount": 0.177126468644694, "valueType": "Amount"}, 
            {"code": "pfa225", "description": "PUFA 22:5 (docosapentaenoic acid [DPA])", "units": "g", "amount": 0.0704315799795576, "valueType": "Amount"}, 
            {"code": "pfa226", "description": "PUFA 22:6 (docosahexaenoic acid [DHA])", "units": "g", "amount": 0.358369227587756, "valueType": "Amount"}, 
            {"code": "pfatot", "description": "Total Polyunsaturated Fatty Acids (PUFA)", "units": "g", "amount": 18.7776268914992, "valueType": "Amount"}, 
            {"code": "phenylal", "description": "Phenylalanine", "units": "g", "amount": 2.89921759384484, "valueType": "Amount"}, 
            {"code": "phosphor", "description": "Phosphorus", "units": "mg", "amount": 1191.60495015982, "valueType": "Amount"}, 
            {"code": "phytic", "description": "Phytic Acid", "units": "mg", "amount": 839.713527781438, "valueType": "Amount"}, 
            {"code": "pinitol", "description": "Pinitol", "units": "g", "amount": 0.0372641105715134, "valueType": "Amount"}, 
            {"code": "potass", "description": "Potassium", "units": "mg", "amount": 4178.40549963951, "valueType": "Amount"}, 
            {"code": "proline", "description": "Proline", "units": "g", "amount": 3.37974266040051, "valueType": "Amount"}, 
            {"code": "protanim", "description": "Animal Protein", "units": "g", "amount": 34.139947679318, "valueType": "Amount"}, 
            {"code": "protein", "description": "Total Protein", "units": "g", "amount": 68.5467889539274, "valueType": "Amount"}, 
            {"code": "protveg", "description": "Vegetable Protein", "units": "g", "amount": 34.4078033666255, "valueType": "Amount"}, 
            {"code": "retinol", "description": "Retinol", "units": "mcg", "amount": 157.655287447923, "valueType": "Amount"}, 
            {"code": "ribofla", "description": "Riboflavin (vitamin B2)", "units": "mg", "amount": 1.63275244678641, "valueType": "Amount"}, 
            {"code": "sacchar", "description": "Saccharin", "units": "mg", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "satoco", "description": "Synthetic Alpha-Tocopherol (all rac-alpha-tocopherol or dl-alpha-tocopherol)", "units": "mg", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "selenium", "description": "Selenium", "units": "mcg", "amount": 77.1658858033905, "valueType": "Amount"}, 
            {"code": "serine", "description": "Serine", "units": "g", "amount": 3.11158681989948, "valueType": "Amount"}, 
            {"code": "sfa100", "description": "SFA 10:0 (capric acid)", "units": "g", "amount": 0.123772762292024, "valueType": "Amount"}, 
            {"code": "sfa120", "description": "SFA 12:0 (lauric acid)", "units": "g", "amount": 0.162566657856428, "valueType": "Amount"}, 
            {"code": "sfa140", "description": "SFA 14:0 (myristic acid)", "units": "g", "amount": 0.928258241022126, "valueType": "Amount"}, 
            {"code": "sfa160", "description": "SFA 16:0 (palmitic acid)", "units": "g", "amount": 11.0583913140683, "valueType": "Amount"}, 
            {"code": "sfa170", "description": "SFA 17:0 (margaric acid)", "units": "g", "amount": 0.0792414742466278, "valueType": "Amount"}, 
            {"code": "sfa180", "description": "SFA 18:0 (stearic acid)", "units": "g", "amount": 4.50331557152288, "valueType": "Amount"}, 
            {"code": "sfa200", "description": "SFA 20:0 (arachidic acid)", "units": "g", "amount": 0.222634147550192, "valueType": "Amount"}, 
            {"code": "sfa220", "description": "SFA 22:0 (behenic acid)", "units": "g", "amount": 0.240415738532113, "valueType": "Amount"}, 
            {"code": "sfa40", "description": "SFA 4:0 (butyric acid)", "units": "g", "amount": 0.16454157410762, "valueType": "Amount"}, 
            {"code": "sfa60", "description": "SFA 6:0 (caproic acid)", "units": "g", "amount": 0.0675730235807897, "valueType": "Amount"}, 
            {"code": "sfa80", "description": "SFA 8:0 (caprylic acid)", "units": "g", "amount": 0.0551364392767923, "valueType": "Amount"}, 
            {"code": "sfatot", "description": "Total Saturated Fatty Acids (SFA)", "units": "g", "amount": 17.9109742062119, "valueType": "Amount"}, 
            {"code": "sodium", "description": "Sodium", "units": "mg", "amount": 3356.10715835513, "valueType": "Amount"}, 
            {"code": "solidfat", "description": "Solid Fats", "units": "g", "amount": 16.9747527054314, "valueType": "Amount"}, 
            {"code": "sorbitol", "description": "Sorbitol", "units": "g", "amount": 0.93428298269052, "valueType": "Amount"}, 
            {"code": "starch", "description": "Starch", "units": "g", "amount": 56.6438582051493, "valueType": "Amount"}, 
            {"code": "sucpoly", "description": "Sucrose polyester", "units": "g", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "sucrlose", "description": "Sucralose", "units": "mg", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "sucrose", "description": "Sucrose", "units": "g", "amount": 31.5401449671408, "valueType": "Amount"}, 
            {"code": "tagatose", "description": "Tagatose", "units": "mg", "amount": 1.50606310896968, "valueType": "Amount"}, 
            {"code": "tfa161t", "description": "TRANS 16:1 (trans-hexadecenoic acid)", "units": "g", "amount": 0.025474956945716, "valueType": "Amount"}, 
            {"code": "tfa181t", "description": "TRANS 18:1 (trans-octadecenoic acid [elaidic acid])", "units": "g", "amount": 1.01554513172964, "valueType": "Amount"}, 
            {"code": "tfa182t", "description": "TRANS 18:2 (trans-octadecadienoic acid [linolelaidic acid]; incl. c-t, t-c, t-t)", "units": "g", "amount": 0.312571874262212, "valueType": "Amount"}, 
            {"code": "thiamin", "description": "Thiamin (vitamin B1)", "units": "mg", "amount": 1.19841980101766, "valueType": "Amount"}, 
            {"code": "threonin", "description": "Threonine", "units": "g", "amount": 2.63688730152425, "valueType": "Amount"}, 
            {"code": "totaltfa", "description": "Total Trans-Fatty Acids (TRANS)", "units": "g", "amount": 1.35773516392536, "valueType": "Amount"}, 
            {"code": "totcla", "description": "Total Conjugated Linoleic Acid (CLA 18:2)", "units": "g", "amount": 0.0503167212948612, "valueType": "Amount"}, 
            {"code": "totfolat", "description": "Total Folate", "units": "mcg", "amount": 519.125420073116, "valueType": "Amount"}, 
            {"code": "totsugar", "description": "Total Sugars", "units": "g", "amount": 86.5017968317162, "valueType": "Amount"}, 
            {"code": "tryptoph", "description": "Tryptophan", "units": "g", "amount": 0.72760915210754, "valueType": "Amount"}, 
            {"code": "tyrosine", "description": "Tyrosine", "units": "g", "amount": 2.16075926250871, "valueType": "Amount"}, 
            {"code": "valine", "description": "Valine", "units": "g", "amount": 3.30563752153854, "valueType": "Amount"}, 
            {"code": "vita_iu", "description": "Total Vitamin A Activity", "units": "IU", "amount": 36238.3518547351, "valueType": "Amount"}, 
            {"code": "vita_rae", "description": "Total Vitamin A Activity (Retinol Activity Equivalents)", "units": "mcg", "amount": 1943.24617069538, "valueType": "Amount"}, 
            {"code": "vita_re", "description": "Total Vitamin A Activity (Retinol Equivalents)", "units": "mcg", "amount": 3728.83517224819, "valueType": "Amount"}, 
            {"code": "vitb12", "description": "Vitamin B-12 (cobalamin)", "units": "mcg", "amount": 3.43408697531301, "valueType": "Amount"}, 
            {"code": "vitb6", "description": "Vitamin B-6 (pyridoxine, pyridoxyl, & pyridoxamine)", "units": "mg", "amount": 2.45279964248773, "valueType": "Amount"}, 
            {"code": "vitc", "description": "Vitamin C (ascorbic acid)", "units": "mg", "amount": 237.097489537344, "valueType": "Amount"}, 
            {"code": "vitd", "description": "Vitamin D (calciferol)", "units": "mcg", "amount": 7.0780265212001, "valueType": "Amount"}, 
            {"code": "vitd2", "description": "Vitamin D2 (ergocalciferol)", "units": "mcg", "amount": 0.267419178069454, "valueType": "Amount"}, 
            {"code": "vitd3", "description": "Vitamin D3 (cholecalciferol)", "units": "mcg", "amount": 6.81060734398797, "valueType": "Amount"}, 
            {"code": "vite_iu", "description": "Vitamin E", "units": "IU", "amount": 20.6156000038304, "valueType": "Amount"}, 
            {"code": "vitk", "description": "Vitamin K (phylloquinone)", "units": "mcg", "amount": 661.63354211431, "valueType": "Amount"}, 
            {"code": "water", "description": "Water", "units": "g", "amount": 4084.9018687902, "valueType": "Amount"}, 
            {"code": "xylitol", "description": "Xylitol", "units": "g", "amount": 0.0733377202226633, "valueType": "Amount"}, 
            {"code": "zinc", "description": "Zinc", "units": "mg", "amount": 9.53314201233853, "valueType": "Amount"}, 
            {"code": "oxalicm", "description": "Oxalic Acid from Mayo", "units": "mg", "amount": 466.891214440084, "valueType": "Amount"}, 
            {"code": "vitd_iu", "description": "Vitamin D", "units": "IU", "amount": 283.121060848004, "valueType": "Amount"}, 
            {"code": "omega3_epadha", "description": "Omega-3 Fatty Acids [EPA + DHA]", "units": "g", "amount": 0.53549569623245, "valueType": "Amount"}, 
            {"code": "omega6_la", "description": "pfa182 + pfa204, la = linoleic acid", "units": "g", "amount": 16.159581216928, "valueType": "Amount"}
        ]
    },
    {"sessionId": "005eae45652f4aef9880502a08139155", 
        "data": [
            {"code": "acesupot", "description": "Acesulfame Potassium", "units": "mg", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "addsugar", "description": "Added Sugars (by Available Carbohydrate)", "units": "g", "amount": 10.0593689531397, "valueType": "Amount"}, 
            {"code": "adsugtot", "description": "Added Sugars (by Total Sugars)", "units": "g", "amount": 8.58780528448219, "valueType": "Amount"}, 
            {"code": "alanine", "description": "Alanine", "units": "g", "amount": 3.20849763435068, "valueType": "Amount"}, 
            {"code": "alcohol", "description": "Alcohol", "units": "g", "amount": 0.0188054794520548, "valueType": "Amount"}, 
            {"code": "alphacar", "description": "Alpha-Carotene (provitamin A carotenoid)", "units": "mcg", "amount": 2277.08848633118, "valueType": "Amount"}, 
            {"code": "alphtoce", "description": "Total Vitamin E Activity (total alpha-tocopherol equivalents)", "units": "mg", "amount": 11.3692646559014, "valueType": "Amount"}, 
            {"code": "alphtoco", "description": "Alpha-Tocopherol", "units": "mg", "amount": 10.5379834555452, "valueType": "Amount"}, 
            {"code": "arginine", "description": "Arginine", "units": "g", "amount": 4.16278498679452, "valueType": "Amount"}, 
            {"code": "ash", "description": "Ash", "units": "g", "amount": 16.758364463863, "valueType": "Amount"}, 
            {"code": "aspartam", "description": "Aspartame", "units": "mg", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "aspartic", "description": "Aspartic Acid", "units": "g", "amount": 6.2246664434411, "valueType": "Amount"}, 
            {"code": "avcarb", "description": "Available Carbohydrate", "units": "g", "amount": 223.215122691923, "valueType": "Amount"}, 
            {"code": "betacar", "description": "Beta-Carotene (provitamin A carotenoid)", "units": "mcg", "amount": 7800.03203611689, "valueType": "Amount"}, 
            {"code": "betacryp", "description": "Beta-Cryptoxanthin (provitamin A carotenoid)", "units": "mcg", "amount": 192.793933629151, "valueType": "Amount"}, 
            {"code": "betaine", "description": "Betaine", "units": "mg", "amount": 183.190891167556, "valueType": "Amount"}, 
            {"code": "betatoco", "description": "Beta-Tocopherol", "units": "mg", "amount": 0.413293872471233, "valueType": "Amount"}, 
            {"code": "biochana", "description": "Biochanin A", "units": "mg", "amount": 0.0101287671232877, "valueType": "Amount"}, 
            {"code": "caffeine", "description": "Caffeine", "units": "mg", "amount": 58.9832390136986, "valueType": "Amount"}, 
            {"code": "calcium", "description": "Calcium", "units": "mg", "amount": 826.617092133046, "valueType": "Amount"}, 
            {"code": "calories", "description": "Energy", "units": "kcal", "amount": 1739.23220407839, "valueType": "Amount"}, 
            {"code": "carbo", "description": "Total Carbohydrate", "units": "g", "amount": 242.324241829896, "valueType": "Amount"}, 
            {"code": "cholest", "description": "Cholesterol", "units": "mg", "amount": 224.50476276531, "valueType": "Amount"}, 
            {"code": "choline", "description": "Choline", "units": "g", "amount": 295.216327394455, "valueType": "Amount"}, 
            {"code": "clac9t11", "description": "CLA cis-9, trans-11", "units": "g", "amount": 0.0770095182739726, "valueType": "Amount"}, 
            {"code": "clat10c12", "description": "CLA trans-10, cis-12", "units": "g", "amount": 0.0131543373150685, "valueType": "Amount"}, 
            {"code": "copper", "description": "Copper", "units": "mg", "amount": 1.24295447491507, "valueType": "Amount"}, 
            {"code": "coumest", "description": "Coumestrol", "units": "mg", "amount": 0.0709090553424658, "valueType": "Amount"}, 
            {"code": "cystine", "description": "Cystine", "units": "g", "amount": 0.895949884, "valueType": "Amount"}, 
            {"code": "daidzein", "description": "Daidzein", "units": "mg", "amount": 0.514257232876712, "valueType": "Amount"}, 
            {"code": "delttoco", "description": "Delta-Tocopherol", "units": "mg", "amount": 1.12679026629589, "valueType": "Amount"}, 
            {"code": "erythr", "description": "Erythritol", "units": "g", "amount": 0.000199452054794521, "valueType": "Amount"}, 
            {"code": "fat", "description": "Total Fat", "units": "g", "amount": 59.1083641264438, "valueType": "Amount"}, 
            {"code": "fiber", "description": "Total Dietary Fiber", "units": "g", "amount": 19.1124415871452, "valueType": "Amount"}, 
            {"code": "fibh2o", "description": "Soluble Dietary Fiber", "units": "g", "amount": 5.12198211601096, "valueType": "Amount"}, 
            {"code": "fibinso", "description": "Insoluble Dietary Fiber", "units": "g", "amount": 13.9870306507507, "valueType": "Amount"}, 
            {"code": "fol_deqv", "description": "Dietary Folate Equivalents", "units": "mcg", "amount": 473.664586953918, "valueType": "Amount"}, 
            {"code": "fol_nat", "description": "Natural Folate (food folate)", "units": "mcg", "amount": 259.676442578575, "valueType": "Amount"}, 
            {"code": "fol_syn", "description": "Synthetic Folate (folic acid)", "units": "mcg", "amount": 125.894627558904, "valueType": "Amount"}, 
            {"code": "formontn", "description": "Formononetin", "units": "mg", "amount": 0.00452438356164383, "valueType": "Amount"}, 
            {"code": "fructose", "description": "Fructose", "units": "g", "amount": 16.5202748540712, "valueType": "Amount"}, 
            {"code": "galactos", "description": "Galactose", "units": "g", "amount": 0.0809179673863014, "valueType": "Amount"}, 
            {"code": "gammtoco", "description": "Gamma-Tocopherol", "units": "mg", "amount": 6.54634189078356, "valueType": "Amount"}, 
            {"code": "genistn", "description": "Genistein", "units": "mg", "amount": 0.491086509216438, "valueType": "Amount"}, 
            {"code": "glucose", "description": "Glucose", "units": "g", "amount": 16.6979352592822, "valueType": "Amount"}, 
            {"code": "glutamic", "description": "Glutamic Acid", "units": "g", "amount": 11.6801490282027, "valueType": "Amount"}, 
            {"code": "glycine", "description": "Glycine", "units": "g", "amount": 2.75431706389041, "valueType": "Amount"}, 
            {"code": "glycitn", "description": "Glycitein", "units": "mg", "amount": 0.283324931506849, "valueType": "Amount"}, 
            {"code": "grams", "description": "Total Grams", "units": "g", "amount": 1887.00364610411, "valueType": "Amount"}, 
            {"code": "histidin", "description": "Histidine", "units": "g", "amount": 1.70424364115069, "valueType": "Amount"}, 
            {"code": "inositol", "description": "Inositol", "units": "g", "amount": 0.691358176076712, "valueType": "Amount"}, 
            {"code": "iron", "description": "Iron", "units": "mg", "amount": 12.5835657849863, "valueType": "Amount"}, 
            {"code": "isoleuc", "description": "Isoleucine", "units": "g", "amount": 2.82562763177534, "valueType": "Amount"}, 
            {"code": "isomalt", "description": "Isomalt", "units": "g", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "joules", "description": "Energy", "units": "kj", "amount": 7276.94714067915, "valueType": "Amount"}, 
            {"code": "lactitol", "description": "Lactitol", "units": "g", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "lactose", "description": "Lactose", "units": "g", "amount": 9.9174482288548, "valueType": "Amount"}, 
            {"code": "leucine", "description": "Leucine", "units": "g", "amount": 4.98000117925479, "valueType": "Amount"}, 
            {"code": "lutzeax", "description": "Lutein + Zeaxanthin", "units": "mcg", "amount": 3615.69626296265, "valueType": "Amount"}, 
            {"code": "lycopene", "description": "Lycopene", "units": "mcg", "amount": 1111.77724286247, "valueType": "Amount"}, 
            {"code": "lysine", "description": "Lysine", "units": "g", "amount": 4.0596495379726, "valueType": "Amount"}, 
            {"code": "magnes", "description": "Magnesium", "units": "mg", "amount": 311.333649623008, "valueType": "Amount"}, 
            {"code": "maltitol", "description": "Maltitol", "units": "g", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "maltose", "description": "Maltose", "units": "g", "amount": 0.95078438700274, "valueType": "Amount"}, 
            {"code": "mangan", "description": "Manganese", "units": "mg", "amount": 4.61517840473972, "valueType": "Amount"}, 
            {"code": "mannitol", "description": "Mannitol", "units": "g", "amount": 0.438020158608219, "valueType": "Amount"}, 
            {"code": "methhis3", "description": "3-Methylhistidine", "units": "mg", "amount": 8.76397505031233, "valueType": "Amount"}, 
            {"code": "methion", "description": "Methionine", "units": "g", "amount": 1.49364869478356, "valueType": "Amount"}, 
            {"code": "mfa141", "description": "MUFA 14:1 (myristoleic acid)", "units": "g", "amount": 0.0725867685369863, "valueType": "Amount"}, 
            {"code": "mfa161", "description": "MUFA 16:1 (palmitoleic acid)", "units": "g", "amount": 0.680041962367124, "valueType": "Amount"}, 
            {"code": "mfa181", "description": "MUFA 18:1 (oleic acid)", "units": "g", "amount": 17.9834683618301, "valueType": "Amount"}, 
            {"code": "mfa201", "description": "MUFA 20:1 (gadoleic acid)", "units": "g", "amount": 0.361690509972603, "valueType": "Amount"}, 
            {"code": "mfa221", "description": "MUFA 22:1 (erucic acid)", "units": "g", "amount": 0.203344162860274, "valueType": "Amount"}, 
            {"code": "mfatot", "description": "Total Monounsaturated Fatty Acids (MUFA)", "units": "g", "amount": 19.4223611311836, "valueType": "Amount"}, 
            {"code": "natoco", "description": "Natural Alpha-Tocopherol (RRR-alpha-tocopherol or d-alpha-tocopherol)", "units": "mg", "amount": 10.5379834555452, "valueType": "Amount"}, 
            {"code": "niacin", "description": "Niacin (vitamin B3)", "units": "mg", "amount": 19.0249455751123, "valueType": "Amount"}, 
            {"code": "niacineq", "description": "Niacin Equivalents", "units": "mg", "amount": 32.0213023981863, "valueType": "Amount"}, 
            {"code": "nitrogen", "description": "Nitrogen", "units": "g", "amount": 10.6362482000055, "valueType": "Amount"}, 
            {"code": "omega3", "description": "Omega-3 Fatty Acids", "units": "g", "amount": 1.33708272343014, "valueType": "Amount"}, 
            {"code": "omega3_epadha", "description": "Omega-3 Fatty Acids [EPA + DHA]", "units": "g", "amount": 0.474352193063014, "valueType": "Amount"}, 
            {"code": "omega6_la", "description": "pfa182 + pfa204, la = linoleic acid", "units": "g", "amount": 14.2876050675671, "valueType": "Amount"}, 
            {"code": "oxalic", "description": "Oxalic Acid", "units": "mg", "amount": 217.697019527589, "valueType": "Amount"}, 
            {"code": "oxalicm", "description": "Oxalic Acid from Mayo", "units": "mg", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "pantothe", "description": "Pantothenic acid", "units": "mg", "amount": 5.4016993594137, "valueType": "Amount"}, 
            {"code": "pectins", "description": "Pectins", "units": "g", "amount": 4.16463615078356, "valueType": "Amount"}, 
            {"code": "pfa182", "description": "PUFA 18:2 (linoleic acid)", "units": "g", "amount": 14.1713516310521, "valueType": "Amount"}, 
            {"code": "pfa183", "description": "PUFA 18:3 (linolenic acid)", "units": "g", "amount": 0.775882518778082, "valueType": "Amount"}, 
            {"code": "pfa183n3", "description": "PUFA 18:3 n-3 (alpha-linolenic acid [ALA])", "units": "g", "amount": 0.755355451320548, "valueType": "Amount"}, 
            {"code": "pfa184", "description": "PUFA 18:4 (parinaric acid)", "units": "g", "amount": 0.0422219178082192, "valueType": "Amount"}, 
            {"code": "pfa204", "description": "PUFA 20:4 (arachidonic acid)", "units": "g", "amount": 0.116253436515069, "valueType": "Amount"}, 
            {"code": "pfa205", "description": "PUFA 20:5 (eicosapentaenoic acid [EPA])", "units": "g", "amount": 0.15721642969863, "valueType": "Amount"}, 
            {"code": "pfa225", "description": "PUFA 22:5 (docosapentaenoic acid [DPA])", "units": "g", "amount": 0.065823147539726, "valueType": "Amount"}, 
            {"code": "pfa226", "description": "PUFA 22:6 (docosahexaenoic acid [DHA])", "units": "g", "amount": 0.317135763364384, "valueType": "Amount"}, 
            {"code": "pfatot", "description": "Total Polyunsaturated Fatty Acids (PUFA)", "units": "g", "amount": 15.7618182617205, "valueType": "Amount"}, 
            {"code": "phenylal", "description": "Phenylalanine", "units": "g", "amount": 2.92383625216438, "valueType": "Amount"}, 
            {"code": "phosphor", "description": "Phosphorus", "units": "mg", "amount": 1143.84820394362, "valueType": "Amount"}, 
            {"code": "phytic", "description": "Phytic Acid", "units": "mg", "amount": 784.56547554291, "valueType": "Amount"}, 
            {"code": "pinitol", "description": "Pinitol", "units": "g", "amount": 0.0119939726027397, "valueType": "Amount"}, 
            {"code": "potass", "description": "Potassium", "units": "mg", "amount": 2670.6109671337, "valueType": "Amount"}, 
            {"code": "proline", "description": "Proline", "units": "g", "amount": 3.72893466056986, "valueType": "Amount"}, 
            {"code": "protanim", "description": "Animal Protein", "units": "g", "amount": 35.1798582700384, "valueType": "Amount"}, 
            {"code": "protein", "description": "Total Protein", "units": "g", "amount": 65.5058044944, "valueType": "Amount"}, 
            {"code": "protveg", "description": "Vegetable Protein", "units": "g", "amount": 30.3258531845699, "valueType": "Amount"}, 
            {"code": "retinol", "description": "Retinol", "units": "mcg", "amount": 312.761589694537, "valueType": "Amount"}, 
            {"code": "ribofla", "description": "Riboflavin (vitamin B2)", "units": "mg", "amount": 1.56460213824658, "valueType": "Amount"}, 
            {"code": "sacchar", "description": "Saccharin", "units": "mg", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "satoco", "description": "Synthetic Alpha-Tocopherol (all rac-alpha-tocopherol or dl-alpha-tocopherol)", "units": "mg", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "selenium", "description": "Selenium", "units": "mcg", "amount": 104.939490702882, "valueType": "Amount"}, 
            {"code": "serine", "description": "Serine", "units": "g", "amount": 3.08193146888767, "valueType": "Amount"}, 
            {"code": "sfa100", "description": "SFA 10:0 (capric acid)", "units": "g", "amount": 0.454141673041096, "valueType": "Amount"}, 
            {"code": "sfa120", "description": "SFA 12:0 (lauric acid)", "units": "g", "amount": 0.504916552010959, "valueType": "Amount"}, 
            {"code": "sfa140", "description": "SFA 14:0 (myristic acid)", "units": "g", "amount": 1.81436346343562, "valueType": "Amount"}, 
            {"code": "sfa160", "description": "SFA 16:0 (palmitic acid)", "units": "g", "amount": 9.85364898575342, "valueType": "Amount"}, 
            {"code": "sfa170", "description": "SFA 17:0 (margaric acid)", "units": "g", "amount": 0.0983085194082191, "valueType": "Amount"}, 
            {"code": "sfa180", "description": "SFA 18:0 (stearic acid)", "units": "g", "amount": 3.93627396236164, "valueType": "Amount"}, 
            {"code": "sfa200", "description": "SFA 20:0 (arachidic acid)", "units": "g", "amount": 0.150607638279452, "valueType": "Amount"}, 
            {"code": "sfa220", "description": "SFA 22:0 (behenic acid)", "units": "g", "amount": 0.244122229682192, "valueType": "Amount"}, 
            {"code": "sfa40", "description": "SFA 4:0 (butyric acid)", "units": "g", "amount": 0.443542062630137, "valueType": "Amount"}, 
            {"code": "sfa60", "description": "SFA 6:0 (caproic acid)", "units": "g", "amount": 0.353628482717808, "valueType": "Amount"}, 
            {"code": "sfa80", "description": "SFA 8:0 (caprylic acid)", "units": "g", "amount": 0.270581145468493, "valueType": "Amount"}, 
            {"code": "sfatot", "description": "Total Saturated Fatty Acids (SFA)", "units": "g", "amount": 18.3894068549041, "valueType": "Amount"}, 
            {"code": "sodium", "description": "Sodium", "units": "mg", "amount": 4038.17710351875, "valueType": "Amount"}, 
            {"code": "solidfat", "description": "Solid Fats", "units": "g", "amount": 25.157357583326, "valueType": "Amount"}, 
            {"code": "sorbitol", "description": "Sorbitol", "units": "g", "amount": 0.294723557808219, "valueType": "Amount"}, 
            {"code": "starch", "description": "Starch", "units": "g", "amount": 127.474536438192, "valueType": "Amount"}, 
            {"code": "sucpoly", "description": "Sucrose polyester", "units": "g", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "sucrlose", "description": "Sucralose", "units": "mg", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "sucrose", "description": "Sucrose", "units": "g", "amount": 19.5512994959397, "valueType": "Amount"}, 
            {"code": "tagatose", "description": "Tagatose", "units": "mg", "amount": 0.0707010410958904, "valueType": "Amount"}, 
            {"code": "tfa161t", "description": "TRANS 16:1 (trans-hexadecenoic acid)", "units": "g", "amount": 0.0296726082082192, "valueType": "Amount"}, 
            {"code": "tfa181t", "description": "TRANS 18:1 (trans-octadecenoic acid [elaidic acid])", "units": "g", "amount": 1.12746876406575, "valueType": "Amount"}, 
            {"code": "tfa182t", "description": "TRANS 18:2 (trans-octadecadienoic acid [linolelaidic acid]; incl. c-t, t-c, t-t)", "units": "g", "amount": 0.217117642263014, "valueType": "Amount"}, 
            {"code": "thiamin", "description": "Thiamin (vitamin B1)", "units": "mg", "amount": 1.54306931196712, "valueType": "Amount"}, 
            {"code": "threonin", "description": "Threonine", "units": "g", "amount": 2.50377781833425, "valueType": "Amount"}, 
            {"code": "totaltfa", "description": "Total Trans-Fatty Acids (TRANS)", "units": "g", "amount": 1.42376384400548, "valueType": "Amount"}, 
            {"code": "totcla", "description": "Total Conjugated Linoleic Acid (CLA 18:2)", "units": "g", "amount": 0.0904158348054794, "valueType": "Amount"}, 
            {"code": "totfolat", "description": "Total Folate", "units": "mcg", "amount": 385.571096986795, "valueType": "Amount"}, 
            {"code": "totsugar", "description": "Total Sugars", "units": "g", "amount": 64.120640023463, "valueType": "Amount"}, 
            {"code": "tryptoph", "description": "Tryptophan", "units": "g", "amount": 0.782529797479452, "valueType": "Amount"}, 
            {"code": "tyrosine", "description": "Tyrosine", "units": "g", "amount": 2.21087033716164, "valueType": "Amount"}, 
            {"code": "valine", "description": "Valine", "units": "g", "amount": 3.35832184191233, "valueType": "Amount"}, 
            {"code": "vita_iu", "description": "Total Vitamin A Activity", "units": "IU", "amount": 16101.0031250239, "valueType": "Amount"}, 
            {"code": "vita_rae", "description": "Total Vitamin A Activity (Retinol Activity Equivalents)", "units": "mcg", "amount": 1065.67667881296, "valueType": "Amount"}, 
            {"code": "vita_re", "description": "Total Vitamin A Activity (Retinol Equivalents)", "units": "mcg", "amount": 1818.59291787945, "valueType": "Amount"}, 
            {"code": "vitb12", "description": "Vitamin B-12 (cobalamin)", "units": "mcg", "amount": 3.7839233009863, "valueType": "Amount"}, 
            {"code": "vitb6", "description": "Vitamin B-6 (pyridoxine, pyridoxyl, & pyridoxamine)", "units": "mg", "amount": 2.17063883660274, "valueType": "Amount"}, 
            {"code": "vitc", "description": "Vitamin C (ascorbic acid)", "units": "mg", "amount": 142.494286920142, "valueType": "Amount"}, 
            {"code": "vitd", "description": "Vitamin D (calciferol)", "units": "mcg", "amount": 11.1982357540274, "valueType": "Amount"}, 
            {"code": "vitd_iu", "description": "Vitamin D", "units": "IU", "amount": 447.929430161096, "valueType": "Amount"}, 
            {"code": "vitd2", "description": "Vitamin D2 (ergocalciferol)", "units": "mcg", "amount": 0.0160904109589041, "valueType": "Amount"}, 
            {"code": "vitd3", "description": "Vitamin D3 (cholecalciferol)", "units": "mcg", "amount": 11.1826631512877, "valueType": "Amount"}, 
            {"code": "vite_iu", "description": "Vitamin E", "units": "IU", "amount": 15.7152047560219, "valueType": "Amount"}, 
            {"code": "vitk", "description": "Vitamin K (phylloquinone)", "units": "mcg", "amount": 162.268865494279, "valueType": "Amount"}, 
            {"code": "water", "description": "Water", "units": "g", "amount": 1525.02060420945, "valueType": "Amount"}, 
            {"code": "xylitol", "description": "Xylitol", "units": "g", "amount": 0.0304087671232877, "valueType": "Amount"}, 
            {"code": "zinc", "description": "Zinc", "units": "mg", "amount": 7.79523011262466, "valueType": "Amount"}
        ]
    }
]

EP_DATA = [
    {"sessionId": "0087da64cdcb41ad800c23531d1198f2", 
        "data": [
            {"code": "ADDEDFATS", "description": "Eating Pattern", "units": "PerDay", "amount": 8.07030444201639, "valueType": "Amount"}, 
            {"code": "ALCOHOLSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 1.30647563412786, "valueType": "Amount"}, 
            {"code": "ANIMALPROTEIN", "description": "Eating Pattern", "units": "PerDay", "amount": 1.96556496716603, "valueType": "Amount"}, 
            {"code": "CALCDAIRYSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 0.364432970091999, "valueType": "Amount"}, 
            {"code": "CALCSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 2.62447202541388, "valueType": "Amount"}, 
            {"code": "FISHSERV", "description": "Eating Pattern", "units": "PerWeek", "amount": 0.392841568548386, "valueType": "Amount"}, 
            {"code": "FRIEDFISH", "description": "Eating Pattern", "units": "PerWeek", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "FRTSUMM", "description": "Eating Pattern", "units": "PerDay", "amount": 4.47806902432647, "valueType": "Amount"}, 
            {"code": "GRAINSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 0.877350918337469, "valueType": "Amount"}, 
            {"code": "JUICESERV", "description": "Eating Pattern", "units": "PerDay", "amount": 0.098804910215613, "valueType": "Amount"}, 
            {"code": "LOWFATDAIRYSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "NOFRYFISHSERV", "description": "Eating Pattern", "units": "PerWeek", "amount": 0.392841568548386, "valueType": "Amount"}, 
            {"code": "NONFATDAIRY", "description": "Eating Pattern", "units": "PerDay", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "PLANTPROTEIN", "description": "Eating Pattern", "units": "PerDay", "amount": 0.200006679966025, "valueType": "Amount"}, 
            {"code": "SALADSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 5.85226950661777, "valueType": "Amount"}, 
            {"code": "SOYFOODS", "description": "Eating Pattern", "units": "PerDay", "amount": 0.205479452054794, "valueType": "Amount"}, 
            {"code": "VEGSUMM", "description": "Eating Pattern", "units": "PerDay", "amount": 13.8556749715375, "valueType": "Amount"}
        ]
    },
    {"sessionId": "005eae45652f4aef9880502a08139155", 
        "data": [
            {"code": "ADDEDFATS", "description": "Eating Pattern", "units": "PerDay", "amount": 5.41350079452055, "valueType": "Amount"}, 
            {"code": "ALCOHOLSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 0.0038081095890411, "valueType": "Amount"}, 
            {"code": "ANIMALPROTEIN", "description": "Eating Pattern", "units": "PerDay", "amount": 1.63842435552564, "valueType": "Amount"}, 
            {"code": "CALCDAIRYSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 1.14563422013742, "valueType": "Amount"}, 
            {"code": "CALCSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 2.75539030711016, "valueType": "Amount"}, 
            {"code": "FISHSERV", "description": "Eating Pattern", "units": "PerWeek", "amount": 0.47322089900137, "valueType": "Amount"}, 
            {"code": "FRIEDFISH", "description": "Eating Pattern", "units": "PerWeek", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "FRTSUMM", "description": "Eating Pattern", "units": "PerDay", "amount": 3.96102171214794, "valueType": "Amount"}, 
            {"code": "GRAINSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 0.646737676712329, "valueType": "Amount"}, 
            {"code": "JUICESERV", "description": "Eating Pattern", "units": "PerDay", "amount": 0.857739213517808, "valueType": "Amount"}, 
            {"code": "LOWFATDAIRYSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "NOFRYFISHSERV", "description": "Eating Pattern", "units": "PerWeek", "amount": 0.47322089900137, "valueType": "Amount"}, 
            {"code": "NONFATDAIRY", "description": "Eating Pattern", "units": "PerDay", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "PLANTPROTEIN", "description": "Eating Pattern", "units": "PerDay", "amount": 0.268328734794521, "valueType": "Amount"}, 
            {"code": "SALADSERV", "description": "Eating Pattern", "units": "PerDay", "amount": 0.0, "valueType": "Amount"}, 
            {"code": "SOYFOODS", "description": "Eating Pattern", "units": "PerDay", "amount": 0.0657534246575342, "valueType": "Amount"}, 
            {"code": "VEGSUMM", "description": "Eating Pattern", "units": "PerDay", "amount": 3.64908085541108, "valueType": "Amount"}
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

        obs = VioscreenEatingPatterns.from_vioscreen(EP_DATA[0])
        self.assertEqual(exp.sessionId, obs.sessionId)
        exp_obj = exp.components[0]
        obs_obj = obs.components[0]
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
