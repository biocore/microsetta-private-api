from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.vioscreen import VioscreenPercentEnergy, VioscreenPercentEnergyComponent
from werkzeug.exceptions import NotFound


class PercentEnergyRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def insert_percent_energy(self, vioscreen_percent_energy):
        with self._transaction.cursor() as cur:
            inserts = [(vioscreen_percent_energy.sessionId, energy_component.code, energy_component.amount)
                       for energy_component in vioscreen_percent_energy.energy_components]
            cur.executemany(
                "INSERT INTO ag.vioscreen_percentenergy (sessionId, code, amount) VALUES (%s, %s, %s)", inserts)

    def get_percent_energy(self, sessionId):
        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT sessionId, code, amount FROM ag.vioscreen_percentenergy WHERE sessionId = %s", (sessionId,))
            rows = cur.fetchall()
            if len(rows) > 0:
                codeInfos = [self._get_code_info(row[1]) for row in rows]
                return VioscreenPercentEnergy(sessionId=sessionId, energy_components=[VioscreenPercentEnergyComponent(codeInfo[0], codeInfo[1], codeInfo[2], codeInfo[3], row[2]) for row, codeInfo in zip(rows, codeInfos)])
            else:
                raise NotFound("No such session id: " + sessionId)

    def _insert_code_info(self):
        # only needs to be run once to populate ag.vioscreen_percentenergy_code
        # to fetch data when running get_percent_energy -> _get_code_info
        with self._transaction.cursor() as cur:
            inserts = [
                (
                    "%protein",
                    "Percent of calories from Protein",
                    "Protein",
                    "%"
                ),
                (
                    "%fat",
                    "Percent of calories from Fat",
                    "Fat",
                    "%"
                ),
                (
                    "%carbo",
                    "Percent of calories from Carbohydrate",
                    "Carbohydrate",
                    "%"
                ),
                (
                    "%alcohol",
                    "Percent of calories from Alcohol",
                    "Alcohol",
                    "%"
                ),
                (
                    "%sfatot",
                    "Percent of calories from Saturated Fat",
                    "Saturated Fat",
                    "%"
                ),
                (
                    "%mfatot",
                    "Percent of calories from Monounsaturated Fat",
                    "Monounsaturated Fat",
                    "%"
                ),
                (
                    "%pfatot",
                    "Percent of calories from Polyunsaturated Fat",
                    "Polyunsaturated Fat",
                    "%"
                ),
                (
                    "%adsugtot",
                    "Percent of calories from Added Sugar",
                    "Added Sugar",
                    "%"
                )
            ]
            cur.executemany(
                "INSERT INTO ag.vioscreen_percentenergy_code (code, description, shortDescription, units) VALUES (%s, %s, %s, %s)", inserts)

    def _get_code_info(self, code):
        with self._transaction.cursor as cur:
            cur.execute(
                "SELECT * FROM ag.vioscreen_percentenergy_code WHERE code = %s", (code,))
            row = cur.fetchone()
            if row is not None:
                return row
            else:
                raise NotFound("No such code: " + code)
