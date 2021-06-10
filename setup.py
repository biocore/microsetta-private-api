# ----------------------------------------------------------------------------
# Copyright (c) 2019-, The Microsetta Initiative development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages
from babel.messages import frontend as babel

import versioneer


command_classes = versioneer.get_cmdclass()
command_classes['compile_catalog'] = babel.compile_catalog


setup(
    name="microsetta-private-api",
    author="Daniel McDonald",
    author_email="danielmcdonald@ucsd.edu",
    packages=find_packages(),
    version=versioneer.get_version(),
    cmdclass=command_classes,
    py_modules=['mpa-cli'],
    url="https://github.com/biocore/microsetta-private-api",
    description="A RESTful API to support The Microsetta Initiative",
    license='BSD-3-Clause',
    package_data={
        '': ['translations/*/*/*.mo',
             'translations/*/*/*.po'],
        'microsetta_private_api': [
                 'babel.cfg',
                 'db/*.*',
                 'db/patches/*.sql',
                 'templates/*',
                 'templates/email/*',
                 'api/microsetta_private_api.yaml',
                 'authrocket.pubkey',
                 'cronjob.pubkey',
                 'server_config.json'
              ]},
    entry_points='''
        [console_scripts]
        mpa-cli=mpa_cli:cli
    '''
)
