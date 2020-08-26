from unittest.mock import patch
from unittest import TestCase
from microsetta_private_api.tasks import send_email


class CeleryTaskTests(TestCase):
    def test_send_email(self):
        with patch('microsetta_private_api.util.email.SendEmail.send'):
            obs = send_email('foobar', 'incorrect_sample_type', {})
            assert obs is None
