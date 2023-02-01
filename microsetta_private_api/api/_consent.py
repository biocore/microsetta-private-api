from flask import jsonify
import uuid
from microsetta_private_api import localization
from microsetta_private_api.api._account import \
    _validate_account_access
from microsetta_private_api.model.consent import ConsentSignature
from microsetta_private_api.repo.consent_repo import ConsentRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.api.literals import CONSENT_DOC_NOT_FOUND_MSG


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
        res = consent_repo.is_consent_required(source_id, consent_type)

    return jsonify({"result": res}), 200


def sign_consent_doc(account_id, source_id, consent_type, body, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        consent_repo = ConsentRepo(t)
        sign_id = str(uuid.uuid4())
        consent_sign = ConsentSignature.from_dict(body, source_id, sign_id)
        try:
            consent_repo.sign_consent(account_id, consent_sign)
            t.commit()
        except Exception as e:
            raise Exception(e)
            return jsonify(code=404, message=e), 404

    response = jsonify({"result": True})
    response.status_code = 201
    response.headers['Location'] = '/api/accounts/%s' % \
        (account_id)

    return response


def get_signed_consents(account_id, source_id, token_info):
    _validate_account_access(token_info, account_id)

    ret_val = {}
    with Transaction() as t:
        consent_repo = ConsentRepo(t)
        survey_consent = consent_repo.get_latest_signed_consent(
            source_id,
            "data"
        )
        if survey_consent is None:
            ret_val['survey'] = None
        else:
            survey_consent = survey_consent.to_api()
            survey_doc = consent_repo.get_consent_document(
                survey_consent['consent_id']
            )
            survey_consent['consent_content'] = survey_doc.consent_content
            if survey_consent['assent_id'] is not None:
                assent_doc = consent_repo.get_consent_document(
                    survey_consent['assent_id']
                )
                survey_consent['assent_content'] = assent_doc.consent_content
            ret_val['survey'] = survey_consent

        sample_consent = consent_repo.get_latest_signed_consent(
            source_id,
            "biospecimen"
        )
        if sample_consent is None:
            ret_val['sample'] = None
        else:
            sample_consent = sample_consent.to_api()
            sample_doc = consent_repo.get_consent_document(
                sample_consent['consent_id']
            )
            sample_consent['consent_content'] = sample_doc.consent_content
            if sample_consent['assent_id'] is not None:
                assent_doc = consent_repo.get_consent_document(
                    sample_consent['assent_id']
                )
                sample_consent['assent_content'] = assent_doc.consent_content
            ret_val['sample'] = sample_consent

    return jsonify(ret_val), 200
