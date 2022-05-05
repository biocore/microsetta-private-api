import datetime
import pytz
import uuid

from microsetta_private_api.config_manager import SERVER_CONFIG


# TODO DOJO learn how to use LANGUAGE_SUPPORT for localization and language

def gen_pffq_id():
    # generate the pffq id locally and return it as a string
    return str(uuid.uuid4())


def gen_survey_url(pffq_id, country=None, study=None):
    # the "handoff url" for Danon composes: 
    # unique identifier, language and country
    if country is None:
        country = "en_us"
    if study is None:
        study = SERVER_CONFIG['pffq_study']
    endpoint = SERVER_CONFIG['pffqsurvey_url']
    return endpoint + f'?yid={pffq_id}&country={country}&study={study}'

 
