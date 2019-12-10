from repo.base_repo import BaseRepo
from model.sample import Sample
from model.kit import Kit


class KitRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    # TODO: Did we want the end users passing in kit_verification_code
    # or kit_password (or pass_reset_code, supplied_kit_id, open_humans_token)?
    def get_kit(self, kit_id, kit_verification_code):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT "
                        "ag_kit.ag_kit_id, "
                        "ag_kit_barcodes.ag_kit_barcode_id, "
                        "ag_kit_barcodes.barcode, "
                        "ag_kit_barcodes.notes, "
                        "ag_kit_barcodes.deposited "
                        "FROM ag_kit LEFT JOIN ag_kit_barcodes ON "
                        "ag_kit.ag_kit_id = ag_kit_barcodes.ag_kit_id "
                        "WHERE "
                        "ag_kit.ag_kit_id = %s AND "
                        "ag_kit.kit_verification_code = %s",
                        (kit_id, kit_verification_code))
            rows = cur.fetchall()
            if len(rows) == 0:
                return None
            else:
                samples = []
                for r in rows:
                    samples.append(Sample(r[1], r[2], r[3], r[4] == "t"))
                return Kit(rows[0][0], samples)
