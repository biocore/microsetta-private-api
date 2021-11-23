from flask import jsonify
from microsetta_private_api.repo.interested_user_repo import InterestedUserRepo
from microsetta_private_api.repo.transaction import Transaction


def create_interested_user(body):
    with Transaction() as t:
        interested_user_repo = InterestedUserRepo(t)

        try:
            interested_user_id = \
                interested_user_repo.insert_interested_user(**body)
        except ValueError as e:
            raise Exception(e)

        t.commit()
        return jsonify(user_id=interested_user_id), 200
