from microsetta_private_api.repo.base_repo import BaseRepo
from werkzeug.exceptions import NotFound


# This was ported from the american_gut_project's ag_data_access.py.
class VioscreenRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def update_vioscreen_status(self, survey_id, status):
        # TODO:  Who is checking permissions for this?
        #  Where should other encrypted fields of the vioscreen information be
        #  validated?  Note that encryption != authentication !!
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

    def get_vioscreen_status(self, survey_id):
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
                raise NotFound("No such survey id: " + survey_id)
            return row[0]
