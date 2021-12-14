import json
import requests
from urllib.parse import urljoin
from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.model.campaign import (FundRazrPayment,
                                                   FundRazrCampaign)


class FundrazrException(Exception):
    pass


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
                                    f'{r.content}')

        try:
            return r.json()
        except json.decoder.JSONDecodeError:
            # in testing, the staging API will return an empty string
            return {}

    def campaigns(self):
        """GET /campaigns?organization={id}

        Obtain general campaign detail
        """
        data = self._req('GET',
                         f'/campaigns?organization={self.ORGANIZATION_ID}')
        return [FundRazrCampaign.from_api(**e) for e in data['entries']]

    def campaign(self, campaign_id):
        """GET /campaigns/{campaign_id}

        Obtain general campaign detail
        """
        data = self._req('GET',
                         f'/campaigns/{campaign_id}')
        return FundRazrCampaign.from_api(**data)

    def payments(self, since=None):
        """GET /payments?organization={orgid}&since={unixtimestamp}&limit=50

        Obtain payments across all campaigns since the last ID

        Response will be paginated so may need to issue multiple queries

        N.B. since on fundrazr API is *inclusive*
        """
        if since is not None:
            # ensure we aren't getting the current transaction if using most
            # recent
            since += 1

        def url_maker(since, id_):
            url = f'/payments?organization={self.ORGANIZATION_ID}'
            if since is not None:
                url += f'&since={since}'
            if id_ is not None:
                url += f'&after={id_}'
            if since is None and id_ is None:
                url += '&since=1293868800'  # before the project started
            url += '&limit=50'
            return url

        current = self._req('GET', url_maker(since, None))

        while current:
            for obj in current['entries']:
                yield FundRazrPayment.from_api(**obj)
            last_id = current.get('after_cursor')

            if last_id is None:
                # nothing more to get
                current = []
            else:
                current = self._req('GET', url_maker(since, last_id))
