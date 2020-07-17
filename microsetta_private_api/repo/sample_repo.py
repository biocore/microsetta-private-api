import werkzeug
from werkzeug.exceptions import NotFound

from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.sample import Sample, SampleInfo

from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.repo.source_repo import SourceRepo


class SampleRepo(BaseRepo):
    PARTIAL_SQL = """SELECT
        ag_kit_barcodes.ag_kit_barcode_id,
        ag.ag_kit_barcodes.sample_date,
        ag.ag_kit_barcodes.sample_time,
        ag.ag_kit_barcodes.site_sampled,
        ag.ag_kit_barcodes.notes,
        ag.ag_kit_barcodes.barcode,
        latest_scan.scan_timestamp
        FROM ag.ag_kit_barcodes
        LEFT JOIN (
            SELECT barcode, max(scan_timestamp) AS scan_timestamp
            FROM barcodes.barcode_scans
            GROUP BY barcode
        ) latest_scan
        ON ag.ag_kit_barcodes.barcode = latest_scan.barcode
        LEFT JOIN ag.source
        ON ag.ag_kit_barcodes.source_id = ag.source.id"""

    def __init__(self, transaction):
        super().__init__(transaction)

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

    def _create_sample_obj(self, sample_row):
        if sample_row is None:
            return None

        sample_barcode = sample_row[5]
        sample_projects = self._retrieve_projects(sample_barcode)

        return Sample.from_db(*sample_row, sample_projects)

    # TODO: I'm still not entirely happy with the linking between samples and
    #  sources.  The new source_id is direct (and required for environmental
    #  samples, which have no surveys) but samples can also link to
    #  surveys which then may link to sources.
    #  Having multiple pathways to link in the db is a recipe for badness.
    #  Should something be done with the source_barcodes_surveys table? (which
    #  itself is required for linking samples to surveys!)
    def _update_sample_association(self, sample_id, source_id):
        with self._transaction.cursor() as cur:
            existing_sample = self._get_sample_by_id(sample_id)
            if existing_sample.is_locked:
                raise RepoException(
                    "Sample edits locked: Sample already received")

            cur.execute("UPDATE "
                        "ag_kit_barcodes "
                        "SET "
                        "source_id = %s "
                        "WHERE "
                        "ag_kit_barcode_id = %s",
                        (source_id, sample_id))

    def _get_sample_by_id(self, sample_id):
        """ Do not use from api layer, you must validate account and source."""

        sql = "{0}{1}".format(
            self.PARTIAL_SQL,
            " WHERE"
            " ag_kit_barcodes.ag_kit_barcode_id = %s")

        with self._transaction.cursor() as cur:
            cur.execute(sql, (sample_id,))
            sample_row = cur.fetchone()
            return self._create_sample_obj(sample_row)

    def get_samples_by_source(self, account_id, source_id):
        sql = "{0}{1}".format(
            self.PARTIAL_SQL,
            " WHERE"
            " source.account_id = %s"
            " AND source.id = %s"
            " ORDER BY ag_kit_barcodes.barcode asc")

        with self._transaction.cursor() as cur:
            acct_repo = AccountRepo(self._transaction)
            if acct_repo.get_account(account_id) is None:
                raise NotFound("No such account")

            source_repo = SourceRepo(self._transaction)
            if source_repo.get_source(account_id, source_id) is None:
                raise NotFound("No such source")

            cur.execute(sql, (account_id, source_id))

            samples = []
            for sample_row in cur.fetchall():
                samples.append(self._create_sample_obj(sample_row))
            return samples

    def get_sample(self, account_id, source_id, sample_id):
        sql = "{0}{1}".format(
            self.PARTIAL_SQL,
            " WHERE"
            " source.account_id = %s"
            " AND source.id = %s"
            " AND ag_kit_barcodes.ag_kit_barcode_id = %s ")

        with self._transaction.cursor() as cur:
            cur.execute(sql, (account_id, source_id, sample_id))
            sample_row = cur.fetchone()
            return self._create_sample_obj(sample_row)

    def update_info(self, account_id, source_id, sample_info):
        """
        Updates end user writable information about a sample that is assigned
        to a source.
        """
        existing_sample = self.get_sample(account_id, source_id,
                                          sample_info.id)
        if existing_sample is None:
            raise werkzeug.exceptions.NotFound("No sample ID: %s" %
                                               sample_info.id)

        if existing_sample.is_locked:
            raise RepoException("Sample edits locked: Sample already received")

        sample_date = None
        sample_time = None
        if sample_info.datetime_collected is not None:
            sample_date = sample_info.datetime_collected.date()
            sample_time = sample_info.datetime_collected.time()
        # TODO:  Need to get the exact policy on which fields user is allowed
        #  to set.  For starters: I think: datetime_collected, site, notes
        with self._transaction.cursor() as cur:
            cur.execute("UPDATE "
                        "ag_kit_barcodes "
                        "SET "
                        "sample_date = %s, "
                        "sample_time = %s, "
                        "site_sampled = %s, "
                        "notes = %s "
                        "WHERE "
                        "ag_kit_barcode_id = %s",
                        (
                            sample_date,
                            sample_time,
                            sample_info.site,
                            sample_info.notes,
                            sample_info.id
                        ))

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
                    # the same account.  We will make them dissociate first.
                    raise RepoException("Sample is already assigned")
            else:
                # This is the case where the sample is not yet assigned
                self._update_sample_association(sample_id, source_id)

    def dissociate_sample(self, account_id, source_id, sample_id):
        existing_sample = self.get_sample(account_id, source_id, sample_id)
        if existing_sample is None:
            raise werkzeug.exceptions.NotFound("No sample ID: %s" %
                                               sample_id)
        if existing_sample.is_locked:
            raise RepoException(
                "Sample edits locked: Sample already received")

        # Wipe any user entered fields from the sample:
        self.update_info(account_id, source_id,
                         SampleInfo(sample_id, None, None, None))

        # And detach the sample from the source
        self._update_sample_association(sample_id, None)
