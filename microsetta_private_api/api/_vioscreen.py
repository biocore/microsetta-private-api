from flask import jsonify
from microsetta_private_api.api._account import \
    _validate_account_access, _validate_has_account
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo
from microsetta_private_api.repo.vioscreen_repo import (
    VioscreenSessionRepo, VioscreenPercentEnergyRepo,
    VioscreenDietaryScoreRepo, VioscreenSupplementsRepo,
    VioscreenFoodComponentsRepo, VioscreenEatingPatternsRepo,
    VioscreenMPedsRepo, VioscreenFoodConsumptionRepo
)


def _get_session_by_account_details(account_id, source_id):
    with Transaction() as t:
        surv_temp = SurveyTemplateRepo(t)
        vio_sess = VioscreenSessionRepo(t)

        vio_username = surv_temp.get_vioscreen_id_if_exists(account_id,
                                                            source_id)
        if vio_username is None:
            return True, (jsonify(code=404, message="Username not found"), 404)

        vioscreen_session = vio_sess.get_sessions_by_username(vio_username)
        if vioscreen_session is None:
            return True, (jsonify(code=404, message="Session not found"), 404)

        return False, vioscreen_session


def read_vioscreen_session(account_id, source_id, token_info):
    _validate_account_access(token_info, account_id)

    is_error, vioscreen_session = _get_session_by_account_details(account_id,
                                                                  source_id)
    if is_error:
        return vioscreen_session

    return jsonify(vioscreen_session[0].to_api()), 200


def read_vioscreen_percent_energy(account_id, source_id, token_info):
    _validate_account_access(token_info, account_id)

    is_error, vioscreen_session = _get_session_by_account_details(account_id,
                                                                  source_id)
    if is_error:
        return vioscreen_session

    with Transaction() as t:
        vio_perc = VioscreenPercentEnergyRepo(t)

        vioscreen_percent_energy = vio_perc.get_percent_energy(
            vioscreen_session[0].sessionId)
        if vioscreen_percent_energy is None:
            return jsonify(code=404, message="Percent Energy not found"), 404

        return jsonify(vioscreen_percent_energy.to_api()), 200


def read_vioscreen_dietary_score(account_id, source_id, token_info):
    _validate_account_access(token_info, account_id)

    is_error, vioscreen_session = _get_session_by_account_details(account_id,
                                                                  source_id)
    if is_error:
        return vioscreen_session

    with Transaction() as t:
        vio_diet = VioscreenDietaryScoreRepo(t)

        vioscreen_dietary_scores = vio_diet.get_dietary_scores(
            vioscreen_session[0].sessionId)
        if vioscreen_dietary_scores is None:
            return jsonify(code=404, message="Dietary Score not found"), 404

        return jsonify([vds.to_api() for vds in vioscreen_dietary_scores]), 200


def read_vioscreen_supplements(account_id, source_id, token_info):
    _validate_account_access(token_info, account_id)

    is_error, vioscreen_session = _get_session_by_account_details(account_id,
                                                                  source_id)
    if is_error:
        return vioscreen_session

    with Transaction() as t:
        vio_supp = VioscreenSupplementsRepo(t)

        vioscreen_supplements = vio_supp.get_supplements(
            vioscreen_session[0].sessionId)
        if vioscreen_supplements is None:
            return jsonify(code=404, message="Supplements not found"), 404

        return jsonify(vioscreen_supplements.to_api()), 200


def read_vioscreen_food_components(account_id, source_id, token_info):
    _validate_account_access(token_info, account_id)

    is_error, vioscreen_session = _get_session_by_account_details(account_id,
                                                                  source_id)
    if is_error:
        return vioscreen_session

    with Transaction() as t:
        vio_food = VioscreenFoodComponentsRepo(t)

        vioscreen_food_components = vio_food.get_food_components(
            vioscreen_session[0].sessionId)
        if vioscreen_food_components is None:
            return jsonify(code=404, message="Food Components not found"), 404

        return jsonify(vioscreen_food_components.to_api()), 200


def read_vioscreen_eating_patterns(account_id, source_id, token_info):
    _validate_account_access(token_info, account_id)

    is_error, vioscreen_session = _get_session_by_account_details(account_id,
                                                                  source_id)
    if is_error:
        return vioscreen_session

    with Transaction() as t:
        vio_eat = VioscreenEatingPatternsRepo(t)

        vioscreen_eating_patterns = vio_eat.get_eating_patterns(
            vioscreen_session[0].sessionId)
        if vioscreen_eating_patterns is None:
            return jsonify(code=404, message="Eating Patterns not found"), 404

        return jsonify(vioscreen_eating_patterns.to_api()), 200


def read_vioscreen_mpeds(account_id, source_id, token_info):
    _validate_account_access(token_info, account_id)

    is_error, vioscreen_session = _get_session_by_account_details(account_id,
                                                                  source_id)
    if is_error:
        return vioscreen_session

    with Transaction() as t:
        vio_mped = VioscreenMPedsRepo(t)

        vioscreen_mpeds = vio_mped.get_mpeds(vioscreen_session[0].sessionId)
        if vioscreen_mpeds is None:
            return jsonify(code=404, message="MPeds not found"), 404

        return jsonify(vioscreen_mpeds.to_api()), 200


def read_vioscreen_food_consumption(account_id, source_id, token_info):
    _validate_account_access(token_info, account_id)

    is_error, vioscreen_session = _get_session_by_account_details(account_id,
                                                                  source_id)
    if is_error:
        return vioscreen_session

    with Transaction() as t:
        vio_cons = VioscreenFoodConsumptionRepo(t)

        vioscreen_food_consumption = vio_cons.get_food_consumption(
            vioscreen_session[0].sessionId)
        if vioscreen_food_consumption is None:
            return jsonify(code=404, message="Food Consumption not found"), 404

        return jsonify(vioscreen_food_consumption.to_api()), 200


def get_vioscreen_dietary_scores_by_component(score_type, score_code,
                                              token_info):
    _validate_has_account(token_info)

    with Transaction() as t:
        vio_diet = VioscreenDietaryScoreRepo(t)
        scores = vio_diet.get_dietary_scores_by_component(score_type,
                                                          score_code)

        if scores is None:
            return jsonify(code=404, message="Dietary Scores not found"), 404

        return jsonify({"scoresType": score_type, "code": score_code,
                        "scores": scores})


def get_vioscreen_dietary_scores_descriptions(token_info):
    _validate_has_account(token_info)

    with Transaction() as t:
        vio_diet = VioscreenDietaryScoreRepo(t)
        descriptions = vio_diet.get_dietary_scores_descriptions()

        if descriptions is None:
            return jsonify(code=404, message="Dietary Scores not found"), 404

        return jsonify(descriptions)


def get_vioscreen_food_components_by_code(fc_code, token_info):
    _validate_has_account(token_info)

    with Transaction() as t:
        vio_food = VioscreenFoodComponentsRepo(t)
        amounts = vio_food.get_food_components_by_code(fc_code)

        if amounts is None:
            return jsonify(code=404, message="Food Components not found"), 404

        return jsonify({"code": fc_code, "amounts": amounts})


def get_vioscreen_food_components_descriptions(token_info):
    _validate_has_account(token_info)

    with Transaction() as t:
        vio_food = VioscreenFoodComponentsRepo(t)
        descriptions = vio_food.get_food_components_descriptions()

        if descriptions is None:
            return jsonify(code=404, message="Food Components not found"), 404

        return jsonify(descriptions)
