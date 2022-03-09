import unittest
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.repo.transaction import Transaction


class SampleTests(unittest.TestCase):
    def _get_source_from_sample(self, t, sample_id):
        cur = t.cursor()
        cur.execute("""SELECT account_id, source_id
                       FROM ag.ag_kit_barcodes
                       JOIN ag.source ON source_id=source.id
                       WHERE ag_kit_barcode_id=%s""",
                    (sample_id, ))
        return cur.fetchone()

    def _sample_in_source(self, source_samples, sample_id):
        found = False
        for sample in source_samples:
            if sample.id == sample_id:
                found = True
                break
        return found

    def test_scrub_bad_source(self):
        samp1 = 'd8592c74-85f0-2135-e040-8a80115d6401'  # 000001766
        with Transaction() as t:
            acct1, src1 = self._get_source_from_sample(t, samp1)
            sr = SampleRepo(t)

            with self.assertRaises(RepoException):
                sr.scrub(acct1, acct1, samp1)

    def test_scrub_bad_sample(self):
        samp1 = 'd8592c74-85f0-2135-e040-8a80115d6401'  # 000001766
        with Transaction() as t:
            acct1, src1 = self._get_source_from_sample(t, samp1)
            sr = SampleRepo(t)

            with self.assertRaises(RepoException):
                sr.scrub(acct1, src1, src1)

    def test_scrub(self):
        samp1 = 'd8592c74-85f0-2135-e040-8a80115d6401'  # 000001766
        with Transaction() as t:
            acct1, src1 = self._get_source_from_sample(t, samp1)

            sr = SampleRepo(t)

            # get original source associations
            src1_sample = sr.get_samples_by_source(acct1, src1)[0]

            res = sr.scrub(acct1, src1, src1_sample.id)
            self.assertTrue(res)

            obs_sample = sr.get_samples_by_source(acct1, src1)[0]
            self.assertNotEqual(src1_sample.notes, obs_sample.notes)

    def test_update_sample_assocation_with_migration(self):
        samp1 = 'd8592c74-85f0-2135-e040-8a80115d6401'  # 000001766
        samp2 = 'ceaa6fd6-0861-4335-aa35-da1857bd5294'  # 000067789

        with Transaction() as t:
            acct1, src1 = self._get_source_from_sample(t, samp1)
            acct2, src2 = self._get_source_from_sample(t, samp2)

            sr = SampleRepo(t)

            # get original source associations
            src1_samples = sr.get_samples_by_source(acct1, src1)
            src2_samples = sr.get_samples_by_source(acct2, src2)

            # verify samples are part of the original source
            self.assertTrue(self._sample_in_source(src1_samples, samp1))
            self.assertTrue(self._sample_in_source(src2_samples, samp2))

            # swap associations
            sr._update_sample_association(samp1, src2, True)
            sr._update_sample_association(samp2, src1, True)

            # get new samples by source
            src1_samples = sr.get_samples_by_source(acct1, src1)
            src2_samples = sr.get_samples_by_source(acct2, src2)

            # verify samples are part of the new source
            self.assertTrue(self._sample_in_source(src1_samples, samp2))
            self.assertTrue(self._sample_in_source(src2_samples, samp1))

            # verify samples are not part of the original source
            self.assertFalse(self._sample_in_source(src1_samples, samp1))
            self.assertFalse(self._sample_in_source(src2_samples, samp2))

            # fix associations
            sr._update_sample_association(samp1, src1, True)
            sr._update_sample_association(samp2, src2, True)

            # ...and verify assocations are fixed
            src1_samples = sr.get_samples_by_source(acct1, src1)
            src2_samples = sr.get_samples_by_source(acct2, src2)
            self.assertTrue(self._sample_in_source(src1_samples, samp1))
            self.assertTrue(self._sample_in_source(src2_samples, samp2))

    def test_migrate_sample_exceptions(self):
        samp1 = 'd8592c74-85f0-2135-e040-8a80115d6401'  # 000001766
        samp2 = 'ceaa6fd6-0861-4335-aa35-da1857bd5294'  # 000067789
        bad = 'ffffffff-ffff-ffff-aaaa-aaaaaaaaaaaa'

        with Transaction() as t:
            _, src1 = self._get_source_from_sample(t, samp1)
            _, src2 = self._get_source_from_sample(t, samp2)
            sr = SampleRepo(t)

            with self.assertRaises(RepoException):
                # verify we dont do something unless we are intentional
                sr.migrate_sample(samp1, src1, src2, False)

            with self.assertRaises(RepoException):
                # the sample must be associated witht the source (src)
                # to move
                sr.migrate_sample(samp2, src1, src2, True)

            with self.assertRaises(RepoException):
                # the destination must exist
                sr.migrate_sample(samp1, src1, bad, True)

    def test_migrate_sample(self):
        samp1 = 'd8592c74-85f0-2135-e040-8a80115d6401'  # 000001766
        samp2 = 'ceaa6fd6-0861-4335-aa35-da1857bd5294'  # 000067789

        with Transaction() as t:
            acct1, src1 = self._get_source_from_sample(t, samp1)
            acct2, src2 = self._get_source_from_sample(t, samp2)
            sr = SampleRepo(t)

            sr.migrate_sample(samp1, src1, src2, True)

            # get new samples by source
            src1_samples = sr.get_samples_by_source(acct1, src1)
            src2_samples = sr.get_samples_by_source(acct2, src2)

            # verify samples are part of the new source
            self.assertFalse(self._sample_in_source(src1_samples, samp1))
            self.assertTrue(self._sample_in_source(src2_samples, samp1))


if __name__ == '__main__':
    unittest.main()
