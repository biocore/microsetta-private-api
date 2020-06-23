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
                     'authrocket.pubkey'
                  ]},
    entry_points='''
        [console_scripts]
        mpa-cli=mpa_cli:cli
    '''
)
