import json
from unittest import TestCase

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

    def test_cant_do_anything(self):
        # Fails without headers
        resp = self.client.get('/api/accounts/%s/sources?language_tag=en-US' %
                               ACCT_ID)
        check_response(resp, 401)
        self.assertEqual(
            json.loads(resp.data)['detail'],
            "No authorization token provided"
        )

        # Fails with invalid token - can't parse the jwt
        resp = self.client.get('/api/accounts/%s/sources?language_tag=en-US' %
                               ACCT_ID, headers={
                                   "Authorization": "Bearer boogaboogaboo"
                               })
        check_response(resp, 401)
        self.assertEqual(
            json.loads(resp.data)['detail'],
            "Invalid Token"
        )

        # Fails with expired token
        resp = self.client.get('/api/accounts/%s/sources?language_tag=en-US' %
                               ACCT_ID, headers={
                                   "Authorization": REPLAY_TOKEN
                               })
        check_response(resp, 401)
        # TODO: Can replace with Invalid Token after 6 hours when token expires
        self.assertIn(json.loads(resp.data)['detail'], [
                # If the token has expired
                "Invalid Token",
                # Or if the token has not expired, but since it doesn't match
                # any account:
                "The server could not verify that you are authorized to access"
                " the URL requested. You either supplied the wrong credentials"
                " (e.g. a bad password), or your browser doesn't understand "
                "how to supply the credentials required."
            ]
        )

        # Fails with invalid token - doesn't pass jwt signature check
        resp = self.client.get('/api/accounts/%s/sources?language_tag=en-US' %
                               ACCT_ID, headers={
                                   "Authorization": MODIFIED_TOKEN
                               })
        check_response(resp, 401)
        self.assertEqual(json.loads(resp.data)['detail'], "Invalid Token")
