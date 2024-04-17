from unittest import TestCase, main
from unittest.mock import patch
from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo
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

    def test_lock_sample_to_survey(self):
        test_account_id = 'ed5ab96f-fc55-ead5-e040-8a80115d1c4b'
        test_source_id = '1d7138e7-f1a7-421b-8c58-9245b2bc343e'
        test_sample_id = 'ed5ab96f-fc57-ead5-e040-8a80115d1c4b'
        test_barcode = '000012914'
        test_barcodes = [test_barcode]
        test_survey_id = '000a1da7d9d7e35b'

        with Transaction() as t:
            answers_repo = SurveyAnswersRepo(t)
            answered_survey_ids = answers_repo.list_answered_surveys_by_sample(
                test_account_id, test_source_id, test_sample_id)

            for curr_answered_survey_id in answered_survey_ids:
                answers_repo.dissociate_answered_survey_from_sample(
                    test_account_id, test_source_id,
                    test_sample_id, curr_answered_survey_id)

            t.commit()

        with Transaction() as t:
            with t.cursor() as cur:
                for sample_barcode in test_barcodes:
                    cur.execute("SELECT * FROM ag.source_barcodes_surveys "
                                "WHERE barcode = %s AND survey_id = %s",
                                (sample_barcode, test_survey_id))
                    barcode_does_not_exist_before = cur.fetchone() is None

                    qiita_repo = QiitaRepo(t)
                    qiita_repo.lock_sample_to_survey(test_barcodes)

                    cur.execute("SELECT * FROM source_barcodes_surveys "
                                "WHERE barcode=%s AND survey_id=%s",
                                (sample_barcode, test_survey_id))
                    inserted_found = cur.fetchone()
                    barcode_exists_after = inserted_found is not None

                    self.assertTrue(barcode_does_not_exist_before)
                    self.assertTrue(barcode_exists_after)


if __name__ == '__main__':
    main()
