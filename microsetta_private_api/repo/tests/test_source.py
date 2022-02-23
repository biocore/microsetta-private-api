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
                      HumanInfo('foo@bar.com', False,
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
            self.assertNotEqual(obs.source_data.email,
                                HUMAN_SOURCE.source_data.email)

            self.assertTrue(obs.source_data.date_revoked is not None)


if __name__ == '__main__':
    unittest.main()
