import pandas as pd
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.vioscreen import (
    VioscreenSession, VioscreenPercentEnergy,
    VioscreenPercentEnergyComponent)
from werkzeug.exceptions import NotFound


class VioscreenSessionRepo(BaseRepo):
    COLS = ["sessionId", "username", "protocolId", "status",
            "startDate", "endDate", "cultureCode", "created",
            "modified"]

    @property
    def _sql_cols(self):
        return ', '.join(self.COLS)

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
            cur.execute(f"""INSERT INTO ag.vioscreen_sessions (
                               {self._sql_cols}
                               )
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                           ON CONFLICT (sessionId)
                           DO UPDATE SET
                               status = EXCLUDED.status,
                               endDate = EXCLUDED.endDate,
                               modified = EXCLUDED.modified""",
                        tuple([getattr(session, attr) for attr in self.COLS]))
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
            cur.execute(f"""SELECT {self._sql_cols}
                            FROM ag.vioscreen_sessions
                            WHERE sessionId = %s""",
                        (sessionId, ))
            row = cur.fetchone()
            if row is None:
                return None
            else:
                return VioscreenSession(*row)

    def get_sessions_by_username(self, username):
        """Obtain all sessions associated with a username

        Parameters
        ----------
        username : str
            The username to search for

        Returns
        -------
        list of VioscreenSession, or None
            Instances of the observed vioscreen sessions or None if the
            username was not found
        """
        with self._transaction.cursor() as cur:
            cur.execute(f"""SELECT {self._sql_cols}
                            FROM ag.vioscreen_sessions
                            WHERE username = %s""",
                        (username, ))
            rows = cur.fetchall()
            if len(rows) == 0:
                return None
            else:
                return [VioscreenSession(*row) for row in rows]

    def get_unfinished_sessions(self):
        """Obtain the sessions for that appear incomplete

        An incomplete session is one that meets any of the following criteria:

        1) the ag.vioscreen_registry.vio_id does not exist in the
           ag.vioscreen_sessions table
        2) the ag.vioscreen_sessions.endDate is null
        3) the ag.vioscreen_sessions.status is not "Finished"

        In the event a user has multiple sessions:

        * if ALL sessions are incomplete, all sessions will be returned
        * if ANY session is complete, no sessions will be returned

        The operating model for AG/TMI has been a single session per vioscreen
        username (i.e., vio_id). As such, *if* a vioscreen vio_id has multiple
        sessions associated with it, we do not actually know right now how to
        appropriately handle a scenario where *multiple* sessions are finished.

        Returns
        -------
        list of VioscreenSession
            In the event of criteria (1) noted above, only the username
            attribute of an instance will be not None
        """
        with self._transaction.cursor() as cur:
            # criteria 1, vio_ids which are not in vioscreen_sessions
            cur.execute("""SELECT distinct(vio_id)
                           FROM ag.vioscreen_registry
                           WHERE vio_id NOT IN (
                               SELECT distinct(username)
                               FROM ag.vioscreen_sessions)""")
            not_in_vioscreen_sessions = [VioscreenSession.not_present(u[0])
                                         for u in cur.fetchall()]

            # criteria 2 and 3
            cur.execute(f"""SELECT {self._sql_cols}
                            FROM ag.vioscreen_sessions""")

            # array_agg doesn't work over these datatypes... ugh. this
            # almost certainly could be done better directly within SQL
            # but another problem for another day
            records = pd.DataFrame(cur.fetchall(), columns=self.COLS)
            incomplete_sessions = []
            for user, rows in records.groupby('username'):
                sessions = rows.apply(lambda row: VioscreenSession(*row),
                                      axis=1)
                are_incomplete = [not s.is_complete for s in sessions]
                if all(are_incomplete):
                    incomplete_sessions.extend(sessions)

            return not_in_vioscreen_sessions + incomplete_sessions

    def get_ffq_status_by_sample(self, sample_uuid):
        """Obtain the FFQ status for a given sample

        Parameters
        ----------
        sample_uuid : UUID4
            The UUID to check the status of

        Returns
        -------
        (bool, bool, str or None)
            The first index if True indicates the FFQ is completed.
            The second index if True indicates the FFQ has been started,
                but may or may not be completed.
            The third index is the exact status from Vioscreen, or None
                if there is no FFQ associated with the sample.
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT status
                           FROM ag.vioscreen_sessions vs
                           JOIN ag.vioscreen_registry vr
                               ON vs.username=vr.vio_id
                           WHERE sample_id=%s""", (sample_uuid, ))
            res = cur.fetchall()
            if len(res) == 0:
                return (False, False, None)
            elif len(res) == 1:
                status = res[0][0]
                is_complete = status == 'Finished'
                is_taken = status in ('Started', 'Review', 'Finished')
                return (is_complete, is_taken, status)
            else:
                raise ValueError("A sample should not have multiple FFQs")


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
            if cur.rowcount == 0:
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
            The observed percent energy data or None if the session ID is
            invalid
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
