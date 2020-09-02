from unittest.mock import patch
from microsetta_private_api.tasks import send_email


def test_task_send_email():
    with patch('microsetta_private_api.util.email.SendEmail.send') as p:
        send_email.apply(args=['foo', 'incorrect_sample_type', 'baz'])
        assert p.called
