import unittest
import pandas as pd
import pandas.testing as pdt
from microsetta_private_api.repo.metadata_repo._transforms import (
    apply_transforms, AgeYears, AgeCat, BMI, BMICat, AlcoholConsumption,
    NormalizeHeight, NormalizeWeight)
from microsetta_private_api.repo.metadata_repo._constants import MISSING_VALUE


class TransformTests(unittest.TestCase):
    def _apply_transforms_helper(self, transforms):
        df = pd.DataFrame([['1990', 'July', '2020-01-01T12:00:00'],
                           ['1995', MISSING_VALUE, '2019-01-23T12:00:00'],
                           [MISSING_VALUE, 'May', '2018-01-23T12:00:00'],
                           [MISSING_VALUE, MISSING_VALUE,
                            '2017-01-23T12:00:00']],
                          index=list('abcd'),
                          columns=['birth_year', 'birth_month',
                                   'collection_timestamp'])

        exp = pd.DataFrame([['1990', 'July', '2020-01-01T12:00:00',
                             '29.5', '20s'],
                            ['1995', MISSING_VALUE, '2019-01-23T12:00:00',
                             MISSING_VALUE, MISSING_VALUE],
                            [MISSING_VALUE, 'May', '2018-01-23T12:00:00',
                             MISSING_VALUE, MISSING_VALUE],
                            [MISSING_VALUE, MISSING_VALUE,
                             '2017-01-23T12:00:00', MISSING_VALUE,
                             MISSING_VALUE]],
                           index=list('abcd'),
                           columns=['birth_year', 'birth_month',
                                    'collection_timestamp', 'age_years',
                                    'age_cat'])
        obs = apply_transforms(df, transforms)
        pdt.assert_frame_equal(obs, exp, check_less_precise=True)

    def test_apply_transforms_missing_column(self):
        # in this case, the dataframe that will be operated on does
        # not have the required columns for BMI
        self._apply_transforms_helper((AgeYears, AgeCat, BMI))

    def test_apply_transforms(self):
        self._apply_transforms_helper((AgeYears, AgeCat))

    def _test_transformer(self, transformer, df, exp):
        obs = transformer.apply(df)
        pdt.assert_series_equal(obs, exp)

    def test_AgeYears(self):
        df = pd.DataFrame([['1990', 'July', '2020-01-01T12:00:00'],
                           ['1995', MISSING_VALUE, '2019-01-23T12:00:00'],
                           [MISSING_VALUE, 'May', '2018-01-23T12:00:00'],
                           [MISSING_VALUE, MISSING_VALUE,
                            '2017-01-23T12:00:00']],
                          index=list('abcd'),
                          columns=['birth_year', 'birth_month',
                                   'collection_timestamp'])
        exp = pd.Series([29.5, MISSING_VALUE, MISSING_VALUE,
                        MISSING_VALUE], index=list('abcd'), name='age_years')
        self._test_transformer(AgeYears, df, exp)

    def test_AgeCat(self):
        df = pd.DataFrame([[-2],
                           [0],
                           [2.9],
                           [3],
                           [12.9],
                           [13],
                           [19.9],
                           [20],
                           [20.9],
                           [30],
                           [39.9],
                           [40],
                           [49.9],
                           [50],
                           [59.9],
                           [60],
                           [69.9],
                           [70],
                           [122],
                           [123],
                           [12345],
                           [MISSING_VALUE]],
                          columns=['age_years'],
                          index=list('abcdefghijklmnopqrstuv'))
        exp = pd.Series([MISSING_VALUE, 'baby', 'baby', 'child', 'child',
                         'teen', 'teen', '20s', '20s', '30s', '30s', '40s',
                         '40s', '50s', '50s', '60s', '60s', '70+', '70+',
                         MISSING_VALUE, MISSING_VALUE, MISSING_VALUE],
                        index=list('abcdefghijklmnopqrstuv'),
                        name='age_cat')
        self._test_transformer(AgeCat, df, exp)

    def test_BMI(self):
        df = pd.DataFrame([[180, 50],
                           [180, 60],
                           [170, 70],
                           [MISSING_VALUE, 60],
                           [150, MISSING_VALUE],
                           [MISSING_VALUE, MISSING_VALUE]],
                          index=list('abcdef'),
                          columns=['height_cm', 'weight_kg'])
        exp = pd.Series([15.4, 18.5, 24.2, MISSING_VALUE, MISSING_VALUE,
                        MISSING_VALUE], index=list('abcdef'), name='bmi')
        self._test_transformer(BMI, df, exp)

    def test_BMICat(self):
        df = pd.DataFrame([[-2],
                           [7.9],
                           [8],
                           [18.4],
                           [18.5],
                           [24.9],
                           [25],
                           [29.9],
                           [30],
                           [79.9],
                           [80],
                           [210],
                           [MISSING_VALUE]],
                          index=list('abcdefghijklm'),
                          columns=['bmi'])
        exp = pd.Series([MISSING_VALUE, MISSING_VALUE, 'Underweight',
                         'Underweight', 'Normal',
                         'Normal', 'Overweight', 'Overweight', 'Obese',
                         'Obese', MISSING_VALUE, MISSING_VALUE, MISSING_VALUE],
                        index=list('abcdefghijklm'), name='bmi_cat')
        self._test_transformer(BMICat, df, exp)

    def test_NormalizeWeight(self):
        df = pd.DataFrame([[180, 'pounds'],
                           [180, 'kilograms'],
                           [-1, 'pounds'],
                           [None, 'pounds'],
                           [180, None]], index=list('abcde'),
                          columns=['weight_kg', 'weight_units'])
        exp = pd.Series([180 / 2.20462, 180, MISSING_VALUE, MISSING_VALUE,
                        MISSING_VALUE],
                        index=list('abcde'), name='weight_kg')
        self._test_transformer(NormalizeWeight, df, exp)

    def test_NormalizeHeight(self):
        df = pd.DataFrame([[180, 'inches'],
                           [180, 'centimeters'],
                           [-1, 'inches'],
                           [None, 'inches'],
                           [180, None]], index=list('abcde'),
                          columns=['height_cm', 'height_units'])
        exp = pd.Series([180 * 2.54, 180, MISSING_VALUE, MISSING_VALUE,
                        MISSING_VALUE],
                        index=list('abcde'), name='height_cm')
        self._test_transformer(NormalizeHeight, df, exp)

    def test_AlcoholConsumption(self):
        df = pd.DataFrame([['Rarely (a few times/month)'],
                           ['Occasionally (1-2 times/week)'],
                           ['Regularly (3-5 times/week)'],
                           ['Daily'],
                           ['Never'],
                           [MISSING_VALUE]],
                          index=list('abcdef'),
                          columns=['alcohol_frequency'])
        exp = pd.Series(['Yes', 'Yes', 'Yes', 'Yes', 'No', MISSING_VALUE],
                        index=list('abcdef'),
                        name='alcohol_consumption')
        self._test_transformer(AlcoholConsumption, df, exp)

    def test_AlcoholConsumption_raises(self):
        df = pd.DataFrame([['Rarely (a few times/month)'],
                           ['Occasionally (1-2 times/week)'],
                           ['Regularly (3-5 times/week)'],
                           ['Dailybadbadbad'],
                           ['Never'],
                           [MISSING_VALUE]],
                          index=list('abcdef'),
                          columns=['alcohol_frequency'])
        with self.assertRaisesRegex(KeyError, "Unexpected"):
            AlcoholConsumption.apply(df)


if __name__ == '__main__':
    unittest.main()
