from flask import jsonify
from microsetta_private_api.api._account import \
    _validate_account_access
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo
from microsetta_private_api.repo.vioscreen_repo import (VioscreenSessionRepo,
    VioscreenPercentEnergyRepo, VioscreenDietaryScoreRepo)


def read_sample_vioscreen_session(account_id, source_id, sample_id, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        surv_temp = SurveyTemplateRepo(t)
        vio_sess = VioscreenSessionRepo(t)

        vio_username = surv_temp.get_vioscreen_id_if_exists(account_id, source_id, sample_id)
        if vio_username is None:
            return jsonify(code=404, message="Session not found"), 404

        vioscreen_session = vio_sess.get_sessions_by_username(vio_username)
        if vioscreen_session is None:
            return jsonify(code=404, message="Session not found"), 404

        return jsonify(vioscreen_session[0].to_api()), 200

def read_sample_vioscreen_percent_energy(account_id, source_id, sample_id, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        surv_temp = SurveyTemplateRepo(t)
        vio_sess = VioscreenSessionRepo(t)
        vio_perc = VioscreenPercentEnergyRepo(t)

        vio_username = surv_temp.get_vioscreen_id_if_exists(account_id, source_id, sample_id)
        if vio_username is None:
            return jsonify(code=404, message="Percent Energy not found"), 404

        vioscreen_session = vio_sess.get_sessions_by_username(vio_username)
        if vioscreen_session is None:
            return jsonify(code=404, message="Percent Energy not found"), 404

        vioscreen_percent_energy = vio_perc.get_percent_energy(vioscreen_session[0].sessionId)
        if vioscreen_percent_energy is None:
            return jsonify(code=404, message="Percent Energy not found"), 404

        return jsonify(vioscreen_percent_energy.to_api()), 200

def read_sample_vioscreen_dietary_score(account_id, source_id, sample_id, token_info):
    _validate_account_access(token_info, account_id)

    with Transaction() as t:
        surv_temp = SurveyTemplateRepo(t)
        vio_sess = VioscreenSessionRepo(t)
        vio_diet = VioscreenDietaryScoreRepo(t)

        vio_username = surv_temp.get_vioscreen_id_if_exists(account_id, source_id, sample_id)
        if vio_username is None:
            return jsonify(code=404, message="Dietary Score not found"), 404

        vioscreen_session = vio_sess.get_sessions_by_username(vio_username)
        if vioscreen_session is None:
            return jsonify(code=404, message="Dietary Score not found"), 404

        vioscreen_dietary_score = vio_diet.get_dietary_score(vioscreen_session[0].sessionId)
        if vioscreen_dietary_score is None:
            return jsonify(code=404, message="Dietary Score not found"), 404

        return jsonify(vioscreen_dietary_score.to_api()), 200