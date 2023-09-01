import unittest

import datetime

from microsetta_private_api.exceptions import RepoException

from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.model.source import Source, HumanInfo


ACCOUNT_ID = '607f6723-c704-4b52-bc26-556a9aec85f6'
HUMAN_SOURCE = Source('ffffffff-ffff-cccc-aaaa-aaaaaaaaaaaa',
                      ACCOUNT_ID,
                      Source.SOURCE_TYPE_HUMAN,
                      'test person',
                      HumanInfo(False,
                                None, None, None,
                                datetime.datetime.now(),
                                None, None, '18-plus'))


class SourceRepoTests(unittest.TestCase):
    def setUp(self):
        with Transaction() as t:
            sr = SourceRepo(t)
            sr.create_source(HUMAN_SOURCE)
            t.commit()

    def tearDown(self):
        with Transaction() as t:
            sr = SourceRepo(t)
            sr.delete_source(HUMAN_SOURCE.account_id,
                             HUMAN_SOURCE.id)
            t.commit()

    def test_scrub_bad_source(self):
        with Transaction() as t:
            sr = SourceRepo(t)
            with self.assertRaises(RepoException):
                sr.scrub(ACCOUNT_ID,
                         'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa')

    def test_scrub_not_human(self):
        with Transaction() as t:
            sr = SourceRepo(t)

            # make the source an animal
            cur = t.cursor()
            cur.execute("""UPDATE ag.source
                           SET source_type=%s
                           WHERE id=%s""",
                        (Source.SOURCE_TYPE_ANIMAL, HUMAN_SOURCE.id))

            with self.assertRaises(RepoException):
                sr.scrub(ACCOUNT_ID,
                         HUMAN_SOURCE.id)

    def test_scrub(self):
        with Transaction() as t:
            sr = SourceRepo(t)
            sr.scrub(HUMAN_SOURCE.account_id,
                     HUMAN_SOURCE.id)

            obs = sr.get_source(HUMAN_SOURCE.account_id,
                                HUMAN_SOURCE.id,
                                allow_revoked=False)
            self.assertEqual(obs, None)

            obs = sr.get_source(HUMAN_SOURCE.account_id,
                                HUMAN_SOURCE.id,
                                allow_revoked=True)

            self.assertNotEqual(obs.name, HUMAN_SOURCE.name)

            self.assertTrue(obs.source_data.date_revoked is not None)

    def test_update_legacy_source_age_range_succeed(self):
        with Transaction() as t:
            # First, we need to update the test source to an age_range of
            # 'legacy'
            cur = t.cursor()
            cur.execute("UPDATE ag.source "
                        "SET age_range = 'legacy' "
                        "WHERE id = %s",
                        (HUMAN_SOURCE.id, )
                        )

            # Now, let's update it
            sr = SourceRepo(t)
            obs = sr.update_legacy_source_age_range(
                HUMAN_SOURCE.id,
                "18-plus"
            )
            self.assertTrue(obs)

    def test_update_legacy_source_age_range_fail(self):
        # We'll try to update the human source without setting its age range
        # to 'legacy'
        with Transaction() as t:
            sr = SourceRepo(t)
            obs = sr.update_legacy_source_age_range(
                HUMAN_SOURCE.id,
                "18-plus"
            )
            self.assertFalse(obs)


if __name__ == '__main__':
    unittest.main()
