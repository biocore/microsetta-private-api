#!/usr/bin/env python3

"""
Basic flask/connexion-based web application

Modified from https://github.com/zalando/connexion/blob/master/examples/swagger2/oauth2/app.py  # noqa: E501

"""

import connexion
from microsetta_private_api.util.util import JsonifyDefaultEncoder


def build_app():
    # Create the application instance
    app = connexion.FlaskApp(__name__)

    # Read the microsetta api spec file to configure the endpoints
    app.add_api('api/microsetta_private_api.yaml')

    # Set default json encoder
    # Note: app.app is the actual Flask application instance, so any Flask
    # settings have to be set there.
    app.app.json_encoder = JsonifyDefaultEncoder
    return app


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app = build_app()
    app.run(port=8082, debug=True)
