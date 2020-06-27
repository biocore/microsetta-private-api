from flask import render_template, jsonify

from microsetta_private_api import localization
from microsetta_private_api.api._account import \
    _validate_account_access


def render_consent_doc(account_id, language_tag, consent_post_url, token_info):
    _validate_account_access(token_info, account_id)

    # NB: Do NOT need to explicitly pass account_id into template for
    # integration into form submission URL because form submit URL builds on
    # the base of the URL that called it (which includes account_id)

    localization_info = localization.LANG_SUPPORT[language_tag]
    payload = {'lang_tag': language_tag,
               'post_url': consent_post_url}
    content = localization_info[localization.NEW_PARTICIPANT_KEY]
    payload.update({k.lower(): v for k,v in content.items()})
    return jsonify(payload), 200
