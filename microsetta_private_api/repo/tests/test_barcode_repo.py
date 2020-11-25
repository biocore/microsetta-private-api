from microsetta_private_api.api.tests.test_integration import \
    _create_mock_kit, _remove_mock_kit
from microsetta_private_api.model.preparation import Preparation
from microsetta_private_api.repo.barcode_repo import BarcodeRepo
import unittest

from microsetta_private_api.repo.transaction import Transaction

BC1 = "77777777"
BC2 = "88888888"
BC3 = "99999999"
S1 = '99999999-aaaa-aaaa-aaaa-bbbbcccccccc'
S2 = '99999999-aaaa-aaaa-aaaa-bbbbcccccccd'
S3 = '99999999-aaaa-aaaa-aaaa-bbbbccccccce'

FAKE_BARCODES = [BC1, BC2, BC3]
FAKE_SAMPLES = [S1, S2, S3]


class BarcodeTests(unittest.TestCase):
    def setUp(self):
        with Transaction() as t:
            _create_mock_kit(t,
                             barcodes=FAKE_BARCODES,
                             mock_sample_ids=FAKE_SAMPLES)
            t.commit()

    def tearDown(self):
        with Transaction() as t:
            _remove_mock_kit(t,
                             barcodes=FAKE_BARCODES,
                             mock_sample_ids=FAKE_SAMPLES)
            t.commit()

    def test_upsert_prep(self):
        with Transaction() as t:
            r = BarcodeRepo(t)
            h = Preparation(
                BC1,
                99999999,
                "16S",
                127
            )

            self.assertEqual(
                len(r.list_preparations(BC1)),
                0,
                "Preexisting Barcode Prep!?"
            )

            r.upsert_preparation(h)
            self.assertEqual(
                len(r.list_preparations(BC1)),
                1,
                "Failed to insert preparation"
            )

            h.barcode = BC2
            r.upsert_preparation(h)
            self.assertEqual(
                len(r.list_preparations(BC1)),
                1,
                "Inserting for BC2 removed from BC1 (but many-to-many)"
            )
            self.assertEqual(
                len(r.list_preparations(BC2)),
                1,
                "Failed to insert preparation (not in bc2)"
            )

            g = r.list_preparations(BC2)[0]
            self.assertDictEqual(h.to_api(), g.to_api())

            t.rollback()

    def test_add_preps(self):
        with Transaction() as t:
            r = BarcodeRepo(t)
            for i in range(10):
                h = Preparation(
                    BC3,
                    99999990 + i,
                    "16S",
                    127
                )

                r.upsert_preparation(h)
            self.assertEqual(len(r.list_preparations(BC1)), 0)
            self.assertEqual(len(r.list_preparations(BC2)), 0)
            self.assertEqual(len(r.list_preparations(BC3)), 10)
            t.rollback()

    def test_del_prep(self):
        with Transaction() as t:
            r = BarcodeRepo(t)
            h = Preparation(BC3, 99999999, "WGS", 57182302)

            self.assertEqual(r.delete_preparation(BC3, 99999999), 0,
                             "Successfully deleted nonexisted prep?")
            r.upsert_preparation(h)
            self.assertEqual(r.delete_preparation(BC3, 99999999), 1,
                             "Failed to delete prep")
            self.assertEqual(r.delete_preparation(BC3, 99999999), 0,
                             "Successfully deleted same prep twice?")
            t.rollback()
