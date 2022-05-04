import uuid
import string
import random
import datetime
import pandas as pd
import psycopg2.extras
import json

from psycopg2 import sql

from microsetta_private_api.exceptions import RepoException

import microsetta_private_api.model.project as p
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.repo.kit_repo import KitRepo
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.repo.source_repo import SourceRepo
from werkzeug.exceptions import NotFound

from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo

# TODO: Refactor repeated elements in project-related sql queries?
PROJECT_FIELDS = f"""
                project_id, {p.DB_PROJ_NAME_KEY},
                {p.IS_MICROSETTA_KEY}, {p.BANK_SAMPLES_KEY},
                {p.PLATING_START_DATE_KEY}, {p.CONTACT_NAME_KEY},
                {p.ADDTL_CONTACT_NAME_KEY}, {p.CONTACT_EMAIL_KEY},
                {p.DEADLINES_KEY}, {p.NUM_SUBJECTS_KEY},
                {p.NUM_TIMEPOINTS_KEY}, {p.START_DATE_KEY},
                {p.DISPOSITION_COMMENTS_KEY}, {p.COLLECTION_KEY},
                {p.IS_FECAL_KEY}, {p.IS_SALIVA_KEY}, {p.IS_SKIN_KEY},
                {p.IS_BLOOD_KEY}, {p.IS_OTHER_KEY},
                {p.DO_16S_KEY}, {p.DO_SHALLOW_SHOTGUN_KEY},
                {p.DO_SHOTGUN_KEY}, {p.DO_RT_QPCR_KEY},
                {p.DO_SEROLOGY_KEY}, {p.DO_METATRANSCRIPTOMICS_KEY},
                {p.DO_MASS_SPEC_KEY}, {p.MASS_SPEC_COMMENTS_KEY},
                {p.MASS_SPEC_CONTACT_NAME_KEY},
                {p.MASS_SPEC_CONTACT_EMAIL_KEY}, {p.DO_OTHER_KEY},
                {p.BRANDING_ASSOC_INSTRUCTIONS_KEY},
                {p.BRANDING_STATUS_KEY},
                {p.SUBPROJECT_NAME_KEY}, {p.ALIAS_KEY},
                {p.SPONSOR_KEY}, {p.COORDINATION_KEY},
                {p.IS_ACTIVE_KEY}"""

PROJECTS_BASICS_SQL = f"""
    SELECT
    {PROJECT_FIELDS},
    count(distinct barcode) as {p.NUM_SAMPLES_KEY},
    count(distinct kit_id) as {p.NUM_KITS_KEY}
    FROM barcodes.project
    LEFT JOIN
    barcodes.project_barcode
    USING (project_id)
    LEFT JOIN
    barcodes.barcode
    USING (barcode)
    GROUP BY project_id
    ORDER BY project_id;"""

# The below sql statements pull various computed counts about projects.
# Each query must follow the convention that it returns a column named
# "project_id" to join on, and that all other columns it returns are unique
# to that query (not also returned by any other query).
NUM_UNIQUE_SOURCES_SQL = f"""
    SELECT project_barcode.project_id,
    count(distinct ag_kit_barcodes.source_id) as {p.NUM_UNIQUE_SOURCES_KEY}
    FROM barcodes.project_barcode
    INNER JOIN ag.ag_kit_barcodes
    USING (barcode)
    GROUP BY project_id
    ORDER BY project_id;"""

NUM_RECEIVED_SAMPLES_SQL = f"""
    SELECT project_id,
    count(distinct barcode) as {p.NUM_SAMPLES_RECEIVED_KEY}
    FROM project_barcode
    INNER JOIN
    barcode_scans
    USING (barcode)
    GROUP BY project_id
    ORDER BY project_id;"""

NUM_AT_LEAST_PARTIALLY_RECEIVED_KITS = f"""
    SELECT project_barcode.project_id,
    count(distinct ag_kit_barcodes.ag_kit_id)
    as {p.NUM_PARTIALLY_RETURNED_KITS_KEY}
    FROM ag.ag_kit_barcodes
    INNER JOIN barcodes.project_barcode
    USING (barcode)
    INNER JOIN barcodes.barcode_scans
    USING (barcode)
    GROUP BY project_barcode.project_id
    ORDER BY project_barcode.project_id;"""

NUM_KITS_W_AT_LEAST_ONE_PROBLEM_SAMPLE_SQL = f"""
        SELECT project_barcode.project_id,
        count(distinct ag_kit_barcodes.ag_kit_id)
        as {p.NUM_KITS_W_PROBLEMS_KEY}
        FROM ag.ag_kit_barcodes
        INNER JOIN barcodes.project_barcode
        USING (barcode)
        INNER JOIN barcodes.barcode_scans
        USING (barcode)
        INNER JOIN (
            SELECT barcode, max(scan_timestamp) AS scan_timestamp
            FROM barcodes.barcode_scans
            GROUP BY barcode
        ) latest_scan
        ON barcode_scans.barcode = latest_scan.barcode
        AND barcode_scans.scan_timestamp = latest_scan.scan_timestamp
        AND barcode_scans.sample_status <> '{p.VALID_SAMPLES_STATUS}'
        GROUP BY project_barcode.project_id;"""

NUM_FULLY_RECEIVED_KITS_SQL = f"""
    SELECT project_id,
    count(distinct ag_kit_id) as {p.NUM_FULLY_RETURNED_KITS_KEY}
    FROM (
        SELECT
        project_barcode.project_id,
        ag_kit_barcodes.ag_kit_id,
        count(distinct ag_kit_barcodes.barcode) as uniq_barcodes_in_kit,
        count(distinct barcode_scans.barcode) as uniq_received_barcodes_in_kit
        FROM ag.ag_kit_barcodes
        INNER JOIN barcodes.project_barcode
        USING (barcode)
        LEFT JOIN barcodes.barcode_scans
        USING (barcode)
        GROUP BY project_id, ag_kit_id
    ) as kit_lists
    WHERE uniq_barcodes_in_kit = uniq_received_barcodes_in_kit
    GROUP by project_id
    ORDER by project_id;"""

KIT_BOX_ID_KEY = "box_id"
KIT_OUTBOUND_KEY = "outbound_fedex_tracking"
KIT_ADDRESS_KEY = "address"
KIT_INBOUND_KEY = "inbound_fedex_tracking"


def _make_statuses_sql(_):
    # Note: scans with multiple identical timestamps are quite unlikely
    # in real life but easy to create in test code.  Such a situation is
    # pathological; we can't tell which scan is the current status (which we
    # base on latest timestamp) if there are multiple scans for the same
    # barcode with the SAME latest timestamp.  The below code is robust to
    # this pathological situation IF the multiple same-latest-timestamp scans
    # for a barcode have identical statuses.  However, if the the multiple
    # same-latest-timestamp scans for a barcode have DIFFERENT statuses, this
    # code will double-count that barcode.  I doubt this situation will ever
    # happen in real life.

    joins = """
        SELECT * FROM crosstab(
            $$select p.project_id, scans.sample_status,
            coalesce(count(distinct scans.barcode),0)
            FROM barcodes.project as p
            INNER JOIN barcodes.project_barcode as pb
            USING (project_id)
            INNER JOIN barcodes.barcode_scans as scans
            USING (barcode)
            INNER JOIN (
                SELECT barcode, max(scan_timestamp) AS scan_timestamp
                FROM barcodes.barcode_scans
                GROUP BY barcode
            ) latest_scan
            ON scans.barcode = latest_scan.barcode
            AND scans.scan_timestamp = latest_scan.scan_timestamp
            GROUP BY project_id, sample_status
            ORDER BY project_id,
            CASE sample_status """

    case_values_connector = """
            END; $$,
            $$VALUES """

    results_name = """; $$
        ) AS ct(project_id bigint, """

    results_order = """)
        ORDER BY ct;"""

    cases = []
    values = []
    colnames = []
    case_num = 1
    for curr_status in p.SAMPLE_STATUSES:
        cases.append(f"WHEN '{curr_status}' THEN {case_num} ")
        values.append(f"('{curr_status}')")
        case_num += 1

    num_status_keys = p.get_status_num_keys()
    for curr_num_status_key in num_status_keys:
        colnames.append(f"{curr_num_status_key} bigint")

    cases_sql = " ".join(cases)
    values_sql = ", ".join(values)
    colnames_sql = ", ".join(colnames)

    final_sql = f"{joins}{cases_sql}{case_values_connector}{values_sql}" \
                f"{results_name}{colnames_sql}{results_order}"

    return final_sql


# NB: PROJECTS_BASICS_SQL *must* come first since its list of project id is a
# superset of other queries' lists.
_PROJECT_SQLS = [
                ((p.NUM_KITS_KEY, p.NUM_SAMPLES_KEY), PROJECTS_BASICS_SQL),
                ((p.NUM_UNIQUE_SOURCES_KEY,), NUM_UNIQUE_SOURCES_SQL),
                ((p.NUM_SAMPLES_RECEIVED_KEY,), NUM_RECEIVED_SAMPLES_SQL),
                (("statuses",), _make_statuses_sql),
                ((p.NUM_PARTIALLY_RETURNED_KITS_KEY,),
                    NUM_AT_LEAST_PARTIALLY_RECEIVED_KITS),
                ((p.NUM_KITS_W_PROBLEMS_KEY,),
                    NUM_KITS_W_AT_LEAST_ONE_PROBLEM_SAMPLE_SQL),
                ((p.NUM_FULLY_RETURNED_KITS_KEY,), NUM_FULLY_RECEIVED_KITS_SQL)
                ]


def _get_kit_tuples(new_kit_uuids, kit_names, kits_details=None):
    result = []
    for i in range(len(new_kit_uuids)):
        curr_kit_uuid = new_kit_uuids[i]
        curr_kit_name = kit_names[i]
        if kits_details is not None:
            curr_kit_details = kits_details[i]
        else:
            curr_kit_details = {KIT_BOX_ID_KEY: curr_kit_uuid}

        curr_tuple = (curr_kit_uuid, curr_kit_name,
                      curr_kit_details.get(KIT_OUTBOUND_KEY),
                      curr_kit_details.get(KIT_ADDRESS_KEY),
                      curr_kit_details.get(KIT_INBOUND_KEY),
                      curr_kit_details[KIT_BOX_ID_KEY])
        result.append(curr_tuple)

    return result


class AdminRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def _read_projects_df_from_db(self, include_stats=True):
        """Return pandas data frame of project info and statistics from db."""

        projects_df = None

        # TODO: should cursor be created here or no?
        # https://www.datacamp.com/community/tutorials/tutorial-postgresql-python  # noqa
        # shows creation of a cursor even though no methods are called on it
        with self._transaction.dict_cursor():
            # TODO: is there a better way to access this?
            conn = self._transaction._conn

            queries = _PROJECT_SQLS if include_stats else [_PROJECT_SQLS[0]]
            for stats_keys, sql_source in queries:
                if callable(sql_source):
                    curr_sql = sql_source(*stats_keys)
                else:
                    curr_sql = sql_source.format(*stats_keys)

                curr_df = pd.read_sql(curr_sql, conn)

                if projects_df is None:
                    projects_df = curr_df
                else:
                    # left join here: the first query produces a df with a
                    # COMPLETE list of all projects, whereas subsequent
                    # queries only return info on projects relevant to their
                    # computed statistic.
                    projects_df = pd.merge(projects_df, curr_df,
                                           how="left", on=["project_id"])

        # make the project_id the index of the final data frame, but
        # do NOT drop the project_id column from the data frame.
        projects_df.set_index('project_id', drop=False, inplace=True)
        return projects_df

    def _get_ids_relevant_to_barcode(self, sample_barcode):
        with self._transaction.dict_cursor() as cur:
            # First, look for this barcode in the set of barcodes
            # associated with AGP kits; if it is there, get its ag kit id
            # (a uuid) and follow the source id associated with that AGP
            # barcode to its source and account ids.
            cur.execute(
                "SELECT "
                "ag_kit_barcodes.ag_kit_barcode_id as sample_id, "
                "source.id as source_id, "
                "account.id as account_id, "
                "ag_kit_barcodes.ag_kit_id as kit_id "
                "FROM "
                "ag.ag_kit_barcodes "
                "INNER JOIN "
                "source "
                "ON "
                "ag_kit_barcodes.source_id = source.id "
                "INNER JOIN "
                "account "
                "ON "
                "account.id = source.account_id "
                "WHERE "
                "ag_kit_barcodes.barcode = %s",
                (sample_barcode,))
            result = cur.fetchone()

            if result is not None:
                return result

            # else if the barcode is not associated with a source id, it may
            # still be (more tenuously) associated with an account if it in
            # the set of barcodes associated with AGP kits and the kit it is
            # in has been used to open an AGP account; in this case, we can get
            # an account id and a kit id but NOT a source id.
            # Even if there is no such account association, we can still get
            # the ag kit id (uuid) if this is an AGP kit
            cur.execute(
                "SELECT ag_kit_barcodes.ag_kit_barcode_id as sample_id, "
                "ag_kit_barcodes.ag_kit_id as kit_id, "
                "ag.account.id as account_id "
                "FROM ag.ag_kit_barcodes "
                "INNER JOIN barcodes.barcode "
                "ON ag_kit_barcodes.barcode = barcode.barcode "
                "LEFT OUTER JOIN ag.account "
                "ON barcodes.barcode.kit_id = ag.account.created_with_kit_id "
                "WHERE ag_kit_barcodes.barcode = %s;",
                (sample_barcode,))
            result = cur.fetchone()
            # NB: if still nothing, this is not an AGP-associated barcode so
            # we can't collect any useful ids

            return result

    def retrieve_diagnostics_by_barcode(self, sample_barcode, grab_kit=True):
        def _rows_to_dicts_list(rows):
            return [dict(x) for x in rows]

        with self._transaction.dict_cursor() as cur:
            ids = self._get_ids_relevant_to_barcode(sample_barcode)

            if ids is None:
                ids = {}

            # default for not found is None
            sample_id = ids.get("sample_id")
            source_id = ids.get("source_id")
            account_id = ids.get("account_id")
            # NB: this is the true UUID kit id (the primary key of
            # ag.ag_kit), NOT the kit's participant-facing string "id"
            kit_id = ids.get("kit_id")

            account = None
            source = None
            sample = None
            kit = None

            # get sample object for this barcode, if any
            if sample_id is not None:
                sample_repo = SampleRepo(self._transaction)
                sample = sample_repo._get_sample_by_id(sample_id)

            # get account object for this barcode, if any
            if account_id is not None:
                account_repo = AccountRepo(self._transaction)
                account = account_repo.get_account(account_id)

            # and source object for this barcode, if any
            if source_id is not None:
                source_repo = SourceRepo(self._transaction)
                source = source_repo.get_source(account_id, source_id)

            # get (partial) projects_info list for this barcode
            query = f"""
                    SELECT {p.DB_PROJ_NAME_KEY}, {p.IS_MICROSETTA_KEY},
                    {p.BANK_SAMPLES_KEY}, {p.PLATING_START_DATE_KEY}
                    FROM barcodes.project
                    INNER JOIN barcodes.project_barcode
                    USING (project_id)
                    WHERE barcode=%s;"""

            cur.execute(query, (sample_barcode,))
            # this can't be None; worst-case is an empty list
            projects_info = _rows_to_dicts_list(cur.fetchall())

            # get scans_info list for this barcode
            # NB: ORDER MATTERS here. Do not change the order unless you
            # are positive you know what already depends on it.
            cur.execute("SELECT barcode_scan_id, barcode, "
                        "scan_timestamp, sample_status, "
                        "technician_notes "
                        "FROM barcodes.barcode_scans "
                        "WHERE barcode=%s "
                        "ORDER BY scan_timestamp asc",
                        (sample_barcode,))
            # this can't be None; worst-case is an empty list
            scans_info = _rows_to_dicts_list(cur.fetchall())

            latest_scan = None
            if len(scans_info) > 0:
                # NB: the correctness of this depends on the scans (queried
                # right above) being in ascending order by timestamp
                latest_scan = scans_info[len(scans_info)-1]

            # get details about this barcode itself; CAN be None if the
            # barcode doesn't exist in db
            barcode_info = None
            cur.execute("SELECT barcode, assigned_on, status, "
                        "sample_postmark_date, biomass_remaining, "
                        "sequencing_status, obsolete, "
                        "create_date_time, kit_id "
                        "FROM barcodes.barcode "
                        "WHERE barcode = %s",
                        (sample_barcode,))
            barcode_row = cur.fetchone()
            if barcode_row is not None:
                barcode_info = dict(barcode_row)

            if account is None and source is None and sample is None and \
                    len(projects_info) == 0 and len(scans_info) == 0 \
                    and barcode_info is None:
                return None

            diagnostic = {
                "account": account,
                "source": source,
                "sample": sample,
                "latest_scan": latest_scan,
                "scans_info": scans_info,
                "barcode_info": barcode_info,
                "projects_info": projects_info
            }

            if grab_kit:
                # get kit object
                if kit_id is not None:
                    kit_repo = KitRepo(self._transaction)
                    kit = kit_repo.get_kit_all_samples_by_kit_id(kit_id)
                diagnostic["kit"] = kit

            return diagnostic

    def get_project_name(self, project_id):
        """Obtain the name of a project using the project_id

        Parameters
        ----------
        project_id : int
            The project ID to obtain barcodes for

        Returns
        -------
        str
            The name of the project

        Raises
        ------
        NotFound
            The project ID could not be found
        """
        test = """SELECT EXISTS(
                    SELECT 1
                    FROM barcodes.project
                    WHERE project_id=%s
                  )"""
        query = """SELECT project
                   FROM barcodes.project
                   WHERE project_id=%s"""

        with self._transaction.cursor() as cur:
            cur.execute(test, [project_id, ])
            if not cur.fetchone()[0]:
                raise NotFound(f"Project f'{project_id}' not found")
            else:
                cur.execute(query, [project_id, ])
                return cur.fetchone()[0]

    def get_project_barcodes(self, project_id):
        """Obtain the barcodes associated with a project

        Parameters
        ----------
        project_id : int
            The project ID to obtain barcodes for

        Returns
        -------
        list
            The list of observed barcodes

        Raises
        ------
        NotFound
            The project ID could not be found
        """
        test = """SELECT EXISTS(
                    SELECT 1
                    FROM barcodes.project
                    WHERE project_id=%s
                  )"""
        query = """SELECT barcode
                   FROM barcodes.project_barcode
                   WHERE project_id=%s"""

        with self._transaction.cursor() as cur:
            cur.execute(test, [project_id, ])
            if not cur.fetchone()[0]:
                raise NotFound(f"Project f'{project_id}' not found")
            else:
                cur.execute(query, [project_id, ])
                return list([v[0] for v in cur.fetchall()])

    def create_project(self, project):
        """Create a project entry in the database

        Parameters
        ----------
        project : Project
            A filled project object
        """

        with self._transaction.cursor() as cur:
            if project.project_id is not None:
                id_ = project.project_id
            else:
                cur.execute("SELECT MAX(project_id) + 1 "
                            "FROM barcodes.project")
                id_ = cur.fetchone()[0]

            query = f"""
                    INSERT INTO barcodes.project
                    ({PROJECT_FIELDS})
                    VALUES (
                     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                     %s, %s, %s, %s, %s, %s, %s);"""

            cur.execute(query,
                        [id_, project.project_name, project.is_microsetta,
                         project.bank_samples, project.plating_start_date,
                         project.contact_name, project.additional_contact_name,
                         project.contact_email, project.deadlines,
                         project.num_subjects, project.num_timepoints,
                         project.start_date, project.disposition_comments,
                         project.collection, project.is_fecal,
                         project.is_saliva, project.is_skin, project.is_blood,
                         project.is_other, project.do_16s,
                         project.do_shallow_shotgun, project.do_shotgun,
                         project.do_rt_qpcr, project.do_serology,
                         project.do_metatranscriptomics,
                         project.do_mass_spec, project.mass_spec_comments,
                         project.mass_spec_contact_name,
                         project.mass_spec_contact_email,
                         project.do_other,
                         project.branding_associated_instructions,
                         project.branding_status, project.subproject_name,
                         project.alias, project.sponsor, project.coordination,
                         project.is_active])

        # if we made it this far, all is well
        return id_

    def update_project(self, project_id, project):
        """
        Updates end-user writable information about a project.
        """

        with self._transaction.cursor() as cur:
            # ensure this project exists
            cur.execute(
                "SELECT project_id "
                "FROM barcodes.project "
                "WHERE project_id=%s;",
                (project_id,))

            row = cur.fetchone()
            if row is None:
                raise NotFound("No project with ID %s" % project_id)

            query = f"""
                    UPDATE barcodes.project
                    SET {p.DB_PROJ_NAME_KEY}=%s,
                    {p.SUBPROJECT_NAME_KEY}=%s,
                    {p.ALIAS_KEY}=%s,
                    {p.IS_MICROSETTA_KEY}=%s,
                    {p.SPONSOR_KEY}=%s,
                    {p.COORDINATION_KEY}=%s,
                    {p.CONTACT_NAME_KEY}=%s,
                    {p.ADDTL_CONTACT_NAME_KEY}=%s,
                    {p.CONTACT_EMAIL_KEY}=%s,
                    {p.DEADLINES_KEY}=%s,
                    {p.NUM_SUBJECTS_KEY}=%s,
                    {p.NUM_TIMEPOINTS_KEY}=%s,
                    {p.START_DATE_KEY}=%s,
                    {p.BANK_SAMPLES_KEY}=%s,
                    {p.PLATING_START_DATE_KEY}=%s,
                    {p.DISPOSITION_COMMENTS_KEY}=%s,
                    {p.COLLECTION_KEY}=%s,
                    {p.IS_FECAL_KEY}=%s,
                    {p.IS_SALIVA_KEY}=%s,
                    {p.IS_SKIN_KEY}=%s,
                    {p.IS_BLOOD_KEY}=%s,
                    {p.IS_OTHER_KEY}=%s,
                    {p.DO_16S_KEY}=%s,
                    {p.DO_SHALLOW_SHOTGUN_KEY}=%s,
                    {p.DO_SHOTGUN_KEY}=%s,
                    {p.DO_RT_QPCR_KEY}=%s,
                    {p.DO_SEROLOGY_KEY}=%s,
                    {p.DO_METATRANSCRIPTOMICS_KEY}=%s,
                    {p.DO_MASS_SPEC_KEY}=%s,
                    {p.MASS_SPEC_COMMENTS_KEY}=%s,
                    {p.MASS_SPEC_CONTACT_NAME_KEY}=%s,
                    {p.MASS_SPEC_CONTACT_EMAIL_KEY}=%s,
                    {p.DO_OTHER_KEY}=%s,
                    {p.BRANDING_ASSOC_INSTRUCTIONS_KEY}=%s,
                    {p.BRANDING_STATUS_KEY}=%s
                    WHERE project_id=%s;"""

            cur.execute(query,
                        (
                            project.project_name,
                            project.subproject_name,
                            project.alias,
                            project.is_microsetta,
                            project.sponsor,
                            project.coordination,
                            project.contact_name,
                            project.additional_contact_name,
                            project.contact_email,
                            project.deadlines,
                            project.num_subjects,
                            project.num_timepoints,
                            project.start_date,
                            project.bank_samples,
                            project.plating_start_date,
                            project.disposition_comments,
                            project.collection,
                            project.is_fecal,
                            project.is_saliva,
                            project.is_skin,
                            project.is_blood,
                            project.is_other,
                            project.do_16s,
                            project.do_shallow_shotgun,
                            project.do_shotgun,
                            project.do_rt_qpcr,
                            project.do_serology,
                            project.do_metatranscriptomics,
                            project.do_mass_spec,
                            project.mass_spec_comments,
                            project.mass_spec_contact_name,
                            project.mass_spec_contact_email,
                            project.do_other,
                            project.branding_associated_instructions,
                            project.branding_status,
                            project_id
                        ))
            return cur.rowcount == 1

    def delete_project_by_name(self, project_name):
        """Delete a project entry and its associations to barcodes from db

        Parameters
        ----------
        project_name : str
            The name of the project to delete
        """
        with self._transaction.cursor() as cur:
            # delete associations between this project and any barcodes
            cur.execute("DELETE FROM barcodes.project_barcode "
                        "WHERE project_id in ("
                        "SELECT project_id FROM barcodes.project "
                        "WHERE project = %s)",
                        (project_name,))

            # now delete the project itself
            cur.execute("DELETE FROM barcodes.project WHERE project = %s",
                        (project_name,))
            return cur.rowcount == 1

    def get_projects(self, include_stats, is_active_val=None):
        """Return a list of Project objects, ordered by project id.

        Parameters
        ----------
        is_active_val : True, False, or None.
            If True or False, the resulting project list will be filtered
            to include only the projects with that active status. If None, all
            projects will be returned regardless of active status.
        """

        # read all kinds of project info and computed counts from the db
        # into a pandas data frame
        projects_df = self._read_projects_df_from_db(
            include_stats=include_stats)

        # if an active value has been provided, look only at project records
        # that have that active value.  NB this has to be a test against None,
        # not against "false-ish" (if not is_active_val)
        if is_active_val is not None:
            is_active_val_mask = projects_df[p.IS_ACTIVE_KEY] == is_active_val
            filtered_df = projects_df.loc[is_active_val_mask]
            projects_df = filtered_df

        if include_stats:
            # cut stats columns out into own df (w same index as projects one)
            stats_keys = p.get_computed_stats_keys()
            stats_df = projects_df[stats_keys].copy()
            projects_df = projects_df.drop(stats_keys, axis=1)

            # within computed stats columns (ONLY--does not apply to
            # descriptive columns from the project table, where None is
            # a real, non-numeric value), NaN and None (which pandas treats as
            # interchangeable :-| ) should be converted to zero.  Everything
            # else should be cast to an integer; for some weird reason pandas
            # is pulling in counts as floats
            stats_df = stats_df.fillna(0).astype(int)

            stats_dict = stats_df.to_dict(orient='index')

        result = []
        # NB: *dataframe*'s to_dict automatically converts numpy data types
        # (e.g., numpy.bool_, numpy.int64) to appropriate python-native data
        # types, but *series* to_dict does NOT do this automatic conversion
        # (at least, as of this writing).  Be cautious if refactoring the below
        projects_dict = projects_df.to_dict(orient='index')
        for k, v in projects_dict.items():
            if include_stats:
                v[p.COMPUTED_STATS_KEY] = stats_dict[k]
            result.append(p.Project.from_dict(v))

        return result

    def _generate_random_kit_name(self, name_length, prefix):
        if prefix is None:
            prefix = 'tmi'

        # O, o, S, I and l removed to improve readability
        chars = 'abcdefghijkmnpqrstuvwxyz' + 'ABCDEFGHJKMNPQRTUVWXYZ'
        chars += string.digits
        rand_name = ''.join(random.choice(chars)
                            for i in range(name_length))
        return prefix + '_' + rand_name

    def create_kits(self, number_of_kits, number_of_samples, kit_prefix,
                    project_ids):
        """Create multiple kits, each with the same number of samples

        Parameters
        ----------
        number_of_kits : int
            Number of kits to create
        number_of_samples : int
            Number of samples that each kit will contain
        kit_prefix : str or None
            A prefix to put on to the kit IDs, this is optional.
        project_ids : list of int
            Project ids the samples are to be associated with
        """

        kit_names = self._generate_novel_kit_names(number_of_kits, kit_prefix)
        kit_name_and_barcode_tuples_list, new_barcodes = \
            self._generate_novel_barcodes(
                number_of_kits, number_of_samples, kit_names)

        return self._create_kits(kit_names, new_barcodes,
                                 kit_name_and_barcode_tuples_list,
                                 number_of_samples, project_ids)

    def _are_any_projects_tmi(self, project_ids):
        """Return true if any input projects are part of microsetta"""

        with self._transaction.cursor() as cur:
            # get existing projects
            query = f"""
                    SELECT project_id,
                    {p.IS_MICROSETTA_KEY}
                    FROM barcodes.project;"""

            cur.execute(query)
            projects_tmi = {id_: bool(tmi) for id_, tmi in cur.fetchall()}
            is_tmi = False
            for input_proj_id in project_ids:
                if input_proj_id not in projects_tmi:
                    raise KeyError("Project id %s does not exist" %
                                   input_proj_id)

                # if *any* of the projects the kits will be associate with are
                # microsetta projects, set is_tmi to true
                if projects_tmi[input_proj_id]:
                    is_tmi = True

        return is_tmi

    def _generate_novel_kit_names(self, number_of_kits, kit_prefix):
        """Generate list of random kit names having input prefix"""

        kit_names = [self._generate_random_kit_name(8, kit_prefix)
                     for i in range(number_of_kits)]

        with self._transaction.cursor() as cur:
            # get existing kits to test for conflicts
            cur.execute("""SELECT kit_id FROM barcodes.kit""")
            existing = set(cur.fetchall())

            # if we observe ANY conflict, let's bail. This should be extremely
            # rare, from googling seemed a easier than having postgres
            # generate a unique identifier that was reasonably short, hard to
            # guess
            if len(set(kit_names) - existing) != number_of_kits:
                raise KeyError("Conflict in created names, kits not created")

        return kit_names

    def _generate_novel_barcodes(self, number_of_kits, number_of_samples,
                                 kit_names):
        """Generate specified number of random barcodes for input kit names"""

        with self._transaction.cursor() as cur:
            # get the maximum observed barcode.
            # historically, barcodes were of the format NNNNNNNNN where each
            # position was a digit. this has created many problems on
            # subsequent use as Excel and other tools naively assume these
            # values are numeric. As of 16APR2020, barcodes will be of the
            # format XNNNNNNNN where the first position is considered a
            # control character that cannot safely be considered a digit.
            # this is *safe* for all prior barcodes as the first character
            # has always been the "0" character.
            total_barcodes = number_of_kits * number_of_samples
            cur.execute("SELECT max(right(barcode,8)::integer) "
                        "FROM barcodes.barcode")
            start_bc = cur.fetchone()[0] + 1
            new_barcodes = ['X%0.8d' % (start_bc + i)
                            for i in range(total_barcodes)]

            kit_name_and_barcode_tuples_list = []
            barcode_offset = range(0, total_barcodes, number_of_samples)
            for offset, name in zip(barcode_offset, kit_names):
                for i in range(number_of_samples):
                    kit_name_and_barcode_tuples_list.append(
                        (name, new_barcodes[offset + i]))

        return kit_name_and_barcode_tuples_list, new_barcodes

    def _create_kits(self, kit_names, new_barcodes,
                     kit_name_and_barcode_tuples_list,
                     number_of_samples, project_ids, kits_details=None):
        """Create one or more kits from input parallel lists

        Parameters
        ----------
        kit_names: list of str
            Value inside the kit box (e.g., "DM24-A3CF9")
        new_barcodes: list of str
            Tube/collection device barcode (e.g., "DMX00-0001")
        kit_name_and_barcode_tuples_list: list of tuple of str
            Kit name and associated barcode (one tuple per barcode)
        number_of_samples: int
            Number of samples (barcodes) in each kit
        project_ids : list of int
            Project ids that all barcodes are to be associated with
        box_ids: list of str (optional)
            Value on outside of kit box (e.g., "DM89D-VW6Y").  If not provided,
            kit uuid is used instead.
        """

        # integer project ids come in as strings ...
        project_ids = [int(x) for x in project_ids]

        is_tmi = self._are_any_projects_tmi(project_ids)

        with self._transaction.cursor() as cur:
            # create barcode project associations
            barcode_projects = []
            for barcode in new_barcodes:
                for prj_id in project_ids:
                    barcode_projects.append((barcode, prj_id))

            # create kits in kit table
            new_kit_uuids = [str(uuid.uuid4()) for x in kit_names]
            barcode_kit_inserts = _get_kit_tuples(
                new_kit_uuids, kit_names, kits_details)

            cur.executemany("INSERT INTO barcodes.kit "
                            "(kit_uuid, kit_id, outbound_fedex_tracking, "
                            "address, inbound_fedex_tracking, box_id) "
                            "VALUES (%s, %s, %s, %s, %s, %s)",
                            barcode_kit_inserts)

            # add new barcodes to barcode table
            barcode_insertions = [(n, b, 'unassigned')
                                  for n, b in kit_name_and_barcode_tuples_list]
            cur.executemany("INSERT INTO barcode (kit_id, barcode, status) "
                            "VALUES (%s, %s, %s)",
                            barcode_insertions)

            # add project information to project_barcode table
            cur.executemany("INSERT INTO project_barcode "
                            "(barcode, project_id) "
                            "VALUES (%s, %s)", barcode_projects)

            if is_tmi:
                # create a record for each new kit in ag_kit table
                ag_kit_inserts = [
                    (str(uuid.uuid4()), kit_name, number_of_samples)
                    for kit_name in kit_names]
                cur.executemany("INSERT INTO ag.ag_kit "
                                "(ag_kit_id, supplied_kit_id, swabs_per_kit) "
                                "VALUES (%s, %s, %s)",
                                ag_kit_inserts)

                # for each new barcode, add a record to the ag_kit_barcodes
                # table associating it to its ag kit, creating a new
                # "sample_barcode"
                kit_id_to_ag_kit_id = {k: u for u, k, _ in ag_kit_inserts}
                kit_barcodes_insert = [(kit_id_to_ag_kit_id[i], b)
                                       for i, b
                                       in kit_name_and_barcode_tuples_list]
                cur.executemany("INSERT INTO ag_kit_barcodes "
                                "(ag_kit_id, barcode) "
                                "VALUES (%s, %s)",
                                kit_barcodes_insert)

        # get the info on the just-created kits/barcodes and return it
        with self._transaction.dict_cursor() as cur:
            cur.execute("SELECT i.kit_id, o.kit_uuid, o.box_id, o.address,"
                        "o.outbound_fedex_tracking, o.inbound_fedex_tracking, "
                        "i.sample_barcodes "
                        "FROM (SELECT kit_id, "
                        "             array_agg(barcode) as sample_barcodes "
                        "      FROM barcodes.kit "
                        "      JOIN barcodes.barcode USING (kit_id) "
                        "      WHERE kit_id IN %s "
                        "      GROUP BY kit_id) i "
                        "JOIN barcodes.kit o USING (kit_id)",
                        (tuple(kit_names), ))

            created = [{'kit_id': k, 'kit_uuid': u, 'box_id': bx,
                        'address': a, 'outbound_fedex_tracking': oft,
                        'inbound_fedex_tracking': ift,
                        'sample_barcodes': b}
                       for k, u, bx, a, oft, ift, b in cur.fetchall()]

        if len(kit_names) != len(created):
            raise KeyError("Not all created kits could be retrieved")

        return {'created': created}

    def create_kit(self, kit_name, box_id, address_dict,
                   outbound_fedex_code, inbound_fedex_code,
                   barcodes_list, project_ids):
        """Create a single kit

        Parameters
        ----------
        kit_name: str
            Value inside the kit box (e.g., "DM24-A3CF9")
        box_id: str
            Value on outside of kit box (e.g., "DM89D-VW6Y")
        address_dict: dict or None
            Address to which the kit was shipped, in format used by Daklapack
        outbound_fedex_code: str or None
            fedex tracking number for shipping kit to a microsetta participant;
            may be None if e.g. kit was handed out in person
        inbound_fedex_code: str or None
            fedex tracking number for returning kit to microsetta project;
            may be None if e.g. kit was purchased in bulk for a subproject
        barcodes_list: list of str
            Tube/collection device barcode (e.g., "DMX00-0001")
        project_ids : list of int
            Project ids that all barcodes in kit are to be associated with
        """

        kit_names = [kit_name]
        address = None if address_dict is None else json.dumps(address_dict)
        kit_details = [{KIT_BOX_ID_KEY: box_id,
                       KIT_ADDRESS_KEY: address,
                       KIT_OUTBOUND_KEY: outbound_fedex_code,
                       KIT_INBOUND_KEY: inbound_fedex_code}]
        kit_name_and_barcode_tuples_list = \
            [(kit_name, x) for x in barcodes_list]

        return self._create_kits(kit_names, barcodes_list,
                                 kit_name_and_barcode_tuples_list,
                                 len(barcodes_list), project_ids, kit_details)

    def retrieve_diagnostics_by_kit_id(self, supplied_kit_id):
        kit_repo = KitRepo(self._transaction)
        kit = kit_repo.get_kit_all_samples(supplied_kit_id)

        if kit is None:
            return None

        sample_assoc = []
        for sample in kit.samples:
            sample_assoc.append(
                self.retrieve_diagnostics_by_barcode(sample.barcode,
                                                     grab_kit=False))

        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT "
                "ag_login_id as account_id "
                "FROM "
                "ag_kit "
                "WHERE "
                "supplied_kit_id = %s",
                (supplied_kit_id,))
            row = cur.fetchone()

        pre_microsetta_acct = None
        if row['account_id'] is not None:
            acct_repo = AccountRepo(self._transaction)
            # This kit predated the microsetta migration, let's pull in the
            # account info associated with it
            pre_microsetta_acct = acct_repo.get_account(row['account_id'])

        # obtain information on any accounts created using the kit ID
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT id as account_id "
                "FROM "
                "account "
                "WHERE "
                "created_with_kit_id = %s",
                (supplied_kit_id, ))
            rows = cur.fetchall()

        accounts_created = None
        if len(rows) > 0:
            acct_repo = AccountRepo(self._transaction)
            accounts_created = [acct_repo.get_account(row['account_id'])
                                for row in rows]

        diagnostic = {
            'accounts_created': accounts_created,
            'kit_id': kit.id,
            'supplied_kit_id': supplied_kit_id,
            'kit': kit,
            'pre_microsetta_acct': pre_microsetta_acct,
            'sample_diagnostic_info': sample_assoc
        }

        return diagnostic

    def retrieve_diagnostics_by_email(self, email):

        acct_repo = AccountRepo(self._transaction)
        ids = acct_repo.get_account_ids_by_email(email)

        if len(ids) == 0:
            return None

        accts = [acct_repo.get_account(acct_id) for acct_id in ids]
        diagnostic = {
            "accounts": accts
        }

        return diagnostic

    def scan_barcode(self, sample_barcode, scan_info):
        with self._transaction.cursor() as cur:

            # not actually using the result, just checking there IS one
            # to ensure this is a valid barcode
            cur.execute(
                "SELECT barcode FROM barcodes.barcode WHERE barcode=%s",
                (sample_barcode,)
            )

            if cur.rowcount == 0:
                raise NotFound("No such barcode: %s" % sample_barcode)
            elif cur.rowcount > 1:
                # Note: This "can't" happen.
                raise RepoException("ERROR: Multiple barcode entries would be "
                                    "affected by scan; failing out")

            # put a new row in the barcodes.barcode_scans table
            new_uuid = str(uuid.uuid4())
            scan_args = (
                new_uuid,
                sample_barcode,
                datetime.datetime.now(),
                scan_info['sample_status'],
                scan_info['technician_notes']
            )

            cur.execute(
                "INSERT INTO barcodes.barcode_scans "
                "(barcode_scan_id, barcode, scan_timestamp, "
                "sample_status, technician_notes) "
                "VALUES (%s, %s, %s, %s, %s)",
                scan_args
            )

            return new_uuid

    def search_barcode(self, sql_cond, cond_params):
        # Security Note:
        # Even with sql queries correctly escaped,
        # exposing a conditional query oracle
        # with unlimited queries grants full read access
        # to all tables joined within the query
        # That is, administrator users searching with
        # this method can reconstruct
        # project_barcode, ag_kit_barcodes and barcode_scans
        # given enough queries, including columns
        # that are not returned by the select
        with self._transaction.cursor() as cur:
            cur.execute(
                sql.SQL("""SELECT project_barcode.barcode
                           FROM project_barcode
                           LEFT JOIN ag_kit_barcodes USING (barcode)
                           LEFT JOIN barcodes.barcode_scans USING (barcode)
                           LEFT JOIN (
                               SELECT barcode,
                                      max(scan_timestamp)
                                          AS scan_timestamp_latest
                               FROM barcodes.barcode_scans
                               GROUP BY barcode
                           ) AS latest_scan
                           ON barcode_scans.barcode = latest_scan.barcode
                               AND barcode_scans.scan_timestamp =
                                   latest_scan.scan_timestamp_latest
                           WHERE {cond}""").format(cond=sql_cond),
                cond_params
            )
            return [r[0] for r in cur.fetchall()]

    def get_survey_metadata(self, sample_barcode, survey_template_id=None):
        ids = self._get_ids_relevant_to_barcode(sample_barcode)

        if ids is None:
            raise NotFound("No such barcode")

        account_id = ids.get('account_id')
        source_id = ids.get('source_id')
        sample_id = ids.get('sample_id')

        account = None
        source = None
        sample = None
        if sample_id is not None:
            sample_repo = SampleRepo(self._transaction)
            sample = sample_repo._get_sample_by_id(sample_id)

        if source_id is not None and account_id is not None:
            source_repo = SourceRepo(self._transaction)
            account_repo = AccountRepo(self._transaction)
            account = account_repo.get_account(account_id)
            source = source_repo.get_source(account_id, source_id)

        if source is None:
            raise RepoException("Barcode is not associated with a source")

        host_subject_id = source_repo.get_host_subject_id(source)

        survey_answers_repo = SurveyAnswersRepo(self._transaction)
        answer_ids = survey_answers_repo.list_answered_surveys_by_sample(
            account_id, source_id, sample_id)

        answer_to_template_map = {}
        for answer_id in answer_ids:
            template_id, status = survey_answers_repo.\
                survey_template_id_and_status(answer_id)
            answer_to_template_map[answer_id] = (template_id, status)

        # if a survey template is specified, filter the returned surveys
        if survey_template_id is not None:
            # TODO: This schema is so awkward for this type of query...
            answers = []
            for answer_id in answer_ids:
                if answer_to_template_map[answer_id][0] == survey_template_id:
                    answers.append(answer_id)

            if len(answers) == 0:
                raise NotFound("This barcode is not associated with any "
                               "surveys matching this template id")
            if len(answers) > 1:
                #  I really hope this can't happen.  (x . x)
                raise RepoException("This barcode is associated with more "
                                    "than one survey matching this template"
                                    " id")
            answer_ids = answers

        metadata_map = survey_answers_repo.build_metadata_map()

        all_survey_answers = []
        for answer_id in answer_ids:
            answer_model = survey_answers_repo.get_answered_survey(
                account_id,
                source_id,
                answer_id,
                "en_US"
            )

            if answer_model is None:
                # if answers are requested for a vioscreen survey
                # the answers model will comeback empty so let's
                # gracefully handle this
                continue

            survey_answers = {}
            for k in answer_model:
                new_k = metadata_map[int(k)]
                survey_answers[k] = [new_k, answer_model[k]]

            all_survey_answers.append(
                {
                    "template": answer_to_template_map[answer_id][0],
                    "survey_status": answer_to_template_map[answer_id][1],
                    "response": survey_answers
                })

        pulldown = {
            "sample_barcode": sample_barcode,
            "host_subject_id": host_subject_id,
            "account": account,
            "source": source,
            "sample": sample,
            "survey_answers": all_survey_answers
        }

        return pulldown

    def get_daklapack_articles(self, include_retired=False):
        retired_constraint = "" if include_retired else "WHERE retired = False"
        cmd = f"SELECT dak_article_id, dak_article_code, short_description, " \
              f"detailed_description " \
              f"FROM barcodes.daklapack_article {retired_constraint} " \
              f"ORDER BY daklapack_article.dak_article_code;"
        with self._transaction.dict_cursor() as cur:
            cur.execute(cmd)
            rows = cur.fetchall()
            return [dict(x) for x in rows]

    def create_daklapack_order(self, daklapack_order):
        order_id = daklapack_order.id

        order_args = (
            order_id,
            daklapack_order.submitter_acct.id,
            daklapack_order.description,
            daklapack_order.planned_send_date,
            daklapack_order.order_json,
            daklapack_order.creation_timestamp,
            daklapack_order.last_polling_timestamp,
            daklapack_order.last_polling_status
        )

        with self._transaction.cursor() as cur:
            cur.execute(
                "INSERT INTO barcodes.daklapack_order "
                "(dak_order_id, submitter_acct_id, description, "
                "planned_send_date, order_json, creation_timestamp, "
                "last_polling_timestamp, last_polling_status) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                order_args
            )

            project_ids = daklapack_order.project_ids_list
            project_ids_tuples = [(order_id, i) for i in project_ids]

            insert_sql = 'insert into barcodes.daklapack_order_to_project' \
                         ' (dak_order_id, project_id) values %s'
            psycopg2.extras.execute_values(cur, insert_sql, project_ids_tuples,
                                           template=None, page_size=100)

        return order_id

    def get_unfinished_daklapack_order_ids(self):
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT dak_order_id "
                "FROM "
                "barcodes.daklapack_order "
                "WHERE last_polling_status NOT IN (%s, %s) "
                "OR last_polling_status IS NULL "
                "ORDER BY last_polling_timestamp DESC;",
                ("Sent", "Error"))
            rows = cur.fetchall()
            return [x[0] for x in rows]

    def get_projects_for_dak_order(self, dak_order_id):
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT project_id "
                "FROM "
                "barcodes.daklapack_order_to_project "
                "WHERE dak_order_id = %s "
                "ORDER BY project_id ASC;",
                (dak_order_id,))
            rows = cur.fetchall()
            return [x[0] for x in rows]

    def set_daklapack_order_poll_info(
            self, dak_order_id, last_polling_timestamp, last_polling_status):

        with self._transaction.cursor() as cur:
            cur.execute(
                "UPDATE barcodes.daklapack_order "
                "SET "
                "last_polling_timestamp = %s, "
                "last_polling_status = %s "
                "WHERE dak_order_id = %s",
                (last_polling_timestamp, last_polling_status, dak_order_id)
            )

    def set_kit_uuids_for_dak_order(self, dak_order_id, kit_uuids):
        kit_uuid_tuples = [(dak_order_id, i) for i in kit_uuids]

        insert_sql = 'insert into barcodes.daklapack_order_to_kit' \
                     ' (dak_order_id, kit_uuid) values %s'
        with self._transaction.cursor() as cur:
            psycopg2.extras.execute_values(cur, insert_sql, kit_uuid_tuples,
                                           template=None, page_size=100)
