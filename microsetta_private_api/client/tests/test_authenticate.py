from unittest import TestCase
from unittest.mock import patch
from microsetta_private_api.client.authenticate import (
    authrocket, AuthenticationError, UserNotFound,
    UserPasswordInvalid
)


class FakeResponse:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content

    def json(self):
        return self.content


class AuthenticateTests(TestCase):
    def test_authentication_error(self):
        with patch('requests.post') as mock_d:
            mock_d.return_value = FakeResponse(403, None)

            with self.assertRaises(AuthenticationError):
                authrocket('foo', 'bar', 'baz', 'bing')

    def test_user_not_found_error(self):
        with patch('requests.post') as mock_d:
            mock_d.return_value = FakeResponse(404, None)

            with self.assertRaises(UserNotFound):
                authrocket('foo', 'bar', 'baz', 'bing')

    def test_user_password_invalid(self):
        with patch('requests.post') as mock_d:
            mock_d.return_value = FakeResponse(422, None)

            with self.assertRaises(UserPasswordInvalid):
                authrocket('foo', 'bar', 'baz', 'bing')

    def test_success(self):
        exp = {'Authorization': 'Bearer cool'}

        with patch('requests.post') as mock_d:
            mock_d.return_value = FakeResponse(201, {'token': 'cool'})
            obs = authrocket('foo', 'bar', 'baz', 'bing')

        self.assertEqual(obs, exp)
