from microsetta_private_api.model.consent import ConsentDocument
from microsetta_private_api.model.consent import ConsentSignature
from microsetta_private_api.repo.base_repo import BaseRepo
from werkzeug.exceptions import NotFound
from microsetta_private_api.repo.source_repo import SourceRepo


def _consent_document_to_row(s):
    row = (s.consent_id,
           s.consent_type,
           s.locale,
           s.date_time,
           s.consent_content,
           s.account_id)
    return row


def _row_to_consent_document(r):
    return ConsentDocument(
        r["consent_id"],
        r["consent_type"],
        r["locale"],
        r["date_time"],
        r["consent_content"],
        getattr(r, 'account_id', None))


def _consent_signature_to_row(s):
    row = (s.signature_id,
           s.consent_id,
           s.source_id,
           s.date_time,
           getattr(s, 'parent_1_name', None),
           getattr(s, 'parent_2_name', None),
           getattr(s, 'deceased_parent', None),
           getattr(s, 'assent_obtainer', None)
           )

    return row


def _row_to_consent_signature(r):
    return ConsentSignature(
        r["signature_id"],
        r["consent_id"],
        r["source_id"],
        r["date_time"],
        r["parent_1_name"],
        r["parent_2_name"],
        r["deceased_parent"],
        r["assent_obtainer"])


class ConsentRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    doc_read_cols = "distinct on (consent_type) consent_id, consent_type, " \
                    "locale, date_time, consent_content" \

    doc_write_cols = "consent_id, consent_type, " \
                     "locale, date_time, consent_content, " \
                     "account_id"

    signature_read_cols = "signature_id, consent_type, " \
                          "consent_audit.date_time AS sign_date, "\
                          "reconsent_required"

    signature_write_cols = "signature_id, consent_id, " \
                           "source_id, date_time, parent_1_name, " \
                           "parent_2_name, deceased_parent, assent_obtainer"

    def get_all_consent_documents(self):
        consent_docs = []

        with self._transaction.dict_cursor() as cur:
            cur.execute("SELECT " + ConsentRepo.doc_read_cols + " FROM "
                        "consent_documents ORDER BY consent_type DESC, "
                        "date_time DESC")

            r = cur.fetchall()

            for index in range(0, len(r)):
                consent_docs.append(_row_to_consent_document(r[index]))

        return consent_docs

    def get_consent_document(self, consent_id):
        with self._transaction.dict_cursor() as cur:
            cur.execute("SELECT " + ConsentRepo.doc_read_cols + " FROM "
                        "consent_documents WHERE "
                        "consent_documents.consent_id = %s", (consent_id,))
            r = cur.fetchone()
            if r is None:
                return None
            else:
                return _row_to_consent_document(r)

    def is_consent_required(self, source_id, consent_type):
        print(consent_type)

        with self._transaction.dict_cursor() as cur:
            cur.execute("SELECT " + ConsentRepo.signature_read_cols + " FROM "
                        "ag.consent_audit INNER JOIN "
                        "ag.consent_documents ON "
                        "consent_audit.consent_id = consent_documents.consent_id "
                        "WHERE consent_audit.source_id = %s and "
                        "consent_documents.consent_type "
                        "LIKE %s ORDER BY sign_date DESC",
                        (source_id, ('%' + consent_type + '%')))

            r = cur.fetchone()
            if r is None:
                return True
            elif r['reconsent_required'] == 0:
                return False
            else:
                consent_doc_type = r["consent_type"]
                cur.execute("SELECT date_time FROM "
                            "consent_documents WHERE consent_type = %s "
                            "ORDER BY date_time DESC LIMIT 1",
                            (consent_doc_type,))

                s = cur.fetchone()
                if s is None:
                    return True
                else:
                    sign_date = r["sign_date"]
                    doc_date = s["date_time"]

                    if doc_date > sign_date:
                        return True
                    else:
                        return False

    def sign_consent(self, account_id, consent_signature):
        with self._transaction.dict_cursor() as cur:
            consentRepo = ConsentRepo(self._transaction)
            consent_id = consent_signature.consent_id
            if consentRepo.get_consent_document(consent_id) is None:
                raise NotFound("Consent Document does not exist!")

            sourceRepo = SourceRepo(self._transaction)
            source_id = consent_signature.source_id
            if sourceRepo.get_source(account_id, source_id) is None:
                raise NotFound("Source does not exist!")

            cur.execute("INSERT INTO consent_audit (" +
                        ConsentRepo.signature_write_cols + ") "
                        "VALUES("
                        "%s, %s, %s, "
                        "%s, %s, %s, "
                        "%s, %s)",
                        _consent_signature_to_row(consent_signature))

            return cur.rowcount == 1
