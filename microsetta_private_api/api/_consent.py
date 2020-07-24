from flask import jsonify

from microsetta_private_api import localization
from microsetta_private_api.api._account import \
    _validate_account_access


def render_consent_doc(account_id, language_tag, token_info):
    _validate_account_access(token_info, account_id)

    # NB: Do NOT need to explicitly pass account_id into template for
    # integration into form submission URL because form submit URL builds on
    # the base of the URL that called it (which includes account_id)

    localization_info = localization.LANG_SUPPORT[language_tag]
    content = localization_info[localization.NEW_PARTICIPANT_KEY]

    return jsonify(content), 200
