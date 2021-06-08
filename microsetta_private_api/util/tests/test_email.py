import unittest
import json
import smtplib
from microsetta_private_api.util.email import SendEmail


class MockConnection:
    def __init__(self, noop=250):
        self._noop = (noop, 'something')
        self.observed = None

    def send_message(self, message):
        self.observed = message

    def noop(self):
        return self._noop


class MockConnect:
    def __init__(self, timeout):
        self.call_count = 0
        if timeout:
            self.status = 421
        else:
            self.status = 250

    def __call__(self):
        self.call_count += 1
        return MockConnection(self.status)


class MockTemplate:
    def __init__(self, content):
        self.content = content

    def render(self, template_args):
        return self.content + "|" + json.dumps(sorted(template_args.items()))


class MockMessage:
    def __init__(self, html):
        self.html = html
        self.subject = 'test_subject'


class EmailTests(unittest.TestCase):
    def setUp(self):
        self.message = MockMessage(MockTemplate("<html>a html message</html>"))

    def tearDown(self):
        SendEmail.connection = None

    def test_send_valid_message(self):
        SendEmail._connect = MockConnect(False)

        SendEmail.send("foo", self.message)
        obs = SendEmail.connection.observed.as_string()
        self.assertRegex(obs, 'Content-Type: text/html')
        self.assertRegex(obs, 'Content-Type: text/plain')
        self.assertRegex(obs, 'a html message|')
        self.assertRegex(obs, "<html>a html message</html>")

    def test_send_valid_message_args(self):
        SendEmail._connect = MockConnect(False)

        SendEmail.send("foo", self.message, {'foo': 'bar', 'baz': 'biz'})
        obs = SendEmail.connection.observed.as_string()
        self.assertRegex(obs, 'Content-Type: text/html')
        self.assertRegex(obs, 'Content-Type: text/plain')
        self.assertRegex(obs, 'a html message'
                         '|[["baz", "biz"], ["foo", "bar"]]')
        self.assertRegex(obs, '<html>a html message</html>'
                         '|[["baz", "biz"], ["foo", "bar"]]')

    def test_send_valid_prior_connection(self):
        SendEmail.connection = MockConnection(250)
        SendEmail.send("foo", self.message)

    def test_failure_on_retry(self):
        SendEmail._connect = MockConnect(True)
        with self.assertRaisesRegex(smtplib.SMTPException, "Unable"):
            SendEmail.send("foo", self.message)
        self.assertEqual(SendEmail._connect.call_count, 4)


if __name__ == '__main__':
    unittest.main()
