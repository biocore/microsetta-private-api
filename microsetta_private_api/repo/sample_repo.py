import werkzeug

from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.sample import Sample

from microsetta_private_api.exceptions import RepoException


class SampleRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def get_samples_by_source(self, account_id, source_id):
        with self._transaction.cursor as cur:
            cur.execute(
                "SELECT "
                "ag_kit_barcodes.ag_kit_barcode_id, "
                "ag_kit_barcodes.sample_date, "
                "ag_kit_barcodes.sample_time, "
                "ag_kit_barcodes.site_sampled, "
                "ag_kit_barcodes.notes, "
                "ag_kit_barcodes.barcode, "
                "barcode.scan_date "
                "FROM ag_kit_barcodes "
                "LEFT JOIN barcode "
                "USING (barcode) "
                "LEFT JOIN source "
                "ON ag_kit_barcodes.source_id = source.id "
                "WHERE "
                "source.account_id = %s AND "
                "source.id = %s",
                (source_id, account_id)
            )

            samples = []
            for sample_row in cur.fetchall():
                barcode = sample_row[5]
                sample_projects = self._retrieve_projects(barcode)
                s = Sample.from_db(*sample_row,
                                   sample_projects)
                samples.append(s)
            return samples

    def _retrieve_projects(self, sample_barcode):
        with self._transaction.cursor() as cur:
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
            return sample_projects


    def _get_sample_by_id(self, sample_id):
        """ Do not use from api layer, you must validate account and source."""
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
                "ag.ag_kit_barcodes "
                "LEFT JOIN barcodes.barcode "
                "ON "
                "ag.ag_kit_barcodes.barcode = barcodes.barcode.barcode "
                "LEFT JOIN source "
                "ON "
                "ag.ag_kit_barcodes.source_id = source.id "
                "WHERE "
                "ag_kit_barcodes.ag_kit_barcode_id = %s",
                (sample_id,))

            sample_row = cur.fetchone()
            if sample_row is None:
                return None

            sample_barcode = sample_row[4]
            sample_projects = self._retrieve_projects(sample_barcode)

            return Sample.from_db(sample_id,
                                  *sample_row,
                                  sample_projects)

    def get_sample(self, account_id, source_id, sample_id):
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
                "ag.ag_kit_barcodes "
                "LEFT JOIN barcodes.barcode "
                "ON "
                "ag.ag_kit_barcodes.barcode = barcodes.barcode.barcode "
                "LEFT JOIN source "
                "ON "
                "ag.ag_kit_barcodes.source_id = source.id "
                "WHERE "
                "ag_kit_barcodes.ag_kit_barcode_id = %s AND "
                "source.id = %s AND "
                "source.account_id = %s",
                (sample_id, source_id, account_id))

            sample_row = cur.fetchone()
            if sample_row is None:
                return None

            sample_barcode = sample_row[4]
            sample_projects = self._retrieve_projects(sample_barcode)

            return Sample.from_db(sample_id,
                                  *sample_row,
                                  sample_projects)

    # TODO: Should this throw if the sample is already associated with
    #  another source in the same account?  Technically they could disassociate
    #  the sample first...
    # TODO: Should this throw if the sample is "locked"?
    #  ie: If barcodes.barcode.scan_date is not null?
    def associate_sample(self, account_id, source_id, sample_id):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT "
                        "ag_kit_barcode_id, "
                        "source.account_id, "
                        "source.id "
                        "FROM "
                        "ag_kit_barcodes "
                        "LEFT OUTER JOIN source "
                        "ON ag_kit_barcodes.source_id = source.id "
                        "WHERE "
                        "ag_kit_barcode_id = %s",
                        (sample_id,))
            row = cur.fetchone()
            if row is None:
                raise werkzeug.exceptions.NotFound("No sample ID: %s" %
                                                   sample_id)
            if row[2] is not None:
                if row[1] != account_id:
                    # This is the case where the sample is already assigned in
                    # another account
                    raise RepoException("Sample is already assigned")
                else:
                    # This is the case where the sample is already assigned in
                    # the same account
                    self._update_sample_association(sample_id, source_id)
            else:
                # This is the case where the sample is not yet assigned
                self._update_sample_association(sample_id, source_id)

    # TODO: I'm still not entirely happy with the linking between samples and
    #  sources.  The new source_id is direct (and required for environmental
    #  samples, which have no surveys) but samples can also link to
    #  surveys which then may link to sources.
    #  Having multiple pathways to link in the db is a recipe for badness.
    #  Should something be done with the source_barcodes_surveys table? (which
    #  itself is required for linking samples to surveys!)
    def _update_sample_association(self, sample_id, source_id):
        with self._transaction.cursor() as cur:
            cur.execute("UPDATE "
                        "ag_kit_barcodes "
                        "SET "
                        "source_id = %s "
                        "WHERE "
                        "ag_kit_barcode_id = %s",
                        (source_id, sample_id))
