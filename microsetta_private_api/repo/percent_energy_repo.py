from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.vioscreen import (
    VioscreenPercentEnergy, VioscreenPercentEnergyComponent)
from werkzeug.exceptions import NotFound


class PercentEnergyRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def insert_percent_energy(self, vioscreen_percent_energy):
        """Add percent energy data for a session

        Parameters
        ----------
        vioscreen_percent_energy : VioscreenPercentEnergy
            The observed percent energy data
        """
        with self._transaction.cursor() as cur:
            energy_components = vioscreen_percent_energy.energy_components
            inserts = [(vioscreen_percent_energy.sessionId,
                        energy_component.code,
                        energy_component.amount)
                       for energy_component in energy_components]

            cur.executemany("""INSERT INTO ag.vioscreen_percentenergy
                               (sessionId, code, amount)
                               VALUES (%s, %s, %s)""",
                            inserts)

    def get_percent_energy(self, sessionId):
        """Obtain the percent energy data for a sessionId

        Parameters
        ----------
        sessionId : str
            The session ID to retrieve data for

        Returns
        -------
        VioscreenPercentEnergy
            The observed percent energy data

        Raises
        ------
        NotFound
            A NotFound is raised if the requested session does not have
            percent energy data
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
                                                           shortDescription=codeInfo[2],  # noqa
                                                           units=codeInfo[3],
                                                           amount=amount)
                    components.append(vpec)
                return VioscreenPercentEnergy(sessionId=sessionId,
                                              energy_components=components)
            else:
                raise NotFound("No such session id: " + sessionId)

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
        with self._transaction.cursor as cur:
            cur.execute("""SELECT code, description, shortDescription, units
                           FROM ag.vioscreen_percentenergy_code
                           WHERE code = %s""",
                        (code,))
            row = cur.fetchone()
            if row is not None:
                return row
            else:
                raise NotFound("No such code: " + code)
