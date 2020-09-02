import json
from unittest import TestCase
from unittest.mock import patch

import pytest

import microsetta_private_api.server

from microsetta_private_api.api.tests.utils import check_response

# This token was valid once, but now it's expired
REPLAY_TOKEN = "Bearer eyJraWQiOiJqa3lfMHZxMGF0RUNuSGp2YW"
"8wTnRCNHNuNiIsImFsZyI6IlJTMjU2In0.eyJleHA"
"iOjE1ODUxMzc5NTgsImlhdCI6MTU4NTExNjM1OCwi"
"aXNzIjoiaHR0cHM6Ly9hdXRocm9ja2V0LmNvbSIsI"
"nJpZCI6InJsXzB2cTBhdEVCV241R3cxeHhLVXZTYW"
"kiLCJzaWQiOiJrc3NfMHZxMmRFQ3QwcXd3TUVPQmJ"
"zdkhvVyIsInN1YiI6InVzcl8wdnEwbDd4MzBRYzVx"
"RU5Bb09wa0k0IiwibmFtZSI6ImZvb2JhckB0ZXN0L"
"mNvbSIsImVtYWlsIjoiZm9vYmFyQHRlc3QuY29tIi"
"wib3JncyI6W3sib2lkIjoib3JnXzB2cTBsN3gzQ0h"
"4UzVlZjZwWnZrR1ciLCJwZXJtIjpbImFyOm93bmVy"
"IiwiYXI6YWRtaW4iXSwibmFtZSI6ImZvb2JhckB0Z"
"XN0LmNvbSIsInNlbGVjdGVkIjp0cnVlLCJtaWQiOi"
"JtYl8wdnEwbDd4M0lRdGswbEJTNTZZU0xBIn1dfQ."
"m_4YS6bMH99KNHXrmQg_fH5w-XM3KD-2VOLSFob2l"
"ZQblGgF_CRd0uHv1t8M4k14nKNZ8wuQnxhKxIS7XU"
"gunif8pzQmai0o88NoYGGTUtduFRN-ruNhjyjmm4Q"
"2azL4EXF0xnFuFg3s76uUqGua-o5L3NNIEk3vTMBG"
"ke8MAIWkff_Oe3hbrSUpPUF5aPkBSqjrEV1qiXbER"
"mdV54-dnF73S6UWKZEAr_En4j4SWiXtbGFfhAyf6x"
"CiPnzkeRzBzdovlZWh_t6hPPJwIWrrWWsOafomIMG"
"igEcJXwA0XrtANYJh4WgoYUY0L9_y2SBsnA-nsjxU"
"0_Avk5Z2RYsu-g"

# A single bit was modified to shift the expiration years into the future
# but this token should still fail because the signature won't match
MODIFIED_TOKEN = "Bearer eyJraWQiOiJqa3lfMHZxMGF0RUNuSGp2YW"
"8wTnRCNHNuNiIsImFsZyI6IlJTMjU2In0.eyJleHA"
"iOjE1ODYxMzc5NTgsImlhdCI6MTU4NTExNjM1OCwi"
"aXNzIjoiaHR0cHM6Ly9hdXRocm9ja2V0LmNvbSIsI"
"nJpZCI6InJsXzB2cTBhdEVCV241R3cxeHhLVXZTYW"
"kiLCJzaWQiOiJrc3NfMHZxMmRFQ3QwcXd3TUVPQmJ"
"zdkhvVyIsInN1YiI6InVzcl8wdnEwbDd4MzBRYzVx"
"RU5Bb09wa0k0IiwibmFtZSI6ImZvb2JhckB0ZXN0L"
"mNvbSIsImVtYWlsIjoiZm9vYmFyQHRlc3QuY29tIi"
"wib3JncyI6W3sib2lkIjoib3JnXzB2cTBsN3gzQ0h"
"4UzVlZjZwWnZrR1ciLCJwZXJtIjpbImFyOm93bmVy"
"IiwiYXI6YWRtaW4iXSwibmFtZSI6ImZvb2JhckB0Z"
"XN0LmNvbSIsInNlbGVjdGVkIjp0cnVlLCJtaWQiOi"
"JtYl8wdnEwbDd4M0lRdGswbEJTNTZZU0xBIn1dfQ."
"m_4YS6bMH99KNHXrmQg_fH5w-XM3KD-2VOLSFob2l"
"ZQblGgF_CRd0uHv1t8M4k14nKNZ8wuQnxhKxIS7XU"
"gunif8pzQmai0o88NoYGGTUtduFRN-ruNhjyjmm4Q"
"2azL4EXF0xnFuFg3s76uUqGua-o5L3NNIEk3vTMBG"
"ke8MAIWkff_Oe3hbrSUpPUF5aPkBSqjrEV1qiXbER"
"mdV54-dnF73S6UWKZEAr_En4j4SWiXtbGFfhAyf6x"
"CiPnzkeRzBzdovlZWh_t6hPPJwIWrrWWsOafomIMG"
"igEcJXwA0XrtANYJh4WgoYUY0L9_y2SBsnA-nsjxU"
"0_Avk5Z2RYsu-g"

FAKE_TOKEN_NO_ISS = "noiss"
FAKE_TOKEN_NO_SUB = "nosub"
FAKE_TOKEN_NO_EMAIL = "noemail"
FAKE_TOKEN_NO_EMAIL_VERIFY = "noemailver"


def decode_fake_token(fake_token, key, algorithms, verify, issuer):
    result = {
        'email': 'a@test.com',
        'email_verified': True,
        'iss': 'anissuer',
        'sub': 'asub'
    }
    if fake_token == FAKE_TOKEN_NO_ISS:
        result.pop('iss')
    elif fake_token == FAKE_TOKEN_NO_SUB:
        result.pop('sub')
    elif fake_token == FAKE_TOKEN_NO_EMAIL:
        result.pop('email')
    elif fake_token == FAKE_TOKEN_NO_EMAIL_VERIFY:
        result.pop('email_verified')
    else:
        raise ValueError("Unrecognized fake token")

    return result


# This leaves authentication enabled, which will make everything we do fail :D
@pytest.fixture(scope="class")
def client(request):
    app = microsetta_private_api.server.build_app()
    app.app.testing = True
    with app.app.test_client() as client:
        request.cls.client = client
        yield client


ACCT_ID = "aaaaaaaa-bbbb-cccc-dddd-eeeeffffffff"


@pytest.mark.usefixtures("client")
class AuthTests(TestCase):

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

    def test_fail_401_no_headers(self):
        # Return 401 if no headers provided
        resp = self.client.get('/api/accounts/%s/sources?language_tag=en-US' %
                               ACCT_ID)

        check_response(resp, 401)
        self.assertEqual(
            json.loads(resp.data)['detail'],
            "No authorization token provided"
        )

    def test_fail_401_unparseable_token(self):
        # Return 401 if can't parse the jwt
        resp = self.client.get('/api/accounts/%s/sources?language_tag=en-US' %
                               ACCT_ID, headers={
                                   "Authorization": "Bearer boogaboogaboo"
                               })

        check_response(resp, 401)
        self.assertEqual(
            json.loads(resp.data)['detail'],
            "Invalid token"
        )

    def test_fail_401_sig_check_failure(self):
        # Return 401 if doesn't pass jwt signature check
        resp = self.client.get('/api/accounts/%s/sources?language_tag=en-US' %
                               ACCT_ID, headers={
                                   "Authorization": MODIFIED_TOKEN
                               })
        check_response(resp, 401)
        self.assertEqual(json.loads(resp.data)['detail'], "Invalid token")

    def test_fail_401_expired_token(self):
        # Return 401 if expired token
        resp = self.client.get('/api/accounts/%s/sources?language_tag=en-US' %
                               ACCT_ID, headers={
                                   "Authorization": REPLAY_TOKEN
                               })

        check_response(resp, 401)
        # TODO: Can replace with Invalid token after 6 hours when token expires
        self.assertIn(json.loads(resp.data)['detail'], [
                # If the token has expired
                "Invalid token",
                # Or if the token has not expired, but since it doesn't match
                # any account:
                "The server could not verify that you are authorized to access"
                " the URL requested. You either supplied the wrong credentials"
                " (e.g. a bad password), or your browser doesn't understand "
                "how to supply the credentials required."
            ]
        )

    def _help_test_mock_decode_token(self, fake_token, expected_code,
                                     expected_error_detail):
        with patch("jwt.decode") as mock_d:
            mock_d.side_effect = decode_fake_token

            resp = self.client.get(
                '/api/accounts/%s/sources?language_tag=en-US' % ACCT_ID,
                headers={"Authorization": "Bearer %s" % fake_token})

            check_response(resp, expected_code)
            self.assertEqual(json.loads(resp.data)['detail'],
                             expected_error_detail)

    def test_fail_401_iss_not_in_token(self):
        self._help_test_mock_decode_token(FAKE_TOKEN_NO_ISS, 401,
                                          "Invalid token")

    def test_fail_401_sub_not_in_token(self):
        self._help_test_mock_decode_token(FAKE_TOKEN_NO_SUB, 401,
                                          "Invalid token")

    def test_fail_401_email_not_in_token(self):
        self._help_test_mock_decode_token(FAKE_TOKEN_NO_EMAIL, 401,
                                          "Invalid token")

    def test_fail_403_email_not_verified(self):
        self._help_test_mock_decode_token(FAKE_TOKEN_NO_EMAIL_VERIFY, 403,
                                          "Email is not verified")
