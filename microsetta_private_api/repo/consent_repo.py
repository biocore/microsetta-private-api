from microsetta_private_api.model.consent import ConsentDocument
from microsetta_private_api.model.consent import ConsentSignature
from microsetta_private_api.repo.base_repo import BaseRepo
from werkzeug.exceptions import NotFound
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.exceptions import RepoException


def _consent_document_to_row(s):
    row = (s.consent_id,
           s.consent_type,
           s.locale,
           s.date_time,
           s.consent_content,
           s.account_id,
           s.reconsent)
    return row


def _row_to_consent_document(r):
    return ConsentDocument(
        r["consent_id"],
        r["consent_type"],
        r["locale"],
        r["date_time"],
        r["consent_content"],
        getattr(r, 'account_id', None),
        r["reconsent_required"])


def _consent_signature_to_row(s):
    row = (s.signature_id,
           s.consent_id,
           s.source_id,
           s.date_time,
           getattr(s, 'parent_1_name', None),
           getattr(s, 'parent_2_name', None),
           getattr(s, 'deceased_parent', None),
           getattr(s, 'assent_obtainer', None),
           getattr(s, 'assent_id', None)
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
        r["assent_obtainer"],
        r["assent_id"],
        "",
        ""
    )


class ConsentRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    doc_read_cols = "distinct on (consent_type) consent_id, consent_type, " \
                    "locale, date_time, consent_content, reconsent_required" \

    doc_write_cols = "consent_id, consent_type, " \
                     "locale, date_time, consent_content, " \
                     "account_id, reconsent_required"

    signature_read_cols = "signature_id, consent_type, " \
                          "consent_audit.date_time AS sign_date, "\
                          "reconsent_required"

    signature_write_cols = "signature_id, consent_id, " \
                           "source_id, date_time, parent_1_name, " \
                           "parent_2_name, deceased_parent, assent_obtainer, "\
                           "assent_id"

    def create_doc(self, consent):
        with self._transaction.dict_cursor() as cur:
            cur.execute("INSERT INTO ag.consent_documents (" +
                        self.doc_write_cols + ") "
                        "VALUES( %s, %s, %s, %s, %s, "
                        "%s, %s) ",
                        _consent_document_to_row(consent))
            return cur.rowcount == 1

    def get_all_consent_documents(self, tag):
        consent_docs = []

        with self._transaction.dict_cursor() as cur:
            cur.execute("SELECT " + self.doc_read_cols + " FROM "
                        "consent_documents WHERE locale = %s"
                        " ORDER BY consent_type DESC, "
                        "date_time DESC", (tag,))

            r = cur.fetchall()
            consent_docs = [_row_to_consent_document(row) for row in r]

        return consent_docs

    def get_consent_document(self, consent_id):
        with self._transaction.dict_cursor() as cur:
            cur.execute("SELECT " + self.doc_read_cols + " FROM "
                        "ag.consent_documents WHERE "
                        "ag.consent_documents.consent_id = %s", (consent_id,))
            r = cur.fetchone()
            if r is None:
                return None
            else:
                return _row_to_consent_document(r)

    def is_consent_required(self, source_id, consent_type):
        with self._transaction.dict_cursor() as cur:
            cur.execute("SELECT " + self.signature_read_cols + " FROM "
                        "ag.consent_audit INNER JOIN ag.consent_documents "
                        "USING (consent_id) "
                        "WHERE consent_audit.source_id = %s and "
                        "consent_documents.consent_type "
                        "LIKE %s ORDER BY sign_date DESC",
                        (source_id, ('%' + consent_type + '%')))

            r = cur.fetchone()
            if r is None:
                return True
            elif r['reconsent_required']:
                consent_doc_type = r["consent_type"]
                cur.execute("SELECT date_time FROM "
                            "ag.consent_documents WHERE consent_type = %s "
                            "ORDER BY date_time DESC LIMIT 1",
                            (consent_doc_type,))

                s = cur.fetchone()
                if s is None:
                    return True
                else:
                    sign_date = r["sign_date"]
                    doc_date = s["date_time"]

                    return doc_date > sign_date
            else:
                return r["reconsent_required"]

    def _is_valid_consent_sign(self, sign, doc):
        res = True

        parent_1 = sign.parent_1_name
        parent_2 = sign.parent_2_name
        obtainer = sign.assent_obtainer
        deceased = sign.deceased_parent

        con = ["parent", "child", "adolescent"]

        for v in con:
            if v in doc.consent_type:
                if parent_1 is None:
                    res = False
                    return res

        if "adult" in doc.consent_type:
            for value in (parent_1, parent_2, obtainer, deceased):
                if value is not None:
                    res = False
                    return res

        return res

    def sign_consent(self, account_id, consent_signature):
        with self._transaction.dict_cursor() as cur:
            consentRepo = ConsentRepo(self._transaction)
            consent_id = consent_signature.consent_id

            consent_doc = consentRepo.get_consent_document(consent_id)

            if consent_doc is None:
                raise NotFound("Consent Document does not exist!")

            sourceRepo = SourceRepo(self._transaction)
            source_id = consent_signature.source_id

            if sourceRepo.get_source(account_id, source_id) is None:
                raise NotFound("Source does not exist!")

            if not self._is_valid_consent_sign(consent_signature, consent_doc):
                raise NotFound("Invalid consent signature!")

            cur.execute("INSERT INTO consent_audit (" +
                        self.signature_write_cols + ") "
                        "VALUES("
                        "%s, %s, %s, "
                        "%s, %s, %s, "
                        "%s, %s, %s)",
                        _consent_signature_to_row(consent_signature))
            return cur.rowcount == 1

    def scrub(self, account_id, source_id):
        with self._transaction.dict_cursor() as cur:
            source_repo = SourceRepo(self._transaction)
            if source_repo.get_source(account_id, source_id) is None:
                raise NotFound("Source does not exist")

            parent_1_name = "scrubbed"
            parent_2_name = "scrubbed"
            deceased_parent = None
            assent_obtainer = "scrubbed"

            cur.execute("UPDATE ag.consent_audit "
                        "SET parent_1_name = %s, "
                        "parent_2_name = %s, "
                        "deceased_parent = %s, "
                        "assent_obtainer = %s, "
                        "date_revoked = NOW() "
                        "WHERE source_id = %s",
                        (parent_1_name, parent_2_name,
                         deceased_parent, assent_obtainer,
                         source_id,))

        return True

    def get_latest_signed_consent(self, source_id, consent_type):
        if consent_type == 'data':
            consent_type_like = "%_data"
        elif consent_type == 'biospecimen':
            consent_type_like = "%_biospecimen"
        else:
            raise RepoException("Unknown consent type: %s" % consent_type)

        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT ca.signature_id, ca.consent_id, ca.source_id, "
                "ca.date_time, ca.parent_1_name, ca.parent_2_name, "
                "ca.deceased_parent, ca.assent_obtainer, ca.assent_id "
                "FROM ag.consent_audit ca "
                "INNER JOIN ag.consent_documents cd "
                "ON ca.consent_id = cd.consent_id "
                "INNER JOIN ag.source s "
                "ON ca.source_id = s.id "
                "WHERE ca.source_id = %s AND cd.consent_type LIKE %s "
                "ORDER BY ca.date_time DESC LIMIT 1",
                (source_id, consent_type_like)
            )
            row = cur.fetchone()
            if row is None:
                return None
            else:
                consent_signature = _row_to_consent_signature(row)

                survey_doc = self.get_consent_document(
                    consent_signature.consent_id
                )
                consent_signature.consent_content = survey_doc.consent_content

                if consent_signature.assent_id is not None:
                    assent_doc = self.get_consent_document(
                        consent_signature.assent_id
                    )
                    consent_signature.assent_content =\
                        assent_doc.consent_content

                return consent_signature
