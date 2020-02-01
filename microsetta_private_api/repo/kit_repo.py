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
                        (supplied_kit_id,))
            rows = cur.fetchall()
            if len(rows) == 0:
                return None
            else:
                samples = [sample_repo.get_sample(r[1]) for r in rows]
                return Kit(rows[0][0], samples)

    # NOTE: This should only be used for unit tests!
    def create_mock_kit(self, supplied_kit_id):
        with self._transaction.cursor() as cur:
            kit_id = '77777777-8888-9999-aaaa-bbbbcccccccc'
            linker_id = '99999999-aaaa-aaaa-aaaa-bbbbcccccccc'
            barcode = '777777777'
            cur.execute("INSERT INTO barcode (barcode, status) "
                        "VALUES(%s, %s)",
                        (barcode,
                         'MOCK SAMPLE FOR UNIT TEST'))
            cur.execute("INSERT INTO ag_kit "
                        "(ag_kit_id, "
                        "supplied_kit_id, swabs_per_kit) "
                        "VALUES(%s, %s, %s)",
                        (kit_id, supplied_kit_id, 1))
            cur.execute("INSERT INTO ag_kit_barcodes "
                        "(ag_kit_barcode_id, ag_kit_id, barcode) "
                        "VALUES(%s, %s, %s)",
                        (linker_id, kit_id, barcode))

        return kit_id

    def remove_mock_kit(self):
        with self._transaction.cursor() as cur:
            kit_id = '77777777-8888-9999-aaaa-bbbbcccccccc'
            linker_id = '99999999-aaaa-aaaa-aaaa-bbbbcccccccc'
            barcode = '777777777'
            cur.execute("DELETE FROM ag_kit_barcodes "
                        "WHERE ag_kit_barcode_id=%s",
                        (linker_id,))
            cur.execute("DELETE FROM ag_kit WHERE ag_kit_id=%s",
                        (kit_id,))
            cur.execute("DELETE FROM barcode WHERE barcode = %s",
                        (barcode,))
