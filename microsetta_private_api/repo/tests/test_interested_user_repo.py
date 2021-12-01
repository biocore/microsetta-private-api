import unittest
import uuid

from microsetta_private_api.repo.interested_user_repo import InterestedUserRepo
from microsetta_private_api.repo.transaction import Transaction
from psycopg2.errors import ForeignKeyViolation


class InterestedUserRepoTests(unittest.TestCase):
    def setUp(self):
        self.test_campaign_title_1 = 'Test Campaign'
        with Transaction() as t:
            cur = t.cursor()
            cur.execute(
                "INSERT INTO barcodes.campaigns (title) "
                "VALUES (%s) "
                "RETURNING campaign_id",
                (self.test_campaign_title_1, )
            )
            self.test_campaign_id = cur.fetchone()[0]

            cur.execute(
                "INSERT INTO barcodes.campaigns_projects "
                "(campaign_id, project_id) "
                "VALUES (%s, 1)",
                (self.test_campaign_id, )
            )
            t.commit()

        # need to create an extra, fake campaign ID
        self.fake_campaign_id = None
        while self.fake_campaign_id is None:
            tmp_fake_campaign_id = uuid.uuid4()
            if tmp_fake_campaign_id != self.test_campaign_id:
                self.fake_campaign_id = str(tmp_fake_campaign_id)

    def tearDown(self):
        with Transaction() as t:
            cur = t.cursor()
            cur.execute(
                "DELETE FROM barcodes.campaigns_projects "
                "WHERE campaign_id = %s",
                (self.test_campaign_id,)
            )
            cur.execute(
                "DELETE FROM barcodes.campaigns "
                "WHERE campaign_id = %s",
                (self.test_campaign_id, )
            )
            t.commit()

    def test_create_interested_user_valid(self):
        with Transaction() as t:
            dummy_user = {
                "campaign_id": self.test_campaign_id,
                "first_name": "Test",
                "last_name": "McTesterson",
                "email": "test@testing.com"
            }
            interested_user_repo = InterestedUserRepo(t)
            obs = interested_user_repo.insert_interested_user(**dummy_user)
            self.assertTrue(obs is not None)
            t.rollback()

    def test_create_interested_user_invalid(self):
        # test with a required field missing
        with Transaction() as t:
            dummy_user = {
                "campaign_id": self.test_campaign_id,
                "first_name": "Test",
                "last_name": "McTesterson"
            }
            interested_user_repo = InterestedUserRepo(t)
            with self.assertRaises(KeyError):
                interested_user_repo.insert_interested_user(**dummy_user)

        # test with invalid campaign ID
        with Transaction() as t:
            dummy_user = {
                "campaign_id": self.fake_campaign_id,
                "first_name": "Test",
                "last_name": "McTesterson",
                "email": "test@testing.com"
            }
            interested_user_repo = InterestedUserRepo(t)
            with self.assertRaises(ForeignKeyViolation):
                interested_user_repo.insert_interested_user(**dummy_user)


if __name__ == '__main__':
    unittest.main()
