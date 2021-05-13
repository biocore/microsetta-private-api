import unittest
from microsetta_private_api.model.vioscreen import (
    VioscreenSession, VioscreenFoodComponents,
    VioscreenFoodComponentsComponent)
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import (
    VioscreenSessionRepo, VioscreenFoodComponentsRepo)
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
FC_DATA = {"sessionId": "0087da64cdcb41ad800c23531d1198f2", 
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
}

VIOSCREEN_FOOD_COMPONENTS = VioscreenFoodComponents.from_vioscreen(FC_DATA)



class TestFoodComponentsRepo(unittest.TestCase):

    def test_insert_food_energy_does_not_exist(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenFoodComponentsRepo(t)
            obs = r.insert_food_components(VIOSCREEN_FOOD_COMPONENTS)
            self.assertEqual(obs, 156)

    def test_get_food_components_exists(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenFoodComponentsRepo(t)
            r.insert_food_components(VIOSCREEN_FOOD_COMPONENTS)
            obs = r.get_food_components(VIOSCREEN_FOOD_COMPONENTS.sessionId)
            self.assertEqual(obs, VIOSCREEN_FOOD_COMPONENTS)

    def test_get_food_components_does_not_exist(self):
        with Transaction() as t:
            s = VioscreenSessionRepo(t)
            s.upsert_session(VIOSCREEN_SESSION)
            r = VioscreenFoodComponentsRepo(t)
            obs = r.get_food_components('does not exist')
            self.assertEqual(obs, None)


if __name__ == '__main__':
    unittest.main()
