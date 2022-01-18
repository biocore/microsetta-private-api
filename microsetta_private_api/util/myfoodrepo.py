from microsetta_private_api.config_manager import SERVER_CONFIG


def gen_survey_url(mfr_id):
    # TODO: get specific URL
    endpoint = SERVER_CONFIG['myfoodrepo_user_url']
    return endpoint + f'/subject/{mfr_id}'


def create_subj():
    # deal with the cohort, create a subject etc
    raise ValueError()
