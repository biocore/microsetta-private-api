from flask import jsonify
from microsetta_private_api.api._account import \
    _validate_account_access
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo
from microsetta_private_api.repo.vioscreen_repo import VioscreenSessionRepo


def read_sample_vioscreen_session(account_id, source_id, sample_id, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        surv_temp = SurveyTemplateRepo(t)
        vio_sess = VioscreenSessionRepo(t)

        vio_username = surv_temp.get_vioscreen_id_if_exists(account_id, source_id, sample_id)
        if vio_username is None:
            return jsonify(code=404, message="Session not found"), 404

        vioscreen_sessions = vio_sess.get_sessions_by_username(vio_username)
        if vioscreen_sessions is None:
            return jsonify(code=404, message="Session not found"), 404

        return jsonify(vioscreen_sessions[0].to_api()), 200
