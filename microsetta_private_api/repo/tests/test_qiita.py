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

    def test_lock_completed_surveys_to_barcodes(self):

        test_barcode = '000069747'
        test_barcodes = [test_barcode]

        with Transaction() as t:
            with t.dict_cursor() as cur:
                # first, find the ids for the barcode and survey we're using
                # as they are dynamically generated.
                cur.execute("select ag_login_id, source_id from "
                            "ag_login_surveys a join source_barcodes_surveys b"
                            " on a.survey_id = b.survey_id and b.barcode = "
                            "'000069747' and survey_template_id = 1")
                row = cur.fetchone()
                account_id = row[0]
                source_id = row[1]

                cur.execute("select ag_kit_barcode_id from ag_kit_barcodes "
                            "where barcode = '000069747'")
                row = cur.fetchone()

                cur.execute("SELECT * FROM source_barcodes_surveys "
                            "WHERE barcode = '000069747'")
                rows_before = cur.fetchall()

            # submit a survey for the barcode
            sar = SurveyAnswersRepo(t)
            survey_10 = {
                '22': 'Unspecified',
                '108': 'Unspecified',
                '109': 'Unspecified',
                '110': 'Unspecified',
                '111': 'Unspecified',
                '112': '1990',
                '113': 'Unspecified',
                '115': 'Unspecified',
                '148': 'Unspecified',
                '492': 'Unspecified',
                '493': 'Unspecified',
                '502': 'Male'
            }
            sar.submit_answered_survey(
                account_id,
                source_id,
                'en_US', 10, survey_10)
            t.commit()

        # now lock the barcode to the survey that was recently submitted
        with Transaction() as t:
            qiita_repo = QiitaRepo(t)
            qiita_repo.lock_completed_surveys_to_barcodes(test_barcodes)

            with t.dict_cursor() as cur:
                cur.execute("SELECT * FROM source_barcodes_surveys "
                            "WHERE barcode = '000069747'")
                rows_after = cur.fetchall()

        self.assertGreater(len(rows_after), len(rows_before))


if __name__ == '__main__':
    main()
