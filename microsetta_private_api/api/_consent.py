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


def check_consent_signature(account_id, source_id, consent_type, language_tag, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        consent_repo = ConsentRepo(t)
        res = consent_repo.is_consent_required(source_id, consent_type)

    return jsonify({"result": res}), 200


def sign_consent_doc(account_id, source_id, consent_type, body, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        # Sources with an age_range of "legacy" will select an age range
        # the first time they sign a new consent document. We need to
        # catch legacy sources as they come in and update their age.
        source_repo = SourceRepo(t)
        source = source_repo.get_source(account_id, source_id)
        if source is None:
            return jsonify(code=404, message=SRC_NOT_FOUND_MSG), 404

        if source.source_data.age_range == "legacy":
            update_success = source_repo.update_legacy_source_age_range(
                source_id, body['age_range']
            )
            if not update_success:
                return jsonify(
                    code=403, message="Invalid age_range update"
                ), 403

        # NB For the time being, we need to block any pre-overhaul under-18
        # profiles from re-consenting. For API purposes, the safest way to
        # check whether it's a pre-overhaul or post-overhaul source is to look
        # at the creation_time on the source. Anything pre-overhaul is
        # prevented from signing a new consent document.
        if source.source_data.age_range not in ["legacy", "18-plus"] and\
                not source_repo.check_source_post_overhaul(
                    account_id, source_id
                ):
            return jsonify(
                code=403, message="Minors may not sign new consent documents"
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
