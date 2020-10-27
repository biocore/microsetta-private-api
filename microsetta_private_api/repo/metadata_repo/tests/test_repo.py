import unittest
import json
import pandas as pd
import pandas.testing as pdt
from microsetta_private_api.repo.metadata_repo._constants import (
    HUMAN_SITE_INVARIANTS, MISSING_VALUE)
from microsetta_private_api.repo.metadata_repo._repo import (
    _build_col_name,
    _find_duplicates,
    _fetch_barcode_metadata,
    _to_pandas_series,
    _to_pandas_dataframe,
    _fetch_survey_template,
    _fetch_observed_survey_templates,
    _construct_multiselect_map,
    drop_private_columns)


class MetadataUtilTests(unittest.TestCase):
    def setUp(self):
        self.raw_sample_1 = {
                'sample_barcode': '000004216',
                'host_subject_id': 'foo',
                'account': {'id': 'foo'},
                'source': {'id': 'bar',
                           'source_type': 'human'},
                "sample": {
                    "sample_projects": ["American Gut Project"],
                    "datetime_collected": "2013-10-15T09:30:00",
                    "site": "Stool"
                },
                'survey_answers': [
                    {'template': 1,
                     'response': {'1': ['DIET_TYPE', '[""]'],
                                  '2': ['MULTIVITAMIN', 'No'],
                                  '3': ['PROBIOTIC_FREQUENCY', 'Unspecified'],
                                  '4': ['VITAMIN_B_SUPPLEMENT_FREQUENCY',
                                        'Unspecified'],
                                  '5': ['VITAMIN_D_SUPPLEMENT_FREQUENCY',
                                        'Unspecified'],
                                  '6': ['OTHER_SUPPLEMENT_FREQUENCY', 'No'],
                                  '9': ['ALLERGIC_TO', ['blahblah',
                                                        'stuff']]}},
                    {'template': 10,
                     'response': {'1': ['abc', 'okay'],
                                  '2': ['def', 'No']}}]}

        self.raw_sample_2 = {
                'sample_barcode': 'XY0004216',
                'host_subject_id': 'bar',
                'account': {'id': 'baz'},
                'source': {'id': 'bonkers',
                           'source_type': 'human'},
                "sample": {
                    "sample_projects": ["American Gut Project"],
                    "datetime_collected": "2013-10-15T09:30:00",
                    "site": "Stool"
                },
                'survey_answers': [
                    {'template': 1,
                     'response': {'1': ['DIET_TYPE', '["Vegan"]'],
                                  '2': ['MULTIVITAMIN', 'Yes'],
                                  '3': ['PROBIOTIC_FREQUENCY', 'Unspecified'],
                                  '4': ['VITAMIN_B_SUPPLEMENT_FREQUENCY',
                                        'Unspecified'],
                                  '5': ['VITAMIN_D_SUPPLEMENT_FREQUENCY',
                                        'Unspecified'],
                                  '6': ['OTHER_SUPPLEMENT_FREQUENCY', 'No'],
                                  '123': ['SAMPLE2SPECIFIC', 'foobar'],
                                  '9': ['ALLERGIC_TO', ['baz',
                                                        'stuff']]}}]}

        self.fake_survey_template1 = {
            'survey_template_text': {
                'groups': [
                    {'fields': [
                        {'id': "5",
                         'shortname': 'foo',
                         'multi': False,
                         'values': ['a', 'b', 'c']},
                        {'id': "7",
                         'shortname': 'bar',
                         'multi': True,
                         'values': ['e', 'f', 'g  h']}
                        ]}]}}

        self.fake_survey_template2 = {
            'survey_template_text': {
                'groups': [
                    {'fields': [
                        {'id': "8",
                         'shortname': 'foo',
                         'multi': False,
                         'values': ['a', 'b', 'c']},
                        {'id': "9",
                         'shortname': 'ALLERGIC_TO',
                         'multi': True,
                         'values': ['x', 'baz', 'stuff', 'blahblah']}
                        ]}]}}

        super().setUp()

    def test_construct_multiselect_map(self):
        templates = {1: self.fake_survey_template1,
                     2: self.fake_survey_template2}
        exp = {(1, '7'): {'e': 'bar_e',
                          'f': 'bar_f',
                          'g  h': 'bar_g__h'},
               (2, '9'): {'x': 'ALLERGIC_TO_x',
                          'baz': 'ALLERGIC_TO_baz',
                          'stuff': 'ALLERGIC_TO_stuff',
                          'blahblah': 'ALLERGIC_TO_blahblah'}}
        obs = _construct_multiselect_map(templates)
        self.assertEqual(obs, exp)

    def test_fetch_observed_survey_templates(self):
        res = {'a': 'dict', 'of': 'stuff'}
        self.mock_get.return_value.status_code = 200
        self.mock_get.return_value.json = lambda: res
        self.mock_get.return_value.text = json.dumps(res)

        exp = {1: res, 10: res}
        obs, errors = _fetch_observed_survey_templates([self.raw_sample_1,
                                                        self.raw_sample_2])

        self.assertEqual(obs, exp)
        self.assertEqual(errors, None)

    def test_fetch_survey_template(self):
        res = {'a': 'dict', 'of': 'stuff'}
        self.mock_get.return_value.status_code = 200
        self.mock_get.return_value.json = lambda: res
        self.mock_get.return_value.text = json.dumps(res)

        survey, errors = _fetch_survey_template(1, {'account_id': 'foo',
                                                    'source_id': 'bar'})

        # verify we obtained data. it is not the responsibility of this
        # test to assert the structure of the metadata as that is the scope of
        # the admin interfaces on the private API
        self.assertEqual(survey, res)
        self.assertEqual(errors, None)

    def test_drop_private_columns(self):
        df = pd.DataFrame([[1, 2, 3], [4, 5, 6]],
                          columns=['pM_foo', 'okay', 'ABOUT_yourSELF_TEXT'])
        exp = pd.DataFrame([[2, ], [5, ]], columns=['okay'])
        obs = drop_private_columns(df)
        pdt.assert_frame_equal(obs, exp)

    def test_build_col_name(self):
        tests_and_expected = [('foo', 'bar', 'foo_bar'),
                              ('foo', 'bar baz', 'foo_bar_baz')]
        for col_name, value, exp in tests_and_expected:
            obs = _build_col_name(col_name, value)
            self.assertEqual(obs, exp)

    def test_find_duplicates(self):
        exp = {'foo', 'bar'}
        exp_errors = {'barcode': ['foo', 'bar'],
                      'error': "Duplicated barcodes in input"}
        obs, errors = _find_duplicates(['foo', 'bar', 'foo', 'bar', 'baz'])
        self.assertEqual(obs, exp)
        self.assertEqual(sorted(errors['barcode']),
                         sorted(exp_errors['barcode']))

        exp = set()
        obs, errors = _find_duplicates(['foo', 'bar'])
        self.assertEqual(obs, exp)
        self.assertEqual(errors, None)

    def test_fetch_barcode_metadata(self):
        res = {'sample_barcode': '000004216'}
        self.mock_get.return_value.status_code = 200
        self.mock_get.return_value.json = lambda: res
        self.mock_get.return_value.text = json.dumps(res)

        obs, obs_errors = _fetch_barcode_metadata('000004216')

        # verify we obtained metadata. it is not the responsibility of this
        # test to assert the structure of the metadata as that is the scope of
        # the admin interfaces on the private API
        self.assertEqual(obs['sample_barcode'], '000004216')
        self.assertEqual(obs_errors, None)

    def test_fetch_barcode_metadata_missing(self):
        res = {}
        self.mock_get.return_value.status_code = 404
        self.mock_get.return_value.json = lambda: res
        self.mock_get.return_value.text = json.dumps(res)

        obs, obs_errors = _fetch_barcode_metadata('badbarcode')
        self.assertNotIn('sample_barcode', obs)
        self.assertEqual(obs_errors, {'barcode': 'badbarcode',
                                      'error': "404 from api"})

    def test_to_pandas_dataframe(self):
        data = [self.raw_sample_1, self.raw_sample_2]
        templates = {1: self.fake_survey_template2}

        exp = pd.DataFrame([['000004216', 'foo', MISSING_VALUE, 'No',
                             'Unspecified', 'Unspecified', 'Unspecified', 'No',
                             'true', 'true', 'false', 'false',
                             MISSING_VALUE,
                             'okay', 'No', "2013-10-15T09:30:00"],
                            ['XY0004216', 'bar', 'Vegan', 'Yes', 'Unspecified',
                             'Unspecified', 'Unspecified', 'No',
                             'false', 'true', 'true', 'false', 'foobar',
                             MISSING_VALUE,
                             MISSING_VALUE,
                             "2013-10-15T09:30:00"]],
                           columns=['sample_name', 'host_subject_id',
                                    'diet_type', 'multivitamin',
                                    'probiotic_frequency',
                                    'vitamin_b_supplement_frequency',
                                    'vitamin_d_supplement_frequency',
                                    'other_supplement_frequency',
                                    'allergic_to_blahblah',
                                    'allergic_to_stuff', 'allergic_to_baz',
                                    'allergic_to_x',
                                    'sample2specific', 'abc', 'def',
                                    'collection_timestamp']
                           ).set_index('sample_name')

        for k, v in HUMAN_SITE_INVARIANTS['Stool'].items():
            exp[k] = v

        obs = _to_pandas_dataframe(data, templates)
        pdt.assert_frame_equal(obs, exp, check_like=True)

    def test_to_pandas_series(self):
        data = self.raw_sample_1

        values = ['foo', '', 'No', 'Unspecified', 'Unspecified',
                  'Unspecified', 'No', 'true', 'true', 'okay', 'No',
                  "2013-10-15T09:30:00"]
        index = ['HOST_SUBJECT_ID', 'DIET_TYPE', 'MULTIVITAMIN',
                 'PROBIOTIC_FREQUENCY', 'VITAMIN_B_SUPPLEMENT_FREQUENCY',
                 'VITAMIN_D_SUPPLEMENT_FREQUENCY',
                 'OTHER_SUPPLEMENT_FREQUENCY',
                 'ALLERGIC_TO_blahblah', 'ALLERGIC_TO_stuff', 'abc', 'def',
                 'COLLECTION_TIMESTAMP']

        for k, v in HUMAN_SITE_INVARIANTS['Stool'].items():
            values.append(v)
            index.append(k)

        templates = {10: self.fake_survey_template1,
                     1: self.fake_survey_template2}

        ms_map = _construct_multiselect_map(templates)
        exp = pd.Series(values, index=index, name='000004216')
        obs = _to_pandas_series(data, ms_map)
        pdt.assert_series_equal(obs, exp.loc[obs.index])


if __name__ == '__main__':
    unittest.main()
