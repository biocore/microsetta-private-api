from ._account import (
    find_accounts_for_login, register_account, claim_legacy_acct,
    read_account, update_account, check_email_match, _verify_jwt,
    _verify_jwt_mock
)

from ._removal_queue import (
    check_request_remove_account, request_remove_account,
    cancel_request_remove_account
)

from ._consent import (
    render_consent_doc,
    check_consent_signature,
    sign_consent_doc,
    get_signed_consent
)
from ._source import (
    create_source, read_source, update_source, read_sources,
    create_human_source_from_consent, check_duplicate_source_name,
    scrub_source, check_source_ffq_prereqs
)
from ._survey import (
    read_survey_template, read_survey_templates, read_answered_survey,
    read_answered_surveys, submit_answered_survey,
    read_answered_survey_associations, top_food_report,
    read_myfoodrepo_available_slots
)
from ._sample import (
    read_sample_association, associate_sample, read_sample_associations,
    update_sample_association, dissociate_answered_survey,
    dissociate_sample, read_kit, associate_answered_survey, get_preparations
)

from ._activation import (
    check_activation
)

from ._vioscreen import (
    read_vioscreen_session, read_vioscreen_percent_energy,
    read_vioscreen_dietary_score, read_vioscreen_supplements,
    read_vioscreen_food_components,
    read_vioscreen_eating_patterns,
    read_vioscreen_mpeds, read_vioscreen_food_consumption,
    get_vioscreen_dietary_scores_by_component,
    get_vioscreen_dietary_scores_descriptions,
    get_vioscreen_food_components_by_code,
    get_vioscreen_food_components_descriptions,
    get_vioscreen_sessions, get_vioscreen_registry_entries, check_ffq_code
)

from ._campaign import (
    get_campaign_information
)

from ._interested_user import (
    create_interested_user, get_interested_user_address_update,
    put_interested_user_address_update, get_opt_out, put_opt_out
)

from ..config_manager import SERVER_CONFIG


verify_jwt = _verify_jwt
if SERVER_CONFIG.get('disable_authentication', False):
    import sys
    print("WARNING: jwt authentication disabled",
          file=sys.stderr, flush=True)
    verify_jwt = _verify_jwt_mock


__all__ = [
    'find_accounts_for_login',
    'register_account',
    'claim_legacy_acct',
    'read_account',
    'update_account',
    'check_email_match',
    'request_remove_account',
    'cancel_request_remove_account',
    'check_request_remove_account',
    'render_consent_doc',
    'create_source',
    'read_source',
    'check_source_ffq_prereqs',
    'update_source',
    'scrub_source',
    'read_sources',
    'check_duplicate_source_name',
    'create_human_source_from_consent',
    'check_consent_signature',
    'sign_consent_doc',
    'get_signed_consent',
    'read_survey_template',
    'read_survey_templates',
    'read_answered_survey',
    'read_answered_surveys',
    'read_answered_survey_associations',
    'top_food_report',
    'read_myfoodrepo_available_slots',
    'read_sample_association',
    'associate_sample',
    'read_sample_associations',
    'update_sample_association',
    'dissociate_answered_survey',
    'dissociate_sample',
    'read_kit',
    'associate_answered_survey',
    'submit_answered_survey',
    'verify_jwt',
    'get_preparations',
    'check_activation',
    'read_vioscreen_session',
    'read_vioscreen_percent_energy',
    'read_vioscreen_dietary_score',
    'read_vioscreen_supplements',
    'read_vioscreen_food_components',
    'read_vioscreen_eating_patterns',
    'read_vioscreen_mpeds',
    'read_vioscreen_food_consumption',
    'get_vioscreen_dietary_scores_by_component',
    'get_vioscreen_dietary_scores_descriptions',
    'get_vioscreen_food_components_by_code',
    'get_vioscreen_food_components_descriptions',
    'get_campaign_information',
    'create_interested_user',
    'get_interested_user_address_update',
    'put_interested_user_address_update',
    'get_vioscreen_sessions',
    'get_vioscreen_registry_entries',
    'check_ffq_code',
    'get_opt_out',
    'put_opt_out'
]
