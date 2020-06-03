import flask
from flask import jsonify, render_template

from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.admin_repo import AdminRepo
from werkzeug.exceptions import Unauthorized


def search_barcode(token_info, sample_barcode):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        diag = admin_repo.retrieve_diagnostics_by_barcode(sample_barcode)
        if diag is None:
            return jsonify(code=404, message="Barcode not found"), 404
        return jsonify(diag), 200


def search_kit_id(token_info, kit_id):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        diag = admin_repo.retrieve_diagnostics_by_kit_id(kit_id)
        if diag is None:
            return jsonify(code=404, message="Kit ID not found"), 404
        return jsonify(diag), 200


def search_email(token_info, email):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        diag = admin_repo.retrieve_diagnostics_by_email(email)
        if diag is None:
            return jsonify(code=404, message="Email not found"), 404
        return jsonify(diag), 200


def scan_barcode(token_info, sample_barcode, body):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        admin_repo.scan_barcode(sample_barcode, body)
        t.commit()

    response = flask.Response()
    response.status_code = 201
    response.headers['Location'] = '/api/admin/search/samples/%s' % \
                                   sample_barcode
    return response


def sample_pulldown_single_survey(token_info,
                                  sample_barcode,
                                  survey_template_id):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        sample_pulldown = admin_repo.get_survey_metadata(
            sample_barcode,
            survey_template_id=survey_template_id)
    return jsonify(sample_pulldown), 200


def sample_pulldown_multiple_survey(token_info,
                                    sample_barcode):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        sample_pulldown = admin_repo.get_survey_metadata(sample_barcode)
    return jsonify(sample_pulldown), 200


def project_statistics_summary(token_info):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        summary = admin_repo.get_project_summary_statistics()
        return jsonify(summary), 200


def project_statistics_detailed(token_info, project_id):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        summary = admin_repo.get_project_detailed_statistics(project_id)
        return jsonify(summary), 200


def token_grants_admin_access(token_info):
    with Transaction() as t:
        account_repo = AccountRepo(t)
        account = account_repo.find_linked_account(token_info['iss'],
                                                   token_info['sub'])
        return account is not None and account.account_type == 'admin'


def validate_admin_access(token_info):
    if not token_grants_admin_access(token_info):
        raise Unauthorized()


def create_project(body, token_info):
    validate_admin_access(token_info)

    project_name = body['project_name']
    is_microsetta = body['is_microsetta']

    if len(project_name) == 0:
        return jsonify(code=400, message="No project name provided"), 400

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        admin_repo.create_project(project_name, is_microsetta)
        t.commit()

    return {}, 201


def create_kits(body, token_info):
    validate_admin_access(token_info)

    number_of_kits = body['number_of_kits']
    number_of_samples = body['number_of_samples']
    kit_prefix = body.get('kit_id_prefix', None)
    projects = body['projects']

    with Transaction() as t:
        admin_repo = AdminRepo(t)

        try:
            kits = admin_repo.create_kits(number_of_kits, number_of_samples,
                                          kit_prefix, projects)
        except KeyError:
            return jsonify(code=422, message="Unable to create kits"), 422
        else:
            t.commit()

    return jsonify(kits), 201
