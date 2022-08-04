from flask import jsonify
from werkzeug.exceptions import Unauthorized, NotFound
from microsetta_private_api.api.literals import \
    JWT_ISS_CLAIM_KEY, JWT_SUB_CLAIM_KEY, JWT_EMAIL_CLAIM_KEY, \
    ACCT_NOT_FOUND_MSG
from microsetta_private_api.model.account import AuthorizationMatch
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.removal_queue_repo import RemovalQueueRepo


def check_request_remove_account(account_id, token_info):
    # raises 401 if method fails
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        rq_repo = RemovalQueueRepo(t)
        status = rq_repo.check_request_remove_account(account_id)
        result = {'account_id': account_id, 'status': status}
        return jsonify(result), 200


def request_remove_account(account_id, token_info):
    # raises 401 if method fails
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        rq_repo = RemovalQueueRepo(t)
        rq_repo.request_remove_account(account_id)

    return jsonify(code=200, message="Request Accepted"), 200


def cancel_request_remove_account(account_id, token_info):
    # raises 401 if method fails
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        rq_repo = RemovalQueueRepo(t)
        rq_repo.cancel_request_remove_account(account_id)

    return jsonify(code=200, message="Request Accepted"), 200


def _validate_account_access(token_info, account_id):
    # Note this function is a duplicate of _validate_account_access() in
    # _account.py. TODO: Remove and replace
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
    # Note this function is a duplicate of _validate_has_account() in
    # _account.py. TODO: Remove and replace
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
