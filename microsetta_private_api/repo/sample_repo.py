import datetime
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
        latest_scan.scan_timestamp,
        ag.source.id,
        ag.source.account_id,
        ag.ag_kit_barcodes.latest_sample_information_update
        FROM ag.ag_kit_barcodes
        LEFT JOIN (
            SELECT barcode, max(scan_timestamp) AS scan_timestamp
            FROM barcodes.barcode_scans
            GROUP BY barcode
        ) latest_scan
        ON ag.ag_kit_barcodes.barcode = latest_scan.barcode
        LEFT JOIN ag.source
        ON ag.ag_kit_barcodes.source_id = ag.source.id"""

    # the nested query requires a full scan of the barcode_scans
    # table, which is not necessary if limited to a specific sample.
    # this query is approximately 200x faster than the above
    # Note the WHERE in the nested query
    PARTIAL_SQL_BARCODE_SPECIFIC = """SELECT
        ag_kit_barcodes.ag_kit_barcode_id,
        ag.ag_kit_barcodes.sample_date,
        ag.ag_kit_barcodes.sample_time,
        ag.ag_kit_barcodes.site_sampled,
        ag.ag_kit_barcodes.notes,
        ag.ag_kit_barcodes.barcode,
        latest_scan.scan_timestamp,
        ag.source.id,
        ag.source.account_id,
        ag.ag_kit_barcodes.latest_sample_information_update
        FROM ag.ag_kit_barcodes
        LEFT JOIN (
            SELECT barcode, max(scan_timestamp) AS scan_timestamp
            FROM barcodes.barcode_scans
            WHERE barcode = %s
            GROUP BY barcode
        ) latest_scan
        ON ag.ag_kit_barcodes.barcode = latest_scan.barcode
        LEFT JOIN ag.source
        ON ag.ag_kit_barcodes.source_id = ag.source.id"""

    SAMPLE_SITE_LAST_WASHED_DATE_FORMAT = "%m/%d/%Y"
    # NB: strptime() and strftime() treat the %I and %-I formats differently.
    # To properly store and retrieve the time format, we use different formats
    # for each function
    SAMPLE_SITE_LAST_WASHED_TIME_FORMAT_STRPTIME = "%I:%M %p"
    SAMPLE_SITE_LAST_WASHED_TIME_FORMAT_STRFTIME = "%-I:%M %p"

    def __init__(self, transaction):
        super().__init__(transaction)

    def _retrieve_projects(self, sample_barcode, return_ids=False):
        with self._transaction.cursor() as cur:
            if return_ids is True:
                # If the caller wants the project IDs, we can directly
                # query the project_barcode table
                cur.execute(
                    "SELECT project_id "
                    "FROM barcodes.project_barcode "
                    "WHERE barcode = %s",
                    (sample_barcode,)
                )
            else:
                # Otherwise, we defualt to the existing behavior of returning
                # the project names.
                # If there is a sample, we look for the projects associated
                # with it.  We do this as a secondary query:
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
        scan_timestamp = sample_row[6]
        sample_projects = self._retrieve_projects(sample_barcode)
        sample_project_ids = self._retrieve_projects(
            sample_barcode, return_ids=True
        )
        sample_status = self.get_sample_status(sample_barcode, scan_timestamp)

        sample = Sample.from_db(*sample_row, sample_projects, sample_status,
                                sample_project_ids=sample_project_ids)
        sample.set_barcode_meta(self._get_barcode_meta(sample.id))
        return sample

    # TODO: I'm still not entirely happy with the linking between samples and
    #  sources.  The new source_id is direct (and required for environmental
    #  samples, which have no surveys) but samples can also link to
    #  surveys which then may link to sources.
    #  Having multiple pathways to link in the db is a recipe for badness.
    #  Should something be done with the source_barcodes_surveys table? (which
    #  itself is required for linking samples to surveys!)
    def _update_sample_association(self, sample_id, source_id,
                                   override_locked=False):
        with self._transaction.cursor() as cur:
            existing_sample = self._get_sample_by_id(sample_id)
            # if the sample is not associated with a source, then
            # we can skip the lock checks
            if existing_sample.source_id is not None \
                    and existing_sample.remove_locked and not override_locked:
                raise RepoException(
                    "Sample association locked: Sample already received")

            barcode = existing_sample.barcode

            # collect old survey associations if they exist
            cur.execute("""SELECT survey_id
                           FROM ag.ag_login_surveys
                           JOIN ag.ag_kit_barcodes USING (source_id)
                           WHERE ag_kit_barcode_id=%s""",
                        (sample_id, ))
            survey_ids = tuple([r[0] for r in cur.fetchall()])

            if len(survey_ids) > 0:
                # if this was a previously assigned sample, then remove any
                # stale relations
                cur.execute("""DELETE FROM ag.source_barcodes_surveys
                               WHERE barcode=%s
                                   AND survey_id IN %s""",
                            (barcode, survey_ids))

            # collect new survey associations if they exist
            cur.execute("""SELECT survey_id
                           FROM ag.ag_login_surveys
                           WHERE source_id=%s""",
                        (source_id, ))
            survey_ids = [r[0] for r in cur.fetchall()]

            # set the barcode source association
            cur.execute("""UPDATE ag_kit_barcodes
                           SET source_id = %s
                           WHERE ag_kit_barcode_id = %s""",
                        (source_id, sample_id))

            # set barcode survey associations
            updates = [(barcode, sid) for sid in survey_ids]
            cur.executemany("""INSERT INTO ag.source_barcodes_surveys
                               (barcode, survey_id)
                               VALUES (%s, %s)""",
                            updates)

            # update any vioscreen associations to reflect the source
            # and the account
            if source_id is not None:
                cur.execute("""SELECT account_id
                               FROM ag.source
                               WHERE id=%s""",
                            (source_id, ))
                account_id = cur.fetchone()

                cur.execute("""UPDATE ag.vioscreen_registry
                               SET source_id=%s, account_id=%s
                               WHERE sample_id=%s""",
                            (source_id, account_id, sample_id))

    def migrate_sample(self, sample_id, source_id_src, source_id_dst,
                       areyousure=False):
        """Migrate a sample among sources

        WARNING !!!

        This is NOT intended for general use. This is an
        administrative method for correcting unusual circumstances, and the
        person issuing this function call knows what they are doing.

        WARNING !!!
        """
        if not areyousure:
            raise RepoException("You aren't sure you want to do this")

        if source_id_src == source_id_dst:
            # nothing to do
            return

        with self._transaction.cursor() as cur:
            # verify the destination source exists
            cur.execute("SELECT id FROM ag.source where id=%s",
                        (source_id_dst, ))
            res = cur.fetchall()
            if len(res) != 1:
                raise RepoException(f"source ({source_id_dst}) does not exist")

            # verify the sample is currently associated with source_id_src
            cur.execute("""SELECT ag_kit_barcode_id
                           FROM ag.ag_kit_barcodes
                           WHERE source_id=%s
                               AND ag_kit_barcode_id=%s""",
                        (source_id_src, sample_id))
            res = cur.fetchall()
            if len(res) != 1:
                raise RepoException(f"{len(res)} entries associated with "
                                    f"source ({source_id_src}) and sample "
                                    f"({sample_id})")

            self._update_sample_association(sample_id, source_id_dst,
                                            override_locked=True)

    def _get_sample_barcode_from_id(self, sample_id):
        """Obtain a barcode from a ag.ag_kit_barcode_id"""
        sql = """SELECT barcode
                 FROM ag.ag_kit_barcodes
                 WHERE ag_kit_barcode_id = %s"""
        with self._transaction.cursor() as cur:
            cur.execute(sql, (sample_id,))
            sample_row = cur.fetchone()
            if sample_row is None:
                return None
            else:
                return sample_row[0]

    def _get_sample_by_id(self, sample_id):
        """ Do not use from api layer, you must validate account and source."""

        sql = "{0}{1}".format(
            self.PARTIAL_SQL_BARCODE_SPECIFIC,
            " WHERE"
            " ag_kit_barcodes.ag_kit_barcode_id = %s")

        with self._transaction.cursor() as cur:
            barcode = self._get_sample_barcode_from_id(sample_id)
            cur.execute(sql, (barcode, sample_id,))
            sample_row = cur.fetchone()
            return self._create_sample_obj(sample_row)

    def get_samples_by_source(self, account_id, source_id,
                              allow_revoked=False):
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
            if source_repo.get_source(account_id, source_id,
                                      allow_revoked=allow_revoked) is None:
                raise NotFound("No such source")

            cur.execute(sql, (account_id, source_id))

            samples = []
            for sample_row in cur.fetchall():
                sample = self._create_sample_obj(sample_row)
                sample.kit_id = self._get_supplied_kit_id_by_sample(
                    sample.barcode
                )
                samples.append(sample)
            return samples

    def get_sample(self, account_id, source_id, sample_id):
        sql = "{0}{1}".format(
            self.PARTIAL_SQL_BARCODE_SPECIFIC,
            " WHERE"
            " source.account_id = %s"
            " AND source.id = %s"
            " AND ag_kit_barcodes.ag_kit_barcode_id = %s ")

        with self._transaction.cursor() as cur:
            barcode = self._get_sample_barcode_from_id(sample_id)
            cur.execute(sql, (barcode, account_id, source_id, sample_id))
            sample_row = cur.fetchone()
            sample = self._create_sample_obj(sample_row)
            return sample

    def update_info(self, account_id, source_id, sample_info,
                    override_locked=False):
        """
        Updates end user writable information about a sample that is assigned
        to a source.
        """
        existing_sample = self.get_sample(account_id, source_id,
                                          sample_info.id)
        if existing_sample is None:
            raise werkzeug.exceptions.NotFound("No sample ID: %s" %
                                               sample_info.id)

        if existing_sample.edit_locked and not override_locked:
            raise RepoException("Sample edits locked: Sample already evaluated"
                                " for processing")

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
                        "notes = %s, "
                        "latest_sample_information_update = %s "
                        "WHERE "
                        "ag_kit_barcode_id = %s",
                        (
                            sample_date,
                            sample_time,
                            sample_info.site,
                            sample_info.notes,
                            datetime.datetime.now(),
                            sample_info.id
                        ))

        # NB: We run this even if the barcode_meta dict is empty, as that
        # means the answers associated with the last sample update should be
        # purged. This applies both to the normal sample update process, as
        # well as dissociate_sample().
        if sample_info.barcode_meta is None:
            sample_info.barcode_meta = {}
        else:
            b_m = self._validate_barcode_meta(
                sample_info.site, sample_info.barcode_meta
            )
            if b_m is False:
                raise RepoException("Invalid barcode_meta fields or values")
            else:
                sample_info.barcode_meta = b_m
        self._update_barcode_meta(sample_info.id, sample_info.barcode_meta)

    def _update_barcode_meta(self, sample_id, barcode_meta):
        """Update barcode-specific metadata

        NB: As with validation, deferring on a more elegant way to handle
        table selection for where to store this data.

        Parameters
        ----------
        sample_id : str, uuid
            The associated sample ID for which to store metadata
        barcode_meta : dict
            The key:value pairs to store
        """
        with self._transaction.cursor() as cur:
            # First, delete existing values
            cur.execute(
                "DELETE FROM ag.ag_kit_barcodes_cheek "
                "WHERE ag_kit_barcode_id = %s",
                (sample_id, )
            )
            # Then, insert new values if the dict isn't empty
            if len(barcode_meta) > 0:
                cur.execute(
                    "INSERT INTO ag.ag_kit_barcodes_cheek "
                    "(ag_kit_barcode_id, sample_site_last_washed_date, "
                    "sample_site_last_washed_time, "
                    "sample_site_last_washed_product) "
                    "VALUES (%s, %s, %s, %s)",
                    (sample_id, barcode_meta['sample_site_last_washed_date'],
                     barcode_meta['sample_site_last_washed_time'],
                     barcode_meta['sample_site_last_washed_product'])
                )

    def _get_barcode_meta(self, sample_id):
        """ Retrieve any barcode-specific metadata

        Parameters
        ----------
        sample_id : str, uuid
            The associated sample ID for which to retrieve metadata

        Returns
        -------
        dict
            The sample-specific metadata, or an empty dict
        """
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT sample_site_last_washed_date, "
                "sample_site_last_washed_time, "
                "sample_site_last_washed_product "
                "FROM ag.ag_kit_barcodes_cheek "
                "WHERE ag_kit_barcode_id = %s",
                (sample_id, )
            )
            row = cur.fetchone()
            if row is None:
                return {}
            else:
                # We need to transform the date/time fields back to what the
                # interface works with
                ret_dict = {
                    'sample_site_last_washed_date': row[
                        'sample_site_last_washed_date'
                    ],
                    'sample_site_last_washed_time': row[
                        'sample_site_last_washed_time'
                    ],
                    'sample_site_last_washed_product': row[
                        'sample_site_last_washed_product'
                    ]
                }
                if ret_dict['sample_site_last_washed_date'] is not None:
                    ret_dict['sample_site_last_washed_date'] = \
                        ret_dict['sample_site_last_washed_date'].strftime(
                            self.SAMPLE_SITE_LAST_WASHED_DATE_FORMAT
                        )
                if ret_dict['sample_site_last_washed_time'] is not None:
                    ret_dict['sample_site_last_washed_time'] = \
                        ret_dict['sample_site_last_washed_time'].strftime(
                            self.SAMPLE_SITE_LAST_WASHED_TIME_FORMAT_STRFTIME
                        )
                return ret_dict

    def associate_sample(self, account_id, source_id, sample_id,
                         override_locked=False):
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
                self._update_sample_association(sample_id, source_id,
                                                override_locked=override_locked)  # noqa

    def dissociate_sample(self, account_id, source_id, sample_id,
                          override_locked=False):
        existing_sample = self.get_sample(account_id, source_id, sample_id)
        if existing_sample is None:
            raise werkzeug.exceptions.NotFound("No sample ID: %s" %
                                               sample_id)

        if existing_sample.edit_locked and not override_locked:
            raise RepoException(
                "Sample information locked: Sample already evaluated for "
                "processing")

        # Wipe any user entered fields from the sample:
        self.update_info(account_id, source_id,
                         SampleInfo(sample_id, None, None, None),
                         override_locked=override_locked)

        if existing_sample.remove_locked and not override_locked:
            raise RepoException(
                "Sample association locked: Sample already received")

        # And detach the sample from the source
        self._update_sample_association(sample_id, None,
                                        override_locked=override_locked)

    def get_sample_status(self, sample_barcode, scan_timestamp):
        if scan_timestamp is None:
            return None

        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT "
                "sample_status "
                "FROM barcodes.barcode_scans "
                "WHERE barcode=%s AND scan_timestamp = %s "
                "LIMIT 1",
                (sample_barcode, scan_timestamp)
            )
            row = cur.fetchone()
            if row is None:
                return None
            return row[0]

    def _get_supplied_kit_id_by_sample(self, sample_barcode):
        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT kit_id "
                "FROM barcodes.barcode "
                "WHERE barcode = %s",
                (sample_barcode, )
            )
            row = cur.fetchone()
            return row[0]

    def scrub(self, account_id, source_id, sample_id):
        """Wipe out free text information for a sample

        Parameters
        ----------
        account_id : str, uuid
            The associated account ID to scrub
        source_id : str, uuid
            The associated source ID to scrub
        sample_id : str, uuid
            The associated sample ID to scrub

        Raises
        ------
        RepoException
            If the account / source is relation is bad
            If the source / sample relation is bad
            If the update fails for any reason

        Returns
        -------
        True if the sample was scrubbed, will raise otherwise
        """
        notes = "scrubbed"
        with self._transaction.cursor() as cur:
            # verify our account / source relation is reasonable
            cur.execute("""SELECT id
                           FROM ag.source
                           WHERE id=%s AND account_id=%s""",
                        (source_id, account_id))
            res = cur.fetchone()

            if res is None:
                raise RepoException("Invalid account / source relation")

            cur.execute("""UPDATE ag_kit_barcodes
                           SET notes=%s
                           WHERE source_id=%s AND ag_kit_barcode_id=%s""",
                        (notes, source_id, sample_id))

            if cur.rowcount != 1:
                raise RepoException("Invalid source / sample relation")
            else:
                return True

    def _validate_barcode_meta(self, sample_site, barcode_meta):
        """ Validate the barcode_meta fields/values provided

        NB: I'm deferring on a more elegant validation system until/unless
        we decide whether barcode-specific metadata will remain in one table
        per sample site, a key-value pairing table, or something else.

        Parameters
        ----------
        sample_site : str
            The sample site
        barcode_meta : dict
            Key:Value pairings of field_name:field_value

        Returns
        -------
        Dict with database-ready values if valid, else False
        """

        # If the barcode_meta dict is empty, we can immediately pass it. This
        # will allow the repo to purge existing values without adding a new
        # record.
        if len(barcode_meta) == 0:
            return {}

        # Only Cheek samples should have barcode_meta values. If it's not a
        # Cheek sample, immediately fail it.
        if sample_site != "Cheek":
            return False

        ret_dict = {}
        bc_valid = True
        for fn, fv in barcode_meta.items():
            if fn == "sample_site_last_washed_date":
                if fv is None or len(fv) == 0:
                    # Null value is acceptable, bypass format validation
                    ret_dict[fn] = None
                else:
                    try:
                        ret_val = datetime.datetime.strptime(
                            fv,
                            self.SAMPLE_SITE_LAST_WASHED_DATE_FORMAT
                        )
                        ret_dict[fn] = ret_val
                    except ValueError:
                        bc_valid = False
            elif fn == "sample_site_last_washed_time":
                if fv is None or len(fv) == 0:
                    # Null value is acceptable, bypass format validation
                    ret_dict[fn] = None
                else:
                    try:
                        ret_val = datetime.datetime.strptime(
                            fv,
                            self.SAMPLE_SITE_LAST_WASHED_TIME_FORMAT_STRPTIME
                        )
                        ret_dict[fn] = ret_val
                    except ValueError:
                        bc_valid = False
            elif fn == "sample_site_last_washed_product":
                if fv is None or len(fv) == 0:
                    # Ensure that blank value - None/Null or "" - is passed on
                    # as None
                    ret_dict[fn] = None
                else:
                    # The ENUM type in the database will validate the value
                    ret_dict[fn] = fv
            else:
                bc_valid = False

        return False if bc_valid is False else ret_dict
