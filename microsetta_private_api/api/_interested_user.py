from flask import jsonify
from microsetta_private_api.model.interested_user import InterestedUser
from microsetta_private_api.repo.interested_user_repo import InterestedUserRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.exceptions import RepoException


def create_interested_user(body):
    body['postal_code'] = body['postal']
    try:
        interested_user = InterestedUser.from_dict(body)
    except ValueError:
        return jsonify(
            code=400,
            message="Failed to instantiate interested user."
        ), 400

    with Transaction() as t:
        interested_user_repo = InterestedUserRepo(t)

        try:
            interested_user_id = \
                interested_user_repo.insert_interested_user(interested_user)
        except RepoException:
            return jsonify(
                code=400,
                message="Failed to create interested user."
            ), 400

        t.commit()

    # opening a new transaction for address verification so we don't lose the
    # interested user record if something unexpected happens during address
    # verification
    with Transaction() as t:
        interested_user_repo = InterestedUserRepo(t)
        try:
            # at this point, we don't particularly care if it's valid
            # we just care that it doesn't fail to execute
            interested_user_repo.verify_address(interested_user_id)
        except RepoException:
            return jsonify(
                code=400,
                message="Failed to verify address."
            ), 400

        t.commit()

    return jsonify(user_id=interested_user_id), 200
