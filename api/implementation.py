"""
Mock functions to implement proof-of-concept OpenAPI 3.0 interface to access private PHI.

Underlies the resource server in the oauth2 workflow. "Resource Server: The server hosting user-owned resources that are
protected by OAuth2. The resource server validates the access-token and serves the protected resources."
--https://dzone.com/articles/oauth-20-beginners-guide

Note that there's no actual back-end yet, so even theoretically state-changing actions don't really change any state :)

Loosely based off examples in https://realpython.com/flask-connexion-rest-api/#building-out-the-complete-api
and associated file https://github.com/realpython/materials/blob/master/flask-connexion-rest/version_3/people.py
"""

from flask import make_response, abort, jsonify
import jwt
from base64 import b64decode
from repo.transaction import Transaction
from repo.account_repo import AccountRepo
from repo.source_repo import SourceRepo
from repo.kit_repo import KitRepo
from model.source import Source
import uuid


# hardcoded mapping of access tokens to uid, standing in for a
# token database shared by the authorization server and resource server
USER_NAME_BY_TOKEN = {
    '123': 'jdoe',
    '456': 'rms'
}

TOKEN_KEY = "QvMWMnlOqBbNsM88AMxpzcJMbBUu/w8U9joIaNYjuEbwEYhLIB5FqEoFWnfLN3JZN4SD0LAtZOwFNqyMLmNruBLqEvbpjQzM6AY+BfXGxDVFL65c9Xw8ocd6t1nF6YvTpHGB4NJhUwngjIQmFx+6TCa5wArtEqUeoIc1ukVTYbioRkxzi5ju8cc9/PoInB0c7wugMz5ihAPWohpDc4kCotYv7C2K/e9J9CPdwbiLJKYKxO4zSQAqk+Sj4wRcn7bJqIOIT6BlvvnzRGXYG33qXAxGylM4UySj7ltwSGOIY0/JUvKEej3fX17C8wWtJvrjbFQacNhoglqfWq2GeOdRSA== "


def not_yet_implemented():
    return {'message': 'functionality not yet implemented'}


def verify_and_decode_token(access_token= "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vbXlhcHAuY29tLyIsInN1YiI6InVzZXJzL3VzZXIxMjM0Iiwic2NvcGUiOiJzZWxmLCBhZG1pbnMiLCJqdGkiOiJkMzBkMzA5ZS1iZTQ5LTRjOWEtYjdhYi1hMGU3MTIwYmFlZDMiLCJpYXQiOjE1NzIzNzY4OTUsImV4cCI6MTU3MjM4MDQ5NX0.EMooERuy2Z4tC_TsXJe6Vx8yCgzTzI_qh84a5DsKPRw") -> dict:
    token_header = jwt.get_unverified_header(access_token)
    print(token_header)
    if token_header['typ'] != "JWT":
        raise ValueError("Provided access token is not in JWT format: {0}".format(access_token))
    alg_type = token_header['alg']
    unverified = jwt.decode(access_token, verify=False)
    print(unverified)
    decoded = jwt.decode(access_token, b64decode(TOKEN_KEY), algorithms=alg_type)
    print(decoded)

    user_name = USER_NAME_BY_TOKEN.get(access_token)

    if not user_name:
        return None

    return {'uid': user_name, 'scope': ['uid']}


def register_account(user):
    if user is None or user not in ["jdoe", "rms"]:
        abort(
            401, "Invalid or missing user {0}".format(user)
        )
    if user == "rms":
        abort(
            404, "User {0} not found".format(user)
        )
    return {"first_name": "Jane", "last_name": "Doe",
            "created_at": True, "updated_at:": True,
            "type": "something", "account_type": "something",
            "email": "jdoe@foo.com", "location": "here"}


def read_account(acct_id):
    # TODO:  Authentication???
    with Transaction() as t:
        acct_repo = AccountRepo(t)
        acc = acct_repo.get_account(acct_id)
        if acc is None:
            return jsonify(error=404, text="Account not found"), 404
        return jsonify(acc)


def update_account(acct_id, first_name, last_name, email, address):
    # TODO:  Authentication??
    with Transaction() as t:
        acct_repo = AccountRepo(t)
        acc = acct_repo.get_account(acct_id)
        if acc is None:
            return jsonify(error=404, text="Account not found"), 404

        acc.first_name = first_name
        acc.last_name = last_name
        acc.email = email
        acc.address = address

        acct_repo.update_account(acc)
        t.commit()
        return jsonify(acc)


def read_sources(acct_id, source_type):
    with Transaction() as t:
        source_repo = SourceRepo(t)
        return jsonify(
            source_repo.get_sources_in_account(acct_id, source_type))


def create_source(acct_id, source_info):
    with Transaction() as t:
        source_repo = SourceRepo(t)
        source_id = str(uuid.uuid4())
        new_source = Source.from_json(source_id, acct_id, source_info)
        source_repo.create_source(new_source)
        # Must pull from db to get creation_time, update_time
        s = source_repo.get_source(acct_id, new_source.id)
        t.commit()
        return jsonify(s)


def read_source(acct_id, source_id):
    with Transaction() as t:
        source_repo = SourceRepo(t)
        return source_repo.get_source(acct_id, source_id)


def update_source(acct_id, source_id):
    with Transaction() as t:
        source_repo = SourceRepo(t)
        source = source_repo.get_source(acct_id, source_id)

        # Uhhh, where do I get source_data from???
        # source.source_data = something?

        source_repo.update_source_data(source)
        # I wonder if there's some way to get the creation_time/update_time
        # during the insert/update...
        source = source_repo.get_source(acct_id, source_id)
        t.commit()
        return jsonify(source)


def delete_source(acct_id, source_id):
    with Transaction() as t:
        source_repo = SourceRepo(t)
        if not source_repo.delete_source(acct_id, source_id):
            return jsonify(error = 404, text="No source found"), 404
        return '', 204


def read_survey_templates(acct_id, source_id, locale_code):
    return not_yet_implemented()


def read_survey_template(acct_id, source_id, survey_template_id, locale_code):
    return not_yet_implemented()


def read_answered_surveys(acct_id, source_id):
    return not_yet_implemented()


def read_answered_survey(acct_id, source_id, survey_id):
    return not_yet_implemented()


def submit_answered_survey(acct_id, source_id, locale_code, survey_template_id, survey_text):
    return not_yet_implemented()


def delete_answered_survey(acct_id, source_id, survey_id):
    return not_yet_implemented()


def read_sample_associations(acct_id, source_id):
    return not_yet_implemented()


def associate_sample(acct_id, source_id):
    return not_yet_implemented()


def read_sample_association(acct_id, source_id, sample_id):
    return not_yet_implemented()


def update_sample_association(acct_id, source_id, sample_id):
    return not_yet_implemented()


def dissociate_sample(acct_id, source_id, sample_id):
    return not_yet_implemented()


def read_answered_survey_associations(acct_id, source_id, sample_id):
    return not_yet_implemented()


def associate_answered_survey(acct_id, source_id, sample_id):
    return not_yet_implemented()


def dissociate_answered_survey(acct_id, source_id, sample_id, survey_id):
    return not_yet_implemented()


def read_kit(kit_id, kit_code):
    with Transaction() as t:
        kit_repo = KitRepo(t)
        kit = kit_repo.get_kit(kit_id, kit_code)
        if kit is None:
            return jsonify(error=404, text="No such kit"), 404
        unused = []
        for s in kit.samples:
            if not s.deposited:
                unused.append(s)
        return jsonify(unused)


def read_survey_templates(acct_id, source_id):
    return not_yet_implemented()
