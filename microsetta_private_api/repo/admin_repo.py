import uuid
import string
import random
import datetime

from microsetta_private_api.exceptions import RepoException

from microsetta_private_api.model.project import Project
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.repo.kit_repo import KitRepo
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.repo.source_repo import SourceRepo

from werkzeug.exceptions import NotFound
from hashlib import sha512

from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo

PARTIAL_PROJ_DETAILS_SQL = """
    SELECT
    p.*,
    count(barcode) as num_samples,
    count(distinct kit_id) as num_kits
    FROM barcodes.project as p
    LEFT JOIN
    barcodes.project_barcode
    USING (project_id)
    LEFT JOIN
    barcodes.barcode
    USING (barcode)
"""

GROUP_PROJ_SQL = " GROUP BY project_id"


class AdminRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def _get_ids_relevant_to_barcode(self, sample_barcode):
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT "
                "ag_kit_barcodes.ag_kit_barcode_id as sample_id, "
                "source.id as source_id, "
                "account.id as account_id, "
                "ag_kit_barcodes.ag_kit_id as kit_id "
                "FROM "
                "ag.ag_kit_barcodes "
                "LEFT OUTER JOIN "
                "source "
                "ON "
                "ag_kit_barcodes.source_id = source.id "
                "LEFT OUTER JOIN "
                "account "
                "ON "
                "account.id = source.account_id "
                "WHERE "
                "ag_kit_barcodes.barcode = %s",
                (sample_barcode,))
            return cur.fetchone()

    def retrieve_diagnostics_by_barcode(self, sample_barcode, grab_kit=True):
        def _rows_to_dicts_list(rows):
            return [dict(x) for x in rows]

        with self._transaction.dict_cursor() as cur:
            ids = self._get_ids_relevant_to_barcode(sample_barcode)

            if ids is None:
                sample_id = None
                source_id = None
                account_id = None
                kit_id = None
            else:
                sample_id = ids["sample_id"]
                source_id = ids["source_id"]
                account_id = ids["account_id"]
                kit_id = ids["kit_id"]

            account = None
            source = None
            sample = None
            kit = None

            # get sample object for this barcode
            if sample_id is not None:
                sample_repo = SampleRepo(self._transaction)
                sample = sample_repo._get_sample_by_id(sample_id)

            # get account and source objects for this barcode
            if source_id is not None and account_id is not None:
                account_repo = AccountRepo(self._transaction)
                source_repo = SourceRepo(self._transaction)
                account = account_repo.get_account(account_id)
                source = source_repo.get_source(account_id, source_id)

            # get projects_info list for this barcode
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

    def get_projects(self):
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT project_id "
                "FROM barcodes.project "
                "ORDER BY project_id ASC;")
            rows = cur.fetchall()

            result = []
            project_ids = [row[0] for row in rows]
            for curr_project_id in project_ids:
                curr_project = self.get_project(curr_project_id)
                result.append(curr_project)

            return result

    def get_project(self, project_id):
        with self._transaction.dict_cursor() as cur:
            # get basic project info + total number of samples and kits
            sql = "{}{}{}".format(PARTIAL_PROJ_DETAILS_SQL,
                                  "WHERE project_id=%s ",
                                  GROUP_PROJ_SQL)
            cur.execute(sql, (project_id,))
            row = cur.fetchone()

            if row is None:
                raise NotFound("No such project")

            proj_dict = dict(row)

            # get number of scanned samples
            cur.execute(
                "SELECT "
                "project_id, count(distinct barcode) as num_samples_received "
                "FROM project_barcode "
                "INNER JOIN "
                "barcode_scans "
                "USING (barcode) "
                "WHERE "
                "project_id = %s "
                "GROUP BY project_id",
                (project_id,)
            )
            row = cur.fetchone()

            num_samples_received = 0  # default assumption
            if row is not None:
                num_samples_received = row['num_samples_received']
            proj_dict["num_samples_received"] = num_samples_received

            # get number of distinct sources linked to barcodes associated
            # with this project
            cur.execute(
                "SELECT project_barcode.project_id, " 
                "count(distinct ag_kit_barcodes.source_id) "
                "   as num_unique_sources "
                "FROM barcodes.project_barcode " 
                "INNER JOIN ag.ag_kit_barcodes "
                "USING (barcode) "
                "WHERE project_id = %s "
                "GROUP BY project_id;",
                (project_id,)
            )
            row = cur.fetchone()

            num_unique_sources = 0  # default assumption
            if row is not None:
                num_unique_sources = row['num_unique_sources']
            proj_dict["num_unique_sources"] = num_unique_sources

            a_project = Project(**proj_dict)
            return a_project

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

        account_id = ids['account_id']
        source_id = ids['source_id']
        sample_id = ids['sample_id']

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
