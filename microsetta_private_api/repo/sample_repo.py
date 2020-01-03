from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.sample import Sample


class SampleRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def get_sample(self, sample_id):
        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT "
                "ag.ag_kit_barcodes.sample_date, "
                "ag.ag_kit_barcodes.sample_time, "
                "ag.ag_kit_barcodes.site_sampled, "
                "ag.ag_kit_barcodes.notes, "
                "barcodes.barcode.barcode, "
                "barcodes.barcode.scan_date "
                "FROM "
                "ag.ag_kit_barcodes  "
                "LEFT JOIN barcodes.barcode ON "
                "ag.ag_kit_barcodes.barcode = barcodes.barcode.barcode "
                "WHERE ag_kit_barcodes.ag_kit_barcode_id = %s",
                (sample_id,))

            # TODO: Daniel said "should also provide the names of the projects
            # that a sample (barcode) participates in";
            # where to get this in db?

            r = cur.fetchone()
            if r is None:
                return None
            return Sample.load_from_db_record(sample_id, *r)
