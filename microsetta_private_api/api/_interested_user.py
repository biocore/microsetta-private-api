from flask import jsonify
from microsetta_private_api.repo.interested_user_repo import InterestedUserRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.exceptions import RepoException


def create_interested_user(body):
    with Transaction() as t:
        interested_user_repo = InterestedUserRepo(t)

        interested_user_id = None

        try:
            interested_user_id = \
                interested_user_repo.insert_interested_user(**body)
        except ValueError as e:
            raise Exception(e)

        if interested_user_id is None:
            return jsonify(
                code=400,
                message="Failed to create interested user"
            ), 400
        else:
            try:
                interested_user_repo.verify_address(interested_user_id)
            except RepoException as e:
                raise Exception(e)

        t.commit()

    return jsonify(user_id=interested_user_id), 200
