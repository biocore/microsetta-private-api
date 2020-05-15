import uuid
import string
import random

from datetime import date

from microsetta_private_api.exceptions import RepoException

from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.repo.kit_repo import KitRepo
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.repo.source_repo import SourceRepo

from werkzeug.exceptions import NotFound
from hashlib import sha512

from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo


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

            if sample_id is not None:
                sample_repo = SampleRepo(self._transaction)
                sample = sample_repo._get_sample_by_id(sample_id)

            if source_id is not None and account_id is not None:
                account_repo = AccountRepo(self._transaction)
                source_repo = SourceRepo(self._transaction)
                account = account_repo.get_account(account_id)
                source = source_repo.get_source(account_id, source_id)

            if kit_id is not None and grab_kit:
                kit_repo = KitRepo(self._transaction)
                kit = kit_repo.get_kit_all_samples_by_kit_id(kit_id)

            cur.execute("SELECT * from barcodes.barcode "
                        "LEFT OUTER JOIN barcodes.project_barcode "
                        "USING (barcode) "
                        "LEFT OUTER JOIN barcodes.project "
                        "USING (project_id) "
                        "where barcode=%s",
                        (sample_barcode,))
            barcode_info = cur.fetchall()

            # How to unwrap a psycopg2 DictRow.  I feel dirty.
            barcode_info = [{k: v for k, v in x.items()}
                            for x in barcode_info]  # Get Inceptioned!!

            # Collapse info from joined project_barcode and project tables
            # into array within barcode_info
            if barcode_info:
                first = barcode_info[0]
                first['projects'] = [
                    {
                        'project_id': r['project_id'],
                        'project': r['project']
                    }
                    for r in barcode_info]
                del first['project_id']
                del first['project']
                barcode_info = first
            else:
                barcode_info = None

            if account is None and \
                    source is None and \
                    sample is None and \
                    barcode_info is None:
                return None

            diagnostic = {
                "barcode": sample_barcode,
                "account": account,
                "source": source,
                "sample": sample,
                "barcode_info": barcode_info
            }

            if grab_kit:
                diagnostic["kit"] = kit

            return diagnostic

    def create_project(self, project_name, is_microsetta):
        """Create a project entry in the database

        Parameters
        ----------
        project_name : str
            The name of the project to create
        is_microsetta : bool
            If the project is part of The Microsetta Initiative
        """
        if is_microsetta:
            tmi = 'yes'
        else:
            tmi = 'no'

        with self._transaction.cursor() as cur:
            cur.execute("SELECT MAX(project_id) + 1 "
                        "FROM barcodes.project")
            id_ = cur.fetchone()[0]

            cur.execute("INSERT INTO barcodes.project "
                        "(project_id, project, is_microsetta) "
                        "VALUES (%s, %s, %s)", [id_, project_name, tmi])
        return True

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

        diagnostic = {
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

        accts = [acct_repo.get_account(acct_id) for acct_id in ids]
        diagnostic = {
            "accounts": accts
        }

        return diagnostic

    def scan_barcode(self, sample_barcode, scan_info):
        with self._transaction.cursor() as cur:

            cur.execute(
                "SELECT scan_date FROM barcodes.barcode WHERE barcode=%s",
                (sample_barcode,)
            )
            row = cur.fetchone()
            if row is None:
                raise NotFound("No such barcode: %s" % sample_barcode)

            existing_scan_date = row[0]
            new_scan_date = existing_scan_date
            if scan_info['sample_status'] == 'sample-is-valid':
                new_scan_date = date.today()

            update_args = (
                scan_info['sample_status'],
                scan_info['technician_notes'],
                new_scan_date,
                sample_barcode
            )

            cur.execute(
                "UPDATE barcodes.barcode "
                "SET "
                "sample_status = %s, "
                "technician_notes = %s, "
                "scan_date = %s "
                "WHERE "
                "barcode = %s",
                update_args
            )

            if cur.rowcount == 0:
                raise NotFound("No such barcode: %s" % sample_barcode)

            if cur.rowcount > 1:
                # Note: This "can't" happen.
                raise RepoException("ERROR: Multiple barcode entries would be "
                                    "updated by scan, failing out")

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
                if answer_to_template_map == survey_template_id:
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

    def get_project_summary_statistics(self):
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT "
                "project_id, project, "
                "count(barcode) as barcode_count, "
                "count(distinct kit_id) as kit_count "
                "FROM project "
                "LEFT JOIN "
                "project_barcode "
                "USING(project_id) "
                "LEFT JOIN "
                "barcode "
                "USING(barcode) "
                "GROUP BY project_id "
                "ORDER BY barcode_count DESC"
            )
            rows = cur.fetchall()

            proj_stats = [
                {
                    'project_id': row['project_id'],
                    'project_name': row['project'],
                    'number_of_samples': row['barcode_count'],
                    'number_of_kits': row['kit_count']
                }
                for row in rows]

            return proj_stats

    def get_project_detailed_statistics(self, project_id):
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT "
                "project_id, project, "
                "count(barcode) as barcode_count, "
                "count(distinct kit_id) as kit_count "
                "FROM project "
                "LEFT JOIN "
                "project_barcode "
                "USING(project_id) "
                "LEFT JOIN "
                "barcode "
                "USING(barcode) "
                "WHERE project_id=%s "
                "GROUP BY project_id",
                (project_id,)
            )
            row = cur.fetchone()

            if row is None:
                raise NotFound("No such project")

            project_id = row['project_id']
            project_name = row['project']
            number_of_samples = row['barcode_count']
            number_of_kits = row['kit_count']

            cur.execute(
                "SELECT "
                "project_id, count(barcode) "
                "FROM project_barcode "
                "LEFT JOIN "
                "barcode "
                "USING(barcode) "
                "WHERE "
                "project_id = %s AND "
                "scan_date is NOT NULL "
                "GROUP BY project_id",
                (project_id,)
            )
            row = cur.fetchone()
            number_of_samples_scanned_in = row['count']

            cur.execute(
                "SELECT "
                "project_id, project, sample_status, count(barcode) "
                "FROM project "
                "LEFT JOIN project_barcode "
                "USING (project_id) "
                "LEFT JOIN barcode "
                "USING (barcode) "
                "WHERE "
                "project_id = 1 AND "
                "sample_status IS NOT NULL "
                "group by project_id, sample_status"
            )
            rows = cur.fetchall()
            sample_status_counts = {
                row['sample_status']: row['count'] for row in rows
            }

            detailed_stats = {
                'project_id': project_id,
                'project_name': project_name,
                'number_of_kits': number_of_kits,
                'number_of_samples': number_of_samples,
                'number_of_samples_scanned_in': number_of_samples_scanned_in,
                'sample_status_counts': sample_status_counts
            }

            return detailed_stats
