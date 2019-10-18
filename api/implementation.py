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


# hardcoded mapping of access tokens to uid, standing in for a
# token database shared by the authorization server and resource server
USER_NAME_BY_TOKEN = {
    '123': 'jdoe',
    '456': 'rms'
}


def verify_and_decode_token(access_token) -> dict:
    user_name = USER_NAME_BY_TOKEN.get(access_token)

    if not user_name:
        return None

    return {'uid': user_name, 'scope': ['uid']}


def read(user):
    if user is None or user not in ["jdoe", "rms"]:
        abort(
            401, "Invalid or missing user {0}".format(user)
        )
    if user == "rms":
        abort(
            404, "User {0} not found".format(user)
        )
    return {"fname": "Jane", "lname": "Doe", "consented": True}


def check_verified(kit_id):
    if kit_id == 1234:
        return {"kit_id": kit_id, "is_verified": True}
    elif kit_id == 5678:
        return {"kit_id": kit_id, "is_verified": False}
    else:
        abort(
            404, "Kit id {0} not found".format(kit_id)
        )


def verify(kit_id):
    if kit_id in [1234, 5678]:
        return {"kit_id": kit_id}
    else:
        abort(
            404, "Kit id {0} not found".format(kit_id)
        )


def register(kit_id):
    if kit_id in [1234, 5678]:
        return make_response(
            "{0} successfully registered".format(kit_id), 201
        )
    else:
        abort(
            404, "Kit id {0} not found".format(kit_id)
        )


def read_settings():
    return {"fname": "Jane", "lname": "Doe", "email": "jdoe@gmail.com"}


def set_settings(fname, lname, email):
    return {"fname": fname, "lname": lname, "email": email}


def read_samples():
    return [{"sample_id": 1, "collection_date": "2016-10-01", "status": "not arrived"},
            {"sample_id":2, "collection_date": "2019-09-04", "status": "sequenced"}]


def add_sample(sample_id, collection_date):
    if sample_id in [1, 2]:
        abort(
            403, "Sample id {0} already exists".format(sample_id)
        )
    return make_response(
        "{0} successfully registered".format(sample_id), 201
    )


def set_sample_status(sample_id, status):
    if sample_id in [1, 2]:
        return {"sample_id": sample_id, "status": status}
    else:
        abort(
            404, "Sample id {0} not found".format(sample_id)
        )


def set_password(password):
    return make_response(
        "Successfully updated password", 200
    )
