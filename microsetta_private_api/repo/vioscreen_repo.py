from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.vioscreen import (
    VioscreenSession, VioscreenPercentEnergy, 
    VioscreenPercentEnergyComponent)
from werkzeug.exceptions import NotFound


class VioscreenSessionRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def upsert_session(self, session):
        """Insert or update a vioscreen session

        Parameters
        ----------
        session : VioscreenSession
            The session object to insert or update

        Returns
        -------
        bool
            True if something was updated or inserted
        """
        # upsert based off of https://stackoverflow.com/a/36799500/19741
        with self._transaction.cursor() as cur:
            cur.execute("""INSERT INTO ag.vioscreen_sessions (
                               sessionId, username, protocolId, status,
                               startDate, endDate, cultureCode, created,
                               modified)
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                           ON CONFLICT (sessionId)
                           DO UPDATE SET
                               status = EXCLUDED.status,
                               endDate = EXCLUDED.endDate,
                               modified = EXCLUDED.modified""",
                        (session.sessionId, session.username,
                         session.protocolId, session.status, session.startDate,
                         session.endDate, session.cultureCode,
                         session.created, session.modified))
            return cur.rowcount == 1

    def get_session(self, sessionId):
        """Obtain a session model for a sessionId

        Parameters
        ----------
        sessionId : str
            The session ID to retrieve

        Returns
        -------
        VioscreenSession or None
            An instance of a VioscreenSession model or None if a session
            was not found
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT sessionId, username, protocolId, status,
                                  startDate, endDate, cultureCode, created,
                                  modified
                           FROM ag.vioscreen_sessions
                           WHERE sessionId = %s""",
                        (sessionId, ))
            row = cur.fetchone()
            if row is None:
                return None
            else:
                return VioscreenSession(sessionId=row[0], username=row[1],
                                        protocolId=row[2], status=row[3],
                                        startDate=row[4], endDate=row[5],
                                        cultureCode=row[6], created=row[7],
                                        modified=row[8])

class VioscreenPercentEnergyRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def insert_percent_energy(self, vioscreen_percent_energy):
        """Add percent energy data for a session

        Parameters
        ----------
        vioscreen_percent_energy : VioscreenPercentEnergy
            The observed percent energy data

        Returns
        -------
            Returns number of rows modified
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT code, amount
                           FROM ag.vioscreen_percentenergy
                           WHERE sessionId = %s""",
                        (vioscreen_percent_energy.sessionId,))
            if(cur.rowcount==0):
                energy_components = vioscreen_percent_energy.energy_components
                inserts = [(vioscreen_percent_energy.sessionId,
                            energy_component.code,
                            energy_component.amount)
                            for energy_component in energy_components]

                cur.executemany("""INSERT INTO ag.vioscreen_percentenergy
                                    (sessionId, code, amount)
                                    VALUES (%s, %s, %s)""",
                                inserts)
                return cur.rowcount
            else:
                return 0

    def get_percent_energy(self, sessionId):
        """Obtain the percent energy data for a sessionId

        Parameters
        ----------
        sessionId : str
            The session ID to retrieve data for

        Returns
        -------
        VioscreenPercentEnergy or None
            The observed percent energy data or None if the session ID is invalid
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT code, amount
                           FROM ag.vioscreen_percentenergy
                           WHERE sessionId = %s""",
                        (sessionId,))

            rows = cur.fetchall()
            if len(rows) > 0:
                codeInfos = [self._get_code_info(code) for code, _ in rows]

                components = []
                for (_, amount), codeInfo in zip(rows, codeInfos):
                    vpec = VioscreenPercentEnergyComponent(code=codeInfo[0],
                                                           description=codeInfo[1],  # noqa
                                                           short_description=codeInfo[2],  # noqa
                                                           units=codeInfo[3],
                                                           amount=amount)
                    components.append(vpec)
                return VioscreenPercentEnergy(sessionId=sessionId,
                                              energy_components=components)
            else:
                return None

    def _get_code_info(self, code):
        """Obtain the detail about a particular energy component by its code

        Parameters
        ----------
        code : str
            The code to obtain detail for

        Returns
        -------
        tuple
            The code, description, short description and units for a
            particular code

        Raises
        ------
        NotFound
            A NotFound error is raised if the code is unrecognized
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT code, description, shortDescription, units
                           FROM ag.vioscreen_percentenergy_code
                           WHERE code = %s""",
                        (code,))
            row = cur.fetchone()
            if row is not None:
                return row
            else:
                raise NotFound("No such code: " + code)

# This was ported from the american_gut_project's ag_data_access.py.
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
