# -----------------------------------------------------------------------------
# Copyright (c) 2014--, The American Gut Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

import json
import os


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
with open(os.path.join(os.path.dirname(__file__), "server_config.json")) as fp:
    SERVER_CONFIG = json.load(fp)
