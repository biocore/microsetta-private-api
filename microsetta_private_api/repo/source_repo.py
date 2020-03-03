from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.source import (Source, DECODER_HOOKS)

from werkzeug.exceptions import NotFound


# Note: By convention, this references sources by both account_id AND source_id
# This should make it more difficult to accidentally muck up sources when the
# user doesn't have the right permissions
class SourceRepo(BaseRepo):

    def __init__(self, transaction):
        super().__init__(transaction)

    read_cols = "id, account_id, " \
                "source_type, source_name, participant_email, " \
                "is_juvenile, parent_1_name, parent_2_name, " \
                "deceased_parent, date_signed, date_revoked, " \
                "assent_obtainer, age_range, description, " \
                "creation_time, update_time"

    write_cols = "id, account_id, source_type, " \
                 "source_name, participant_email, " \
                 "is_juvenile, parent_1_name, parent_2_name, " \
                 "deceased_parent, date_signed, date_revoked, " \
                 "assent_obtainer, age_range, description"

    @staticmethod
    def _row_to_source(r):
        hook = DECODER_HOOKS[r['source_type']]
        source_data = {
            'source_name': r['source_name'],
            'email': r['participant_email'],
            'is_juvenile': r['is_juvenile'],
            'parent1_name': r['parent_1_name'],
            'parent2_name': r['parent_2_name'],
            'deceased_parent': r['deceased_parent'],
            'consent_date': r['date_signed'],
            'date_revoked': r['date_revoked'],
            'assent_obtainer': r['assent_obtainer'],
            'age_range': r['age_range'],
            'source_description': r['description']
        }
        return Source(r[0], r[1], r[2], hook(source_data))

    @staticmethod
    def _source_to_row(s):
        d = s.source_data
        row = (s.id,
               s.account_id,
               s.source_type,
               getattr(d, 'name', None),
               getattr(d, 'email', None),
               getattr(d, 'is_juvenile', None),
               getattr(d, 'parent1_name', None),
               getattr(d, 'parent2_name', None),
               getattr(d, 'deceased_parent', None),
               getattr(d, 'consent_date', None),
               getattr(d, 'date_revoked', None),
               getattr(d, 'assent_obtainer', None),
               getattr(d, 'age_range', None),
               getattr(d, 'description', None))
        return row

    def get_sources_in_account(self, account_id, source_type=None):
        with self._transaction.dict_cursor() as cur:
            if source_type is None:
                cur.execute("SELECT " + SourceRepo.read_cols + " FROM "
                            "source "
                            "WHERE "
                            "source.account_id = %s AND "
                            "source.date_revoked IS NULL",
                            (account_id,))
            else:
                cur.execute("SELECT " + SourceRepo.read_cols + " FROM "
                            "source "
                            "WHERE "
                            "source.account_id = %s AND "
                            "source.source_type = %s AND "
                            "source.date_revoked IS NULL",
                            (account_id, source_type))

            rows = cur.fetchall()
            return [SourceRepo._row_to_source(x) for x in rows]

    def get_source(self, account_id, source_id):
        with self._transaction.dict_cursor() as cur:
            cur.execute("SELECT " + SourceRepo.read_cols + " FROM "
                        "source "
                        "WHERE "
                        "source.id = %s AND "
                        "source.account_id = %s AND "
                        "source.date_revoked IS NULL",
                        (source_id, account_id))
            r = cur.fetchone()
            if r is None:
                return None
            return SourceRepo._row_to_source(r)

    def update_source_data_api_fields(self, source):
        # Business Policy: For now I will let them edit only name and
        # description.  Anything else they have to recreate the source
        # Everything else they send up, we currently ignore.
        # TODO: Change yaml to remove extraneous fields?
        #  Raise exc in this layer?

        with self._transaction.cursor() as cur:
            cur.execute("UPDATE source "
                        "SET "
                        "source_name = %s, "
                        "description = %s "
                        "WHERE "
                        "source.id = %s AND "
                        "source.account_id = %s",
                        (
                            getattr(source.source_data, 'name', None),
                            getattr(source.source_data, 'description', None),
                            source.id,
                            source.account_id
                        )
                        )
            return cur.rowcount == 1

    def create_source(self, source):
        with self._transaction.cursor() as cur:
            acct_repo = AccountRepo(self._transaction)
            if acct_repo.get_account(source.account_id) is None:
                raise NotFound("No such account_id")

            cur.execute("INSERT INTO source (" + SourceRepo.write_cols + ") "
                        "VALUES("
                        "%s, %s, %s, "
                        "%s, %s, "
                        "%s, %s, %s, "
                        "%s, %s, %s, "
                        "%s, %s, %s)",
                        SourceRepo._source_to_row(source))
            return cur.rowcount == 1

    def delete_source(self, account_id, source_id):
        with self._transaction.cursor() as cur:
            cur.execute("DELETE FROM source WHERE source.id = %s AND "
                        "source.account_id = %s",
                        (source_id, account_id))
            return cur.rowcount == 1
