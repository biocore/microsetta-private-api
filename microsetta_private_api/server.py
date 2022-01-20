#!/usr/bin/env python3
import secrets
import logging

from microsetta_private_api.config_manager import SERVER_CONFIG
import flask
from flask import jsonify, request
from flask_babel import Babel

from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.celery_utils import celery, init_celery
from microsetta_private_api.localization import EN_US, ES_MX


"""
Basic flask/connexion-based web application

Modified from https://github.com/zalando/connexion/blob/master/examples/swagger2/oauth2/app.py  # noqa: E501

"""

import connexion
from microsetta_private_api.util.util import JsonifyDefaultEncoder


# https://stackoverflow.com/a/37842465
# allow for rewriting the scheme in a reverse proxy production
# environment. this is what allows url_for and redirect calls
# to use https
class ReverseProxied(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        scheme = SERVER_CONFIG.get('url_scheme')
        if scheme is not None:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)


def handle_422(repo_exc):
    return jsonify(code=422, message=str(repo_exc)), 422


def build_app():
    # Create the application instance
    app = connexion.FlaskApp(__name__)

    # Read the microsetta api spec file to configure the endpoints
    app.add_api('api/microsetta_private_api.yaml', validate_responses=True)

    flask_secret = SERVER_CONFIG["FLASK_SECRET_KEY"]
    if flask_secret is None:
        print("WARNING: FLASK_SECRET_KEY must be set to run with gUnicorn")
        flask_secret = secrets.token_urlsafe(16)
    app.app.secret_key = flask_secret
    app.app.config['SESSION_TYPE'] = 'memcached'
    app.app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
    app.app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

    # ---

    # Set default json encoder
    # Note: app.app is the actual Flask application instance, so any Flask
    # settings have to be set there.
    app.app.json_encoder = JsonifyDefaultEncoder

    # Set mapping from exception type to response code
    app.app.register_error_handler(RepoException, handle_422)

    # attach the reverse proxy mechanism
    app.app.wsgi_app = ReverseProxied(app.app.wsgi_app)

    if not SERVER_CONFIG['debug']:
        gunicorn_logger = logging.getLogger('gunicorn.error')
        app.app.logger.handlers = gunicorn_logger.handlers
        app.app.logger.setLevel(gunicorn_logger.level)

    global babel
    babel = Babel(app.app)

    @babel.localeselector
    def get_locale():
        # for unit test support
        if not flask.has_request_context():
            return EN_US

        return request.accept_languages.best_match([EN_US, ES_MX],
                                                   default=EN_US)

    init_celery(celery, app.app)

    return app


def run(app):
    if SERVER_CONFIG["ssl_cert_path"] and SERVER_CONFIG["ssl_key_path"]:
        ssl_context = (
            SERVER_CONFIG["ssl_cert_path"], SERVER_CONFIG["ssl_key_path"]
        )
    else:
        ssl_context = None

    app.run(
        port=SERVER_CONFIG['port'],
        debug=SERVER_CONFIG['debug'],
        ssl_context=ssl_context
    )


babel = None
app = build_app()

# This hooks up app.app.logger to the gunicorn file, allowing us to write
# to that file with app.app.logger.debug/info/warning/error/critical()
# See https://trstringer.com/logging-flask-gunicorn-the-manageable-way/
gunicorn_logger = logging.getLogger('gunicorn.error')
app.app.logger.handlers = gunicorn_logger.handlers
app.app.logger.setLevel(gunicorn_logger.level)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    run(app)
