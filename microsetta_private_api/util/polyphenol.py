import uuid

from microsetta_private_api.config_manager import SERVER_CONFIG


class MissingLangTagError(Exception):
    def __init__(self, errstr):
        self.error_string = errstr

    def __repr__(self,):
        return r'%s' % self.error_string


def gen_pffq_id():
    # generate the pffq id locally and return it as a string
    return str(uuid.uuid4())


# RULE IS: transaction DB is done
def gen_survey_url(pffq_id, language_tag=None):
    ''' generate the pffq survey endpoint . The "handoff url arguments"
    for Danon composes: unique identifier,  country(lang) and study (THDMI)
    '''

    if language_tag is None:
        raise MissingLangTagError('There is no language tag set')
    else:
        country = language_tag.lower()
    study = SERVER_CONFIG['pffq_study']
    endpoint = SERVER_CONFIG['pffqsurvey_url']
    return endpoint + f'?yid={pffq_id}&country={country}&study={study}'
