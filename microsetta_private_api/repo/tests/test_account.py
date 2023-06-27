import unittest
import datetime

from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.account_repo import AccountRepo


ACCOUNT_ID = '607f6723-c704-4b52-bc26-556a9aec85f6'
BAD_ACCOUNT_ID = 'badbadba-dbad-badb-adba-dbadbadbadba'

ACCT_ID_1 = '7a98df6a-e4db-40f4-91ec-627ac315d881'
DUMMY_ACCT_INFO_1 = {
    "address": {
        "city": "Springfield",
        "country_code": "US",
        "post_code": "12345",
        "state": "CA",
        "street": "123 Main St. E.",
        "street2": "Apt. 2"
    },
    "email": "geocode_test_1@testing.com",
    "first_name": "Jane",
    "last_name": "Doe",
    "language": "en_US",
    "kit_name": 'jb_qhxqe',
    "consent_privacy_terms": True,
    "id": ACCT_ID_1
}
ACCT_MOCK_ISS_1 = "MrUnitTest.go"
ACCT_MOCK_SUB_1 = "NotARealSub"
RESULT_LAT = 32.882274018668355
RESULT_LONG = -117.2353976693118


class AccountTests(unittest.TestCase):
    def setUp(self):
        with Transaction() as t:
            ar = AccountRepo(t)
            self.untouched = ar.get_account(ACCOUNT_ID)

    def test_scrub(self):
        with Transaction() as t:
            ar = AccountRepo(t)
            ar.scrub(ACCOUNT_ID)
            obs = ar.get_account(ACCOUNT_ID)

            self.assertEqual(obs.id, self.untouched.id)
            self.assertNotEqual(obs.email, self.untouched.email)
            self.assertEqual(obs.account_type, 'deleted')
            self.assertEqual(obs.auth_issuer, None)
            self.assertEqual(obs.auth_sub, None)
            self.assertEqual(obs.first_name, 'scrubbed')
            self.assertEqual(obs.last_name, 'scrubbed')
            self.assertEqual(obs.address.street, 'scrubbed')
            self.assertEqual(obs.address.city, 'scrubbed')
            self.assertEqual(obs.address.state, 'NA')
            self.assertEqual(obs.address.post_code, 'scrubbed')

            # keeping country is reasonable as it's so broad
            self.assertEqual(obs.address.country_code,
                             self.untouched.address.country_code)
            self.assertEqual(obs.created_with_kit_id,
                             self.untouched.created_with_kit_id)
            self.assertEqual(obs.creation_time,
                             self.untouched.creation_time)
            self.assertNotEqual(obs.update_time,
                                self.untouched.update_time)
            self.assertEqual(obs.language,
                             self.untouched.language)

            email = obs.email
            date, remainder = email.split('@', 1)
            date = date.split('T')[0].strip('"')
            obs_date = datetime.datetime.strptime(date, "%Y-%m-%d")
            today = datetime.datetime.now()
            today = datetime.datetime(year=today.year,
                                      month=today.month,
                                      day=today.day)
            self.assertEqual(obs_date, today)
            self.assertEqual(remainder, 'microsetta.ucsd.edu')

    def test_scrub_no_account(self):
        with Transaction() as t:
            ar = AccountRepo(t)
            with self.assertRaises(RepoException):
                ar.scrub(BAD_ACCOUNT_ID)


if __name__ == '__main__':
    unittest.main()
