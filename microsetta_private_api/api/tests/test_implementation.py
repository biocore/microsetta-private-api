import pytest
from unittest import TestCase
import microsetta_private_api.server


@pytest.mark.usefixtures("client")
class IntegrationTests(TestCase):
    lang_query_dict = {
        "language_tag": "en_US"
    }

    def setUp(self):
        app = microsetta_private_api.server.build_app()
        self.client = app.app.test_client()
        # This isn't perfect, due to possibility of exceptions being thrown
        # is there some better pattern I can use to split up what should be
        # a 'with' call?
        self.client.__enter__()

    def tearDown(self):
        # This isn't perfect, due to possibility of exceptions being thrown
        # is there some better pattern I can use to split up what should be
        # a 'with' call?
        self.client.__exit__(None, None, None)
