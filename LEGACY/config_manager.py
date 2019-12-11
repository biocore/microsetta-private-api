# -----------------------------------------------------------------------------
# Copyright (c) 2014--, The American Gut Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------


class DBConfig(object):
    def __init__(self):
        self.user = 'postgres'
        self.password = ''
        self.database = 'ag_test'
        self.host = 'localhost'
        self.port = 5432

AMGUT_CONFIG = DBConfig()
