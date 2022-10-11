import flask
from flask import jsonify, make_response
from werkzeug.exceptions import NotFound

from microsetta_private_api.api._account import \
    _validate_account_access
from microsetta_private_api.model.source import Source
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import VioscreenRepo
from microsetta_private_api.util import vioscreen, myfoodrepo, vue_adapter, \
    polyphenol_ffq
from microsetta_private_api.util.vioscreen import VioscreenAdminAPI
from microsetta_private_api.config_manager import SERVER_CONFIG


def read_survey_templates(account_id, source_id, language_tag, token_info):
    _validate_account_access(token_info, account_id)

    # TODO: I don't think surveys have names... only survey groups have names.
    #  So what can I pass down to the user that will make any sense here?

    # Note to future maintainers,
    # 2/21/20: currently the only way to figure this out
    # is to look through the "surveys" and "survey_group" tables, try:
    # select survey_id, american from surveys left join survey_group on
    # survey_group = group_order;

    with Transaction() as t:
        source_repo = SourceRepo(t)
        source = source_repo.get_source(account_id, source_id)
        if source is None:
            return jsonify(code=404, message="No source found"), 404
        template_repo = SurveyTemplateRepo(t)
        if source.source_type == Source.SOURCE_TYPE_HUMAN:
            return jsonify([template_repo.get_survey_template_link_info(x)
                           for x in [1, 3, 4, 5, 6, 7,
                                     SurveyTemplateRepo.VIOSCREEN_ID,
                                     SurveyTemplateRepo.MYFOODREPO_ID,
                                     SurveyTemplateRepo.POLYPHENOL_FFQ_ID,
                                     SurveyTemplateRepo.SPAIN_FFQ_ID]
                            ]), 200
        elif source.source_type == Source.SOURCE_TYPE_ANIMAL:
            return jsonify([template_repo.get_survey_template_link_info(x)
                           for x in [2]]), 200
        else:
            return jsonify([]), 200


def _remote_survey_url_vioscreen(transaction, account_id, source_id,
                                 language_tag, survey_redirect_url):
    # assumes an instance of Transaction is already available
    acct_repo = AccountRepo(transaction)
    survey_template_repo = SurveyTemplateRepo(transaction)

    # User is about to start a vioscreen survey
    # record this in the database.
    db_vioscreen_id = survey_template_repo.create_vioscreen_id(
            account_id, source_id)

    (birth_year, gender, height, weight) = \
        survey_template_repo.fetch_user_basic_physiology(
        account_id, source_id)

    account = acct_repo.get_account(account_id)
    country_code = account.address.country_code

    url = vioscreen.gen_survey_url(
        db_vioscreen_id,
        language_tag,
        survey_redirect_url,
        birth_year=birth_year,
        gender=gender,
        height=height,
        weight=weight,
        country_code=country_code
    )

    return url


def _remote_survey_url_myfoodrepo(transaction, account_id, source_id,
                                  language_tag):
    # assumes an instance of Transaction is already available
    st_repo = SurveyTemplateRepo(transaction)

    # do we already have an id?
    mfr_id, created = st_repo.get_myfoodrepo_id_if_exists(account_id,
                                                          source_id)

    if mfr_id is None:
        # we need an ID so let's try and get one
        if created is None:
            # we need a slot and an id
            slot = st_repo.create_myfoodrepo_entry(account_id, source_id)
            if not slot:
                # we could not obtain a slot
                raise NotFound("Sorry, but the annotators are all allocated")

            mfr_id = myfoodrepo.create_subj()
        else:
            # we have a slot but no id
            mfr_id = myfoodrepo.create_subj()

        st_repo.set_myfoodrepo_id(account_id, source_id, mfr_id)
    else:
        # we already have an ID then just return the URL
        pass

    return myfoodrepo.gen_survey_url(mfr_id)


def _remote_survey_url_polyphenol_ffq(transaction, account_id, source_id,
                                      language_tag):
    st_repo = SurveyTemplateRepo(transaction)

    # right now, ID won't exist
    # future plans to allow surveys to behave more flexibly will use this
    # functionality to allow participants to re-join in-progress surveys
    polyphenol_ffq_id, study = \
        st_repo.get_polyphenol_ffq_id_if_exists(account_id, source_id)

    if polyphenol_ffq_id is None:
        # The Polyphenol FFQ belongs to Danone and they're interested in
        # tracking results that come from their sponsored studies
        # separately from other samples. We pass 'THDMI' as the study for
        # THDMI samples and 'Microsetta' for all other samples. Therefore,
        # we need to determine if the source has any THDMI-associated samples.
        # Without investing significant developer effort to build a category
        # system around projects, a basic text search is the best compromise.
        study = 'Microsetta'
        sample_repo = SampleRepo(transaction)
        samples = sample_repo.get_samples_by_source(account_id, source_id)
        for s in samples:
            for s_p in s.sample_projects:
                if s_p.startswith('THDMI'):
                    study = 'THDMI'
                    break

        polyphenol_ffq_id = st_repo.create_polyphenol_ffq_entry(account_id,
                                                                source_id,
                                                                language_tag,
                                                                study)

    return polyphenol_ffq.gen_ffq_url(polyphenol_ffq_id, study, language_tag)


def _remote_survey_url_spain_ffq(transaction, account_id, source_id):
    st_repo = SurveyTemplateRepo(transaction)

    # right now, ID won't exist
    # future plans to allow surveys to behave more flexibly will use this
    # functionality to allow participants to re-join in-progress surveys
    spain_ffq_id = st_repo.get_spain_ffq_id_if_exists(account_id, source_id)

    if spain_ffq_id is None:
        st_repo.create_spain_ffq_entry(account_id, source_id)

    return SERVER_CONFIG['spain_ffq_url']


def read_survey_template(account_id, source_id, survey_template_id,
                         language_tag, token_info, survey_redirect_url=None):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        survey_template_repo = SurveyTemplateRepo(t)
        info = survey_template_repo.get_survey_template_link_info(
            survey_template_id)
        remote_surveys = set(survey_template_repo.remote_surveys())

        # For external surveys, we generate links pointing out
        if survey_template_id in remote_surveys:
            if survey_template_id == SurveyTemplateRepo.VIOSCREEN_ID:
                url = _remote_survey_url_vioscreen(t,
                                                   account_id,
                                                   source_id,
                                                   language_tag,
                                                   survey_redirect_url)
            elif survey_template_id == SurveyTemplateRepo.MYFOODREPO_ID:
                url = _remote_survey_url_myfoodrepo(t,
                                                    account_id,
                                                    source_id,
                                                    language_tag)
            elif survey_template_id == SurveyTemplateRepo.POLYPHENOL_FFQ_ID:
                url = _remote_survey_url_polyphenol_ffq(t,
                                                        account_id,
                                                        source_id,
                                                        language_tag)
            elif survey_template_id == SurveyTemplateRepo.SPAIN_FFQ_ID:
                url = _remote_survey_url_spain_ffq(t,
                                                   account_id,
                                                   source_id)
            else:
                raise ValueError(f"Cannot generate URL for survey "
                                 f"{survey_template_id}")

            # TODO FIXME HACK: This field's contents are not specified!
            info.survey_template_text = {
                "url": url
            }
            t.commit()
            return jsonify(info), 200

        # For local surveys, we generate the json representing the survey
        survey_template = survey_template_repo.get_survey_template(
            survey_template_id, language_tag)
        info.survey_template_text = vue_adapter.to_vue_schema(survey_template)

        # TODO FIXME HACK: We need a better way to enforce validation on fields
        #  that need it, can this be stored adjacent to the survey questions?
        client_side_validation = {
            "108": {
                # Height
                "inputType": "number",
                "validator": "integer",
                "min": 0,
                "max": None
            },
            "113": {
                # Weight
                "inputType": "number",
                "validator": "integer",
                "min": 0,
                "max": None
            }
        }
        for group in info.survey_template_text.groups:
            for field in group.fields:
                if field.id in client_side_validation:
                    field.set(**client_side_validation[field.id])

        return jsonify(info), 200


def read_answered_surveys(account_id, source_id, language_tag, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        survey_answers_repo = SurveyAnswersRepo(t)
        survey_template_repo = SurveyTemplateRepo(t)
        answered_surveys = survey_answers_repo.list_answered_surveys(
                account_id,
                source_id)
        api_objs = []
        for ans in answered_surveys:
            template_id, status = survey_answers_repo.\
                survey_template_id_and_status(ans)
            if template_id is None:
                continue
            o = survey_template_repo.get_survey_template_link_info(template_id)
            api_objs.append(o.to_api(ans, status))
        return jsonify(api_objs), 200


def read_answered_survey(account_id, source_id, survey_id, language_tag,
                         token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        survey_answers_repo = SurveyAnswersRepo(t)
        survey_answers = survey_answers_repo.get_answered_survey(
            account_id,
            source_id,
            survey_id,
            language_tag)
        if not survey_answers:
            return jsonify(code=404, message="No survey answers found"), 404

        template_id, status = survey_answers_repo.\
            survey_template_id_and_status(survey_id)
        if template_id is None:
            return jsonify(code=422, message="No answers in survey"), 422

        template_repo = SurveyTemplateRepo(t)
        link_info = template_repo.get_survey_template_link_info(template_id)
        link_info.survey_id = survey_id
        link_info.survey_status = status
        link_info.survey_text = survey_answers
        return jsonify(link_info), 200


def submit_answered_survey(account_id, source_id, language_tag, body,
                           token_info):
    _validate_account_access(token_info, account_id)

    if body['survey_template_id'] == SurveyTemplateRepo.VIOSCREEN_ID:
        return _submit_vioscreen_status(account_id, source_id,
                                        body["survey_text"]["key"])
    if body['survey_template_id'] == SurveyTemplateRepo.MYFOODREPO_ID:
        raise NotFound("We don't have a notion of answering this survey type")

    # TODO: Is this supposed to return new survey id?
    # TODO: Rename survey_text to survey_model/model to match Vue's naming?
    with Transaction() as t:
        survey_answers_repo = SurveyAnswersRepo(t)
        survey_answers_id = survey_answers_repo.submit_answered_survey(
            account_id,
            source_id,
            language_tag,
            body["survey_template_id"],
            body["survey_text"]
        )
        t.commit()

        response = flask.Response()
        response.status_code = 201
        response.headers['Location'] = '/api/accounts/%s' \
                                       '/sources/%s' \
                                       '/surveys/%s' % \
                                       (account_id,
                                        source_id,
                                        survey_answers_id)
        return response


def read_answered_survey_associations(account_id, source_id, sample_id,
                                      token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        answers_repo = SurveyAnswersRepo(t)
        template_repo = SurveyTemplateRepo(t)
        answered_surveys = answers_repo.list_answered_surveys_by_sample(
            account_id,
            source_id,
            sample_id)

        resp_obj = []
        for answered_survey in answered_surveys:
            template_id, status = answers_repo.\
                survey_template_id_and_status(answered_survey)
            if template_id is None:
                continue
            info = template_repo.get_survey_template_link_info(template_id)
            resp_obj.append(info.to_api(answered_survey, status))

        t.commit()
        return jsonify(resp_obj), 200


def _submit_vioscreen_status(account_id, source_id, info_str):
    # get information out of encrypted vioscreen url
    info = vioscreen.decode_key(info_str).decode("utf-8")
    vio_info = {}
    for keyval in info.split("&"):
        key, val = keyval.split("=")
        vio_info[key.lower()] = val

    with Transaction() as t:
        vio_repo = VioscreenRepo(t)

        # Add the status to the survey
        vio_repo.upsert_vioscreen_status(account_id, source_id,
                                         vio_info["username"],
                                         int(vio_info["status"]))
        t.commit()

    response = flask.Response()
    response.status_code = 201
    # TODO FIXME HACK:  This location can't actually return any info about ffq!
    #  But I need SOME response that contains the survey_id or client can't
    #  associate the survey with a sample.
    response.headers['Location'] = '/api/accounts/%s' \
                                   '/sources/%s' \
                                   '/surveys/%s' % \
                                   (account_id,
                                    source_id,
                                    vio_info["username"])
    return response


def top_food_report(account_id, source_id, survey_id, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        vioscreen_repo = VioscreenRepo(t)

        # Vioscreen username is our survey_id
        status = vioscreen_repo.get_vioscreen_status(account_id,
                                                     source_id,
                                                     survey_id)
        if status != 3:
            # Oops, we don't have results available for this one
            raise NotFound("No such survey recorded")

        vio = VioscreenAdminAPI()
        sessions = vio.sessions(survey_id)
        # Looks like vioscreen supports multiple sessions per user, do we care?
        session_id = sessions[0]['sessionId']
        report = vio.top_food_report(session_id)

        if report is None:
            return NotFound("The requested FFQ is empty")

        response = make_response(report)
        response.headers.set("Content-Type", "application/pdf")
        # TODO: Do we want it to download a file or be embedded in the html?
        # response.headers.set('Content-Disposition',
        #                      'attachment',
        #                      filename='top-food-report.pdf')

        return response


def read_myfoodrepo_available_slots():
    with Transaction() as t:
        st_repo = SurveyTemplateRepo(t)
        available = st_repo.myfoodrepo_slots_available()
        total = st_repo.myfoodrepo_slots_total()

    resp = jsonify(code=200, number_of_available_slots=available,
                   total_number_of_slots=total)
    return resp, 200
