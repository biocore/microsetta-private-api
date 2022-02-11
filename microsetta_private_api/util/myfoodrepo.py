from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.client.myfoodrepo import MFRClient


def gen_survey_url(mfr_id):
    # TODO: get specific URL and structure from the myfoodrepo team,
    # this is not known as of this comment
    endpoint = SERVER_CONFIG['myfoodrepo_user_url']
    return endpoint + f'/subject/{mfr_id}'


def create_subj():
    client = MFRClient(SERVER_CONFIG["myfoodrepo_study"])
    cohort = client.default_cohort

    # should we set the subject to expire after a given time period?
    subj = client.create_subj(cohort)

    return subj.data.subject.key
