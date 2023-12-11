import uuid
import re
from flask import jsonify
from microsetta_private_api.model.interested_user import InterestedUser
from microsetta_private_api.repo.interested_user_repo import InterestedUserRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.repo.campaign_repo import CampaignRepo
from microsetta_private_api.repo.melissa_repo import MelissaRepo
from microsetta_private_api.repo.perk_fulfillment_repo import\
    PerkFulfillmentRepo
from microsetta_private_api.tasks import send_email
from microsetta_private_api.admin.admin_impl import validate_admin_access


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

        campaign_repo = CampaignRepo(t)
        campaign_info =\
            campaign_repo.get_campaign_by_id(interested_user.campaign_id)

        if campaign_info.send_thdmi_confirmation:
            try:
                # Send a confirmation email
                # TODO: Add more intelligent locale determination.
                # Punting on that since our current campaign use cases
                # are only a single language.
                send_email(interested_user.email,
                           "submit_interest_confirmation",
                           {"contact_name": interested_user.first_name},
                           campaign_info.language_key)
            except:  # noqa
                # try our best to email
                pass

        t.commit()

    # opening a new transaction for address verification so we don't lose the
    # interested user record if something unexpected happens during address
    # verification

    # NOTE 2022-09-01: Disabling address verification for interested users as
    # Melissa seems to be throwing false negatives for Spain. Will revisit
    # in the future.
    # with Transaction() as t:
    #    interested_user_repo = InterestedUserRepo(t)
    #    try:
    #        at this point, we don't particularly care if it's valid
    #        we just care that it doesn't fail to execute
    #        interested_user_repo.verify_address(interested_user_id)
    #    except RepoException:
    #        return jsonify(
    #            code=400,
    #            message="Failed to verify address."
    #        ), 400

    #    t.commit()

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
                # If the address is already valid, no reason to update.
                if interested_user.address_valid:
                    return jsonify(
                        code=400,
                        message="Address already verified."
                    ), 400
                else:
                    # We've determined it's a valid user and their address
                    # needs to be fixed, so we return a subset of their info.
                    # We also need to grab the reason(s) that Melissa couldn't
                    # verify the address.
                    melissa_repo = MelissaRepo(t)
                    melissa_result = melissa_repo.check_duplicate(
                        interested_user.address_1,
                        interested_user.address_2,
                        interested_user.postal_code,
                        interested_user.country
                    )

                    if melissa_result is False:
                        # We shouldn't reach this point, but it means the
                        # address wasn't actually checked
                        return jsonify(
                            code=404,
                            message="Address verification data missing."
                        ), 404

                    result_codes = melissa_result['result_codes'].split(",")
                    error_codes = []
                    for code in result_codes:
                        # We're only interested in AE codes
                        if code[0:2] == "AE":
                            error_codes.append(code)

                    return jsonify(
                        interested_user_id=interested_user.interested_user_id,
                        email=interested_user.email,
                        address_1=interested_user.address_1,
                        address_2=interested_user.address_2,
                        address_3=interested_user.address_3,
                        city=interested_user.city,
                        state=interested_user.state,
                        postal_code=interested_user.postal_code,
                        country=interested_user.country,
                        error_codes=error_codes
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
                interested_user.address_3 = body['address_3']
                interested_user.phone = body['phone']
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


def get_opt_out(interested_user_id):
    with Transaction() as t:
        i_u_repo = InterestedUserRepo(t)
        i_u = i_u_repo.get_interested_user_by_id(interested_user_id)

        if i_u is None:
            return jsonify(
                code=404,
                message="Interested user not found."
            ), 404
        else:
            campaign_repo = CampaignRepo(t)
            campaign_info = \
                campaign_repo.get_campaign_by_id(i_u.campaign_id)

        return jsonify(
            interested_user_id=interested_user_id,
            force_primary_language=campaign_info.force_primary_language,
            language_key=campaign_info.language_key
        ), 200


def put_opt_out(interested_user_id):
    with Transaction() as t:
        i_u_repo = InterestedUserRepo(t)
        i_u = i_u_repo.get_interested_user_by_id(interested_user_id)

        if i_u is None:
            return jsonify(
                code=404,
                message="Interested user not found."
            ), 404
        else:
            # We don't care if they've already opted out, we're just going to
            # tell them we've removed them from the list
            _ = i_u_repo.opt_out_interested_user(interested_user_id)

            campaign_repo = CampaignRepo(t)
            campaign_info = \
                campaign_repo.get_campaign_by_id(i_u.campaign_id)

            t.commit()

        return jsonify(
            interested_user_id=interested_user_id,
            force_primary_language=campaign_info.force_primary_language,
            language_key=campaign_info.language_key
        ), 200


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


def search_ffq_codes_by_email(email, token_info):
    validate_admin_access(token_info)

    with Transaction() as t:
        pfr = PerkFulfillmentRepo(t)
        ffq_diag = pfr.get_ffq_codes_by_email(email)
        ffq_codes_obj = {
            "ffq_codes": ffq_diag
        }
        if ffq_diag is None:
            return jsonify(code=404, message="Email not found"), 404
        return jsonify(ffq_codes_obj), 200
