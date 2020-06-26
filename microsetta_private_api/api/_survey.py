import flask
from flask import jsonify

from microsetta_private_api.api.implementation import \
    _validate_account_access
from microsetta_private_api.model.source import Source
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import VioscreenRepo
from microsetta_private_api.util import vioscreen, vue_adapter


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
                           for x in [1, 3, 4, 5, 6,
                                     SurveyTemplateRepo.VIOSCREEN_ID]]), 200
        elif source.source_type == Source.SOURCE_TYPE_ANIMAL:
            return jsonify([template_repo.get_survey_template_link_info(x)
                           for x in [2]]), 200
        else:
            return jsonify([]), 200


def read_survey_template(account_id, source_id, survey_template_id,
                         language_tag, token_info, survey_redirect_url=None):
    _validate_account_access(token_info, account_id)

    # TODO: can we get rid of source_id?  I don't have anything useful to do
    #  with it...  I guess I could check if the source is a dog before giving
    #  out a pet information survey?

    with Transaction() as t:
        survey_template_repo = SurveyTemplateRepo(t)
        info = survey_template_repo.get_survey_template_link_info(
            survey_template_id)

        # For external surveys, we generate links pointing out
        if survey_template_id == SurveyTemplateRepo.VIOSCREEN_ID:

            url = vioscreen.gen_survey_url(
                language_tag, survey_redirect_url
            )
            # TODO FIXME HACK: This field's contents are not specified!
            info.survey_template_text = {
                "url": url
            }
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
                "validator": "number",
                "min": 0,
                "max": None
            },
            "113": {
                # Weight
                "inputType": "number",
                "validator": "number",
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
            template_id = survey_answers_repo.find_survey_template_id(ans)
            if template_id is None:
                continue
            o = survey_template_repo.get_survey_template_link_info(template_id)
            api_objs.append(o.to_api(ans))
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

        template_id = survey_answers_repo.find_survey_template_id(survey_id)
        if template_id is None:
            return jsonify(code=422, message="No answers in survey"), 422

        template_repo = SurveyTemplateRepo(t)
        link_info = template_repo.get_survey_template_link_info(template_id)
        link_info.survey_id = survey_id
        link_info.survey_text = survey_answers
        return jsonify(link_info), 200


def submit_answered_survey(account_id, source_id, language_tag, body,
                           token_info):
    _validate_account_access(token_info, account_id)

    if body['survey_template_id'] == SurveyTemplateRepo.VIOSCREEN_ID:
        return _submit_vioscreen_status(account_id, source_id,
                                        body["survey_text"]["key"])

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
            template_id = answers_repo.find_survey_template_id(answered_survey)
            if template_id is None:
                continue
            info = template_repo.get_survey_template_link_info(template_id)
            resp_obj.append(info.to_api(answered_survey))

        t.commit()
        return jsonify(resp_obj), 200


def _submit_vioscreen_status(account_id, source_id, info_str):
    # get information out of encrypted vioscreen url
    info = vioscreen.decode_key(info_str).decode("utf-8")
    vio_info = {}
    for keyval in info.split("&"):
        key, val = keyval.split("=")
        vio_info[key] = val

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
