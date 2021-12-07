import os
from json import loads, dumps

print("in set gh secrets")
# test if one of our secrets exists
if os.environ.get('MFR_URL') is not None:
    print("actually setting gh secrets")
    config = loads(open('microsetta_private_api/server_config.json').read())

    config['myfoodrepo_url'] = os.environ['MFR_URL']
    config['myfoodrepo_key'] = os.environ['MFR_TEST_APIKEY']
    config['fundrazr_key'] = os.environ['FUNDRAZR_TEST_APIKEY']
    config['fundrazr_url'] = os.environ['FUNDRAZR_TEST_URL']
    config['fundrazr_organization'] = os.environ['FUNDRAZR_TEST_ORG']

    with open('microsetta_private_api/server_config.json', 'w') as fp:
        fp.write(dumps(config))
