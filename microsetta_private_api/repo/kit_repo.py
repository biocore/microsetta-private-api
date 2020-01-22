from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.model.kit import Kit


class KitRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def get_kit(self, supplied_kit_id):

        sample_repo = SampleRepo(self._transaction)

        with self._transaction.cursor() as cur:
            cur.execute("SELECT "
                        "ag_kit.ag_kit_id, "
                        "ag_kit_barcodes.ag_kit_barcode_id "
                        "FROM ag_kit LEFT JOIN ag_kit_barcodes ON "
                        "ag_kit.ag_kit_id = ag_kit_barcodes.ag_kit_id "
                        "WHERE "
                        "ag_kit.supplied_kit_id = %s",
                        supplied_kit_id)
            rows = cur.fetchall()
            if len(rows) == 0:
                return None
            else:
                samples = [sample_repo.get_sample(r[1]) for r in rows]
                return Kit(rows[0][0], samples)
