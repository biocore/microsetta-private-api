import json
import requests
from urllib.parse import urljoin
from types import SimpleNamespace
from microsetta_private_api.config_manager import SERVER_CONFIG


class MFRException(Exception):
    pass


# implement
# https://myfoodrepo.org/api_doc/v1/studies_and_cohorts
class MFRClient:
    HEADERS = {
        'Accept-Language': 'en',
        "Authorization": f"Token token={SERVER_CONFIG['myfoodrepo_key']}"
    }
    BASEURL = SERVER_CONFIG['myfoodrepo_url']

    def __init__(self, study):
        self.study_codename = study
        self.s = requests.Session()
        self._actions = {'GET': self.s.get,
                         'POST': self.s.post,
                         'PUT': self.s.put,
                         'DELETE': self.s.delete}
        self._default_cohort = None

    @property
    def default_cohort(self):
        if self._default_cohort is None:
            data = self.cohorts()
            self._default_cohort = data.data.cohorts[0].codename
        return self._default_cohort

    def __del__(self):
        self.s.close()

    def _json_to_model(self, data):
        """Naively map the JSON to an attributed Python object

        A SimpleNamespace translation is performed. As an example, the
        following structure:

        {
          "foo": "bar",
          "baz": {"key1": "value1"},
          "items": [
            "item1",
            {"key2": "value2"}
          ]
        }

        Is mapped into an object which contains the following attributes:

        .foo -> "bar"
        .baz -> obj
        .baz.key1 -> "value1"
        .items -> list
        .items[0] -> "item1"
        .items[1] -> obj
        .items[1].key2 -> "value2"

        Returns
        -------
        object
            A SimpleNamespace translation of the JSON is returned
        """
        # https://stackoverflow.com/a/15882054
        def hook(d):
            return SimpleNamespace(**d)
        return json.loads(data, object_hook=hook)

    def _req(self, action, url, data=None, **kwargs):
        """Make a request and return a structured model"""
        method = self._actions[action]

        # we do not want the root...
        if url.startswith('/'):
            url = url[1:]

        formed = urljoin(self.BASEURL, url)
        r = method(formed, headers=self.HEADERS, data=data, **kwargs)

        if r.status_code != 200:
            raise MFRException(f'Failure, ({r.status_code})\n'
                               f'{json.dumps(r.json(), indent=2)}')

        return self._json_to_model(r.content)

    def cohorts(self):
        """Obtain cohorts associated with the study

        Returns
        -------
        object
            SimpleNamespace translation of

            {
              "data": {
                "study": { "codename": "healthy_humans" },
                "cohorts": [
                  { "codename": "programmers" },
                  { "codename": "doctors" },
                  { "codename": "pilots" }
                ]
              }
            }

        Notes
        -----
        Return body from: https://myfoodrepo.org/api_doc/v1/studies_and_cohorts
        """
        return self._req('GET', f'/studies/{self.study_codename}/cohorts')

    def create_subj(self, cohort):
        """Create a new subject within a cohort

        Returns
        -------
        object
            SimpleNamespace translation of

            {
              "data": {
                "subject": {
                  "key": "abcdef",
                  "created_at": "2021-03-01T14:30:00.123456Z",
                  "first_attached_at": null,
                  "expired_at": null
                }
              }
            }

        Notes
        -----
        Return body from: https://myfoodrepo.org/api_doc/v1/studies_and_cohorts
        """
        return self._req('POST', f'/studies/{self.study_codename}'
                                 f'/cohorts/{cohort}/subjects')

    def read_subj(self, cohort, subj):
        """Reads details about a subject

        Returns
        -------
        object
            SimpleNamespace translation of

            {
              "data": {
                "subject": {
                  "key": "abcdef",
                  "created_at": "2021-03-01T14:30:00.123456Z",
                  "first_attached_at": null,
                  "expired_at": null
                }
              }
            }

        Notes
        -----
        Return body from: https://myfoodrepo.org/api_doc/v1/studies_and_cohorts
        """
        return self._req('GET', f'/studies/{self.study_codename}'
                                f'/cohorts/{cohort}'
                                f'/subjects/{subj}')

    def update_subj(self, cohort, subj, expired_at):
        """Update the expired_at attribute of a subject

        Returns
        -------
        object
            SimpleNamespace translation of


        Notes
        -----
        Return body from: https://myfoodrepo.org/api_doc/v1/studies_and_cohorts
        """
        return self._req('PUT', f'/studies/{self.study_codename}'
                                f'/cohorts/{cohort}'
                                f'/subjects/{subj}',
                         json={'subject': {'expired_at': str(expired_at)}})

    def delete_subj(self, cohort, subj):
        """Remove a subject being tracked

        Returns
        -------
        object
            SimpleNamespace translation of


        Notes
        -----
        Return body from: https://myfoodrepo.org/api_doc/v1/studies_and_cohorts
        """
        return self._req('DELETE', f'/studies/{self.study_codename}'
                                   f'/cohorts/{cohort}'
                                   f'/subjects/{subj}')
