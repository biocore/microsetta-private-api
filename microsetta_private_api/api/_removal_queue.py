from flask import jsonify
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.removal_queue_repo import RemovalQueueRepo
from microsetta_private_api.api._account import _validate_account_access


def check_request_remove_account(account_id, token_info):
    # raises 401 if method fails
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        rq_repo = RemovalQueueRepo(t)
        status = rq_repo.check_request_remove_account(account_id)
        result = {'account_id': account_id, 'status': status}
        return jsonify(result), 200


def request_remove_account(account_id, token_info, user_delete_reason=None):
    # raises 401 if method fails
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        rq_repo = RemovalQueueRepo(t)
        rq_repo.request_remove_account(account_id, user_delete_reason)
        t.commit()

    return jsonify(code=200, message="Request Accepted"), 200


def cancel_request_remove_account(account_id, token_info):
    # raises 401 if method fails
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        rq_repo = RemovalQueueRepo(t)
        rq_repo.cancel_request_remove_account(account_id)
        t.commit()

    return jsonify(code=200, message="Request Accepted"), 200
