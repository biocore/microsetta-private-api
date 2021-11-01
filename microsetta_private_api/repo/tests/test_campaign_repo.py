import unittest
import uuid

from microsetta_private_api.repo.campaign_repo import CampaignRepo
from microsetta_private_api.repo.transaction import Transaction
from psycopg2.errors import UniqueViolation, ForeignKeyViolation


EMAIL_1 = 'foo@bar.com'
EMAIL_2 = 'wwbhsqo5s9@fi9s6.nzb'  # a valid email stable in the test database
ACCT_ID_1 = 'c979cc9e-a82f-4f53-a456-9fa9be9f52d4'
SRC_ID_1 = ''


# source IDs are constructed during patching and are not stable
# so let's pull one at runtime
with Transaction() as t:
    cur = t.cursor()
    cur.execute("""SELECT id as source_id
                   FROM ag.source
                   WHERE account_id=%s
                   LIMIT 1""",
                (ACCT_ID_1, ))
    SRC_ID_1 = cur.fetchone()[0]


class CampaignRepoTests(unittest.TestCase):
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
                "title": "Unique Campaign Name"
            }
            campaign_repo = CampaignRepo(t)
            with self.assertRaises(KeyError):
                campaign_repo.create_campaign(**campaign_no_projects)

        # test to verify that associated_projects must be valid project_ids
        with Transaction() as t:
            campaign_bad_projects = {
                "title": "Unique Campaign Name",
                "associated_projects": "-1"
            }
            campaign_repo = CampaignRepo(t)
            with self.assertRaises(ForeignKeyViolation):
                campaign_repo.create_campaign(**campaign_bad_projects)

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

    def test_is_member_by_source(self):
        with Transaction() as t:
            cr = CampaignRepo(t)
            obs = cr.is_member_by_source(ACCT_ID_1, SRC_ID_1,
                                         self.test_campaign_id1)
            self.assertTrue(obs)

            for aid, sid, cid in [(str(uuid.uuid4()), str(uuid.uuid4()),
                                   str(uuid.uuid4())),
                                  (ACCT_ID_1, str(uuid.uuid4()),
                                   str(uuid.uuid4())),
                                  (str(uuid.uuid4()), SRC_ID_1,
                                   str(uuid.uuid4())),
                                  (ACCT_ID_1, SRC_ID_1,
                                   str(uuid.uuid4()))]:
                obs = cr.is_member_by_source(aid, sid, cid)
                self.assertFalse(obs)

    def test_is_member_by_email(self):
        with Transaction() as t:
            cur = t.cursor()
            cur.execute("""INSERT INTO barcodes.interested_users
                           (campaign_id, first_name, last_name, email,
                            address_checked, address_valid,
                            converted_to_account)
                           VALUES (%s, 'cool', 'bob', %s,
                                   'N', 'N', 'N')""",
                        (self.test_campaign_id1, EMAIL_1))

            cr = CampaignRepo(t)
            obs = cr.is_member_by_email(EMAIL_1, self.test_campaign_id1)
            self.assertTrue(obs)

            obs = cr.is_member_by_email(EMAIL_2, self.test_campaign_id1)
            self.assertTrue(obs)

            for email, cid in [('foobar@baz.com', self.test_campaign_id1),

                               # this email exists and is stable in the test
                               # database, and is not associated with project
                               # 1
                               ('bsbk(ounxw@)9t30.wid',
                                self.test_campaign_id1),

                               (EMAIL_1, str(uuid.uuid4()))]:
                obs = cr.is_member_by_email(email, cid)
                self.assertFalse(obs)


if __name__ == '__main__':
    unittest.main()
