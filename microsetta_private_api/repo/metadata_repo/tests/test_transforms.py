import unittest
import pandas as pd
import pandas.testing as pdt
from microsetta_private_api.repo.metadata_repo._transforms import (
    apply_transforms, HostAge, AgeCat, BMI, BMICat, AlcoholConsumption,
    NormalizeHeight, NormalizeWeight, Sex, Lifestage, HOST_AGE, BIRTH_YEAR,
    BIRTH_MONTH, COLLECTION_TIMESTAMP, HOST_WEIGHT, HOST_HEIGHT, AGE_CAT,
    SEX, GENDER, BMI_, ALCOHOL_FREQUENCY, ALCOHOL_CONSUMPTION, Rename,
    Constant, Normalize, BMI_CAT, HOST_WEIGHT_UNITS, HOST_HEIGHT_UNITS,
    LIFESTAGE)
from microsetta_private_api.repo.metadata_repo._constants import (
    UNSPECIFIED)


class TransformTests(unittest.TestCase):
    def _apply_transforms_helper(self, transforms):
        df = pd.DataFrame([['1990', 'July', '2020-01-01T12:00:00'],
                           ['1995', UNSPECIFIED, '2019-01-23T12:00:00'],
                           [UNSPECIFIED, 'May', '2018-01-23T12:00:00'],
                           [UNSPECIFIED, UNSPECIFIED,
                            '2017-01-23T12:00:00']],
                          index=list('abcd'),
                          columns=[BIRTH_YEAR, BIRTH_MONTH,
                                   COLLECTION_TIMESTAMP])

        exp = pd.DataFrame([['1990', 'July', '2020-01-01T12:00:00',
                             '29.5', '20s'],
                            ['1995', UNSPECIFIED, '2019-01-23T12:00:00',
                             UNSPECIFIED, UNSPECIFIED],
                            [UNSPECIFIED, 'May', '2018-01-23T12:00:00',
                             UNSPECIFIED, UNSPECIFIED],
                            [UNSPECIFIED, UNSPECIFIED,
                             '2017-01-23T12:00:00', UNSPECIFIED,
                             UNSPECIFIED]],
                           index=list('abcd'),
                           columns=[BIRTH_YEAR, BIRTH_MONTH,
                                    COLLECTION_TIMESTAMP, HOST_AGE,
                                    AGE_CAT])
        obs = apply_transforms(df, transforms)
        pdt.assert_frame_equal(obs, exp, check_less_precise=True)

    def test_apply_transforms_missing_column(self):
        # in this case, the dataframe that will be operated on does
        # not have the required columns for BMI
        self._apply_transforms_helper((HostAge, AgeCat, BMI))

    def test_apply_transforms(self):
        self._apply_transforms_helper((HostAge, AgeCat))

    def _test_transformer(self, transformer, df, exp):
        obs = transformer.apply(df)
        pdt.assert_series_equal(obs, exp)

    def test_AgeYears(self):
        df = pd.DataFrame([['1990', 'July', '2020-01-01T12:00:00'],
                           ['1995', UNSPECIFIED, '2019-01-23T12:00:00'],
                           [UNSPECIFIED, 'May', '2018-01-23T12:00:00'],
                           [UNSPECIFIED, UNSPECIFIED,
                            '2017-01-23T12:00:00']],
                          index=list('abcd'),
                          columns=[BIRTH_YEAR, BIRTH_MONTH,
                                   COLLECTION_TIMESTAMP])
        exp = pd.Series([29.5, UNSPECIFIED, UNSPECIFIED,
                        UNSPECIFIED], index=list('abcd'), name=HOST_AGE)
        self._test_transformer(HostAge, df, exp)

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
                           [UNSPECIFIED]],
                          columns=[HOST_AGE],
                          index=list('abcdefghijklmnopqrstuv'))
        exp = pd.Series([UNSPECIFIED, 'baby', 'baby', 'child', 'child',
                         'teen', 'teen', '20s', '20s', '30s', '30s', '40s',
                         '40s', '50s', '50s', '60s', '60s', '70+', '70+',
                         UNSPECIFIED, UNSPECIFIED, UNSPECIFIED],
                        index=list('abcdefghijklmnopqrstuv'),
                        name=AGE_CAT)
        self._test_transformer(AgeCat, df, exp)

    def test_Lifestage(self):
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
                           [UNSPECIFIED]],
                          columns=[HOST_AGE],
                          index=list('abcdefghijklmnopqrstuv'))
        exp = pd.Series([UNSPECIFIED, 'Infant', 'Infant', 'Child', 'Child',
                         'Teen', 'Teen', 'Adult', 'Adult', 'Adult', 'Adult',
                         'Adult', 'Adult', 'Adult', 'Adult', 'Adult', 'Adult',
                         'Elderly', 'Elderly', UNSPECIFIED, UNSPECIFIED,
                         UNSPECIFIED],
                        index=list('abcdefghijklmnopqrstuv'),
                        name=LIFESTAGE)
        self._test_transformer(Lifestage, df, exp)

    def test_Sex(self):
        df = pd.DataFrame([['Male'],
                           ['Female'],
                           ['Unspecified'],
                           [UNSPECIFIED],
                           ['Other']],
                          index=list('abcde'),
                          columns=[GENDER, ])
        exp = pd.Series(['male', 'female', 'unspecified', UNSPECIFIED.lower(),
                         'other'], index=list('abcde'), name=SEX)
        self._test_transformer(Sex, df, exp)

    def test_BMI(self):
        df = pd.DataFrame([[180, 50],
                           [180, 60],
                           [170, 70],
                           [UNSPECIFIED, 60],
                           [150, UNSPECIFIED],
                           [UNSPECIFIED, UNSPECIFIED]],
                          index=list('abcdef'),
                          columns=[HOST_HEIGHT, HOST_WEIGHT])
        exp = pd.Series([15.4, 18.5, 24.2, UNSPECIFIED, UNSPECIFIED,
                        UNSPECIFIED], index=list('abcdef'), name=BMI_)
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
                           [UNSPECIFIED]],
                          index=list('abcdefghijklm'),
                          columns=[BMI_])
        exp = pd.Series([UNSPECIFIED, UNSPECIFIED, 'Underweight',
                         'Underweight', 'Normal',
                         'Normal', 'Overweight', 'Overweight', 'Obese',
                         'Obese', UNSPECIFIED, UNSPECIFIED, UNSPECIFIED],
                        index=list('abcdefghijklm'), name=BMI_CAT)
        self._test_transformer(BMICat, df, exp)

    def test_NormalizeWeight(self):
        df = pd.DataFrame([[180, 'pounds'],
                           [180, 'kilograms'],
                           [-1, 'pounds'],
                           [None, 'pounds'],
                           [180, None]], index=list('abcde'),
                          columns=[HOST_WEIGHT, HOST_WEIGHT_UNITS])
        exp = pd.Series([180 / 2.20462, 180, UNSPECIFIED, UNSPECIFIED,
                        UNSPECIFIED],
                        index=list('abcde'), name=HOST_WEIGHT)
        self._test_transformer(NormalizeWeight, df, exp)

    def test_NormalizeHeight(self):
        df = pd.DataFrame([[180, 'inches'],
                           [180, 'centimeters'],
                           [-1, 'inches'],
                           [None, 'inches'],
                           [180, None]], index=list('abcde'),
                          columns=[HOST_HEIGHT, HOST_HEIGHT_UNITS])
        exp = pd.Series([180 * 2.54, 180, UNSPECIFIED, UNSPECIFIED,
                        UNSPECIFIED],
                        index=list('abcde'), name=HOST_HEIGHT)
        self._test_transformer(NormalizeHeight, df, exp)

    def test_AlcoholConsumption(self):
        df = pd.DataFrame([['Rarely (a few times/month)'],
                           ['Occasionally (1-2 times/week)'],
                           ['Regularly (3-5 times/week)'],
                           ['Daily'],
                           ['Never'],
                           [UNSPECIFIED]],
                          index=list('abcdef'),
                          columns=[ALCOHOL_FREQUENCY])
        exp = pd.Series(['Yes', 'Yes', 'Yes', 'Yes', 'No', UNSPECIFIED],
                        index=list('abcdef'),
                        name=ALCOHOL_CONSUMPTION)
        self._test_transformer(AlcoholConsumption, df, exp)

    def test_AlcoholConsumption_raises(self):
        df = pd.DataFrame([['Rarely (a few times/month)'],
                           ['Occasionally (1-2 times/week)'],
                           ['Regularly (3-5 times/week)'],
                           ['Dailybadbadbad'],
                           ['Never'],
                           [UNSPECIFIED]],
                          index=list('abcdef'),
                          columns=[ALCOHOL_FREQUENCY])
        with self.assertRaisesRegex(KeyError, "Unexpected"):
            AlcoholConsumption.apply(df)

    def test_rename_valid(self):
        class rename(Rename):
            SRC = 'foo'
            DST = 'bar'

        df = pd.DataFrame([['a'], ['b'], ['c']],
                          index=list('xyz'),
                          columns=['foo'])
        exp = pd.DataFrame([['a'], ['b'], ['c']],
                           index=list('xyz'),
                           columns=['bar'])
        self.assertTrue(rename.satisfies_requirements(df))
        obs = rename.apply(df)
        pdt.assert_frame_equal(obs, exp)

    def test_rename_invalid(self):
        class rename(Rename):
            SRC = 'foo'
            DST = 'bar'

        df = pd.DataFrame([['a'], ['b'], ['c']],
                          index=list('xyz'),
                          columns=['baz'])

        # foo not present
        self.assertFalse(rename.satisfies_requirements(df))

        df = pd.DataFrame([['a', 1], ['b', 2], ['c', 3]],
                          index=list('xyz'),
                          columns=['foo', 'bar'])
        # bar is present
        self.assertFalse(rename.satisfies_requirements(df))

    def test_constant(self):
        class constant(Constant):
            REQUIRED_COLUMNS = frozenset(['baz', ])
            COLUMN_NAME = 'cool'
            VALUE = '1234'

        df = pd.DataFrame([['a'], ['b'], ['c']],
                          index=list('xyz'),
                          columns=['baz'])
        exp = pd.Series(['1234'] * 3,
                        index=list('xyz'),
                        name='cool')
        self.assertTrue(constant.satisfies_requirements(df))
        obs = constant.apply(df)
        pdt.assert_series_equal(obs, exp)

    def test_normalize(self):
        class normalize(Normalize):
            FOCUS_COL = 'foo'
            FOCUS_UNITS = 'thing'
            UNITS_COL = 'units'
            FACTOR = 10

        df = pd.DataFrame([[1, 'thing'], [2, 'notthing'], [3, 'thing']],
                          index=list('xyz'),
                          columns=['foo', 'units'])
        exp = pd.Series([10., 2., 30.], index=list('xyz'), name='foo')
        obs = normalize.apply(df)
        pdt.assert_series_equal(obs, exp)


if __name__ == '__main__':
    unittest.main()
