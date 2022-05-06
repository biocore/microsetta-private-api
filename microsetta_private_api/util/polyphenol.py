import datetime
import pytz
import uuid

from microsetta_private_api.config_manager import SERVER_CONFIG


# TODO DOJO learn how to use LANGUAGE_SUPPORT for localization and language

def gen_pffq_id():
    # generate the pffq id locally and return it as a string
    return str(uuid.uuid4())

# Should the language_tag set it's default to en_us ?
def gen_survey_url(pffq_id, language_tag=None):
    ''' generate the pffq survey endpoint . The "handoff url arguments" for Danon composes: 
    unique identifier,  country(lang) and study (THDMI)
    '''

    if language_tag is None:
        print(f'Error: there is no language tag set')
        # TODO raise language_tag error 
    else:
        country = language_tag.lower()
    study = SERVER_CONFIG['pffq_study']
    endpoint = SERVER_CONFIG['pffqsurvey_url']
    return endpoint + f'?yid={pffq_id}&country={country}&study={study}'

 
