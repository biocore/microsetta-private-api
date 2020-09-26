from microsetta_private_api.repo.base_repo import BaseRepo
from werkzeug.exceptions import NotFound


# This was ported from the american_gut_project's ag_data_access.py.
from microsetta_private_api.repo.source_repo import SourceRepo


class VioscreenRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def upsert_vioscreen_status(self, account_id, source_id,
                                survey_id, status):
        # Check current survey status
        cur_status = self.get_vioscreen_status(account_id,
                                               source_id,
                                               survey_id)

        # If there is no status, insert a row.
        if cur_status is None:
            with self._transaction.cursor() as cur:
                cur.execute(
                    "INSERT INTO ag_login_surveys("
                    "ag_login_id, survey_id, vioscreen_status, source_id) "
                    "VALUES(%s, %s, %s, %s)",
                    (account_id, survey_id, status, source_id)
                )
        else:
            # Else, upsert a status.
            with self._transaction.cursor() as cur:
                cur.execute(
                    "UPDATE "
                    "ag_login_surveys "
                    "SET "
                    "vioscreen_status = %s "
                    "WHERE "
                    "survey_id = %s",
                    (status, survey_id)
                )
                if cur.rowcount != 1:
                    raise NotFound("No such survey id: " + survey_id)

    def get_vioscreen_status(self, account_id, source_id, survey_id):
        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT "
                "vioscreen_status "
                "FROM "
                "ag.ag_login_surveys "
                "WHERE "
                "ag_login_id = %s AND "
                "source_id = %s AND "
                "survey_id = %s",
                (account_id, source_id, survey_id,)
            )
            row = cur.fetchone()
            if row is None:
                return None
            return row[0]

    def _get_vioscreen_status(self, survey_id):
        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT "
                "vioscreen_status "
                "FROM "
                "ag.ag_login_surveys "
                "WHERE "
                "survey_id = %s",
                (survey_id,)
            )
            row = cur.fetchone()
            if row is None:
                return None
            return row[0]
