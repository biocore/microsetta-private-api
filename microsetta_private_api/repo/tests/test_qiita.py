from unittest import TestCase, main
from unittest.mock import patch
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.qiita_repo import QiitaRepo


class FakeColumns:
    def __init__(self, columns):
        self._columns = columns

    def __getitem__(self, thing):
        pass

    def __iter__(self):
        return iter(self._columns)


class FakeFrame:
    def __init__(self, columns):
        self.columns = FakeColumns(columns)

    def to_json(self, *args, **kwargs):
        return "[]"

    def __len__(self):
        return 1


class AdminTests(TestCase):
    @patch('microsetta_private_api.qiita.qclient.get')
    @patch('microsetta_private_api.qiita.qclient.http_patch')
    @patch('microsetta_private_api.repo.qiita_repo.retrieve_metadata')
    def test_push_metadata_to_qiita(self, test_retrieve_metadata,
                                    test_http_patch, test_get):
        # fake codes
        fecal_valid_barcode = '0x0004801'
        oral_valid_barcode = '0x0015213'
        skin_valid_barcode = '0x0027751'

        blank = 'foobarblank'
        test_barcodes = [fecal_valid_barcode,
                         oral_valid_barcode,
                         skin_valid_barcode]

        failure = [{skin_valid_barcode: ("This barcode is not "
                                         "associated with any surveys "
                                         "matching this template id")}, ]
        # one inserts, one fails
        # using side_effect to change returns
        # https://stackoverflow.com/a/24897297
        test_get.side_effect = [
            ['foo.' + blank,
             'foo.' + oral_valid_barcode, ],  # first .get for samples
            {'categories': ['a', 'b', 'c', 'd']},  # second .get for categories
        ]
        test_http_patch.return_value = []
        test_retrieve_metadata.return_value = (
            FakeFrame(['a', 'b', 'c', 'd']),
            failure
        )

        with Transaction() as t:
            qiita_repo = QiitaRepo(t)
            success, failed = qiita_repo.push_metadata_to_qiita(test_barcodes)

            self.assertEqual(success, 1)
            self.assertEqual(failed, [
                {skin_valid_barcode: ("This barcode is not "
                                      "associated with any surveys "
                                      "matching this template id")}])


if __name__ == '__main__':
    main()
