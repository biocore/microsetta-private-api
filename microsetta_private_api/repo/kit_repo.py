from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.model.kit import Kit


class KitRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    # Kit ID is the uuid primary key of ag_kit, as opposed to supplied_kit_id,
    # the more easily typed string we put on pieces of paper inside the kit
    def get_kit_all_samples_by_kit_id(self, kit_id):
        sample_repo = SampleRepo(self._transaction)
        with self._transaction.cursor() as cur:
            cur.execute("SELECT "
                        "ag_kit.ag_kit_id, "
                        "ag_kit_barcodes.ag_kit_barcode_id "
                        "FROM ag_kit LEFT JOIN ag_kit_barcodes ON "
                        "ag_kit.ag_kit_id = ag_kit_barcodes.ag_kit_id "
                        "WHERE "
                        "ag_kit.ag_kit_id = %s",
                        (kit_id,))
            rows = cur.fetchall()
            if len(rows) == 0:
                return None
            else:
                samples = [sample_repo._get_sample_by_id(r[1]) for r in rows]
                return Kit(rows[0][0], samples)

    def get_kit_all_samples(self, supplied_kit_id):
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
                samples = [sample_repo._get_sample_by_id(r[1]) for r in rows]
                return Kit(rows[0][0], samples)

    def get_kit_unused_samples(self, supplied_kit_id):
        sample_repo = SampleRepo(self._transaction)

        # Business Logic: We now define an unclaimed sample as a sample with
        # a null source_id in ag_kit_barcodes
        with self._transaction.cursor() as cur:
            cur.execute("SELECT "
                        "ag_kit.ag_kit_id, "
                        "ag_kit_barcodes.ag_kit_barcode_id "
                        "FROM ag_kit LEFT JOIN ag_kit_barcodes ON "
                        "ag_kit.ag_kit_id = ag_kit_barcodes.ag_kit_id "
                        "WHERE "
                        "ag_kit.supplied_kit_id = %s AND "
                        "ag_kit_barcodes.source_id is null",
                        (supplied_kit_id,))
            rows = cur.fetchall()
            if len(rows) == 0:
                return None
            else:
                samples = [sample_repo._get_sample_by_id(r[1]) for r in rows]
                return Kit(rows[0][0], samples)

    def get_kit_id_name_by_barcode(self, barcode):
        with self._transaction.cursor() as cur:
            cur.execute("""
                        SELECT kit_id
                        FROM barcodes.barcode
                        WHERE barcode = %s
                        """, (barcode,))

            rows = cur.fetchall()

            if len(rows) == 0:
                return None
            else:
                return rows[0][0]
