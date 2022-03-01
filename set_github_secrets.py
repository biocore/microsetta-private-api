import os
from json import loads, dumps

# test if one of our secrets exists
if os.environ.get('MFR_URL', '') != '':
    config = loads(open('microsetta_private_api/server_config.json').read())

    config['myfoodrepo_url'] = os.environ['MFR_URL']
    config['myfoodrepo_key'] = os.environ['MFR_TEST_APIKEY']
    config['myfoodrepo_study'] = os.environ['MFR_STUDY']
    config['fundrazr_key'] = os.environ['FUNDRAZR_TEST_APIKEY']
    config['fundrazr_url'] = os.environ['FUNDRAZR_TEST_URL']
    config['fundrazr_organization'] = os.environ['FUNDRAZR_TEST_ORG']
    config["vioscreen_endpoint"] = os.environ['VS_ENDPOINT']
    config["vioscreen_regcode"] = os.environ['VS_REGCODE']
    config["vioscreen_cryptokey"] = os.environ['VS_CRYPTOKEY']
    config["vioscreen_admin_username"] = os.environ['VS_USER']
    config["vioscreen_admin_password"] = os.environ['VS_PASSWORD']

    # a nonsecret to help examine the logs
    # we're munging to circumvent githubs log filtering
    print(' '.join(config['fundrazr_url'].upper()))

    with open('microsetta_private_api/server_config.json', 'w') as fp:
        fp.write(dumps(config))
