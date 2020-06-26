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
import jwt

from jwt import InvalidTokenError

from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.account_repo import AccountRepo

from microsetta_private_api.model.account import AuthorizationMatch

from werkzeug.exceptions import Unauthorized, Forbidden, NotFound

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
        token_associated_account = account_repo.find_linked_account(
            token_info['iss'],
            token_info['sub'])
        account = account_repo.get_account(account_id)
        if account is None:
            raise NotFound(ACCT_NOT_FOUND_MSG)
        else:
            # Whether or not the token_info is associated with an admin acct
            token_authenticates_admin = \
                token_associated_account is not None and \
                token_associated_account.account_type == 'admin'

            # Enum of how closely token info matches requested account_id
            auth_match = account.account_matches_auth(
                token_info[JWT_EMAIL_CLAIM_KEY],
                token_info[JWT_ISS_CLAIM_KEY],
                token_info[JWT_SUB_CLAIM_KEY])

            # If token doesn't match requested account id, and doesn't grant
            # admin access to the system, deny.
            if auth_match == AuthorizationMatch.NO_MATCH and \
                    not token_authenticates_admin:
                raise Unauthorized()

        return account
