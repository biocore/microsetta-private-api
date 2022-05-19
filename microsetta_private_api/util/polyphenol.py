from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.repo.transaction import Transaction


class MissingLangTagError(Exception):
    def __init__(self, errstr):
        self.error_string = errstr

    def __repr__(self,):
        return r'%s' % self.error_string


def gen_survey_url(pffq_id, account_id, source_id, language_tag=None):
    ''' generate the pffq survey endpoint . The "handoff url arguments"
    for Danone composes: unique identifier,  country(lang) and study:
    (THDMI) or Microsetta
    '''
    study = 'Microsetta'  # default value Danone accepts if not THDMI
    # get the samples by source. If there are no samples, set as
    # default study: 'Microsetta'
    with Transaction() as t:
        sample_repo = SampleRepo(t)
        samples = sample_repo.get_samples_by_source(account_id,
                                                    source_id)
        if len(samples) > 0:
            for s in samples:
                if "THDMI" in s.sample_projects:
                    study = 'THDMI'
                elif "American Gut Project" in s.sample_projects:
                    print('got AGP project')  # TODO remove this line
                else:
                    print('leave study as default')
        else:
            pass  # leave as default study
    if language_tag is None:
        raise MissingLangTagError('There is no language tag set')
    else:
        country = language_tag.lower()

    endpoint = SERVER_CONFIG['pffqsurvey_url']
    return endpoint + f'?yid={pffq_id}&country={country}&study={study}'
