#!/usr/bin/env python3
import secrets

from flask import jsonify
from werkzeug.utils import redirect

from microsetta_private_api.exceptions import RepoException

"""
Basic flask/connexion-based web application

Modified from https://github.com/zalando/connexion/blob/master/examples/swagger2/oauth2/app.py  # noqa: E501

"""

import connexion
from microsetta_private_api.util.util import JsonifyDefaultEncoder


def handle_422(repo_exc):
    return jsonify(code=422, message=str(repo_exc)), 422


def build_app():
    # Create the application instance
    app = connexion.FlaskApp(__name__)

    # Read the microsetta api spec file to configure the endpoints
    app.add_api('api/microsetta_private_api.yaml', validate_responses=True)

    # ---
    # Example Client Settings
    app.add_api('example/client.yaml', validate_responses=True)
    app.app.secret_key = secrets.token_urlsafe(16)
    app.app.config['SESSION_TYPE'] = 'memcached'
    # ---

    # Set default json encoder
    # Note: app.app is the actual Flask application instance, so any Flask
    # settings have to be set there.
    app.app.json_encoder = JsonifyDefaultEncoder

    # Set mapping from exception type to response code
    app.app.register_error_handler(RepoException, handle_422)

    @app.route('/americangut/static/<path:filename>')
    def reroute_americangut(filename):
        # This is dumb as rocks, but it fixes static images referenced in
        # surveys without a schema change.
        return redirect('/static/' + filename)
    return app


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app = build_app()
    app.run(port=8082, debug=True)
