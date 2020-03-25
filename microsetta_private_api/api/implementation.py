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

from microsetta_private_api.model.account import Account
from microsetta_private_api.model.source import Source, info_from_api
from microsetta_private_api.model.source import human_info_from_api
from microsetta_private_api.LEGACY.locale_data import american_gut, british_gut

from werkzeug.exceptions import BadRequest, Unauthorized

from microsetta_private_api.util import vue_adapter
from microsetta_private_api.util.util import fromisotime

import uuid

from datetime import date


# Authrocket uses RS256 public keys, so you can validate anywhere and safely
# store the key in code. Obviously using this mechanism, we'd have to push code
# to reroll the keys, which is not ideal, but you can instead hold this in a
# config somewhere and reload

# Python is dumb, don't put spaces anywhere in this string.
AUTHROCKET_PUB_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAp68T9XnX7d53Zo8pt072
y+W0sV51EDZi7f2zeBbw5qvht9coFX4LF/p9Rcac7TajVJj+YE64vHm+YAL3ToJq
XOOF/6tmPYMbbg3DRdvUopH3URCR8o7cQXN//gDKruB9+xpB3v1Wq5SCX6t8SRFw
ixw3mKgpPoh+Ou5OohxmtJ+D7lr5R2DDW8QWAWpBdGgttdnex1OqDIsprJihx/SW
sHK4ql+H4MzX5PvY7S/XF2Ibl1xWsYLPvSzV/eJoG4hIwf7efUrXiVkwqFKNYzpL
YzmOf3F/k7TdpWqzic9y0ejMKzYu0ozGlKytxp3PbpI7B18nklVkGF07g/jNPwHN
7QIDAQAB
-----END PUBLIC KEY-----"""


def not_yet_implemented():
    return {'message': 'functionality not yet implemented'}


def register_account(body, token_info):
    # First register with AuthRocket, then come here to make the account
    new_acct_id = str(uuid.uuid4())
    with Transaction() as t:
        kit_repo = KitRepo(t)
        kit = kit_repo.get_kit(body['kit_name'])
        if kit is None:
            return jsonify(error=404, text="Kit name not found"), 404

        acct_repo = AccountRepo(t)
        # TODO: The email they provide our website may not match the email they
        #  use for login to our Identity Provider.  If that occurs, should we
        #  reject the account registration?  If we don't use the email from the
        #  IDP, we have to do our own email validation...
        acct_repo.create_account(Account(
            new_acct_id,
            body['email'],
            "standard",
            token_info['iss'],
            token_info['sub'],
            body['first_name'],
            body['last_name'],
            Address(
                body['address']['street'],
                body['address']['city'],
                body['address']['state'],
                body['address']['post_code'],
                body['address']['country_code'],
            )
        ))
        new_acct = acct_repo.get_account(new_acct_id)
        t.commit()

    response = jsonify(new_acct.to_api())
    response.status_code = 201
    response.headers['Location'] = '/api/accounts/%s' % new_acct_id
    return response


def read_account(account_id, token_info):
    validate_access(token_info, account_id)

    with Transaction() as t:
        acct_repo = AccountRepo(t)
        acc = acct_repo.get_account(account_id)
        if acc is None:
            return jsonify(code=404, message="Account not found"), 404
        return jsonify(acc.to_api()), 200


def update_account(account_id, body, token_info):
    validate_access(token_info, account_id)

    with Transaction() as t:
        acct_repo = AccountRepo(t)
        acc = acct_repo.get_account(account_id)
        if acc is None:
            return jsonify(code=404, message="Account not found"), 404

        # TODO: add 422 handling

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

        acct_repo.update_account(acc)
        t.commit()
        return jsonify(acc.to_api()), 200


def read_sources(account_id, token_info, source_type=None):
    validate_access(token_info, account_id)

    with Transaction() as t:
        source_repo = SourceRepo(t)
        sources = source_repo.get_sources_in_account(account_id, source_type)
        api_sources = [x.to_api() for x in sources]
        # TODO: Also support 404? Or is that not necessary?
        return jsonify(api_sources), 200


def create_source(account_id, body, token_info):
    validate_access(token_info, account_id)

    with Transaction() as t:
        source_repo = SourceRepo(t)
        source_id = str(uuid.uuid4())

        if body['source_type'] == Source.SOURCE_TYPE_HUMAN:
            # TODO: Unfortunately, humans require a lot of special handling,
            #  and we started mixing Source calls used for transforming to/
            #  from the database with source calls to/from the api.
            #  Would be nice to split this out better.
            new_source = Source(source_id,
                                account_id,
                                Source.SOURCE_TYPE_HUMAN,
                                human_info_from_api(
                                    body,
                                    consent_date=date.today(),
                                    date_revoked=None)
                                )
        else:
            new_source = Source.build_source(source_id, account_id, body)

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
    validate_access(token_info, account_id)

    with Transaction() as t:
        source_repo = SourceRepo(t)
        source = source_repo.get_source(account_id, source_id)
        if source is None:
            return jsonify(code=404, message="Source not found"), 404
        return jsonify(source.to_api()), 200


def update_source(account_id, source_id, body, token_info):
    validate_access(token_info, account_id)

    with Transaction() as t:
        source_repo = SourceRepo(t)
        source = source_repo.get_source(account_id, source_id)

        source.source_data = info_from_api(body)
        source_repo.update_source_data_api_fields(source)
        # I wonder if there's some way to get the creation_time/update_time
        # during the insert/update...
        source = source_repo.get_source(account_id, source_id)
        t.commit()
        # TODO: 404 and 422?
        return jsonify(source.to_api()), 200


def delete_source(account_id, source_id, token_info):
    validate_access(token_info, account_id)

    with Transaction() as t:
        source_repo = SourceRepo(t)
        if not source_repo.delete_source(account_id, source_id):
            return jsonify(code=404, message="No source found"), 404
        # TODO: 422?
        t.commit()
        return '', 204


def read_survey_templates(account_id, source_id, language_tag, token_info):
    validate_access(token_info, account_id)

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
                           for x in [1, 3, 4, 5]]), 200
        elif source.source_type == Source.SOURCE_TYPE_ANIMAL:
            return jsonify([template_repo.get_survey_template_link_info(x)
                           for x in [2]]), 200
        else:
            return jsonify([]), 200


def read_survey_template(account_id, source_id, survey_template_id,
                         language_tag, token_info):
    validate_access(token_info, account_id)

    # TODO: can we get rid of source_id?  I don't have anything useful to do
    #  with it...  I guess I could check if the source is a dog before giving
    #  out a pet information survey?

    with Transaction() as t:
        survey_template_repo = SurveyTemplateRepo(t)
        info = survey_template_repo.get_survey_template_link_info(
            survey_template_id)
        survey_template = survey_template_repo.get_survey_template(
            survey_template_id, language_tag)
        info.survey_template_text = vue_adapter.to_vue_schema(survey_template)
        return jsonify(info), 200


def read_answered_surveys(account_id, source_id, language_tag, token_info):
    validate_access(token_info, account_id)

    with Transaction() as t:
        survey_answers_repo = SurveyAnswersRepo(t)
        return jsonify(
            survey_answers_repo.list_answered_surveys(
                account_id,
                source_id)), 200


def read_answered_survey(account_id, source_id, survey_id, language_tag,
                         token_info):
    validate_access(token_info, account_id)

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
    validate_access(token_info, account_id)

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
    validate_access(token_info, account_id)

    with Transaction() as t:
        sample_repo = SampleRepo(t)
        samples = sample_repo.get_samples_by_source(account_id, source_id)

    api_samples = [x.to_api() for x in samples]
    return jsonify(api_samples), 200


def associate_sample(account_id, source_id, body, token_info):
    validate_access(token_info, account_id)

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
    validate_access(token_info, account_id)

    with Transaction() as t:
        sample_repo = SampleRepo(t)
        sample = sample_repo.get_sample(account_id, source_id, sample_id)
        if sample is None:
            return jsonify(code=404, message="Sample not found"), 404

        return jsonify(sample.to_api()), 200


def update_sample_association(account_id, source_id, sample_id, body,
                              token_info):
    validate_access(token_info, account_id)

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
    validate_access(token_info, account_id)

    with Transaction() as t:
        sample_repo = SampleRepo(t)
        sample_repo.dissociate_sample(account_id, source_id, sample_id)
        t.commit()
        return '', 204


def read_answered_survey_associations(account_id, source_id, sample_id,
                                      token_info):
    validate_access(token_info, account_id)

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
    validate_access(token_info, account_id)

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
    validate_access(token_info, account_id)

    with Transaction() as t:
        answers_repo = SurveyAnswersRepo(t)
        answers_repo.dissociate_answered_survey_from_sample(
            account_id, source_id, sample_id, survey_id)
        t.commit()
    return '', 204


def read_kit(kit_name):
    # NOTE:  Nothing in this route requires a particular user to be logged in,
    # so long as the user has -an- account.  Thus there is nothing to validate
    # a particular token_info against.
    with Transaction() as t:
        kit_repo = KitRepo(t)
        kit = kit_repo.get_kit(kit_name)
        if kit is None:
            return jsonify(code=404, message="No such kit"), 404
        return jsonify(kit.to_api()), 200


def render_consent_doc(account_id, language_tag, token_info):
    validate_access(token_info, account_id)

    # return render_template("new_participant.jinja2",
    #                        message=MockJinja("message"),
    #                        media_locale=MockJinja("media_locale"),
    #                        tl=MockJinja("tl"))

    # NB: Do NOT need to explicitly pass account_id into template for
    # integration into form submission URL because form submit URL builds on
    # the base of the URL that called it (which includes account_id)

    # TODO !!CRITICAL!! Is this the right way to choose which consent docs to
    #  send based on language_tag?  Or should it always send american_gut but
    #  a different language field somewhere else?
    media_locales = {
        localization.EN_US: american_gut.media_locale,
        localization.EN_GB: british_gut.media_locale
    }
    tls = {
        localization.EN_US: american_gut._NEW_PARTICIPANT,
        localization.EN_GB: british_gut._NEW_PARTICIPANT
    }

    return render_template("new_participant.jinja2",
                           message=None,
                           media_locale=media_locales[language_tag],
                           tl=tls[language_tag],
                           lang_tag=language_tag)


def create_human_source_from_consent(account_id, body, token_info):
    validate_access(token_info, account_id)

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

    child_keys = {'parent_1_name', 'parent_2_name', 'deceased_parent',
                  'obtainer_name'}

    intersection = child_keys.intersection(body)
    if intersection:
        source['consent']['child_info'] = {}
        for key in intersection:
            source['consent']['child_info'][key] = body[key]

    # NB: Don't expect to handle errors 404, 422 in this function; expect to
    # farm out to `create_source`
    return create_source(account_id, source, token_info)


def verify_authrocket(token):
    try:
        token_info = jwt.decode(token,
                                AUTHROCKET_PUB_KEY,
                                algorithm="RS256",
                                verify=True)
        if token_info['iss'] != "https://authrocket.com":
            raise(Unauthorized("Invalid issuer"))

        # TODO: Ensure that we're checking every field that we care about

        return token_info
    except InvalidTokenError as e:
        raise(Unauthorized("Invalid Token", e))


def validate_access(token_info, account_id):
    with Transaction() as t:
        account_repo = AccountRepo(t)
        account = account_repo.get_account(account_id)
        if account.auth_issuer != token_info['iss'] or \
                account.auth_sub != token_info['sub']:
            raise Unauthorized()
