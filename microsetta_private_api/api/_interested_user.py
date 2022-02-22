import uuid
import re
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


def get_interested_user_address_update(interested_user_id, email):
    valid_data = _validate_iuid_and_email_syntax(interested_user_id, email)
    if not valid_data:
        return jsonify(
            code=404,
            message="Invalid user."
        ), 404
    else:
        with Transaction() as t:
            i_u_repo = InterestedUserRepo(t)
            interested_user = \
                i_u_repo.get_interested_user_by_id(interested_user_id)

            valid_user = _validate_user_match(interested_user, email)
            if not valid_user:
                return jsonify(
                    code=404,
                    message="Invalid user."
                ), 404
            else:
                # if the address is already valid, no reason to update
                if interested_user.address_valid:
                    return jsonify(
                        code=400,
                        message="Address already verified."
                    ), 400
                else:
                    # we've determined it's a valid user and their address
                    # needs to be fixed, so we return a subset of their info
                    return jsonify(
                        interested_user_id=interested_user.interested_user_id,
                        email=interested_user.email,
                        address_1=interested_user.address_1,
                        address_2=interested_user.address_2,
                        city=interested_user.city,
                        state=interested_user.state,
                        postal_code=interested_user.postal_code,
                        country=interested_user.country
                    ), 200


def put_interested_user_address_update(body):
    interested_user_id = body['interested_user_id']
    email = body['email']

    valid_data = _validate_iuid_and_email_syntax(interested_user_id, email)
    if not valid_data:
        return jsonify(
            code=404,
            message="Invalid user."
        ), 404
    else:
        with Transaction() as t:
            i_u_repo = InterestedUserRepo(t)
            interested_user = \
                i_u_repo.get_interested_user_by_id(interested_user_id)

            valid_user = _validate_user_match(interested_user, email)
            if not valid_user:
                return jsonify(
                    code=404,
                    message="Invalid user."
                ), 404
            else:
                # reset address_checked flag so the verify_address() function
                # can run and update with Melissa-generated results
                interested_user.address_checked = False
                interested_user.address_1 = body['address_1']
                interested_user.address_2 = body['address_2']
                interested_user.city = body['city']
                interested_user.state = body['state']
                interested_user.postal_code = body['postal']
                update_success = \
                    i_u_repo.update_interested_user(interested_user)

                if update_success is False:
                    return jsonify(
                        code=400,
                        message="Failed to update address."
                    ), 400
                t.commit()

        # open new transaction so we don't lose user data if there's a problem
        # with address validation
        with Transaction() as t:
            interested_user_repo = InterestedUserRepo(t)
            try:
                interested_user_repo.verify_address(interested_user_id)
            except RepoException:
                # we really shouldn't reach this point, but just in case
                return jsonify(
                    code=400,
                    message="Failed to verify address."
                ), 400

            t.commit()

        return jsonify(user_id=interested_user_id), 200


def _validate_iuid_and_email_syntax(interested_user_id, email):
    try:
        uuid.UUID(interested_user_id)
    except ValueError:
        return False

    if re.fullmatch(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                    email):
        return True
    else:
        return False


def _validate_user_match(interested_user, email):
    if interested_user is None:
        return False
    else:
        # we're using both email and interested_user_id to make sure
        # someone doesn't stumble upon a valid email and/or id.
        # if they don't both match, treat as invalid
        return interested_user.email == email
