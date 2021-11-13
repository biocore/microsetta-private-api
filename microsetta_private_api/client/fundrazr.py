import json
import requests
from urllib.parse import urljoin
from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.model.campaign import FundRazrPayment


class FundrazrException(Exception):
    pass


CAMPAIGN_TITLE = 'title'
CAMPAIGN_ITEMS = 'items'
CAMPAIGN_CREATED = 'created'
CAMPAIGN_ID = 'id'

Campaign = None  # placeholder pending upstream PR


def _fundrazr_campaign_to_campaign_model(fr_data):
    projects = SERVER_CONFIG['fundrazr_campaign_to_project']

    # default to The Microsetta Initiative
    projects = projects.get(fr_data[CAMPAIGN_ID], [118, ])
    return Campaign(fr_data[CAMPAIGN_ID],
                    fr_data[CAMPAIGN_TITLE],
                    None,  # instructions
                    None,  # header_image
                    None,  # permitted_countries
                    None,  # language_key
                    True,  # accepting_participants
                    projects,
                    None,  # language_key_alt
                    None,  # title_key_alt
                    None)  # instructions_alt


class FundrazrClient:
    HEADERS = {
        "Authorization": f"Bearer {SERVER_CONFIG['fundrazr_key']}"
    }
    BASEURL = SERVER_CONFIG['fundrazr_url']
    ORGANIZATION_ID = SERVER_CONFIG['fundrazr_organization']

    def __init__(self):
        self.s = requests.Session()
        self._actions = {'GET': self.s.get,
                         'POST': self.s.post,
                         'PUT': self.s.put,
                         'DELETE': self.s.delete}

    def __del__(self):
        self.s.close()

    def _req(self, action, url, data=None, **kwargs):
        """Make a request and return a structured model"""
        method = self._actions[action]

        # we do not want the root...
        if url.startswith('/'):
            url = url[1:]

        formed = urljoin(self.BASEURL, url)
        r = method(formed, headers=self.HEADERS, data=data, **kwargs)
        if r.status_code != 200:
            raise FundrazrException(f'Failure, ({r.status_code})\n'
                                    f'{json.dumps(r.json(), indent=2)}')

        try:
            return r.json()
        except json.decoder.JSONDecodeError:
            # in testing, the staging API will return an empty string
            return {}

    def campaigns(self):
        """GET /campaigns?organization={id}

        Obtain general campaign detail
        """
        raise NotImplementedError("Add if needed in the future")

    def payments(self, since=None):
        """GET /payments?organization={orgid}&since={unixtimestamp}&limit=50

        Obtain payments across all campaigns since the last ID

        Response will be paginated so may need to issue multiple queries
        """
        def url_maker(since, id_):
            url = f'/payments?organization={self.ORGANIZATION_ID}'
            if since is not None:
                url += f'&since={since}'
            if id_ is not None:
                url += f'&since_id={id_}'
            url += '&limit=50'
            return url

        current = self._req('GET', url_maker(since, None))

        while current:
            for obj in current['entries']:
                yield FundRazrPayment.from_api(**obj)
            last_id = current.get('after_id')

            if last_id is None:
                # nothing more to get
                current = []
            else:
                current = self._req('GET', url_maker(None, last_id))
