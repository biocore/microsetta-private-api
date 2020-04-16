from flask import jsonify

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


def validate_admin_access(token_info):
    with Transaction() as t:
        account_repo = AccountRepo(t)
        account = account_repo.find_linked_account(token_info['iss'],
                                                   token_info['sub'])
        if account is None or account.account_type != 'admin':
            raise Unauthorized()


def create_kits(body, token_info):
    validate_admin_access(token_info)

    number_of_kits = body['number_of_kits']
    number_of_samples = body['number_of_samples']
    kit_prefix = body.get('kit_prefix', None)
    projects = body['projects']

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        kits = admin_repo.create_kits(number_of_kits, number_of_samples,
                                      kit_prefix, projects)

        if kits:
            t.commit()

    return jsonify(kits), 201
