from flask import jsonify
import uuid
from microsetta_private_api import localization
from microsetta_private_api.api._account import \
    _validate_account_access
from microsetta_private_api.model.consent import ConsentSignature
from microsetta_private_api.repo.consent_repo import ConsentRepo
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.api.literals import CONSENT_DOC_NOT_FOUND_MSG
from werkzeug.exceptions import NotFound
from microsetta_private_api.api.literals import SRC_NOT_FOUND_MSG


def render_consent_doc(account_id, language_tag, token_info):
    _validate_account_access(token_info, account_id)

    consent_form = {}

    localization_info = localization.LANG_SUPPORT[language_tag]
    content = localization_info[localization.NEW_PARTICIPANT_KEY]
    consent_form["PARTICIPANT_FORM"] = content

    with Transaction() as t:
        consent_repo = ConsentRepo(t)
        documents = consent_repo.get_all_consent_documents(language_tag)
        data = [x.to_api() for x in documents]
        consent_form["CONSENT_DOCS"] = data

    return jsonify(consent_form), 200


def get_consent_doc(account_id, consent_id, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        consent_repo = ConsentRepo(t)
        document = consent_repo.get_consent_document(consent_id)

    if document:
        data = document.to_api()
        return jsonify(data), 200
    else:
        return jsonify(code=404, message=CONSENT_DOC_NOT_FOUND_MSG), 404


def check_consent_signature(account_id, source_id, consent_type, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        consent_repo = ConsentRepo(t)
        source_repo = SourceRepo(t)
        source = source_repo.get_source(account_id, source_id)
        age_range = source.source_data.age_range
        res = consent_repo.is_consent_required(
            source_id, age_range, consent_type
        )

    return jsonify({"result": res}), 200


def sign_consent_doc(account_id, source_id, consent_type, body, token_info):
    _validate_account_access(token_info, account_id)

    human_consent_age_groups = ["0-6", "7-12", "13-17", "18-plus"]

    with Transaction() as t:
        # Sources are now permitted to update their age range, but only if it
        # moves the source to an older age group. For this purpose, "legacy"
        # is treated as younger than "0-6", as they're choosing an age group
        # for the first time.
        source_repo = SourceRepo(t)
        source = source_repo.get_source(account_id, source_id)
        if source is None:
            return jsonify(code=404, message=SRC_NOT_FOUND_MSG), 404

        if source.source_data.age_range != body['age_range']:
            # Let's make sure it's a valid change. First, grab the index of
            # their current age range.
            try:
                cur_age_index = human_consent_age_groups.index(
                    source.source_data.age_range
                )
            except ValueError as e:
                # Catch any sources that have a blank, "legacy", or faulty
                # age_range
                cur_age_index = -1

            # Next, make sure their new age range is valid
            try:
                new_age_index = human_consent_age_groups.index(
                    body['age_range']
                )
            except ValueError as e:
                # Shouldn't reach this point, but if we do, reject it
                return jsonify(
                    code=403, message="Invalid age_range update"
                ), 403

            # Finally, make sure the new age_range isn't younger than the
            # current age_range.
            if new_age_index < cur_age_index:
                return jsonify(
                    code=403, message="Invalid age_range update"
                ), 403

            update_success = source_repo.update_source_age_range(
                source_id, body['age_range']
            )
            if not update_success:
                return jsonify(
                    code=403, message="Invalid age_range update"
                ), 403

        # Now back to the normal flow of signing a consent document
        consent_repo = ConsentRepo(t)
        sign_id = str(uuid.uuid4())
        consent_sign = ConsentSignature.from_dict(body, source_id, sign_id)
        try:
            consent_repo.sign_consent(account_id, consent_sign)
            t.commit()
        except NotFound as e:
            return jsonify(code=404, message=e.description), 404

    response = jsonify({"result": True})
    response.status_code = 201
    response.headers['Location'] = '/api/accounts/%s' % \
        (account_id)

    return response


def get_signed_consent(account_id, source_id, consent_type, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        consent_repo = ConsentRepo(t)
        signed_consent = consent_repo.get_latest_signed_consent(
            source_id,
            consent_type
        )
        if signed_consent is None:
            return jsonify(code=404, message="No signed consent found"), 404

    return jsonify(signed_consent.to_api()), 200
