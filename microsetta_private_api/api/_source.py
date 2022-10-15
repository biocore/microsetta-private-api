import uuid
from datetime import date

from flask import jsonify

from microsetta_private_api.api._account import _validate_account_access
from microsetta_private_api.api.literals import SRC_NOT_FOUND_MSG
from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.model.source import Source, HumanInfo, NonHumanInfo
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo
from microsetta_private_api.repo.transaction import Transaction


def read_sources(account_id, token_info, source_type=None):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        source_repo = SourceRepo(t)
        sources = source_repo.get_sources_in_account(account_id, source_type)
        api_sources = [x.to_api() for x in sources]
        # TODO: Also support 404? Or is that not necessary?
        return jsonify(api_sources), 200


def create_source(account_id, body, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        source_repo = SourceRepo(t)
        source_id = str(uuid.uuid4())
        name = body["source_name"]
        source_type = body['source_type']

        if source_type == Source.SOURCE_TYPE_HUMAN:
            # TODO: Unfortunately, humans require a lot of special handling,
            #  and we started mixing Source calls used for transforming to/
            #  from the database with source calls to/from the api.
            #  Would be nice to split this out better.
            source_info = HumanInfo.from_dict(body,
                                              consent_date=date.today(),
                                              date_revoked=None)
            # the "legacy" value of the age_range enum is not valid to use when
            # creating a new source, so do not allow that.
            # NB: Not necessary to do this check when updating a source as
            # only source name and description (not age_range) may be updated.
            if source_info.age_range == "legacy":
                raise RepoException("Age range may not be set to legacy.")
        else:
            source_info = NonHumanInfo.from_dict(body)

        new_source = Source(source_id,
                            account_id,
                            source_type,
                            name,
                            source_info)
        source_repo.create_source(new_source)

        # Must pull from db to get creation_time, update_time
        s = source_repo.get_source(account_id, new_source.id)
        t.commit()

    response = jsonify(s.to_api())
    response.status_code = 201
    response.headers['Location'] = '/api/accounts/%s/sources/%s' % \
                                   (account_id, source_id)
    return response


def read_source(account_id, source_id, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        source_repo = SourceRepo(t)
        source = source_repo.get_source(account_id, source_id)
        if source is None:
            return jsonify(code=404, message=SRC_NOT_FOUND_MSG), 404
        return jsonify(source.to_api()), 200


def update_source(account_id, source_id, body, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        source_repo = SourceRepo(t)
        source = source_repo.get_source(account_id, source_id)
        if source is None:
            return jsonify(code=404, message=SRC_NOT_FOUND_MSG), 404

        source.name = body["source_name"]
        # every type of source has a name but not every type has a description
        if getattr(source.source_data, "description", False):
            source.source_data.description = body.get(
                "source_description", None)
        source_repo.update_source_data_api_fields(source)

        # I wonder if there's some way to get the creation_time/update_time
        # during the insert/update...
        source = source_repo.get_source(account_id, source_id)
        t.commit()

        # TODO: 422? Not sure this can actually happen anymore ...
        return jsonify(source.to_api()), 200


def delete_source(account_id, source_id, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        source_repo = SourceRepo(t)
        survey_answers_repo = SurveyAnswersRepo(t)

        answers = survey_answers_repo.list_answered_surveys(account_id,
                                                            source_id)
        for survey_id in answers:
            survey_answers_repo.delete_answered_survey(account_id,
                                                       survey_id)

        if not source_repo.delete_source(account_id, source_id):
            return jsonify(code=404, message=SRC_NOT_FOUND_MSG), 404
        # TODO: 422?
        t.commit()
        return '', 204


def create_human_source_from_consent(account_id, body, token_info):
    _validate_account_access(token_info, account_id)

    # Must convert consent form body into object processable by create_source.

    # Not adding any error handling here because if 'participant_name' isn't
    # here, we SHOULD be getting an error.
    source = {
        'source_type': Source.SOURCE_TYPE_HUMAN,
        'source_name': body['participant_name'],
        'consent': {
            'age_range': body['age_range']
        }
    }

    deceased_parent_key = 'deceased_parent'
    child_keys = {'parent_1_name', 'parent_2_name', deceased_parent_key,
                  'obtainer_name'}

    intersection = child_keys.intersection(body)
    if intersection:
        source['consent']['child_info'] = {}
        for key in intersection:
            if key == deceased_parent_key:
                body[deceased_parent_key] = body[deceased_parent_key] == 'true'
            source['consent']['child_info'][key] = body[key]

    # NB: Don't expect to handle errors 404, 422 in this function; expect to
    # farm out to `create_source`
    return create_source(account_id, source, token_info)


def check_duplicate_source_name(account_id, body, token_info):
    _validate_account_access(token_info, account_id)
    with Transaction() as t:
        source_repo = SourceRepo(t)
        source_name = body['participant_name']
        source = source_repo.get_duplicate_source_name(
            account_id, source_name)
        return jsonify(source), 200
