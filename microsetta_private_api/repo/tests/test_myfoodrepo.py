import unittest
from microsetta_private_api.repo.mfr_repo import MFRRepo
from microsetta_private_api.repo.transaction import Transaction

ACCT_ID_1 = ""
ACCT_ID_2 = ""
SRC_ID_1 = ""
SRC_ID_2 = ""
CAMPAIGN_ID_1 = "test"


def get_an_account_and_source(exclude=None):
    def _getter(exclude):
        with Transaction() as t:
            cur = t.cursor()
            if exclude is None:
                cur.execute("""SELECT account_id, source.id as source_id
                               FROM ag.source""")
            else:
                cur.execute("""SELECT account_id, source.id as source_id
                               FROM ag.source
                               WHERE account_id NOT IN (%s)""",
                            (exclude, ))

            return cur.fetchone()

    global ACCT_ID_1, ACCT_ID_1, SRC_ID_1, SRC_ID_2
    ACCT_ID_1, SRC_ID_1 = _getter()
    ACCT_ID_2, SRC_ID_2 = _getter(exclude=[ACCT_ID_1, ])


class MFRRepoTests(unittest.TestCase):
    # The MFR URL and API key are encoded as github repository secrets.
    # Secrets are not passed when a fork issues a PR. This test will still
    # execute from master once a PR is merged.
    @skipIf(SERVER_CONFIG['myfoodrepo_url'] in ('', 'mfr_url_placeholder'),
            "MFR secrets not provided")
    def test_add_subject(self):
        with Transaction() as t:
            mfr = MFRRepo(t)
            # store their creation and expiratio
            # update mfr to et their expiration
            subj = mfr.add_subject(ACCT_ID_1, SRC_ID_1, CAMPAIGN_ID_1)

            # already added
            with self.assertRaises(RepoException):
                mfr.add_subject(ACCT_ID_1, SRC_ID_1, CAMPAIGN_ID_1)

            # a nonsense id association
            with self.assertRaises(RepoException):
                mfr.add_subject(ACCT_ID_2, SRC_ID_1, CAMPAIGN_ID_1)

            t.rollback()

    @skipIf(SERVER_CONFIG['myfoodrepo_url'] in ('', 'mfr_url_placeholder'),
            "MFR secrets not provided")
    def test_active_subjects(self):
        with Transaction() as t:
            mfr = MFRRepo(t)
            obs = mfr.active_subjects(CAMPAIGN_ID_1)
            self.assertEqual(obs, 0)

            mfr.add_subject(ACCT_ID_1, SRC_ID_1, CAMPAIGN_ID_1)
            mfr.add_subject(ACCT_ID_2, SRC_ID_2, CAMPAIGN_ID_1)
            obs = mfr.active_subjects(CAMPAIGN_ID_1)
            self.assertEqual(obs, 2)

            # expire an added subject
            mfr.expire_subject(ACCT_ID_1, SRC_ID_1, CAMPAIGN_ID_1)
            obs = mfr.active_subjects(CAMPAIGN_ID_1)
            self.assertEqual(obs, 1)

            t.rollback()

    @skipIf(SERVER_CONFIG['myfoodrepo_url'] in ('', 'mfr_url_placeholder'),
            "MFR secrets not provided")
    def test_expire_subject(self):
        with Transaction() as t:
            mfr = MFRRepo(t)
            mfr.add_subject(ACCT_ID_1, SRC_ID_1, CAMPAIGN_ID_1)
            mfr.expire_subject(ACCT_ID_1, SRC_ID_1, CAMPAIGN_ID_1)

            # already expired
            with self.assertRaises(RepoException):
                mfr.expire_subject(ACCT_ID_1, SRC_ID_1, CAMPAIGN_ID_1)

            # a nonsense id association
            with self.assertRaises(RepoException):
                mfr.expire_subject(ACCT_ID_2, SRC_ID_1, CAMPAIGN_ID_1)

            t.rollback()

    @skipIf(SERVER_CONFIG['myfoodrepo_url'] in ('', 'mfr_url_placeholder'),
            "MFR secrets not provided")
    def test_delete_subject(self):
        with Transaction() as t:
            mfr = MFRRepo(t)
            mfr.add_subject(ACCT_ID_1, SRC_ID_1, CAMPAIGN_ID_1)
            mfr.delete_subject(ACCT_ID_1, SRC_ID_1, CAMPAIGN_ID_1)

            # already expired
            with self.assertRaises(RepoException):
                mfr.delete_subject(ACCT_ID_1, SRC_ID_1, CAMPAIGN_ID_1)

            t.rollback()

    @skipIf(SERVER_CONFIG['myfoodrepo_url'] in ('', 'mfr_url_placeholder'),
            "MFR secrets not provided")
    def test_get_set_max_active_subjects(self):
        with Transaction() as t:
            mfr = MFRRepo(t)

            # doesn't exist
            obs = mfr.get_max_active_subjects(CAMPAIGN_ID_1)
            self.assertEqual(obs, 0)

            # act as upsert
            obs = mfr.set_max_active_subjects(CAMPAIGN_ID_1, 10)
            obs = mfr.get_max_active_subjects(CAMPAIGN_ID_1)
            self.assertEqual(obs, 10)

            ### NOTE: CAMPAIGN_ID *must* link to the lead table strutures

if __name__ == '__main__':
    unittest.main()
