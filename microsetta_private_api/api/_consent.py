from flask import jsonify
import uuid
from microsetta_private_api import localization
from microsetta_private_api.api._account import \
    _validate_account_access
from microsetta_private_api.model.consent import ConsentSignature
from microsetta_private_api.repo.consent_repo import ConsentRepo
from microsetta_private_api.repo.transaction import Transaction


def render_consent_doc(account_id, language_tag, token_info):
    _validate_account_access(token_info, account_id)

    consent_form = {}

    localization_info = localization.LANG_SUPPORT[language_tag]
    content = localization_info[localization.NEW_PARTICIPANT_KEY]
    consent_form["PARTICIPANT_FORM"] = content

    with Transaction() as t:
        consent_repo = ConsentRepo(t)
        documents = consent_repo.get_all_consent_documents()
        data = [x.to_api() for x in documents]
        consent_form["CONSENT_DOCS"] = data

    return jsonify(consent_form), 200


def get_consent_doc(account_id, consent_id, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        consent_repo = ConsentRepo(t)
        documents = consent_repo.get_consent_document(consent_id)
        data = [x.to_api() for x in documents]

    return jsonify(data), 200


def check_consent_signature(account_id, source_id, consent_type, token_info):
    _validate_account_access(token_info, account_id)

    res = False

    with Transaction() as t:
        consent_repo = ConsentRepo(t)
        res = consent_repo.is_consent_required(source_id, consent_type)

    return jsonify({"result":res}), 200


def sign_consent_document(account_id, source_id, consent_type, body, token_info):

    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        consent_repo = ConsentRepo(t)
        signature_id = str(uuid.uuid4())

        consent_sign = ConsentSignature.from_dict(body, source_id, signature_id)
        consent_repo.sign_consent(account_id, consent_sign)
        t.commit()

        response = jsonify({"result": True})
        response.status_code = 201
        response.headers['Location'] = '/api/accounts/%s' % \
                                   (account_id)

        return response


# def render_consent_doc(account_id, language_tag, token_info):
#     _validate_account_access(token_info, account_id)

#     # NB: Do NOT need to explicitly pass account_id into template for
#     # integration into form submission URL because form submit URL builds on
#     # the base of the URL that called it (which includes account_id)

#     localization_info = localization.LANG_SUPPORT[language_tag]
#     content = localization_info[localization.NEW_PARTICIPANT_KEY]

#     return jsonify(content), 200