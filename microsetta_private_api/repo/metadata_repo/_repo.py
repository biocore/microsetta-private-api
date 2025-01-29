from ._constants import HUMAN_SITE_INVARIANTS, MISSING_VALUE, UNSPECIFIED
from ._transforms import HUMAN_TRANSFORMS, apply_transforms
from ..admin_repo import AdminRepo
from ..survey_template_repo import SurveyTemplateRepo
from ..transaction import Transaction
from ...exceptions import RepoException
from ...util import vue_adapter

from werkzeug.exceptions import NotFound
from collections import Counter
import re
import pandas as pd
import numpy as np
import json
import pytz
import datetime
jsonify = json.dumps

# the vioscreen survey currently cannot be fetched from the database
# there seems to be some detached survey IDs -- see 000089779
# that account has a long and unusual history though
# Adding the MyFoodRepo, Polyphenol FFQ, and Spain FFQs to the
# ignore list.
# do not add legacy template_ids (1-7) to this dict at this time.
# there are users of this dict that process valid grabs on legacy template
# dagta.
TEMPLATES_TO_IGNORE = {SurveyTemplateRepo.VIOSCREEN_ID,
                       SurveyTemplateRepo.MYFOODREPO_ID,
                       SurveyTemplateRepo.POLYPHENOL_FFQ_ID,
                       SurveyTemplateRepo.SPAIN_FFQ_ID,
                       None}

# TODO 2022-10-03
# Adding questions from Cooking Oils & Oxalate-rich Foods survey
# to ignore list as they don't exist in Qiita (OILS_*). We're blocked on
# pushing them, pending an update to Qiita's API.
EBI_REMOVE = ['ABOUT_YOURSELF_TEXT', 'ANTIBIOTIC_CONDITION',
              'ANTIBIOTIC_MED', 'PM_NAME', 'PM_EMAIL',
              'BIRTH_MONTH', 'CAT_CONTACT', 'CAT_LOCATION',
              'CONDITIONS_MEDICATION', 'DIET_RESTRICTIONS_LIST',
              'DOG_CONTACT', 'HUMANS_FREE_TEXT', 'NAME',
              'DOG_LOCATION', 'GENDER', 'MEDICATION_LIST',
              'OTHER_CONDITIONS_LIST', 'PREGNANT_DUE_DATE',
              'RACE_OTHER',
              'RELATIONSHIPS_WITH_OTHERS_IN_STUDY',
              'SPECIAL_RESTRICTIONS',
              'SUPPLEMENTS', 'TRAVEL_LOCATIONS_LIST', 'ZIP_CODE',
              'WILLING_TO_BE_CONTACTED', 'pets_other_freetext',
              'ANIMAL_FREE_TEXT', 'ANIMAL_TYPE_FREE_TEXT',
              'COVID_OCCUPATION', 'COVID_SUSPECTED_POSITIVE_DATE',
              'COVID_SYMPTOMS_OTHER', 'FERMENTED_CONSUMED_OTHER',
              'FERMENTED_OTHER', 'FERMENTED_PRODUCE_COMMERCIAL_OTHER',
              'FERMENTED_PRODUCE_PERSONAL_OTHER',
              'OTHER_ANIMALS_FREE_TEXT', 'OILS_FREQUENCY_VEGETABLE',
              'OILS_FREQUENCY_ANIMAL', 'OILS_FREQUENCY_OTHER',
              'OILS_FREQUENCY_MARGARINE', 'OILS_FREQUENCY_OXALATE'
              'OILS_FREQUENCY_SOY']


def drop_private_columns(df):
    """Remove columns that should not be shared publicly

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe to operate on

    Returns
    -------
    pd.DataFrame
        The filtered dataframe
    """
    # The personal microbiome survey contains additional fields that are
    # sensitive in nature
    pm_remove = {c.lower() for c in df.columns if c.lower().startswith('pm_')}

    freetext_fields = {c.lower() for c in _get_freetext_fields()}

    remove = pm_remove | {c.lower() for c in EBI_REMOVE} | freetext_fields
    to_drop = [c for c in df.columns if c.lower() in remove]

    return df.drop(columns=to_drop, inplace=False)


def retrieve_metadata(sample_barcodes, include_private=False):
    """Retrieve all sample metadata for the provided barcodes

    Parameters
    ----------
    sample_barcodes : Iterable
        The barcodes to request
    include_private : bool, optional
        If true, retain private columns

    Returns
    -------
    pd.DataFrame
        A DataFrame representation of the sample metadata.
    list of dict
        A report of the observed errors in the metadata pulldown. The dicts
        are composed of {"barcode": list of str | str, "error": str}.
    """
    error_report = []

    dups, errors = _find_duplicates(sample_barcodes)
    if errors is not None:
        error_report.append(errors)

    fetched = []
    for sample_barcode in set(sample_barcodes):
        try:
            bc_md, errors = _fetch_barcode_metadata(sample_barcode)
        except RepoException as e:
            errors = e.args[0]
        except NotFound as e:
            errors = e.description

        if errors is not None:
            error_report.append({sample_barcode: errors})
            continue

        fetched.append(bc_md)

    df = pd.DataFrame()
    if len(fetched) == 0:
        error_report.append({"error": "No metadata was obtained"})
    else:
        survey_templates, st_errors = _fetch_observed_survey_templates(fetched)
        if st_errors is not None:
            error_report.append(st_errors)
        else:
            df_errors, df = _to_pandas_dataframe(fetched, survey_templates)
            if df_errors:
                error_report.extend(df_errors)

    if not include_private:
        df = drop_private_columns(df)

    return df, error_report


def _fetch_observed_survey_templates(sample_metadata):
    """Determine which templates to obtain and then fetch

    Parameters
    ----------
    sample_metadata : list of dict
        Each element corresponds to the structure obtained from
        _fetch_barcode_metadata

    Returns
    -------
    dict
        The survey template IDs as keys, and the Vue form representation of
        each survey
    dict or None
        Any error information associated with the retreival. If an error is
        observed, the survey responses should not be considered valid.
    """
    errors = {}

    templates = {}
    for bc_md in sample_metadata:
        account_id = bc_md['account'].id
        source_id = bc_md['source'].id
        observed_templates = {s['template'] for s in bc_md['survey_answers']
                              if s['template'] not in TEMPLATES_TO_IGNORE}

        # it doesn't matter which set of IDs we use but they need to be valid
        # for the particular survey template
        for template_id in observed_templates:
            if template_id not in templates:
                templates[template_id] = {'account_id': account_id,
                                          'source_id': source_id}

    surveys = {}
    for template_id, ids in templates.items():
        survey, error = _fetch_survey_template(template_id)
        if error:
            errors[template_id] = error
        else:
            surveys[template_id] = survey

    return surveys, errors if errors else None


def _fetch_survey_template(template_id):
    """Fetch the survey structure to get full multi-choice detail

    Parameters
    ----------
    template_id : int
        The survey template ID to fetch

    Returns
    -------
    dict
        The survey structure as returned from the private API
    string or None
        Any error information associated with the retreival. If an error is
        observed, the survey responses should not be considered valid.
    """
    with Transaction() as t:
        error = None

        survey_template_repo = SurveyTemplateRepo(t)
        info = survey_template_repo.get_survey_template_link_info(
            template_id)

        # For local surveys, we generate the json representing the survey
        try:
            survey_template = survey_template_repo.get_survey_template(
                template_id, "en_US")
        except NotFound as e:
            error = repr(e)

        if error is None:
            survey_template_text = vue_adapter.to_vue_schema(survey_template)

            info = info.to_api(None, None, None)
            info['survey_template_text'] = survey_template_text

        return info, error


def _to_pandas_dataframe(metadatas, survey_templates):
    """Convert the raw barcode metadata into a DataFrame

    Parameters
    ----------
    metadatas : list of dict
        The raw metadata obtained from the private API
    survey_templates : dict
        Raw survey template data for the surveys represented by
        the metadatas

    Returns
    -------
    pd.DataFrame
        The fully constructed sample metadata
    """
    errors = []
    transformed = []

    multiselect_map = _construct_multiselect_map(survey_templates)

    for metadata in metadatas:
        metadata['survey_answers'] = _find_best_answers(
            metadata['survey_answers'],
            metadata['sample'].datetime_collected
        )

        # metadata is a dict representing a barcode's metadata.
        try:
            as_series = _to_pandas_series(metadata, multiselect_map)
        except RepoException as e:
            barcode = metadata['sample_barcode']
            errors.append({barcode: repr(e)})
        else:
            transformed.append(as_series)

    df = pd.DataFrame(transformed)
    df.index.name = 'sample_name'
    df['anonymized_name'] = list(df.index)
    included_columns = set(df.columns)

    all_multiselect_columns = {v for ms in multiselect_map.values()
                               for v in ms.values()}

    # for all reported multiselect columns, remap "null" values to
    # false
    for column in all_multiselect_columns & included_columns:
        df.loc[df[column].isnull(), column] = 'false'

    # Add an entry for all multiselect columns which were not reported.
    # Since no answers were collected, it's inappropriate to use 'false.'
    # Instead, we'll use the MISSING_VALUE constant.
    for column in all_multiselect_columns - set(df.columns):
        df[column] = MISSING_VALUE

    # force a consistent case
    df.rename(columns={c: c.lower() for c in df.columns},
              inplace=True)

    # remap the empty string to null so it is picked up by
    # fillna
    df.replace("", np.nan, inplace=True)
    df.replace(r'\n',  ' ', regex=True, inplace=True)
    df.replace(r'\r',  ' ', regex=True, inplace=True)

    # fill in any other nulls that may be present in the frame
    # as could happen if not all individuals took all surveys.
    # human samples get UNSPECIFIED. Everything else is missing.
    if 'host_taxid' in df.columns:
        # host_taxid is not assured to be present if all samples are
        # environmental
        human_mask = df['host_taxid'] == '9606'
        df.loc[human_mask] = df.loc[human_mask].fillna(UNSPECIFIED)
    df.fillna(MISSING_VALUE, inplace=True)

    # We have values of 'Unspecified' coming out of the database, which is
    # inappropriate to push to Qiita. We'll replace them with the UNSPECIFIED
    # constant as the last step of creating the dataframe
    df.replace("Unspecified", UNSPECIFIED, inplace=True)

    return errors, apply_transforms(df, HUMAN_TRANSFORMS)


def _find_best_answers(survey_responses, sample_ts):
    if isinstance(sample_ts, str):
        sample_ts = datetime.datetime.strptime(sample_ts, "%Y-%m-%dT%H:%M:%S")
    pst = pytz.timezone('US/Pacific')
    sample_ts = pst.localize(sample_ts)

    # we need to keep a list of the closest temporal answers to compare as
    # we iterate through the survey responses
    best_ts = {}

    # we also need to keep a list of what we're going to discard
    answers_discard = {}
    for survey in survey_responses:
        for qid, answer in survey['response'].items():
            if qid in best_ts:
                # we already have a response for this question, so we need to
                # compare the timestamps
                cur_time_diff = abs(
                    (best_ts[qid][1] - sample_ts).total_seconds()
                )
                new_time_diff = abs(
                    (survey['survey_timestamp'] - sample_ts).total_seconds()
                )

                if new_time_diff < cur_time_diff:
                    # found a closer temporal response for the question

                    # first, mark the old "best" question for discard

                    # if we're already discarding questions for that template
                    # we just append this question id
                    if best_ts[qid][0] in answers_discard:
                        answers_discard[best_ts[qid][0]].append(qid)
                    # otherwise, we start a new list
                    else:
                        answers_discard[best_ts[qid][0]] = [qid]

                    # then set the new "best" question
                    best_ts[qid] = (
                        survey['template'],
                        survey['survey_timestamp']
                    )
                else:
                    # this isn't the best answer, so we need to discard it
                    if survey['template'] in answers_discard:
                        answers_discard[survey['template']].append(qid)
                    else:
                        answers_discard[survey['template']] = [qid]
            else:
                # we don't have a response for this question stored yet, so
                # we mark it as our best available
                best_ts[qid] = (
                    survey['template'],
                    survey['survey_timestamp']
                )

    cleaned_surveys = []
    for survey in survey_responses:
        if survey['template'] in answers_discard:
            for qid in answers_discard[survey['template']]:
                survey['response'].pop(qid, None)
        cleaned_surveys.append(survey)

    return cleaned_surveys


def _construct_multiselect_map(survey_templates):
    """Identify multi-select questions, and construct stable names

    Parameters
    ----------
    survey_templates : dict
        Raw survey template data for the surveys represented by
        the metadatas

    Returns
    -------
    dict
        A dict keyed by (template_id, question_id) and valued by
    """
    result = {}
    for template_id, template in survey_templates.items():
        template_text = template['survey_template_text']

        for group in template_text.groups:
            for field in group.fields:
                # some vues are apparently missing values property
                # assert hasattr(field, 'values')
                if not field.multi:
                    continue

                base = field.shortname
                choices = field.values
                qid = field.id

                multi_values = {}
                for choice in choices:
                    # if someone selects the "other", it's not interesting
                    # metadata, and the actual interesting piece is the
                    # free text they enter
                    if choice.lower() == 'other':
                        continue

                    new_shortname = _build_col_name(base, choice)
                    multi_values[choice] = new_shortname

                result[(template_id, qid)] = multi_values

    return result


def _to_pandas_series(metadata, multiselect_map):
    """Convert the sample metadata object from the private API to a pd.Series

    Parameters
    ----------
    metadata : dict
        The response object from a query to fetch all sample metadata for a
        barcode.
    multiselect_map : dict
        A dict keyed by (template_id, question_id) and valued by
        {"response": "column_name"}. This is used to remap multiselect values
        to stable fields.

    Returns
    -------
    pd.Series
        The transformed responses
    set
        Observed multi-selection responses
    """
    name = metadata['sample_barcode']
    hsi = metadata['host_subject_id']
    source_type = metadata['source'].source_type

    geo_state = metadata['account'].address.state

    if metadata['account'].address.country_code is None:
        geo_loc_name = MISSING_VALUE
    else:
        geo_loc_name = metadata['account'].address.country_code
        if geo_state is not None:
            geo_loc_name += ":" + geo_state

    if metadata['account'].latitude is None:
        latitude = MISSING_VALUE
    else:
        latitude = str(int(round(metadata['account'].latitude)))

    if metadata['account'].longitude is None:
        longitude = MISSING_VALUE
    else:
        longitude = str(int(round(metadata['account'].longitude)))

    sample_detail = metadata['sample']
    collection_timestamp = sample_detail.datetime_collected
    sample_type = sample_detail.site

    if source_type is None:
        raise RepoException("Sample is missing a source type")

    if sample_type is None and source_type in ('human', 'animal'):
        raise RepoException(f"{name} is missing site_sampled")

    if source_type == 'human':
        sample_type = sample_detail.site
        sample_invariants = HUMAN_SITE_INVARIANTS.get(sample_type)

        # there are a handful of samples that exhibit an unusual state
        # of reporting as human, but a site sampled as Fur. I believe
        # these are tests, but regardless, resolution is not clear.
        # let's catch unexpected, and move forward so we don't bomb on
        # a KeyError
        if sample_invariants is None:
            raise RepoException("Unexpected sample type: %s" % sample_type)

    elif source_type == 'animal':
        sample_type = sample_detail.site
        sample_invariants = {}
    elif source_type == 'environmental':
        sample_type = metadata['source'].source_data.description
        sample_invariants = {}
    else:
        raise RepoException("Sample has an unknown sample type")

    values = [hsi, collection_timestamp, geo_loc_name, geo_state, latitude,
              longitude]
    index = ['HOST_SUBJECT_ID', 'COLLECTION_TIMESTAMP', 'GEO_LOC_NAME',
             'STATE', 'LATITUDE', 'LONGITUDE']

    collected = set()

    for survey in metadata['survey_answers']:
        template = survey['template']

        if template in collected:
            # As surveys can now be retaken, it will become more common for
            # duplicates to appear. However, those duplicates are typically
            # merged before this function is called. Hence, it would continue
            # to be a somewhat unusual and unexpected state to process two or
            # more surveys with the same template id here. For now, continue
            # to gather the results only once.
            continue

        collected.add(template)

        for qid, (shortname, answer) in survey['response'].items():
            if (template, qid) in multiselect_map:
                # if we have a question that is a multiselect
                assert isinstance(answer, list)

                # pull out the previously computed column names
                specific_shortnames = multiselect_map[(template, qid)]

                if len(answer) > 0:
                    # the user selected at least one option, so we need to
                    # put a true/false value for every option
                    for key in specific_shortnames:
                        specific_shortname = specific_shortnames[key]
                        index.append(specific_shortname)

                        if key in answer:
                            # the user selected this answer, so mark it true
                            values.append('true')
                        else:
                            # the user did not select this answer, mark false
                            values.append('false')
                else:
                    # the user did not select any options, so we're going to
                    # let all of the options be populated by 'not collected'
                    # downstream
                    continue
            else:
                if '["' in answer and '"]' in answer:
                    # process this STRING/TEXT value
                    index.append(shortname)
                    values.append(answer.replace('["', '').replace('"]', ''))
                else:
                    # process this SINGLE value
                    index.append(shortname)
                    values.append(answer)

    for variable, value in sample_invariants.items():
        index.append(variable)
        values.append(value)

    return pd.Series(values, index=index, name=name)


def _fetch_barcode_metadata(sample_barcode):
    """Query the private API to obtain per-sample metadata

    Parameters
    ----------
    sample_barcode : str
        The barcode to request

    Returns
    -------
    dict
        The survey responses associated with the sample barcode
    dict or None
        Any error information associated with the retreival. If an error is
        observed, the survey responses should not be considered valid.
    """
    with Transaction() as t:
        admin_repo = AdminRepo(t)
        sample_pulldown = admin_repo.get_survey_metadata(sample_barcode)
    return sample_pulldown, None


def _build_col_name(col_name, multiselect_answer):
    """For a multiselect response, form a stable metadata variable name

    Parameters
    ----------
    col_name : str
        The basename for the column which would correspond to the question.
    multiselect_answer : str
        The selected answer

    Returns
    -------
    str
        The formatted column name, For example, in the primary survey
        there is a multiple select option for alcohol which includes beer
        and wine. The basename would be "alcohol", one multiselect_answer
        would be "beer", and the formatted column name would be
        "alcohol_beer".

    Raises
    ------
    ValueError
        If there are removed characters as it may create an unsafe column name.
        For example, "A+" and "A-" for blood types would both map to "A".
    """
    # replace some characters with _
    multiselect_answer = multiselect_answer.replace(' ', '_')
    multiselect_answer = multiselect_answer.replace('-', '_')

    reduced = re.sub('[^0-9a-zA-Z_]+', '', multiselect_answer)
    return f"{col_name}_{reduced}"


def _find_duplicates(barcodes):
    """Report any barcode observed more than a single time

    Parameters
    ----------
    barcodes : iterable of str
        The barcodes to check for duplicates in

    Returns
    -------
    set
        Any barcode observed more than a single time
    dict
        Any error information or None
    """
    error = None
    counts = Counter(barcodes)
    dups = {barcode for barcode, count in counts.items() if count > 1}

    if len(dups) > 0:
        error = {
            "barcode": list(dups),
            "error": "Duplicated barcodes in input"
        }

    return dups, error


def _get_freetext_fields():
    """ Retrieve a list of all free-text survey fields from the database

    Returns
    -------
    list of str
        The question_shortname values for all free-text survey questions
    """
    with Transaction() as t:
        with t.cursor() as cur:
            cur.execute(
                "SELECT sq.question_shortname "
                "FROM ag.survey_question sq "
                "INNER JOIN ag.survey_question_response_type sqrtype "
                "ON sq.survey_question_id = sqrtype.survey_question_id "
                "WHERE survey_response_type IN ('TEXT', 'STRING')"
            )
            rows = cur.fetchall()
            return [x[0] for x in rows]
