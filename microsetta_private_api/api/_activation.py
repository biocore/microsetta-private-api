from flask import jsonify

from microsetta_private_api.repo.activation_repo import ActivationRepo
from microsetta_private_api.repo.transaction import Transaction


def check_activation(email, code):
    with Transaction() as t:
        activation = ActivationRepo(t)
        can, cause = activation.can_activate_with_cause(email, code)
    return jsonify({
        "can_activate": can,
        "error": cause
    }), 200
