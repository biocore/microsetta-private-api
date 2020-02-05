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

from flask import jsonify, render_template
import jwt
from base64 import b64decode

from microsetta_private_api.model.address import Address
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.repo.kit_repo import KitRepo
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo
from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo
from microsetta_private_api.repo.sample_repo import SampleRepo

from microsetta_private_api.model.account import Account
from microsetta_private_api.model.source import Source
from microsetta_private_api.model.source import human_info_from_api
from microsetta_private_api.LEGACY.locale_data import american_gut

from microsetta_private_api.util import vue_adapter

import uuid
import json
from datetime import date

TOKEN_KEY = "QvMWMnlOqBbNsM88AMxpzcJMbBUu/w8U9joIaNYjuEbwEYhLIB5FqEoFWnfLN3JZN4SD0LAtZOwFNqyMLmNruBLqEvbpjQzM6AY+BfXGxDVFL65c9Xw8ocd6t1nF6YvTpHGB4NJhUwngjIQmFx+6TCa5wArtEqUeoIc1ukVTYbioRkxzi5ju8cc9/PoInB0c7wugMz5ihAPWohpDc4kCotYv7C2K/e9J9CPdwbiLJKYKxO4zSQAqk+Sj4wRcn7bJqIOIT6BlvvnzRGXYG33qXAxGylM4UySj7ltwSGOIY0/JUvKEej3fX17C8wWtJvrjbFQacNhoglqfWq2GeOdRSA== "  # noqa: E501
TEMP_ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vbXlhcHAuY29tLyIsInN1YiI6InVzZXJzL3VzZXIxMjM0Iiwic2NvcGUiOiJzZWxmLCBhZG1pbnMiLCJqdGkiOiJkMzBkMzA5ZS1iZTQ5LTRjOWEtYjdhYi1hMGU3MTIwYmFlZDMiLCJpYXQiOjE1NzIzNzY4OTUsImV4cCI6MTU3MjM4MDQ5NX0.EMooERuy2Z4tC_TsXJe6Vx8yCgzTzI_qh84a5DsKPRw"  # noqa: E501
TEMP_DUMMY_ACCESS_TOKEN = "eyJ1aWQiOiJKYW5lIiwgImVtYWlsIjogImphbmVAc29tZXdoZXJlLmNvbSJ9"  # noqa: E501


def not_yet_implemented():
    return {'message': 'functionality not yet implemented'}


# not yet used, here to record POC work for future
def verify_and_decode_oauth2_jwt(access_token=TEMP_ACCESS_TOKEN) -> dict:
    token_header = jwt.get_unverified_header(access_token)
    if token_header['typ'] != "JWT":
        raise ValueError(
            "Provided access token is not in JWT format: {0}".format(
                access_token))
    alg_type = token_header['alg']

    decoded = jwt.decode(access_token, b64decode(TOKEN_KEY),
                         algorithms=alg_type, verify=False)
    # NOTE: doing a noop to avoid a flake8 item until this function goes into
    # actual use
    decoded = decoded

    # TODO: figure out what to return and how to dig it out of JWT
    return {'uid': "not_implemented", 'scope': ['uid']}


# temporary function that simply decodes a base64-encoded json string
def verify_and_decode_token(access_token) -> dict:
    decoded_token = b64decode(TEMP_DUMMY_ACCESS_TOKEN)
    token_obj = json.loads(decoded_token)
    token_obj["scope"] = ['uid']
    return token_obj


def register_account(body):
    # TODO: Do they register with GLOBUS first, then make the account here?
    #  What should be done with the kit_name?
    new_acct_id = str(uuid.uuid4())
    with Transaction() as t:
        kit_repo = KitRepo(t)
        kit = kit_repo.get_kit(body['kit_name'])
        if kit is None:
            return jsonify(error=403, text="Incorrect kit_name"), 403

        acct_repo = AccountRepo(t)
        acct_repo.create_account(Account(
            new_acct_id,
            body['email'],
            "standard",
            "GLOBUS",  # TODO: This is dependent on their login token!
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


def read_account(token_info, account_id):
    # TODO:  Authentication???
    with Transaction() as t:
        acct_repo = AccountRepo(t)
        acc = acct_repo.get_account(account_id)
        if acc is None:
            # TODO: Think this should be "code", "message" to match api?
            return jsonify(error=404, text="Account not found"), 404
        return jsonify(acc.to_api()), 200


def update_account(account_id, body):
    # TODO:  Authentication??
    with Transaction() as t:
        acct_repo = AccountRepo(t)
        acc = acct_repo.get_account(account_id)
        if acc is None:
            return jsonify(error=404, text="Account not found"), 404

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


def read_sources(account_id, source_type=None):
    with Transaction() as t:
        source_repo = SourceRepo(t)
        sources = source_repo.get_sources_in_account(account_id, source_type)
        api_sources = [x.to_api() for x in sources]
        # TODO: Also support 404? Or is that not necessary?
        return jsonify(api_sources), 200


def create_source(account_id, body):
    with Transaction() as t:
        source_repo = SourceRepo(t)
        source_id = str(uuid.uuid4())

        if body['source_type'] == 'human':
            # TODO: Unfortunately, humans require a lot of special handling,
            #  and we started mixing Source calls used for transforming to/
            #  from the database with source calls to/from the api.
            #  Would be nice to split this out better.
            new_source = Source(source_id,
                                account_id,
                                'human',
                                human_info_from_api(body,
                                                    consent_date=date.today(),
                                                    date_revoked=None))
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


def read_source(account_id, source_id):
    with Transaction() as t:
        source_repo = SourceRepo(t)
        # TODO: What about 404?
        source = source_repo.get_source(account_id, source_id)
        if source is None:
            return jsonify(error=404, text="Source not found"), 404
        return jsonify(source.to_api()), 200


def update_source(account_id, source_id, body):
    with Transaction() as t:
        source_repo = SourceRepo(t)
        source = source_repo.get_source(account_id, source_id)

        # Uhhh, where do I get source_data from???
        # source.source_data = something?
        # TODO: Answer: source data is coming in in the request body,
        #  Fill it in!

        source_repo.update_source_data(source)
        # I wonder if there's some way to get the creation_time/update_time
        # during the insert/update...
        source = source_repo.get_source(account_id, source_id)
        t.commit()
        # TODO: 404 and 422?
        return jsonify(source.to_api()), 200


def delete_source(account_id, source_id):
    with Transaction() as t:
        source_repo = SourceRepo(t)
        if not source_repo.delete_source(account_id, source_id):
            return jsonify(error=404, text="No source found"), 404
        # TODO: 422?
        t.commit()
        return '', 204


def read_survey_templates(account_id, source_id, language_tag):
    # TODO: I don't think this query is backed by one of the existing tables
    # I think it was just hardcoded...  Which honestly seems like a fine
    # solution to me...  How much do we care that survey identifiers are
    # guessable?

    # TODO: I don't think surveys have names... only survey groups have names.
    # So what can I pass down to the user that will make any sense here?
    with Transaction() as t:
        source_repo = SourceRepo(t)
        source = source_repo.get_source(account_id, source_id)
        if source is None:
            return jsonify(error=404, text="No source found"), 404
        if source.source_type == Source.SOURCE_TYPE_HUMAN:
            return jsonify([1, 3, 4, 5]), 200
        elif source.source_type == Source.SOURCE_TYPE_ANIMAL:
            return jsonify([2]), 200
        else:
            return jsonify([]), 200


def read_survey_template(account_id, source_id, survey_template_id,
                         language_tag):
    # TODO: can we get rid of source_id?  I don't have anything useful to do
    #  with it...  I guess I could check if the source is a dog before giving
    #  out a pet information survey?

    with Transaction() as t:
        survey_template_repo = SurveyTemplateRepo(t)
        survey_template = survey_template_repo.get_survey_template(
            survey_template_id)
        return jsonify(vue_adapter.to_vue_schema(survey_template)), 200


def read_answered_surveys(account_id, source_id, language_tag):
    with Transaction() as t:
        survey_answers_repo = SurveyAnswersRepo(t)
        return jsonify(
            survey_answers_repo.list_answered_surveys(
                account_id,
                source_id)), 200


def read_answered_survey(account_id, source_id, survey_id):
    # TODO: Don't need source_id, drop it or include for validation at db
    #  layer?
    with Transaction() as t:
        survey_answers_repo = SurveyAnswersRepo(t)
        survey_answers = survey_answers_repo.get_answered_survey(
            account_id,
            survey_id)
        return jsonify(survey_answers), 200


def submit_answered_survey(account_id, source_id, language_tag, body):
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

        response = jsonify('')
        response.status_code = 201
        response.headers['Location'] = '/api/accounts/%s' \
                                       '/sources/%s' \
                                       '/surveys/%s' % \
                                       (account_id,
                                        source_id,
                                        survey_answers_id)
        return response


def read_sample_associations(account_id, source_id):
    with Transaction() as t:
        sample_repo = SampleRepo(t)
        samples = sample_repo.get_samples_by_source(account_id, source_id)

    api_samples = [x.to_api() for x in samples]
    return jsonify(api_samples), 200


def associate_sample(account_id, source_id, body):
    with Transaction() as t:
        sample_repo = SampleRepo(t)
        sample_repo.associate_sample(account_id,
                                     source_id,
                                     body['sample_id'])
        t.commit()
    response = jsonify('')
    response.status_code = 201
    response.headers['Location'] = '/api/accounts/%s/sources/%s/samples/%s' % \
                                   (account_id, source_id, ['sample_id'])
    return response


def read_sample_association(account_id, source_id, sample_id):
    with Transaction() as t:
        sample_repo = SampleRepo(t)
        sample = sample_repo.get_sample(account_id, source_id, sample_id)
        if sample is None:
            return jsonify(error=404, text="Sample not found"), 404

        return jsonify(sample.to_api()), 200


def update_sample_association(account_id, source_id, sample_id, body):
    return not_yet_implemented()


def dissociate_sample(account_id, source_id, sample_id):
    return not_yet_implemented()


def read_answered_survey_associations(account_id, source_id, sample_id):
    return not_yet_implemented()


def associate_answered_survey(account_id, source_id, sample_id, body):
    return not_yet_implemented()


def dissociate_answered_survey(account_id, source_id, sample_id, survey_id):
    return not_yet_implemented()


def read_kit(kit_name):
    with Transaction() as t:
        kit_repo = KitRepo(t)
        # TODO: Ensure this name is what the repo layer expects
        kit = kit_repo.get_kit(kit_name)
        if kit is None:
            return jsonify(error=404, text="No such kit"), 404
        return jsonify(kit.to_api()), 200


def render_consent_doc(account_id):
    # return render_template("new_participant.jinja2",
    #                        message=MockJinja("message"),
    #                        media_locale=MockJinja("media_locale"),
    #                        tl=MockJinja("tl"))

    # NB: Do NOT need to explicitly pass account_id into template for
    # integration into form submission URL because form submit URL builds on
    # the base of the URL that called it (which includes account_id)
    return render_template("new_participant.jinja2",
                           message=None,
                           media_locale=american_gut.media_locale,
                           tl=american_gut._NEW_PARTICIPANT)


def create_human_source_from_consent(account_id, body):
    # Must convert consent form body into object processable by create_source.

    # Not adding any error handling here because if 'participant_name' isn't
    # here, we SHOULD be getting an error.
    source = {
        'source_type': "human",
        'source_name': body['participant_name'],
        'consent': {
            'participant_email': body['participant_email'],
            'age_range': body['age_range']
        }
    }

    child_keys = ['parent_1_name', 'parent_2_name',
                  'deceased_parent', 'obtainer_name']

    any_in = False
    for key in child_keys:
        if key in body:
            any_in = True

    if any_in:
        source['consent']['child_info'] = {}
        for key in child_keys:
            if key in body:
                source['consent']['child_info'][key] = body[key]

    # NB: Don't expect to handle errors 404, 422 in this function; expect to
    # farm out to `create_source`
    return create_source(account_id, source)
