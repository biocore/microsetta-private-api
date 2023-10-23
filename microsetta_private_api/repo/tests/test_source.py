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

            file_name = "test_source.py"
            file_label = "Test Source Repo"
            # Opening and reading a file's contents doesn't appear to work on
            # GitHub during workflow, so we need to fake the contents
            file_contents = b'Imagine a full file here'
            cur = t.cursor()
            cur.execute(
                "INSERT INTO ag.external_reports ("
                "source_id, file_name, file_title, file_type, "
                "file_contents, report_type"
                ") VALUES (%s, %s, %s, %s, %s, %s)",
                (HUMAN_SOURCE.id, file_name, file_label,
                 "application/pdf", file_contents, "ffq")
            )

            t.commit()

    def tearDown(self):
        with Transaction() as t:
            cur = t.cursor()
            cur.execute(
                "DELETE FROM ag.external_reports "
                "WHERE source_id = %s",
                (HUMAN_SOURCE.id, )
            )

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

    def test_check_source_post_overhaul_true(self):
        # We'll check a newly created source and confirm that it's
        # treated as post-overhaul. The source created during setUp
        # can safely be used as-is.
        with Transaction() as t:
            sr = SourceRepo(t)
            obs = sr.check_source_post_overhaul(ACCOUNT_ID, HUMAN_SOURCE.id)
            self.assertTrue(obs)

    def test_check_source_post_overhaul_false(self):
        # Now we'll modify the creation_time column by hand and confirm it's
        # treated as pre-overhaul
        with Transaction() as t:
            cur = t.cursor()
            cur.execute(
                "UPDATE ag.source "
                "SET creation_time = '2023-01-01 10:00:00' "
                "WHERE id = %s",
                (HUMAN_SOURCE.id, )
            )

            sr = SourceRepo(t)
            obs = sr.check_source_post_overhaul(ACCOUNT_ID, HUMAN_SOURCE.id)
            self.assertFalse(obs)

    def test_get_external_reports(self):
        with Transaction() as t:
            sr = SourceRepo(t)
            obs = sr.get_external_reports(HUMAN_SOURCE.id)

            # We should observe one external report
            self.assertEqual(len(obs), 1)

    def test_get_external_reports_fake_source(self):
        with Transaction() as t:
            sr = SourceRepo(t)
            # Changed the source ID's second section from "ffff" to "aaaa"
            obs = sr.get_external_reports(
                "ffffffff-aaaa-cccc-aaaa-aaaaaaaaaaaa"
            )

            # We should observe zero external reports
            self.assertEqual(len(obs), 0)

    def test_get_external_report(self):
        with Transaction() as t:
            sr = SourceRepo(t)
            reports = sr.get_external_reports(HUMAN_SOURCE.id)

            er = reports[0]
            obs = sr.get_external_report(
                HUMAN_SOURCE.id, er.external_report_id
            )

            self.assertEqual(obs.source_id, HUMAN_SOURCE.id)
            self.assertEqual(obs.file_title, "Test Source Repo")

    def test_get_external_report_fail(self):
        with Transaction() as t:
            sr = SourceRepo(t)
            reports = sr.get_external_reports(HUMAN_SOURCE.id)

            er = reports[0]
            obs = sr.get_external_report(
                "ffffffff-aaaa-cccc-aaaa-aaaaaaaaaaaa", er.external_report_id
            )

            self.assertEqual(obs, None)

    def test_get_external_report_bytes(self):
        with Transaction() as t:
            sr = SourceRepo(t)
            reports = sr.get_external_reports(HUMAN_SOURCE.id)

            er = reports[0]
            obs = sr.get_external_report(
                HUMAN_SOURCE.id, er.external_report_id
            )

            act = b'Imagine a full file here'

            self.assertEqual(bytes(obs.file_contents), act)


if __name__ == '__main__':
    unittest.main()
