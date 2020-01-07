from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.source import (HumanInfo, CanineInfo,
                                                 EnvironmentInfo, Source,
                                                 DECODER_HOOKS)
import json
from microsetta_private_api.util.util import json_converter


# Note: By convention, this references sources by both account_id AND source_id
# This should make it more difficult to accidentally muck up sources when the
# user doesn't have the right permissions
class SourceRepo(BaseRepo):

    def __init__(self, transaction):
        super().__init__(transaction)

    read_cols = "id, account_id, source_type, source_data, " \
                "creation_time, update_time"
    write_cols = "id, account_id, source_type, source_data"

    @staticmethod
    def _row_to_source(r):
        hook = DECODER_HOOKS[r[2]]
        return Source(r[0], r[1], r[2], json.loads(r[3], object_hook=hook))

    @staticmethod
    def _source_to_row(s):
        row = (s.id, s.account_id, s.source_type,
               json.dumps(s.source_data, default=json_converter))
        return row

    def get_sources_in_account(self, account_id, source_type=None):
        with self._transaction.cursor() as cur:
            if source_type is None:
                cur.execute("SELECT " + SourceRepo.read_cols + " FROM "
                            "source "
                            "WHERE "
                            "source.account_id = %s", (account_id,))
            else:
                cur.execute("SELECT " + SourceRepo.read_cols + " FROM "
                            "source "
                            "WHERE "
                            "source.account_id = %s AND "
                            "source.source_type = %s",
                            (account_id, source_type))

            rows = cur.fetchall()
            return [SourceRepo._row_to_source(x) for x in rows]

    def get_source(self, account_id, source_id):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT " + SourceRepo.read_cols + " FROM "
                        "source "
                        "WHERE "
                        "source.id = %s AND "
                        "source.account_id = %s", (source_id, account_id))
            r = cur.fetchone()
            if r is None:
                return None
            return SourceRepo._row_to_source(r)

    def update_source_data(self, source):
        with self._transaction.cursor() as cur:
            cur.execute("UPDATE source "
                        "SET "
                        "source_data = %s "
                        "WHERE "
                        "source.id = %s AND "
                        "source.account_id = %s",
                        (json.dumps(source.source_data),
                         source.id, source.account_id)
                        )
            return cur.rowcount == 1

    def create_source(self, source):
        with self._transaction.cursor() as cur:
            cur.execute("INSERT INTO source (" + SourceRepo.write_cols + ") "
                        "VALUES(%s, %s, %s, %s)",
                        SourceRepo._source_to_row(source))
            return cur.rowcount == 1

    def delete_source(self, account_id, source_id):
        with self._transaction.cursor() as cur:
            cur.execute("DELETE FROM source WHERE source.id = %s AND "
                        "source.account_id=%s",
                        (source_id, account_id))
            return cur.rowcount == 1
