"""
Mock functions to implement proof-of-concept OpenAPI 3.0 interface to access private PHI.

Underlies the resource server in the oauth2 workflow. "Resource Server: The server hosting user-owned resources that are
protected by OAuth2. The resource server validates the access-token and serves the protected resources."
--https://dzone.com/articles/oauth-20-beginners-guide

Note that there's no actual back-end yet, so even theoretically state-changing actions don't really change any state :)

Loosely based off examples in https://realpython.com/flask-connexion-rest-api/#building-out-the-complete-api
and associated file https://github.com/realpython/materials/blob/master/flask-connexion-rest/version_3/people.py
"""

from flask import make_response, abort
import jwt
from base64 import b64decode


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


def read_account():
    return {"fname": "Jane", "lname": "Doe", "email": "jdoe@gmail.com"}


def update_account(fname, lname, email):
    return {"fname": fname, "lname": lname, "email": email}


def read_sources(acct_id):
    return not_yet_implemented()


def create_source(acct_id):
    return not_yet_implemented()


def read_source(acct_id, source_id):
    return not_yet_implemented()


def update_source(acct_id, source_id):
    return not_yet_implemented()


def read_answered_surveys(acct_id, source_id):
    return not_yet_implemented()


def read_answered_survey(acct_id, source_id, answered_survey_id):
    return not_yet_implemented()


def read_sample_associations(acct_id, source_id):
    return not_yet_implemented()


def associate_sample(acct_id, source_id):
    return not_yet_implemented()


def read_sample_association(acct_id, source_id, sample_association_id):
    return not_yet_implemented()


def unassociate_sample(acct_id, source_id, sample_association_id):
    return not_yet_implemented()


def read_answered_survey_associations(acct_id, source_id, sample_association_id):
    return not_yet_implemented()


def associate_answered_survey(acct_id, source_id, sample_association_id):
    return not_yet_implemented()


def unassociate_answered_survey(acct_id, source_id, sample_association_id, survey_association_id):
    return not_yet_implemented()


def read_kits(kit_name, kit_code):
    return not_yet_implemented()


def read_kit(kit_id):
    return not_yet_implemented()
