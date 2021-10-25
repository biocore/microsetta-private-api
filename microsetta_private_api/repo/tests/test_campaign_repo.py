import unittest

from microsetta_private_api.repo.campaign_repo import CampaignRepo
from microsetta_private_api.repo.transaction import Transaction
from psycopg2.errors import UniqueViolation


class CampaignRepoTests(unittest.TestCase):
    def setUp(self):
        self.test_campaign_title_1 = 'Test Campaign'
        associated_projects = "1"
        with Transaction() as t:
            cur = t.cursor()
            cur.execute(
                "INSERT INTO barcodes.campaigns (title) "
                "VALUES (%s) "
                "RETURNING campaign_id",
                (self.test_campaign_title_1, )
            )
            self.test_campaign_id1 = cur.fetchone()[0]

            cur.execute(
                "INSERT INTO barcodes.campaigns_projects "
                "(campaign_id, project_id) "
                "VALUES (%s, 1)",
                (self.test_campaign_id1, )
            )
            t.commit()

    def tearDown(self):
        with Transaction() as t:
            cur = t.cursor()
            cur.execute(
                "DELETE FROM barcodes.campaigns_projects "
                "WHERE campaign_id = %s",
                (self.test_campaign_id1,)
            )
            cur.execute(
                "DELETE FROM barcodes.campaigns "
                "WHERE campaign_id = %s",
                (self.test_campaign_id1, )
            )
            t.commit()

    def test_create_campaign_valid(self):
        # create a campaign with minimal required fields
        with Transaction() as t:
            new_campaign = {
                "title": "Unique Campaign Name",
                "associated_projects": "1"
            }
            campaign_repo = CampaignRepo(t)
            obs = campaign_repo.create_campaign(**new_campaign)
            self.assertTrue(obs is not None)
            t.rollback()

    def test_create_campaign_invalid(self):
        # test to verify unique constraint on title
        with Transaction() as t:
            duplicate_campaign = {
                "title": "Test Campaign",
                "associated_projects": "1"
            }
            campaign_repo = CampaignRepo(t)
            with self.assertRaises(UniqueViolation):
                campaign_repo.create_campaign(**duplicate_campaign)

        # test to verify requirement of associated_projects
        with Transaction() as t:
            campaign_no_projects = {
                "title": "Test Campaign"
            }
            campaign_repo = CampaignRepo(t)
            with self.assertRaises(KeyError):
                campaign_repo.create_campaign(**campaign_no_projects)

    def test_get_campaign_by_id_valid(self):
        # verify that it does not return None when using valid campaign_id
        with Transaction() as t:
            campaign_repo = CampaignRepo(t)
            obs = campaign_repo.get_campaign_by_id(self.test_campaign_id1)
            self.assertTrue(obs is not None)

    def test_get_campaign_by_id_invalid(self):
        # verify that it returns None when using an invalid campaign_id
        with Transaction() as t:
            campaign_repo = CampaignRepo(t)
            obs = campaign_repo.get_campaign_by_id('INVALID_ID')
            self.assertEqual(obs, None)


if __name__ == '__main__':
    unittest.main()
