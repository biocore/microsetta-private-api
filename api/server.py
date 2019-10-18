#!/usr/bin/env python3

"""
Basic flask/connexion-based web application

Modified from https://github.com/zalando/connexion/blob/master/examples/swagger2/oauth2/app.py

"""

import connexion


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    # Create the application instance
    app = connexion.FlaskApp(__name__)

    # Read the microsetta api spec file to configure the endpoints
    app.add_api('microsetta_private_api.yaml')
    app.run(port=8082, debug=True)
