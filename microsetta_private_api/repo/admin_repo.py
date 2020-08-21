import uuid
import string
import random
import datetime
import pandas as pd

from microsetta_private_api.exceptions import RepoException

from microsetta_private_api.model.project import Project, COMPUTED_STATS_KEY, \
    get_computed_stats_keys, SAMPLE_STATUSES, get_num_status_keys,\
    NUM_KITS_KEY, NUM_SAMPLES_KEY, NUM_UNIQUE_SOURCES_KEY, \
    NUM_SAMPLES_RECEIVED_KEY, NUM_FULLY_RETURNED_KITS_KEY, \
    NUM_PARTIALLY_RETURNED_KITS_KEY, NUM_KITS_W_PROBLEMS_KEY, \
    VALID_SAMPLES_STATUS
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.repo.kit_repo import KitRepo
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.repo.source_repo import SourceRepo

from werkzeug.exceptions import NotFound
from hashlib import sha512

from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo

# TODO: Refactor repeated elements in project-related sql queries?
PROJECTS_BASICS_SQL = """
    SELECT
    p.*,
    count(distinct barcode) as {0},  -- number of samples
    count(distinct kit_id) as {1}  -- number of kits
    FROM barcodes.project as p
    LEFT JOIN
    barcodes.project_barcode
    USING (project_id)
    LEFT JOIN
    barcodes.barcode
    USING (barcode)
    GROUP BY project_id
    ORDER BY project_id;
"""

# The below sql statements pull various computed counts about projects.
# Each query must follow the convention that it returns a column named
# "project_id" to join on, and that all other columns it returns are unique
# to that query (not also returned by any other query).
NUM_UNIQUE_SOURCES_SQL = """
    SELECT project_barcode.project_id,
    count(distinct ag_kit_barcodes.source_id) as {0}  --num_unique_sources
    FROM barcodes.project_barcode
    INNER JOIN ag.ag_kit_barcodes
    USING (barcode)
    GROUP BY project_id
    ORDER BY project_id; """

NUM_RECEIVED_SAMPLES_SQL = """
    SELECT project_id,
    count(distinct barcode) as {0}  --num_samples_received
    FROM project_barcode
    INNER JOIN
    barcode_scans
    USING (barcode)
    GROUP BY project_id
    ORDER BY project_id; """

NUM_FULLY_RECEIVED_KITS_SQL = """
    SELECT project_id,
    count(distinct ag_kit_id) as {0}  --num_fully_returned_kits
    FROM (
        -- query to get a list of kits for which ALL samples have been
        -- returned (not guaranteed to be returned *valid*, just
        -- returned), per project.  Uses an intersect to only keep kits
        -- for which the total number of samples in a kit matches the
        -- number of returned (scanned) samples for that kit.

        -- get total number of samples (barcodes) in each kit, per proj
        SELECT
        project_barcode.project_id,
        ag_kit_barcodes.ag_kit_id,
        count(ag_kit_barcodes.barcode)
        FROM ag.ag_kit_barcodes
        LEFT JOIN barcodes.project_barcode
        USING (barcode)
        GROUP BY project_id, ag_kit_id
        INTERSECT
        -- get the number of returned samples (via latest barcode scan)
        -- in each kit with at least one returned sample, per project
        SELECT
        project_barcode.project_id,
        ag_kit_barcodes.ag_kit_id,
        count(barcode_scans.barcode)
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
        USING (barcode)
        GROUP BY project_id, ag_kit_id
        ORDER BY project_id, ag_kit_id
        ) as kits_list
        GROUP BY project_id
        ORDER BY project_id;
    """


def _make_statuses_sql(_):
    first_chunk = """
        SELECT * FROM crosstab(
            $$select p.project_id, scans.sample_status,
            coalesce(count(scans.barcode),0)
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
            ON pb.barcode = latest_scan.barcode
            GROUP BY project_id, sample_status
            ORDER BY project_id,
            CASE sample_status """

    second_chunk = """
            END; $$,
            $$VALUES """

    third_chunk = """; $$
        ) AS ct(project_id bigint, """

    fourth_chunk = """)
        ORDER BY ct;"""

    cases = []
    values = []
    colnames = []
    case_num = 1
    for curr_status in SAMPLE_STATUSES:
        cases.append("WHEN '{0}' THEN {1} ".format(curr_status, case_num))
        values.append("('{0}')".format(curr_status))
        case_num += 1

    num_status_keys = get_num_status_keys()
    for curr_num_status_key in num_status_keys:
        colnames.append("{0} bigint".format(curr_num_status_key))

    cases_sql = " ".join(cases)
    values_sql = ", ".join(values)
    colnames_sql = ", ".join(colnames)

    final_sql = "{}{}{}{}{}{}{}".format(first_chunk, cases_sql, second_chunk,
                                        values_sql, third_chunk, colnames_sql,
                                        fourth_chunk)

    return final_sql


def _make_received_kits_sql(count_name, limit_to_problems):
    first_chunk = """
        SELECT project_barcode.project_id,
        -- num_partially_returned_kits
        count(distinct ag_kit_barcodes.ag_kit_id) as {0}
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
        USING (barcode)"""

    second_chunk = """
        GROUP BY project_barcode.project_id
        ORDER BY project_barcode.project_id
    """

    limit_to_problems_chunk = """
        -- this constraint limits query to getting number of kits with
        -- at least one PROBLEM sample
        WHERE barcode_scans.sample_status <> '{0}'
    """

    constraint = ""
    if limit_to_problems:
        constraint = limit_to_problems_chunk.format(VALID_SAMPLES_STATUS)

    qualified_first_chunk = first_chunk.format(count_name)
    final_sql = "{}{}{}".format(qualified_first_chunk, constraint,
                                second_chunk)
    return final_sql


# NB: PROJECTS_BASICS_SQL *must* come first since its list of project id is a
# superset of other queries' lists.
_PROJECT_SQLS = [
                ((NUM_KITS_KEY, NUM_SAMPLES_KEY), PROJECTS_BASICS_SQL),
                ((NUM_UNIQUE_SOURCES_KEY,), NUM_UNIQUE_SOURCES_SQL),
                ((NUM_SAMPLES_RECEIVED_KEY,), NUM_RECEIVED_SAMPLES_SQL),
                (("statuses",), _make_statuses_sql),
                ((NUM_PARTIALLY_RETURNED_KITS_KEY, False),
                 _make_received_kits_sql),
                ((NUM_KITS_W_PROBLEMS_KEY, True),
                 _make_received_kits_sql),
                ((NUM_FULLY_RETURNED_KITS_KEY,), NUM_FULLY_RECEIVED_KITS_SQL)
                ]


class AdminRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def _read_projects_df_from_db(self):
        """Return pandas data frame of project info and statistics from db."""

        projects_df = None

        # TODO: should cursor be created here or no?
        # https://www.datacamp.com/community/tutorials/tutorial-postgresql-python  # noqa
        # shows creation of a cursor even though no methods are called on it
        with self._transaction.dict_cursor():
            # TODO: is there a better way to access this?
            conn = self._transaction._conn

            for stats_keys, sql_source in _PROJECT_SQLS:
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
            cur.execute("SELECT project, is_microsetta, "
                        "bank_samples, plating_start_date "
                        "FROM barcodes.project "
                        "INNER JOIN barcodes.project_barcode "
                        "USING (project_id) "
                        "WHERE barcode=%s",
                        (sample_barcode,))
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

            cur.execute("INSERT INTO barcodes.project "
                        "(project_id, project, is_microsetta, bank_samples, "
                        "plating_start_date, contact_name, "
                        "additional_contact_name, contact_email, "
                        "deadlines, num_subjects, num_timepoints, start_date, "
                        "disposition_comments, collection,"
                        "is_fecal, is_saliva, is_skin, is_blood, is_other, "
                        "do_16s, do_shallow_shotgun, do_shotgun, do_rt_qpcr, "
                        "do_serology, do_metatranscriptomics, do_mass_spec, "
                        "mass_spec_comments, mass_spec_contact_name, "
                        "mass_spec_contact_email, do_other, "
                        "branding_associated_instructions, branding_status, "
                        "subproject_name, alias, sponsor, coordination"
                        ") "
                        "VALUES ("
                        " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                        " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                        " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                        " %s, %s, %s, %s, %s, %s)",
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
                         project.alias, project.sponsor, project.coordination])

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

            cur.execute("UPDATE barcodes.project "
                        "SET project=%s, "
                        "subproject_name=%s, "
                        "alias=%s, "
                        "is_microsetta=%s, "
                        "sponsor=%s, "
                        "coordination=%s, "
                        "contact_name=%s, "
                        "additional_contact_name=%s, "
                        "contact_email=%s, "
                        "deadlines=%s, "
                        "num_subjects=%s, "
                        "num_timepoints=%s, "
                        "start_date=%s, "
                        "bank_samples=%s, "
                        "plating_start_date=%s, "
                        "disposition_comments=%s, "
                        "collection=%s, "
                        "is_fecal=%s, "
                        "is_saliva=%s, "
                        "is_skin=%s, "
                        "is_blood=%s, "
                        "is_other=%s, "
                        "do_16s=%s, "
                        "do_shallow_shotgun=%s, "
                        "do_shotgun=%s, "
                        "do_rt_qpcr=%s, "
                        "do_serology=%s, "
                        "do_metatranscriptomics=%s, "
                        "do_mass_spec=%s, "
                        "mass_spec_comments=%s, "
                        "mass_spec_contact_name=%s, "
                        "mass_spec_contact_email=%s, "
                        "do_other=%s, "
                        "branding_associated_instructions=%s, "
                        "branding_status=%s "
                        "WHERE project_id=%s;",
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

    def get_projects(self):
        """Return a list of Project objects, ordered by project id."""

        # read all kinds of project info and computed counts from the db
        # into a pandas data frame
        projects_df = self._read_projects_df_from_db()

        # convert data frame into dictionary of dictionaries;
        # important to use built-in pandas method, which automatically
        # converts numpy data types (e.g., numpy.bool_, numpy.int64) to
        # appropriate python-native data types
        projects_dict = projects_df.to_dict(orient='index')

        # turn the above dictionary into a list of Project objects, ordered
        # by project id, while also pulling out the computed statistics for
        # each project into their own sub-dictionary in the Project object.
        result = []
        for k, v in projects_dict.items():
            stats_dict = {}
            # pull computed statistics out of main project dictionary and
            # into a sub-dictionary, cleaning them up in the process
            computed_stats_keys = get_computed_stats_keys()
            for curr_stats_key in computed_stats_keys:
                curr_stat = v.pop(curr_stats_key)

                # only NaN returns false when compared to itself;
                # in case of NaN, set value of metric to 0
                if curr_stat != curr_stat:
                    curr_stat = 0
                # alternately, if the metric is an integer, cast it to that;
                # for some weird reason pandas is pulling in counts as floats
                elif curr_stat == int(curr_stat):
                    curr_stat = int(curr_stat)

                stats_dict[curr_stats_key] = curr_stat

            v[COMPUTED_STATS_KEY] = stats_dict
            a_project = Project(**v)
            result.append(a_project)

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
                    projects):
        """Create kits each with the same number of samples

        Parameters
        ----------
        number_of_kits : int
            Number of kits to create
        number_of_samples : int
            Number of samples that each kit will contain
        kit_prefix : str or None
            A prefix to put on to the kit IDs, this is optional.
        projects : list of str
            Project names the samples are to be associated with
        """
        with self._transaction.cursor() as cur:
            # get existing projects
            cur.execute("SELECT project, project_id, is_microsetta "
                        "FROM barcodes.project")
            known_projects = {prj: (id_, tmi)
                              for prj, id_, tmi in cur.fetchall()}
            is_tmi = False
            for name in projects:
                if name not in known_projects:
                    raise KeyError("%s does not exist" % name)
                if known_projects[name][1]:
                    is_tmi = True

            # get existing kits to test for conflicts
            cur.execute("""SELECT kit_id FROM barcodes.kit""")
            existing = set(cur.fetchall())
            names = [self._generate_random_kit_name(8, kit_prefix)
                     for i in range(number_of_kits)]

            # if we observe ANY conflict, lets bail. This should be extremely
            # rare, from googling seemed a easier than having postgres
            # generate a unique identifier that was reasonably short, hard to
            # guess
            if len(set(names) - existing) != number_of_kits:
                raise KeyError("Conflict in created names, kits not created")

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

            # partition up barcodes and associate to kit names
            kit_barcodes = []
            barcode_offset = range(0, total_barcodes, number_of_samples)
            for offset, name in zip(barcode_offset, names):
                for i in range(number_of_samples):
                    kit_barcodes.append((name, new_barcodes[offset + i]))

            # create barcode project associations
            barcode_projects = []
            for barcode in new_barcodes:
                for project in projects:
                    prj_id = known_projects[project][0]
                    barcode_projects.append((barcode, prj_id))

            # create shipping IDs
            cur.executemany("INSERT INTO barcodes.kit "
                            "(kit_id) "
                            "VALUES (%s)", [(n, ) for n in names])

            # add a new barcode to barcode table
            barcode_insertions = [(n, b, 'unassigned')
                                  for n, b in kit_barcodes]
            cur.executemany("INSERT INTO barcode (kit_id, barcode, status) "
                            "VALUES (%s, %s, %s)",
                            barcode_insertions)

            # add project information
            cur.executemany("INSERT INTO project_barcode "
                            "(barcode, project_id) "
                            "VALUES (%s, %s)", barcode_projects)

            if is_tmi:
                # create a record for the new kit in ag_kit table
                ag_kit_inserts = [(str(uuid.uuid4()), name, number_of_samples)
                                  for name in names]
                cur.executemany("INSERT INTO ag.ag_kit "
                                "(ag_kit_id, supplied_kit_id, swabs_per_kit) "
                                "VALUES (%s, %s, %s)",
                                ag_kit_inserts)

                # associate the new barcode to a new sample id and
                # to the new kit in the ag_kit_barcodes table
                kit_id_to_ag_kit_id = {k: u for u, k, _ in ag_kit_inserts}
                kit_barcodes_insert = [(kit_id_to_ag_kit_id[i], b)
                                       for i, b in kit_barcodes]
                cur.executemany("INSERT INTO ag_kit_barcodes "
                                "(ag_kit_id, barcode) "
                                "VALUES (%s, %s)",
                                kit_barcodes_insert)

        with self._transaction.dict_cursor() as cur:
            cur.execute("SELECT i.kit_id, o.kit_uuid, i.sample_barcodes "
                        "FROM (SELECT kit_id, "
                        "             array_agg(barcode) as sample_barcodes "
                        "      FROM barcodes.kit "
                        "      JOIN barcodes.barcode USING (kit_id) "
                        "      WHERE kit_id IN %s "
                        "      GROUP BY kit_id) i "
                        "JOIN barcodes.kit o USING (kit_id)", (tuple(names), ))

            created = [{'kit_id': k, 'kit_uuid': u, 'sample_barcodes': b}
                       for k, u, b in cur.fetchall()]

        if len(names) != len(created):
            raise KeyError("Not all created kits could be retrieved")

        return {'created': created}

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

        # TODO: This is my best understanding of how the data must be
        #  transformed to get the host_subject_id, needs verification that it
        #  generates the expected values for preexisting samples.
        prehash = account_id + source.name.lower()
        host_subject_id = sha512(prehash.encode()).hexdigest()

        survey_answers_repo = SurveyAnswersRepo(self._transaction)
        answer_ids = survey_answers_repo.list_answered_surveys_by_sample(
            account_id, source_id, sample_id)

        answer_to_template_map = {}
        for answer_id in answer_ids:
            template_id = survey_answers_repo.find_survey_template_id(
                answer_id)
            answer_to_template_map[answer_id] = template_id

        # if a survey template is specified, filter the returned surveys
        if survey_template_id is not None:
            # TODO: This schema is so awkward for this type of query...
            answers = []
            for answer_id in answer_ids:
                if answer_to_template_map[answer_id] == survey_template_id:
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
                "en-US"
            )

            survey_answers = {}
            for k in answer_model:
                new_k = metadata_map[int(k)]
                survey_answers[k] = [new_k, answer_model[k]]

            all_survey_answers.append(
                {
                    "template": answer_to_template_map[answer_id],
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
