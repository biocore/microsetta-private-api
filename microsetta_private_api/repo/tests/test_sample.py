import unittest
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.model.sample import SampleInfo
import datetime


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

    def test_get_supplied_kit_id_by_sample(self):
        with Transaction() as t:
            # First we'll create a kit so that we have a kit_id/barcode combo
            # to test with
            admin_repo = AdminRepo(t)
            res = admin_repo.create_kits(
                1,
                1,
                "UNITTEST",
                [[]],
                [1]
            )

            # Extract the info from results. We know we created 1 kit with 1
            # sample so we don't need to iterate
            kit_info = res['created'][0]
            kit_id = kit_info['kit_id']
            sample_barcode = kit_info['sample_barcodes'][0]

            # Verify that the function returns the correct kit_id
            sample_repo = SampleRepo(t)
            supplied_kit_id = sample_repo._get_supplied_kit_id_by_sample(
                sample_barcode
            )
            self.assertEqual(kit_id, supplied_kit_id)

    def test_validate_barcode_meta_pass(self):
        with Transaction() as t:
            sample_repo = SampleRepo(t)

            # Build a barcode_meta dict matching what we expect for cheek
            # samples with all fields completed
            bc_meta = {
                "sample_site_last_washed_date": "01/10/2025",
                "sample_site_last_washed_time": "9:30 AM",
                "sample_site_last_washed_product": "Face cleanser"
            }
            bc_valid = sample_repo._validate_barcode_meta("Cheek", bc_meta)
            self.assertNotEqual(bc_valid, False)

            # Test each scenario where only one field is present to confirm
            # that any other field can be nullable
            bc_meta = {
                "sample_site_last_washed_date": "01/10/2025",
                "sample_site_last_washed_time": "",
                "sample_site_last_washed_product": ""
            }
            exp = {
                "sample_site_last_washed_date": datetime.datetime(
                    2025, 1, 10),
                "sample_site_last_washed_time": None,
                "sample_site_last_washed_product": None
            }
            bc_valid = sample_repo._validate_barcode_meta("Cheek", bc_meta)
            self.assertEqual(bc_valid, exp)

            bc_meta = {
                "sample_site_last_washed_date": "",
                "sample_site_last_washed_time": "9:30 AM",
                "sample_site_last_washed_product": ""
            }
            exp = {
                "sample_site_last_washed_date": None,
                "sample_site_last_washed_time": datetime.datetime(
                    1900, 1, 1, 9, 30),
                "sample_site_last_washed_product": None
            }
            bc_valid = sample_repo._validate_barcode_meta("Cheek", bc_meta)
            self.assertEqual(bc_valid, exp)

            bc_meta = {
                "sample_site_last_washed_date": "",
                "sample_site_last_washed_time": "",
                "sample_site_last_washed_product": "Face cleanser"
            }
            exp = {
                "sample_site_last_washed_date": None,
                "sample_site_last_washed_time": None,
                "sample_site_last_washed_product": "Face cleanser"
            }
            bc_valid = sample_repo._validate_barcode_meta("Cheek", bc_meta)
            self.assertEqual(bc_valid, exp)

            # Confirm that empty dicts pass, regardless of site
            bc_meta = {}
            bc_valid = sample_repo._validate_barcode_meta("Stool", bc_meta)
            self.assertEqual(bc_valid, {})

    def test_validate_barcode_meta_fail(self):
        with Transaction() as t:
            sample_repo = SampleRepo(t)
            # Try using an invalid field name
            bc_meta = {
                "my_life_story": "I've done stuff and things"
            }
            bc_valid = sample_repo._validate_barcode_meta("Cheek", bc_meta)
            self.assertFalse(bc_valid)

            # Try using an invalid site
            bc_meta = {
                "sample_site_last_washed_product": "Face cleanser"
            }
            bc_valid = sample_repo._validate_barcode_meta("Stool", bc_meta)
            self.assertFalse(bc_valid)

            # Try using an invalid value for the date
            bc_meta = {
                "sample_site_last_washed_date": "Cookie monster",
                "sample_site_last_washed_time": "",
                "sample_site_last_washed_product": "Face cleanser"
            }
            bc_valid = sample_repo._validate_barcode_meta("Cheek", bc_meta)
            self.assertEqual(bc_valid, False)

            # Try using an invalid value for the time
            bc_meta = {
                "sample_site_last_washed_date": "",
                "sample_site_last_washed_time": "Rosemary focaccia",
                "sample_site_last_washed_product": "Face cleanser"
            }
            bc_valid = sample_repo._validate_barcode_meta("Cheek", bc_meta)
            self.assertEqual(bc_valid, False)

    def test_update_barcode_meta_via_update_info(self):
        # We're going to use a stable sample and override_locked to test
        # the barcode meta update via update_info()
        sample_id = "d8592c74-85f0-2135-e040-8a80115d6401"
        bc_meta = {
            "sample_site_last_washed_date": "01/10/2025",
            "sample_site_last_washed_time": "9:30 AM",
            "sample_site_last_washed_product": "Face cleanser"
        }
        sample_info = SampleInfo(
            sample_id,
            datetime.datetime.now(),
            "Cheek",
            "",
            bc_meta
        )

        with Transaction() as t:
            account_id, source_id = self._get_source_from_sample(t, sample_id)

            sample_repo = SampleRepo(t)
            sample_repo.update_info(account_id, source_id, sample_info, True)

            sample = sample_repo.get_sample(account_id, source_id, sample_id)
            self.assertEqual(bc_meta, sample.barcode_meta)

    def test_get_barcode_meta(self):
        # First, we need to set the barcode metadata. Same process as
        # test_update_barcode_meta_via_update_info()
        sample_id = "d8592c74-85f0-2135-e040-8a80115d6401"
        bc_meta = {
            "sample_site_last_washed_date": "01/10/2025",
            "sample_site_last_washed_time": "9:30 AM",
            "sample_site_last_washed_product": "Face cleanser"
        }
        sample_info = SampleInfo(
            sample_id,
            datetime.datetime.now(),
            "Cheek",
            "",
            bc_meta
        )

        with Transaction() as t:
            account_id, source_id = self._get_source_from_sample(t, sample_id)

            sample_repo = SampleRepo(t)
            sample_repo.update_info(account_id, source_id, sample_info, True)

            # Then, we'll get the sample and confirm that the sample's
            # barcode_meta property matches the above input
            sample = sample_repo.get_sample(account_id, source_id, sample_id)
            print(sample.barcode_meta)
            self.assertEqual(bc_meta, sample.barcode_meta)


if __name__ == '__main__':
    unittest.main()
