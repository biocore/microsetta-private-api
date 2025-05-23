import unittest
import pandas as pd
import pandas.testing as pdt
import datetime
from copy import copy, deepcopy
from werkzeug.exceptions import NotFound
from microsetta_private_api.repo.metadata_repo._constants import (
    HUMAN_SITE_INVARIANTS, UNSPECIFIED)
from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.repo.metadata_repo._repo import (
    _build_col_name,
    _find_duplicates,
    _fetch_barcode_metadata,
    _to_pandas_series,
    _to_pandas_dataframe,
    _fetch_survey_template,
    _fetch_observed_survey_templates,
    _construct_multiselect_map,
    _find_best_answers,
    drop_private_columns,
    _get_freetext_fields,
    _expand_ebi_remove_fields,
    EBI_REMOVE)
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo
from microsetta_private_api.model.account import Account
from microsetta_private_api.model.address import Address
from microsetta_private_api.repo.transaction import Transaction


class MM:
    """Mock model object"""
    def __init__(self, data):
        self.d = data

    def __getattr__(self, key):
        return self.d[key]

    def __getitem__(self, key):
        return self.d[key]


class MetadataUtilTests(unittest.TestCase):
    def setUp(self):
        self.raw_sample_1 = {
                'sample_barcode': '000004216',
                'host_subject_id': 'foo',
                'account': Account("foo",
                                   "foo@baz.com",
                                   "standard",
                                   "https://MOCKUNITTEST.com",
                                   "1234ThisIsNotARealSub",
                                   "NotDan",
                                   "NotH",
                                   Address(
                                       "123 Dan Lane",
                                       "NotDanville",
                                       "CA",
                                       12345,
                                       "US"
                                   ),
                                   32.8798916,
                                   -117.2363115,
                                   False,
                                   "en_US",
                                   True),
                'source': MM({'id': 'bar',
                              'source_type': 'human'}),
                "sample": MM({
                    "sample_projects": ["American Gut Project"],
                    "datetime_collected": "2013-10-15T09:30:00",
                    "site": "Stool",
                    "barcode_meta": {
                        "sample_site_last_washed_date": "01/10/2025"
                    }
                }),
                'survey_answers': [
                    {'template': 1,
                     'survey_timestamp': datetime.datetime(
                         2013,
                         10,
                         13,
                         9,
                         0,
                         0,
                         tzinfo=datetime.timezone(
                             datetime.timedelta(minutes=-420)
                         )
                     ),
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
                    {'template': 2,
                     'survey_timestamp': datetime.datetime(
                         2013,
                         10,
                         13,
                         9,
                         15,
                         0,
                         tzinfo=datetime.timezone(
                             datetime.timedelta(minutes=-420)
                         )
                     ),
                     'response': {'275': ['abc', 'okay'],
                                  '276': ['def', 'No']}}]}

        self.raw_sample_2 = {
                'sample_barcode': 'XY0004216',
                'host_subject_id': 'bar',
                'account': Account("foo",
                                   "foo@baz.com",
                                   "standard",
                                   "https://MOCKUNITTEST.com",
                                   "1234ThisIsNotARealSub",
                                   "NotDan",
                                   "NotH",
                                   Address(
                                       "123 Dan Lane",
                                       "NotDanville",
                                       "CA",
                                       12345,
                                       "US"
                                   ),
                                   32.8798916,
                                   -117.2363115,
                                   False,
                                   "en_US",
                                   True),
                'source': MM({'id': 'bonkers',
                              'source_type': 'human'}),
                "sample": MM({
                    "sample_projects": ["American Gut Project"],
                    "datetime_collected": "2013-10-15T09:30:00",
                    "site": "Stool",
                    "barcode_meta": {}
                }),
                'survey_answers': [
                    {'template': 1,
                     'survey_timestamp': datetime.datetime(
                         2013,
                         10,
                         13,
                         9,
                         15,
                         0,
                         tzinfo=datetime.timezone(
                             datetime.timedelta(minutes=-420)
                         )
                     ),
                     'response': {'1': ['DIET_TYPE', '["Vegan\nfoo"]'],
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

        self.raw_sample_17 = {
                'sample_barcode': 'XY0004216',
                'host_subject_id': 'bar',
                'account': MM({'id': 'baz'}),
                'source': MM({'id': 'bonkers',
                              'source_type': 'human'}),
                "sample": MM({
                    "sample_projects": ["American Gut Project"],
                    "datetime_collected": "2013-10-15T09:30:00",
                    "site": "Stool",
                    "barcode_meta": {}
                }),
                'survey_answers': [
                    {'template': SurveyTemplateRepo.DIET_ID,
                     'response': {'1': ['DIET_TYPE', '["Vegan\nfoo"]'],
                                  '2': ['MULTIVITAMIN', 'Yes'],
                                  '3': ['PROBIOTIC_FREQUENCY', 'Unspecified'],
                                  '4': ['VITAMIN_B_SUPPLEMENT_FREQUENCY',
                                        'Unspecified'],
                                  '5': ['VITAMIN_D_SUPPLEMENT_FREQUENCY',
                                        'Unspecified'],
                                  '6': ['OTHER_SUPPLEMENT_FREQUENCY', 'No'],
                                  '123': ['SAMPLE2SPECIFIC', 'foobar'],
                                  '433': ['FIBER_SUPPLEMENT_TYPES', [
                                          'Oat fiber', 'Apple fiber']]}}]}

        self.fake_survey_template1 = {
            'survey_template_text': MM({
                'groups': [
                    MM({'fields': [
                        MM({'id': "5",
                            'shortname': 'foo',
                            'multi': False,
                            'values': ['a', 'b', 'c']}),
                        MM({'id': "7",
                            'shortname': 'bar',
                            'multi': True,
                            'values': ['e', 'f', 'g  h']})
                        ]})]})}

        self.fake_survey_template2 = {
            'survey_template_text': MM({
                'groups': [
                    MM({'fields': [
                        MM({'id': "8",
                            'shortname': 'foo',
                            'multi': False,
                            'values': ['a', 'b', 'c']}),
                        MM({'id': "9",
                            'shortname': 'ALLERGIC_TO',
                            'multi': True,
                            'values': ['x', 'baz', 'stuff', 'blahblah']})
                        ]})]})}

        self.survey_responses_with_duplicate_questions = [
            {'template': 1,
             'survey_timestamp': datetime.datetime(
                 2013,
                 10,
                 13,
                 9,
                 0,
                 0,
                 tzinfo=datetime.timezone(datetime.timedelta(minutes=-420))
             ),
             'response': {'1': ['DIET_TYPE', '[""]'],
                          '2': ['MULTIVITAMIN', 'No'],
                          '3': ['PROBIOTIC_FREQUENCY', 'Unspecified'],
                          '4': ['VITAMIN_B_SUPPLEMENT_FREQUENCY',
                                'Unspecified'],
                          '5': ['VITAMIN_D_SUPPLEMENT_FREQUENCY',
                                'Unspecified'],
                          '6': ['OTHER_SUPPLEMENT_FREQUENCY', 'No'],
                          '9': ['ALLERGIC_TO', ['blahblah',
                                                'stuff']],
                          '22': ['DOMINANT_HAND', 'Unspecified'],
                          '110': ['COUNTRY_OF_BIRTH', 'Unspecified'],
                          '111': ['BIRTH_MONTH', 'Unspecified']
                          }
             },
            {'template': 10,
             'survey_timestamp': datetime.datetime(
                 2022,
                 12,
                 20,
                 9,
                 15,
                 0,
                 tzinfo=datetime.timezone(datetime.timedelta(minutes=-420))
             ),
             'response': {'22': ['DOMINANT_HAND', 'I am right handed'],
                          '110': ['COUNTRY_OF_BIRTH', 'United States'],
                          '111': ['BIRTH_MONTH', 'June']
                          }
             }
        ]

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
        exp = {1: {'survey_id': None,
                   'survey_status': None,
                   'survey_template_id': 1,
                   'survey_template_title': 'Primary Questionnaire',
                   'survey_template_type': 'local',
                   'survey_template_version': '1.0',
                   'percentage_completed': None},
               2: {'survey_id': None,
                   'survey_status': None,
                   'survey_template_id': 2,
                   'survey_template_title': 'Pet Information',
                   'survey_template_type': 'local',
                   'survey_template_version': '1.0',
                   'percentage_completed': None}}

        obs, errors = _fetch_observed_survey_templates([self.raw_sample_1,
                                                        self.raw_sample_2])
        # concern here is that this key exists, not its content
        for o in obs.values():
            o.pop('survey_template_text')
        self.assertEqual(obs, exp)
        self.assertEqual(errors, None)

    def test_fetch_survey_template(self):
        exp = {'survey_id': None,
               'survey_status': None,
               'survey_template_id': SurveyTemplateRepo.BASIC_INFO_ID,
               'survey_template_title': 'Basic Information',
               'survey_template_type': 'local',
               'survey_template_version': '1.0',
               'percentage_completed': None}
        survey, errors = _fetch_survey_template(
            SurveyTemplateRepo.BASIC_INFO_ID)

        # concern here is that this key exists, not its content
        survey.pop('survey_template_text')

        # verify we obtained data. it is not the responsibility of this
        # test to assert the structure of the metadata as that is the scope of
        # the admin interfaces on the private API
        self.assertEqual(survey, exp)
        self.assertEqual(errors, None)

    def test_fetch_survey_template_remote(self):
        # attempt to fetch info for Vioscreen survey
        survey, errors = _fetch_survey_template(
            SurveyTemplateRepo.VIOSCREEN_ID)

        # verify that _fetch_survey_template returns an error, reflecting
        # that it's a remote survey for which we can't extract local data
        self.assertNotEqual(errors, None)

    def test_drop_private_columns(self):
        df = pd.DataFrame([[1, 2, 3], [4, 5, 6]],
                          columns=['pM_foo', 'okay', 'ABOUT_yourSELF_TEXT'])
        exp = pd.DataFrame([[2, ], [5, ]], columns=['okay'])
        obs = drop_private_columns(df)
        pdt.assert_frame_equal(obs, exp)

    def test_drop_private_columns_freetext(self):
        # This test specifically asserts that the new code to drop free-text
        # fields works, even if those fields are not represented in the
        # EBI_REMOVE list

        # First, assert that ALL_ROOMMATES is not in EBI_REMOVE
        self.assertFalse("ALL_ROOMMATES" in EBI_REMOVE)

        # Next, assert that ALL_ROOMMATES is a free-text field
        freetext_fields = _get_freetext_fields()
        self.assertTrue("ALL_ROOMMATES" in freetext_fields)

        # Now, set up a test dataframe, based on the existing
        # test_drop_private_columns df, but with the ALL_ROOMMATES field added
        df = pd.DataFrame([[1, 2, 3, 4], [5, 6, 7, 8]],
                          columns=[
                              'pM_foo',
                              'okay',
                              'ABOUT_yourSELF_TEXT',
                              'ALL_ROOMMATES'])

        # We only expect the "okay" column to remain
        exp = pd.DataFrame([[2, ], [6, ]], columns=['okay'])
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
        obs, obs_errors = _fetch_barcode_metadata('000001656')

        # verify we obtained metadata. it is not the responsibility of this
        # test to assert the structure of the metadata as that is the scope of
        # the admin interfaces on the private API

        self.assertEqual(obs['sample_barcode'], '000001656')
        self.assertEqual(obs_errors, None)

    def test_fetch_barcode_metadata_missing(self):
        with self.assertRaises(NotFound):
            _fetch_barcode_metadata('badbarcode')

    def test_fetch_valid_unlinked_barcode(self):
        with self.assertRaises(RepoException):
            _fetch_barcode_metadata('000004126')

    def test_to_pandas_dataframe(self):
        data = [self.raw_sample_1, self.raw_sample_2]
        templates = {1: self.fake_survey_template2}

        exp = pd.DataFrame([['000004216', 'foo', UNSPECIFIED, 'No',
                             UNSPECIFIED, UNSPECIFIED, UNSPECIFIED, 'No',
                             'true', 'true', 'false', 'false',
                             UNSPECIFIED,
                             'okay', 'No', "2013-10-15T09:30:00", '000004216',
                             'US:CA', 'CA', '33', '-117', '01/10/2025'],
                            ['XY0004216', 'bar', 'Vegan foo', 'Yes',
                             UNSPECIFIED, UNSPECIFIED, UNSPECIFIED,
                             'No', 'false', 'true', 'true', 'false',
                             'foobar', UNSPECIFIED, UNSPECIFIED,
                             "2013-10-15T09:30:00", 'XY0004216',
                             'US:CA', 'CA', '33', '-117', 'not provided']],
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
                                    'collection_timestamp',
                                    'anonymized_name', 'geo_loc_name',
                                    'state', 'latitude', 'longitude',
                                    'sample_site_last_washed_date']
                           ).set_index('sample_name')

        for k, v in HUMAN_SITE_INVARIANTS['Stool'].items():
            exp[k] = v

        err, obs = _to_pandas_dataframe(data, templates)
        pdt.assert_frame_equal(obs, exp, check_like=True)
        self.assertEqual(err, [])

    def test_to_pandas_dataframe_site_sampled_bug(self):
        raw_sample_3 = copy(self.raw_sample_1)
        raw_sample_3['sample'].d['site'] = 'Fur'
        data = [raw_sample_3, ]

        templates = {1: self.fake_survey_template2}
        err, obs = _to_pandas_dataframe(data, templates)

        self.assertEqual(len(obs), 0)
        self.assertEqual(len(err), 1)
        self.assertIn(raw_sample_3['sample_barcode'], err[0])

    def test_to_pandas_series(self):
        data = self.raw_sample_1

        values = ['foo', '', 'No', 'Unspecified', 'Unspecified',
                  'Unspecified', 'No', 'true', 'true', 'false',
                  'false', 'okay', 'No',
                  '2013-10-15T09:30:00', 'US:CA', 'CA', '33', '-117',
                  '01/10/2025']
        index = ['HOST_SUBJECT_ID', 'DIET_TYPE', 'MULTIVITAMIN',
                 'PROBIOTIC_FREQUENCY', 'VITAMIN_B_SUPPLEMENT_FREQUENCY',
                 'VITAMIN_D_SUPPLEMENT_FREQUENCY',
                 'OTHER_SUPPLEMENT_FREQUENCY',
                 'ALLERGIC_TO_blahblah', 'ALLERGIC_TO_stuff', 'ALLERGIC_TO_x',
                 'ALLERGIC_TO_baz', 'abc', 'def',
                 'COLLECTION_TIMESTAMP', 'GEO_LOC_NAME', 'STATE', 'LATITUDE',
                 'LONGITUDE', 'sample_site_last_washed_date']

        for k, v in HUMAN_SITE_INVARIANTS['Stool'].items():
            values.append(v)
            index.append(k)

        templates = {10: self.fake_survey_template1,
                     1: self.fake_survey_template2}

        ms_map = _construct_multiselect_map(templates)
        exp = pd.Series(values, index=index, name='000004216')
        obs = _to_pandas_series(data, ms_map)
        pdt.assert_series_equal(obs, exp.loc[obs.index])

    def test_to_pandsa_series_non_human_site(self):
        data = self.raw_sample_1
        data['sample'].d['site'] = 'Fur'

        templates = {10: self.fake_survey_template1,
                     1: self.fake_survey_template2}

        ms_map = _construct_multiselect_map(templates)
        with self.assertRaises(RepoException):
            _to_pandas_series(data, ms_map)

    def test_find_best_answers(self):
        # this test verifies that the _find_best_answers() function uses a
        # given sample date to preserve the closest instance of each survey
        # question and discard all other instances of the given question
        data = deepcopy(self.survey_responses_with_duplicate_questions)
        data_2 = deepcopy(self.survey_responses_with_duplicate_questions)

        # the test data we'll use contains a subset of the old primary survey
        # and a subset of the new basic info survey. when we test with an old
        # sample collection date, we should observe the answers from the old
        # primary survey being returned and that the same questions no longer
        # exist on the new basic info survey
        obs = _find_best_answers(
            data,
            "2013-10-15T09:30:00"
        )

        # make sure that the three shared questions reflect the old answer
        self.assertEqual(obs[0]['response']['22'],
                         ['DOMINANT_HAND', 'Unspecified'])
        self.assertEqual(obs[0]['response']['110'],
                         ['COUNTRY_OF_BIRTH', 'Unspecified'])
        self.assertEqual(obs[0]['response']['111'],
                         ['BIRTH_MONTH', 'Unspecified'])

        # and verify that they don't exist in the newer survey
        with self.assertRaises(KeyError):
            _ = obs[1]['response']['22']
        with self.assertRaises(KeyError):
            _ = obs[1]['response']['110']
        with self.assertRaises(KeyError):
            _ = obs[1]['response']['111']

        # now, we're going to repeat the exercise with a newer collection date
        # and observe the opposite results
        obs = _find_best_answers(
            data_2,
            "2022-12-30T09:30:00"
        )

        # make sure that the three shared questions reflect the new answer
        self.assertEqual(obs[1]['response']['22'],
                         ['DOMINANT_HAND', 'I am right handed'])
        self.assertEqual(obs[1]['response']['110'],
                         ['COUNTRY_OF_BIRTH', 'United States'])
        self.assertEqual(obs[1]['response']['111'], ['BIRTH_MONTH', 'June'])

        # and verify that they don't exist in the old survey
        with self.assertRaises(KeyError):
            _ = obs[0]['response']['22']
        with self.assertRaises(KeyError):
            _ = obs[0]['response']['110']
        with self.assertRaises(KeyError):
            _ = obs[0]['response']['111']

    def test_get_freetext_fields(self):
        with Transaction() as t:
            with t.cursor() as cur:
                # Grab the count for the number of free-text fields that exist
                # in the database
                cur.execute(
                    "SELECT COUNT(*) "
                    "FROM ag.survey_question_response_type "
                    "WHERE survey_response_type IN ('TEXT', 'STRING')"
                )
                row = cur.fetchone()
                freetext_count = row[0]

        # Use the _get_freetext_fields() function to pull the actual list
        freetext_fields = _get_freetext_fields()

        # Assert that the field count matches
        self.assertEqual(len(freetext_fields), freetext_count)

        # Assert that a few known free-text fields exist in the list
        self.assertTrue("ABOUT_YOURSELF_TEXT" in freetext_fields)
        self.assertTrue("ALL_ROOMMATES" in freetext_fields)
        self.assertTrue("DIET_RESTRICTIONS" in freetext_fields)

    def test_expand_ebi_remove_fields(self):
        # First, let's assert that normal single-response fields are passed
        # through as expected
        col_names = ['ACNE_MEDICATION_OTC', 'SKIN_COLOR']
        obs = _expand_ebi_remove_fields(col_names)
        self.assertEqual(col_names, obs)

        # Next, let's confirm that a multiselect field is expanded to include
        # all options, and that the root question name is kept as well
        col_names = ['SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES']
        exp = [
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Abdomen',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Armpits',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Arms',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Back',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Chest',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Elbows',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Face',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Feet',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Hands',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Knees',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Legs',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Neck',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Other',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Scalp',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Unspecified'
        ]
        obs = _expand_ebi_remove_fields(col_names)
        self.assertEqual(obs, exp)

        # And lastly, confirm that a combination of single-response and
        # multiselect fields works as expected
        col_names = [
            'ACNE_MEDICATION_OTC',
            'SKIN_COLOR',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES'
        ]
        exp = [
            'ACNE_MEDICATION_OTC',
            'SKIN_COLOR',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Abdomen',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Armpits',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Arms',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Back',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Chest',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Elbows',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Face',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Feet',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Hands',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Knees',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Legs',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Neck',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Other',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Scalp',
            'SKIN_CONDITIONS_RECENT_ACNE_BODY_SITES_Unspecified'
        ]
        obs = _expand_ebi_remove_fields(col_names)
        self.assertEqual(obs, exp)


if __name__ == '__main__':
    unittest.main()
