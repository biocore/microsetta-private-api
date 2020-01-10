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

            sample_row = cur.fetchone()
            if sample_row is None:
                return None

            sample_barcode = sample_row[4]

            # If there is a sample, we can look for the projects associated
            #  with it.  We do this as a secondary query:
            cur.execute("SELECT barcodes.project.project FROM "
                        "barcodes.barcode "
                        "LEFT JOIN "
                        "barcodes.project_barcode "
                        "ON "
                        "barcodes.barcode.barcode = "
                        "barcodes.project_barcode.barcode "                        
                        "LEFT JOIN barcodes.project "
                        "ON "                        
                        "barcodes.project_barcode.project_id = "
                        "barcodes.project.project_id "
                        "WHERE "
                        "barcodes.barcode.barcode = %s",
                        (sample_barcode,))

            project_rows = cur.fetchall()
            sample_projects = [project[0] for project in project_rows]

            return Sample.from_db(sample_id,
                                  *sample_row,
                                  sample_projects)
