# -----------------------------------------------------------------------------
# Copyright (c) 2014--, The American Gut Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

import json
import os
# NOTE: importlib replaces setuptools' pkg_resources as of Python 3.7
# See: https://stackoverflow.com/questions/6028000/how-to-read-a-static-file-from-inside-a-python-package # noqa
import importlib.resources as pkg_resources


class DBConfig(object):
    def __init__(self):
        self.user = 'postgres'
        self.password = ''
        self.database = 'ag_test'
        self.host = 'localhost'
        self.port = 5432

        self.project_name = "PROJECT_NAME"
        self.project_shorthand = "PROJECT_SHORTHAND"
        self.sitebase = "PROJECT_SITEBASE"
        self.locale = "american_gut"


AMGUT_CONFIG = DBConfig()
with pkg_resources.open_text('microsetta_private_api', "config_manager.py") \
        as just_testing:
    print("Can find config_manager.py!")

with pkg_resources.open_text('microsetta_private_api', "server_config.json") \
        as fp:
    SERVER_CONFIG = json.load(fp)
