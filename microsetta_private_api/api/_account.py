import uuid

import jwt
from flask import jsonify
from jwt import InvalidTokenError

from werkzeug.exceptions import Unauthorized, Forbidden, NotFound

from microsetta_private_api.api.literals import AUTHROCKET_PUB_KEY, \
    INVALID_TOKEN_MSG, JWT_ISS_CLAIM_KEY, JWT_SUB_CLAIM_KEY, \
    JWT_EMAIL_CLAIM_KEY, ACCT_NOT_FOUND_MSG, CRONJOB_PUB_KEY
from microsetta_private_api.model.account import Account, AuthorizationMatch
from microsetta_private_api.model.address import Address
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.activation_repo import ActivationRepo
from microsetta_private_api.repo.kit_repo import KitRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.config_manager import SERVER_CONFIG


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
    # Account.from_dict requires a kit_name, even if blank
    kit_name = body.get("kit_name", "")
    body["kit_name"] = kit_name
    code = body.get("code", "")
    body["code"] = code

    account_obj = Account.from_dict(body, token_info[JWT_ISS_CLAIM_KEY],
                                    token_info[JWT_SUB_CLAIM_KEY])

    if kit_name == "" and code == "":
        return jsonify(
            code=400,
            message="Account registration requires "
                    "valid kit ID or activation code"), 400

    with Transaction() as t:
        activation_repo = ActivationRepo(t)
        if code != "":
            can_activate, cause = activation_repo.can_activate_with_cause(
                body["email"],
                code
            )
            if not can_activate:
                return jsonify(code=404, message=cause), 404
            else:
                activation_repo.use_activation_code(body["email"], code)

        if kit_name != "":
            kit_repo = KitRepo(t)
            kit = kit_repo.get_kit_all_samples(kit_name)
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
        acc.language = body['language']

        # 422 handling is done inside acct_repo
        acct_repo.update_account(acc)
        t.commit()

        return jsonify(acc.to_api()), 200


JWT_SCHEMES = (
    {'key': AUTHROCKET_PUB_KEY,
     'algorithms': ["RS256"],
     'verify': True,
     'issuer': 'https://authrocket.com'},
    {'key': CRONJOB_PUB_KEY,
     'algorithms': ["RS256"],
     'verify': True,
     'issuer': 'https://microsetta.ucsd.edu'},
)


def _verify_jwt_mock(token):
    assert SERVER_CONFIG.get('disable_authentication', False)

    ###########################################################################
    # WARNING: use of this mock DISABLES verification of the JWT              #
    #                                                                         #
    # This method is intended only for use during integration testing         #
    ###########################################################################
    email_verification_key = 'email_verified'

    token_info = None
    try:
        token_info = jwt.decode(token, options={"verify_signature": False})
    except InvalidTokenError:
        pass

    # if we can't get out the encoded email, then we can't do anything
    # interesting anyway
    if token_info is None:
        raise Unauthorized(INVALID_TOKEN_MSG)

    # allow the test harness to explore email verification
    if token_info[email_verification_key] is not True:
        raise Forbidden("Email is not verified")

    return token_info


def _verify_jwt(token):
    email_verification_key = 'email_verified'

    token_info = None
    for scheme in JWT_SCHEMES:
        try:
            token_info = jwt.decode(token, **scheme)
        except InvalidTokenError:
            continue
        else:
            break

    if token_info is None:
        raise Unauthorized(INVALID_TOKEN_MSG)

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
            if token_associated_account is not None and \
                    token_associated_account.account_type == 'deleted':
                raise Unauthorized()

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


def _validate_has_account(token_info):
    # WARNING: this does NOT authenticate a user but tests for the
    # presence of an account
    with Transaction() as t:
        account_repo = AccountRepo(t)
        token_associated_account = account_repo.find_linked_account(
            token_info['iss'],
            token_info['sub'])

    if token_associated_account is None:
        raise Unauthorized()
    else:
        return
