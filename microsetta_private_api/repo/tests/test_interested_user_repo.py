import unittest
import uuid

from unittest.mock import patch
from microsetta_private_api.model.interested_user import InterestedUser
from microsetta_private_api.repo.interested_user_repo import InterestedUserRepo
from microsetta_private_api.repo.transaction import Transaction
from psycopg2.errors import ForeignKeyViolation


ADDRESS_1 = "9500 Gilman Dr"
ADDRESS_2 = ""
CITY = "La Jolla"
STATE = "CA"
POSTAL = "92093"
COUNTRY = "United States"
LATITUDE = "32.88003507430753"
LONGITUDE = "-117.23394724325632"


class InterestedUserRepoTests(unittest.TestCase):
    def setUp(self):
        self.test_campaign_title_1 = 'Test Campaign'
        with Transaction() as t:
            cur = t.cursor()

            # create a test campaign
            cur.execute(
                "INSERT INTO campaign.campaigns (title) "
                "VALUES (%s) "
                "RETURNING campaign_id",
                (self.test_campaign_title_1, )
            )
            self.test_campaign_id = cur.fetchone()[0]

            # create necessary campaign/project relationship
            cur.execute(
                "INSERT INTO campaign.campaigns_projects "
                "(campaign_id, project_id) "
                "VALUES (%s, 1)",
                (self.test_campaign_id, )
            )

            # create an interested user
            dummy_user = {
                "campaign_id": self.test_campaign_id,
                "first_name": "Testing",
                "last_name": "Testerson",
                "email": "test_user_1234@testing.com"
            }
            interested_user = InterestedUser.from_dict(dummy_user)
            interested_user_repo = InterestedUserRepo(t)
            iuid = interested_user_repo.insert_interested_user(interested_user)
            self.test_iuid = iuid
            self.test_email = dummy_user["email"]

            t.commit()

        # need to create an extra, fake campaign ID
        self.fake_campaign_id = None
        while self.fake_campaign_id is None:
            tmp_fake_campaign_id = uuid.uuid4()
            if tmp_fake_campaign_id != self.test_campaign_id:
                self.fake_campaign_id = str(tmp_fake_campaign_id)

        # need to create an extra, fake user ID
        self.fake_iuid = None
        while self.fake_iuid is None:
            tmp_fake_iuid = uuid.uuid4()
            if tmp_fake_iuid != self.test_iuid:
                self.fake_iuid = str(tmp_fake_iuid)

    def tearDown(self):
        with Transaction() as t:
            cur = t.cursor()
            cur.execute(
                "DELETE FROM campaign.interested_users "
                "WHERE interested_user_id = %s",
                (self.test_iuid,)
            )
            cur.execute(
                "DELETE FROM campaign.campaigns_projects "
                "WHERE campaign_id = %s",
                (self.test_campaign_id,)
            )
            cur.execute(
                "DELETE FROM campaign.campaigns "
                "WHERE campaign_id = %s",
                (self.test_campaign_id,)
            )
            t.commit()

    def test_create_interested_user_valid(self):
        dummy_user = {
            "campaign_id": self.test_campaign_id,
            "first_name": "Test",
            "last_name": "McTesterson",
            "email": "test@testing.com"
        }

        interested_user = InterestedUser.from_dict(dummy_user)

        with Transaction() as t:
            interested_user_repo = InterestedUserRepo(t)
            obs = interested_user_repo.insert_interested_user(interested_user)
            self.assertTrue(obs is not None)

    def test_create_interested_user_invalid(self):
        # test with a required field missing
        dummy_user = {
            "campaign_id": self.test_campaign_id,
            "first_name": "Test",
            "last_name": "McTesterson"
        }
        with self.assertRaises(KeyError):
            interested_user = InterestedUser.from_dict(dummy_user)

        # test with invalid campaign ID
        dummy_user = {
            "campaign_id": self.fake_campaign_id,
            "first_name": "Test",
            "last_name": "McTesterson",
            "email": "test@testing.com"
        }
        interested_user = InterestedUser.from_dict(dummy_user)
        with Transaction() as t:
            interested_user_repo = InterestedUserRepo(t)
            with self.assertRaises(ForeignKeyViolation):
                interested_user_repo.insert_interested_user(interested_user)

    def test_verify_address_already_verified(self):
        dummy_user = {
            "campaign_id": self.test_campaign_id,
            "first_name": "Test",
            "last_name": "McTesterson",
            "email": "test@testing.com",
            "address_checked": True
        }
        interested_user = InterestedUser.from_dict(dummy_user)
        with Transaction() as t:
            interested_user_repo = InterestedUserRepo(t)
            user_id = \
                interested_user_repo.insert_interested_user(interested_user)
            obs = interested_user_repo.verify_address(user_id)
            self.assertTrue(obs is None)

    @patch("microsetta_private_api.repo.interested_user_repo.verify_address")
    def test_verify_address_not_verified_is_valid(self, test_verify_address):
        test_verify_address.return_value = {
            "address_1": ADDRESS_1,
            "address_2": ADDRESS_2,
            "city": CITY,
            "state": STATE,
            "postal": POSTAL,
            "country": COUNTRY,
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "valid": True
        }
        dummy_user = {
            "campaign_id": self.test_campaign_id,
            "first_name": "Test",
            "last_name": "McTesterson",
            "email": "test@testing.com",
            "address_1": ADDRESS_1,
            "city": CITY,
            "state": STATE,
            "postal_code": POSTAL,
            "country": COUNTRY
        }
        interested_user = InterestedUser.from_dict(dummy_user)
        with Transaction() as t:
            interested_user_repo = InterestedUserRepo(t)
            user_id = \
                interested_user_repo.insert_interested_user(interested_user)
            obs = interested_user_repo.verify_address(user_id)
            self.assertTrue(obs is True)

    @patch("microsetta_private_api.repo.interested_user_repo.verify_address")
    def test_verify_address_not_verified_is_invalid(self, test_verify_address):
        test_verify_address.return_value = {
            "address_1": ADDRESS_1,
            "address_2": ADDRESS_2,
            "city": CITY,
            "state": STATE,
            "postal": POSTAL,
            "country": COUNTRY,
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "valid": False
        }
        dummy_user = {
            "campaign_id": self.test_campaign_id,
            "first_name": "Test",
            "last_name": "McTesterson",
            "email": "test@testing.com",
            "address_1": ADDRESS_1,
            "city": CITY,
            "state": STATE,
            "postal_code": POSTAL,
            "country": COUNTRY
        }
        interested_user = InterestedUser.from_dict(dummy_user)
        with Transaction() as t:
            interested_user_repo = InterestedUserRepo(t)
            user_id = \
                interested_user_repo.insert_interested_user(interested_user)
            obs = interested_user_repo.verify_address(user_id)
            self.assertTrue(obs is False)

    def test_update_interested_user_valid(self):
        dummy_user = {
            "campaign_id": self.test_campaign_id,
            "first_name": "Test",
            "last_name": "McTesterson",
            "email": "test@testing.com"
        }

        interested_user = InterestedUser.from_dict(dummy_user)

        with Transaction() as t:
            interested_user_repo = InterestedUserRepo(t)
            iuid = interested_user_repo.insert_interested_user(interested_user)

            # need to create a fake user ID
            fake_iuid = None
            while fake_iuid is None:
                tmp_fake_iuid = uuid.uuid4()
                if tmp_fake_iuid != iuid:
                    fake_iuid = str(tmp_fake_iuid)

            interested_user.interested_user_id = fake_iuid
            interested_user.address_1 = "9500 Gilman Dr"
            interested_user.city = "La Jolla"
            interested_user.state = "CA"
            interested_user.postal_code = "92093"
            interested_user.country = "United States"

            obs = interested_user_repo.update_interested_user(interested_user)
            self.assertTrue(obs is False)

    def test_update_interested_user_invalid(self):
        dummy_user = {
            "campaign_id": self.test_campaign_id,
            "first_name": "Test",
            "last_name": "McTesterson",
            "email": "test@testing.com"
        }

        interested_user = InterestedUser.from_dict(dummy_user)

        with Transaction() as t:
            interested_user_repo = InterestedUserRepo(t)
            iuid = interested_user_repo.insert_interested_user(interested_user)

            interested_user.interested_user_id = iuid
            interested_user.address_1 = "9500 Gilman Dr"
            interested_user.city = "La Jolla"
            interested_user.state = "CA"
            interested_user.postal_code = "92093"
            interested_user.country = "United States"

            obs = interested_user_repo.update_interested_user(interested_user)
            self.assertTrue(obs is True)

    def test_get_interested_user_by_id_valid(self):
        with Transaction() as t:
            interested_user_repo = InterestedUserRepo(t)
            obs = \
                interested_user_repo.get_interested_user_by_id(self.test_iuid)
            self.assertTrue(obs is not None)

    def test_get_interested_user_by_id_invalid(self):
        with Transaction() as t:
            interested_user_repo = InterestedUserRepo(t)
            obs = \
                interested_user_repo.get_interested_user_by_id(self.fake_iuid)
            self.assertTrue(obs is None)

    def test_get_interested_user_by_email_valid(self):
        with Transaction() as t:
            t_e = self.test_email
            interested_user_repo = InterestedUserRepo(t)
            obs = \
                interested_user_repo.get_interested_user_by_email(t_e)
            self.assertTrue(obs is not None)

    def test_get_interested_user_by_email_invalid(self):
        with Transaction() as t:
            t_e = "THISSTRINGSHOULDNTMATCHANEMAILADDRESSINTHETABLE"
            interested_user_repo = InterestedUserRepo(t)
            obs = \
                interested_user_repo.get_interested_user_by_email(t_e)
            self.assertFalse(obs is False)


if __name__ == '__main__':
    unittest.main()
