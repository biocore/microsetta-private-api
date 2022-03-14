import datetime
import pytz

from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.client.myfoodrepo import MFRClient


def gen_survey_url(mfr_id):
    endpoint = SERVER_CONFIG['myfoodrepo_user_url']
    return endpoint + f'?key={mfr_id}'


def create_subj():
    # WARNING
    # This creates a subject *remotely* but does not associate the
    # ID with a source

    client = MFRClient(SERVER_CONFIG["myfoodrepo_study"])
    participation_length = SERVER_CONFIG["myfoodrepo_participation_days"]
    cohort = SERVER_CONFIG['myfoodrepo_cohort']

    subj = client.create_subj(cohort)
    subj_id = subj.data.subject.key

    now = datetime.datetime.now(pytz.utc)
    expire_at = now + datetime.timedelta(days=participation_length)
    client.update_subj(cohort, subj_id, expire_at)

    return subj_id
