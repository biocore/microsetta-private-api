# ----------------------------------------------------------------------------
# Copyright (c) 2019-, The Microsetta Initiative development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

import versioneer

setup(
    name="microsetta-private-api",
    author="Daniel McDonald",
    author_email="danielmcdonald@ucsd.edu",
    packages=find_packages(),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    py_modules=['mpa-cli'],
    url="https://github.com/biocore/microsetta-private-api",
    description="A RESTful API to support The Microsetta Initiative",
    license='BSD-3-Clause',
    package_data={'microsetta_private_api':
                  [
                     'db/*.*',
                     'db/patches/*.sql',
                     'api/microsetta_private_api.yaml',
                     'example/client.yaml',
                     'server_config.json',
                     'templates/*.*',
                     'static/*',
                     'static/css/*',
                     'static/img/*',
                     'static/vendor/js/*',
                     'static/vendor/bootstrap-4.4.1-dist/js/*',
                     'static/vendor/bootstrap-4.4.1-dist/css/*',
                     'static/vendor/bootstrap-datetimepicker-4.14.30/*',
                     'static/vendor/vue-form-generator-2.3.4/*',
                     'static/vendor/bootstrap-3.3.7-dist/js/*',
                     'static/vendor/bootstrap-3.3.7-dist/css/*',
                     'static/vendor/bootstrap-3.3.7-dist/fonts/*',
                     'authrocket.pubkey'
                  ]},
    entry_points='''
        [console_scripts]
        mpa-cli=mpa_cli:cli
    '''
)
