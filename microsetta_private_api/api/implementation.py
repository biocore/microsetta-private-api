"""
Functions to implement OpenAPI 3.0 interface to access private PHI.

Underlies the resource server in the oauth2 workflow. "Resource Server: The
server hosting user-owned resources that are protected by OAuth2. The resource
server validates the access-token and serves the protected resources."
--https://dzone.com/articles/oauth-20-beginners-guide

Loosely based off examples in
https://realpython.com/flask-connexion-rest-api/#building-out-the-complete-api
and associated file
https://github.com/realpython/materials/blob/master/flask-connexion-rest/version_3/people.py  # noqa: E501
"""

import flask
from flask import jsonify, render_template
import jwt

from jwt import InvalidTokenError

from microsetta_private_api import localization
from microsetta_private_api.model.address import Address
from microsetta_private_api.model.sample import SampleInfo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.repo.kit_repo import KitRepo
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo
from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.repo.vioscreen_repo import VioscreenRepo

from microsetta_private_api.model.account import Account, AuthorizationMatch
from microsetta_private_api.model.source import Source, HumanInfo, NonHumanInfo

from werkzeug.exceptions import BadRequest, Unauthorized, Forbidden, NotFound

from microsetta_private_api.util import vue_adapter
from microsetta_private_api.util.util import fromisotime
from microsetta_private_api.util import vioscreen

import uuid

from datetime import date
import importlib.resources as pkg_resources


# Authrocket uses RS256 public keys, so you can validate anywhere and safely
# store the key.
AUTHROCKET_PUB_KEY = pkg_resources.read_text(
    'microsetta_private_api',
    "authrocket.pubkey")
JWT_ISS_CLAIM_KEY = 'iss'
JWT_SUB_CLAIM_KEY = 'sub'
JWT_EMAIL_CLAIM_KEY = 'email'

ACCT_NOT_FOUND_MSG = "Account not found"
SRC_NOT_FOUND_MSG = "Source not found"
INVALID_TOKEN_MSG = "Invalid token"


def find_accounts_for_login(token_info):
    # Note: Returns an array of accounts accessible by token_info because
    # we'll use that functionality when we add in administrator accounts.
    with Transaction() as t:
        acct_repo = AccountRepo(t)
        acct = acct_repo.find_linked_account(
            token_info[JWT_ISS_CLAIM_KEY],
            token_info[JWT_SUB_CLAIM_KEY])

        if acct is None:
            return jsonify([]), 200
        return jsonify([acct.to_api()]), 200


def claim_legacy_acct(token_info):
    # If there exists a legacy account for the email in the token, which the
    # user represented by the token does not already own but can claim, this
    # claims the legacy account for the user and returns a 200 code with json
    # list containing the object for the claimed account.  Otherwise, this
    # returns an empty json list. This function can also trigger a 422 from the
    # repo layer in the case of inconsistent account data.

    email = token_info[JWT_EMAIL_CLAIM_KEY]
    auth_iss = token_info[JWT_ISS_CLAIM_KEY]
    auth_sub = token_info[JWT_SUB_CLAIM_KEY]

    with Transaction() as t:
        acct_repo = AccountRepo(t)
        acct = acct_repo.claim_legacy_account(email, auth_iss, auth_sub)
        t.commit()

        if acct is None:
            return jsonify([]), 200

        return jsonify([acct.to_api()]), 200


def register_account(body, token_info):
    # First register with AuthRocket, then come here to make the account
    new_acct_id = str(uuid.uuid4())
    body["id"] = new_acct_id
    account_obj = Account.from_dict(body, token_info[JWT_ISS_CLAIM_KEY],
                                    token_info[JWT_SUB_CLAIM_KEY])

    with Transaction() as t:
        kit_repo = KitRepo(t)
        kit = kit_repo.get_kit_all_samples(body['kit_name'])
        if kit is None:
            return jsonify(code=404, message="Kit name not found"), 404

        acct_repo = AccountRepo(t)
        acct_repo.create_account(account_obj)
        new_acct = acct_repo.get_account(new_acct_id)
        t.commit()

    response = jsonify(new_acct.to_api())
    response.status_code = 201
    response.headers['Location'] = '/api/accounts/%s' % new_acct_id
    return response


def read_account(account_id, token_info):
    acc = _validate_account_access(token_info, account_id)
    return jsonify(acc.to_api()), 200


def check_email_match(account_id, token_info):
    acc = _validate_account_access(token_info, account_id)

    match_status = acc.account_matches_auth(
        token_info[JWT_EMAIL_CLAIM_KEY], token_info[JWT_ISS_CLAIM_KEY],
        token_info[JWT_SUB_CLAIM_KEY])

    if match_status == AuthorizationMatch.AUTH_ONLY_MATCH:
        result = {'email_match': False}
    elif match_status == AuthorizationMatch.FULL_MATCH:
        result = {'email_match': True}
    else:
        raise ValueError("Unexpected authorization match value")

    return jsonify(result), 200


def update_account(account_id, body, token_info):
    acc = _validate_account_access(token_info, account_id)

    with Transaction() as t:
        acct_repo = AccountRepo(t)
        acc.first_name = body['first_name']
        acc.last_name = body['last_name']
        acc.email = body['email']
        acc.address = Address(
            body['address']['street'],
            body['address']['city'],
            body['address']['state'],
            body['address']['post_code'],
            body['address']['country_code']
        )

        # 422 handling is done inside acct_repo
        acct_repo.update_account(acc)
        t.commit()

        return jsonify(acc.to_api()), 200


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
        if not source_repo.delete_source(account_id, source_id):
            return jsonify(code=404, message=SRC_NOT_FOUND_MSG), 404
        # TODO: 422?
        t.commit()
        return '', 204


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
                           for x in [1, 3, 4, 5,
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
                survey_template_id, language_tag, survey_redirect_url
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
        template_repo = SurveyTemplateRepo(t)
        link_info = template_repo.get_survey_template_link_info(template_id)
        link_info.survey_id = survey_id
        link_info.survey_text = survey_answers
        return jsonify(link_info), 200


def submit_answered_survey(account_id, source_id, language_tag, body,
                           token_info):
    _validate_account_access(token_info, account_id)

    if body['survey_template_id'] == SurveyTemplateRepo.VIOSCREEN_ID:
        return _submit_vioscreen_status(body["survey_text"])

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


def read_sample_associations(account_id, source_id, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        sample_repo = SampleRepo(t)
        samples = sample_repo.get_samples_by_source(account_id, source_id)

    api_samples = [x.to_api() for x in samples]
    return jsonify(api_samples), 200


def associate_sample(account_id, source_id, body, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        sample_repo = SampleRepo(t)
        sample_repo.associate_sample(account_id,
                                     source_id,
                                     body['sample_id'])
        t.commit()
    response = flask.Response()
    response.status_code = 201
    response.headers['Location'] = '/api/accounts/%s/sources/%s/samples/%s' % \
                                   (account_id, source_id, ['sample_id'])
    return response


def read_sample_association(account_id, source_id, sample_id, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        sample_repo = SampleRepo(t)
        sample = sample_repo.get_sample(account_id, source_id, sample_id)
        if sample is None:
            return jsonify(code=404, message="Sample not found"), 404

        return jsonify(sample.to_api()), 200


def update_sample_association(account_id, source_id, sample_id, body,
                              token_info):
    _validate_account_access(token_info, account_id)

    # TODO: API layer doesn't understand that BadRequest can be thrown,
    #  but that looks to be the right result if sample_site bad.
    #  Need to update the api layer if we want to specify 400s.
    #  (Or we leave api as is and say 400's can always be thrown if your
    #  request is bad)
    with Transaction() as t:
        sample_repo = SampleRepo(t)
        source_repo = SourceRepo(t)

        source = source_repo.get_source(account_id, source_id)
        if source is None:
            return jsonify(code=404, message="No such source"), 404

        needs_sample_site = source.source_type in [Source.SOURCE_TYPE_HUMAN,
                                                   Source.SOURCE_TYPE_ANIMAL]

        precludes_sample_site = source.source_type == \
            Source.SOURCE_TYPE_ENVIRONMENT

        sample_site_present = "sample_site" in body and \
                              body["sample_site"] is not None

        if needs_sample_site and not sample_site_present:
            # Human/Animal sources require sample_site to be set
            raise BadRequest("human/animal samples require sample_site")
        if precludes_sample_site and sample_site_present:
            raise BadRequest("environmental samples cannot specify "
                             "sample_site")

        sample_datetime = body['sample_datetime']
        try:
            sample_datetime = fromisotime(sample_datetime)
        except ValueError:
            raise BadRequest("Invalid sample_datetime")
        sample_info = SampleInfo(
            sample_id,
            sample_datetime,
            body["sample_site"],
            body["sample_notes"]
        )
        sample_repo.update_info(account_id, source_id, sample_info)
        final_sample = sample_repo.get_sample(account_id, source_id, sample_id)
        t.commit()
    return jsonify(final_sample), 200


def dissociate_sample(account_id, source_id, sample_id, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        sample_repo = SampleRepo(t)
        sample_repo.dissociate_sample(account_id, source_id, sample_id)
        t.commit()
        return '', 204


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
            info = template_repo.get_survey_template_link_info(template_id)
            resp_obj.append(info.to_api(answered_survey))

        t.commit()
        return jsonify(resp_obj), 200


def associate_answered_survey(account_id, source_id, sample_id, body,
                              token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        answers_repo = SurveyAnswersRepo(t)
        answers_repo.associate_answered_survey_with_sample(
            account_id, source_id, sample_id, body['survey_id']
        )
        t.commit()

    response = flask.Response()
    response.status_code = 201
    response.headers['Location'] = '/api/accounts/%s' \
                                   '/sources/%s' \
                                   '/surveys/%s' % \
                                   (account_id,
                                    source_id,
                                    body['survey_id'])
    return response


def dissociate_answered_survey(account_id, source_id, sample_id, survey_id,
                               token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        answers_repo = SurveyAnswersRepo(t)
        answers_repo.dissociate_answered_survey_from_sample(
            account_id, source_id, sample_id, survey_id)
        t.commit()
    return '', 204


def read_kit(kit_name):
    # NOTE:  Nothing in this route requires a particular user to be logged in,
    # so long as the user has -an- account.

    with Transaction() as t:
        kit_repo = KitRepo(t)
        kit = kit_repo.get_kit_unused_samples(kit_name)
        if kit is None:
            return jsonify(code=404, message="No such kit"), 404
        return jsonify(kit.to_api()), 200


def render_consent_doc(account_id, language_tag, consent_post_url, token_info):
    _validate_account_access(token_info, account_id)

    # return render_template("new_participant.jinja2",
    #                        message=MockJinja("message"),
    #                        media_locale=MockJinja("media_locale"),
    #                        tl=MockJinja("tl"))

    # NB: Do NOT need to explicitly pass account_id into template for
    # integration into form submission URL because form submit URL builds on
    # the base of the URL that called it (which includes account_id)

    localization_info = localization.LANG_SUPPORT[language_tag]
    consent_html = render_template(
        "new_participant.jinja2",
        tl=localization_info[localization.NEW_PARTICIPANT_KEY],
        lang_tag=language_tag,
        post_url=consent_post_url
    )
    return jsonify({"consent_html": consent_html}), 200


def create_human_source_from_consent(account_id, body, token_info):
    _validate_account_access(token_info, account_id)

    # Must convert consent form body into object processable by create_source.

    # Not adding any error handling here because if 'participant_name' isn't
    # here, we SHOULD be getting an error.
    source = {
        'source_type': Source.SOURCE_TYPE_HUMAN,
        'source_name': body['participant_name'],
        'consent': {
            'participant_email': body['participant_email'],
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


def verify_authrocket(token):
    email_verification_key = 'email_verified'

    try:
        token_info = jwt.decode(token,
                                AUTHROCKET_PUB_KEY,
                                algorithms=["RS256"],
                                verify=True,
                                issuer="https://authrocket.com")
    except InvalidTokenError as e:
        raise(Unauthorized(INVALID_TOKEN_MSG, e))

    if JWT_ISS_CLAIM_KEY not in token_info or \
            JWT_SUB_CLAIM_KEY not in token_info or \
            JWT_EMAIL_CLAIM_KEY not in token_info:
        # token is malformed--no soup for you
        raise Unauthorized(INVALID_TOKEN_MSG)

    # if the user's email is not yet verified, they are forbidden to
    # access their account even regardless of whether they have
    # authenticated with authrocket
    if email_verification_key not in token_info or \
            token_info[email_verification_key] is not True:
        raise Forbidden("Email is not verified")

    return token_info


def _validate_account_access(token_info, account_id):
    with Transaction() as t:
        account_repo = AccountRepo(t)
        account = account_repo.get_account(account_id)

        if account is None:
            raise NotFound(ACCT_NOT_FOUND_MSG)
        else:
            auth_match = account.account_matches_auth(
                token_info[JWT_EMAIL_CLAIM_KEY],
                token_info[JWT_ISS_CLAIM_KEY],
                token_info[JWT_SUB_CLAIM_KEY])
            if auth_match == AuthorizationMatch.NO_MATCH:
                raise Unauthorized()

        return account


def _submit_vioscreen_status(info_str):
    # get information out of encrypted vioscreen url
    info = vioscreen.decode_key(info_str)
    vio_info = {}
    for keyval in info.split("&"):
        key, val = keyval.split("=")
        vio_info[key] = val

    with Transaction() as t:
        vio_repo = VioscreenRepo(t)

        # Add the status to the survey
        vio_repo.update_vioscreen_status(vio_info["username"],
                                         int(vio_info["status"]))
        t.commit()

    # TODO: Any reason to respond with anything?
    return '', 204
