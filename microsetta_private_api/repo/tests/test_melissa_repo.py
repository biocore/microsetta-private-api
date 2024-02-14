import unittest

from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.melissa_repo import MelissaRepo


class MelissaRepoTests(unittest.TestCase):
    def test_create_record(self):
        with Transaction() as t:
            mr = MelissaRepo(t)
            record_id = mr.create_record(
                "9500 Gilman Dr",
                "",
                "",
                "La Jolla",
                "CA",
                "92093",
                "US"
            )
            self.assertNotEqual(record_id, None)

    def test_update_results(self):
        with Transaction() as t:
            mr = MelissaRepo(t)
            record_id = mr.create_record(
                "9500 Gilman Dr",
                "",
                "",
                "La Jolla",
                "CA",
                "92093",
                "US"
            )

            obs = mr.update_results(
                record_id,
                "http://foo.bar",
                "RAW_RESULT",
                "AV24, GS05",
                True,
                "9500 Gilman Dr, La Jolla, CA 92093, US",
                "9500 Gilman Dr",
                "",
                "",
                "La Jolla",
                "CA",
                "92093",
                "US",
                32.8798916,
                -117.2363115
            )

            self.assertTrue(obs)

    def test_check_duplicate_no_match(self):
        with Transaction() as t:
            mr = MelissaRepo(t)
            obs = mr.check_duplicate(
                "1234 Not Real St",
                "",
                "99999",
                "US"
            )

            self.assertFalse(obs)

    def test_check_duplicate_with_address_2(self):
        with Transaction() as t:
            mr = MelissaRepo(t)
            record_id = mr.create_record(
                "9500 Gilman Dr",
                "Suite 100",
                "",
                "La Jolla",
                "CA",
                "92093",
                "US"
            )

            # We need the result_processed column to be TRUE for the dupe check
            cur = t.cursor()
            cur.execute(
                "UPDATE campaign.melissa_address_queries "
                "SET result_processed = TRUE "
                "WHERE melissa_address_query_id = %s",
                (record_id, )
            )

            obs = mr.check_duplicate(
                "9500 Gilman Dr",
                "Suite 100",
                "92093",
                "US"
            )

            self.assertEqual(record_id, obs['melissa_address_query_id'])

    def test_check_duplicate_no_address_2(self):
        with Transaction() as t:
            mr = MelissaRepo(t)
            record_id = mr.create_record(
                "9500 Gilman Dr",
                None,
                None,
                "La Jolla",
                "CA",
                "92093",
                "US"
            )

            # We need the result_processed column to be TRUE for the dupe check
            cur = t.cursor()
            cur.execute(
                "UPDATE campaign.melissa_address_queries "
                "SET result_processed = TRUE "
                "WHERE melissa_address_query_id = %s",
                (record_id, )
            )

            obs = mr.check_duplicate(
                "9500 Gilman Dr",
                None,
                "92093",
                "US"
            )

            self.assertEqual(record_id, obs['melissa_address_query_id'])


if __name__ == '__main__':
    unittest.main()
