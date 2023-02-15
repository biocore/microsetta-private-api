import unittest
from datetime import datetime
from werkzeug.exceptions import NotFound
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.consent_repo import ConsentRepo
from microsetta_private_api.model.consent import ConsentDocument, \
    ConsentSignature
from microsetta_private_api.model.source import HumanInfo, Source
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.model.account import Account
from microsetta_private_api.model.address import Address
import uuid

SOURCE_ID = '4affcca2-1ca4-480d-88a4-b6dd2a3ba55b'
INVALID_DOC_ID = 'ecabc635-3df8-49ee-ae19-db3db03c7393'
ACCT_ID = '500d79fc-99e8-4c48-b911-a72005c9e0c9'

DATA_DOC = {"consent_type": "Adult Consent - Data",
            "locale": "en_US",
            "consent": "Adult Data Consent",
            "reconsent": '1'
            }

BIO_DOC = {"consent_type": "Adult Consent - Biospecimen",
           "locale": "en_US",
           "consent": "Adult Biospecimen Consent",
           "reconsent": '1'
           }

CORRECT_SIGN = {"source_id": SOURCE_ID,
                "date_time": datetime.now(),
                "parent_1_name": None,
                "parent_2_name": None,
                "deceased__parent":  None,
                "assent_obtainer": None,
                "age_range": "18-plus"
                }

INVALID_SOURCE_SIGN = {"signature_id": '21cac84d-951d-470e-a001-463d911f1222',
                       "source_id": 'ecabc635-3df8-49ee-ae19-db3db03c7883',
                       "date_time": datetime.now(),
                       "parent_1_name": "father",
                       "parent_2_name": 'mother',
                       "deceased__parent": "false",
                       "assent_obtainer": "demo"
                       }

INVALID_SIGN = {"source_id": SOURCE_ID,
                "consent_id": 'ecabc635-3df8-49ee-ae19-db3db03c7393',
                "date_time": datetime.now(),
                "parent_1_name": "father",
                "parent_2_name": 'mother',
                "deceased__parent": "false",
                "assent_obtainer": "demo"
                }

MALFORMED_SIGN = {"source_id": SOURCE_ID,
                  "date_time": datetime.now(),
                  "parent_1_name": "demo",
                  "parent_2_name": "demo",
                  "deceased__parent": "false",
                  "assent_obtainer": "demo"
                  }


class ConsentRepoTests(unittest.TestCase):
    # We can't safely assume that consent document IDs will be stable over
    # time, so we'll collect them from the database during test setup.
    def setUp(self):
        with Transaction() as t:
            with t.dict_cursor() as cur:
                cur.execute(
                    "SELECT consent_id "
                    "FROM ag.consent_documents "
                    "WHERE locale = 'en_US' AND consent_type = 'adult_data' "
                    "ORDER BY date_time DESC LIMIT 1"
                )
                row = cur.fetchone()
                self.adult_data_consent = row['consent_id']

                cur.execute(
                    "SELECT consent_id "
                    "FROM ag.consent_documents "
                    "WHERE locale = 'en_US' AND consent_type = 'adult_biospecimen' "
                    "ORDER BY date_time DESC LIMIT 1"
                )
                row = cur.fetchone()
                self.adult_bio_consent = row['consent_id']

                cur.execute(
                    "SELECT consent_id "
                    "FROM ag.consent_documents "
                    "WHERE locale = 'en_US' AND consent_type = 'child_data' "
                    "ORDER BY date_time DESC LIMIT 1"
                )
                row = cur.fetchone()
                self.child_data_consent = row['consent_id']

    def test_sign_data_consent(self):
        with Transaction() as t:
            consent_repo = ConsentRepo(t)
            acct_repo = AccountRepo(t)
            source_repo = SourceRepo(t)

            # Set up test account with sources
            acc = Account(ACCT_ID,
                          "foo@baz.com",
                          "standard",
                          "https://MOCKUNITTEST.com",
                          "1234ThisIsNotARealSub",
                          "Dan",
                          "H",
                          Address(
                              "123 Dan Lane",
                              "Danville",
                              "CA",
                              12345,
                              "US"
                          ),
                          "en_US",
                          True)
            acct_repo.create_account(acc)

            source = CORRECT_SIGN["source_id"]
            source_repo.create_source(Source(
                source,
                ACCT_ID,
                Source.SOURCE_TYPE_HUMAN,
                "Dummy",
                HumanInfo(False, None, None,
                          False, datetime.utcnow(), None,
                          "Mr. Obtainer",
                          "18-plus")
            ))

            CORRECT_SIGN.update({"consent_id": self.adult_data_consent})
            signature_id = str(uuid.uuid4())
            sign = ConsentSignature.from_dict(
                CORRECT_SIGN,
                source,
                signature_id
            )
            res = consent_repo.sign_consent(ACCT_ID, sign)
            self.assertTrue(res)

    def test_sign_biospecimen_consent(self):
        with Transaction() as t:
            consent_repo = ConsentRepo(t)
            acct_repo = AccountRepo(t)

            # Set up test account with sources
            acc = Account(ACCT_ID,
                          "foo@baz.com",
                          "standard",
                          "https://MOCKUNITTEST.com",
                          "1234ThisIsNotARealSub",
                          "Dan",
                          "H",
                          Address(
                              "123 Dan Lane",
                              "Danville",
                              "CA",
                              12345,
                              "US"
                          ),
                          "en_US",
                          True)
            acct_repo.create_account(acc)

            source_repo = SourceRepo(t)
            source = CORRECT_SIGN["source_id"]

            source_repo.create_source(Source(
                source,
                ACCT_ID,
                Source.SOURCE_TYPE_HUMAN,
                "Dummy",
                HumanInfo(False, None, None,
                          False, datetime.utcnow(), None,
                          "Mr. Obtainer",
                          "18-plus")
            ))

            CORRECT_SIGN.update({"consent_id": self.adult_bio_consent})
            signature_id = str(uuid.uuid4())
            sign = ConsentSignature.from_dict(
                CORRECT_SIGN,
                source,
                signature_id
            )
            res = consent_repo.sign_consent(ACCT_ID, sign)
            self.assertTrue(res)

    def test_sign_invalid_source_consent(self):
        with Transaction() as t:
            consent_repo = ConsentRepo(t)
            src = INVALID_SOURCE_SIGN["source_id"]
            INVALID_SOURCE_SIGN.update({"consent_id": self.child_data_consent})
            signature_id = str(uuid.uuid4())
            sign = ConsentSignature.from_dict(
                INVALID_SOURCE_SIGN,
                src,
                signature_id
            )
            with self.assertRaises(NotFound):
                consent_repo.sign_consent(ACCT_ID, sign)

    def test_sign_invalid_consent(self):
        with Transaction() as t:
            consent_repo = ConsentRepo(t)
            source = INVALID_SIGN["source_id"]
            signature_id = str(uuid.uuid4())
            sign = ConsentSignature.from_dict(
                INVALID_SIGN,
                source,
                signature_id
            )
            with self.assertRaises(NotFound):
                consent_repo.sign_consent(ACCT_ID, sign)

    def test_sign_malformed_data(self):
        with Transaction() as t:
            consent_repo = ConsentRepo(t)
            source = MALFORMED_SIGN["source_id"]
            MALFORMED_SIGN.update({"consent_id": self.adult_data_consent})
            con = self.adult_data_consent
            sign = ConsentSignature.from_dict(MALFORMED_SIGN, source, con)
            with self.assertRaises(NotFound):
                consent_repo.sign_consent(ACCT_ID, sign)

    def test_fetch_invalid_document(self):
        with Transaction() as t:
            consent_repo = ConsentRepo(t)
            res = consent_repo.get_consent_document(INVALID_DOC_ID)
            self.assertEqual(None, res)

    def test_check_invalid_consent(self):
        with Transaction() as t:
            consent_repo = ConsentRepo(t)
            source = INVALID_SOURCE_SIGN['source_id']
            res = consent_repo.is_consent_required(source, "Data")
            self.assertTrue(res)

    def test_get_latest_signed_consent(self):
        with Transaction() as t:
            consent_repo = ConsentRepo(t)
            acct_repo = AccountRepo(t)
            source_repo = SourceRepo(t)

            # Set up test account with sources
            acc = Account(ACCT_ID,
                          "foo@baz.com",
                          "standard",
                          "https://MOCKUNITTEST.com",
                          "1234ThisIsNotARealSub",
                          "Dan",
                          "H",
                          Address(
                              "123 Dan Lane",
                              "Danville",
                              "CA",
                              12345,
                              "US"
                          ),
                          "en_US",
                          True)
            acct_repo.create_account(acc)

            source = CORRECT_SIGN["source_id"]
            source_repo.create_source(Source(
                source,
                ACCT_ID,
                Source.SOURCE_TYPE_HUMAN,
                "Dummy",
                HumanInfo(False, None, None,
                          False, datetime.utcnow(), None,
                          "Mr. Obtainer",
                          "18-plus")
            ))

            CORRECT_SIGN.update({"consent_id": self.adult_data_consent})
            signature_id = str(uuid.uuid4())
            sign = ConsentSignature.from_dict(
                CORRECT_SIGN,
                source,
                signature_id
            )
            res = consent_repo.sign_consent(ACCT_ID, sign)
            self.assertTrue(res)

            res = consent_repo.get_latest_signed_consent(source, "data")
            self.assertEqual(res.consent_id, self.adult_data_consent)


if __name__ == '__main__':
    unittest.main()
