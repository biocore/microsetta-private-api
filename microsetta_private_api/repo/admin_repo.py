<<<<<<< HEAD
import uuid
import string
import random

=======
from datetime import date

from microsetta_private_api.exceptions import RepoException
>>>>>>> 139f2db7a5b77fe309c77f740460f47605a8c3f0
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.repo.kit_repo import KitRepo
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.repo.source_repo import SourceRepo
from werkzeug.exceptions import NotFound


class AdminRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def retrieve_diagnostics_by_barcode(self, sample_barcode, grab_kit=True):
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

            row = cur.fetchone()

            if row is None:
                sample_id = None
                source_id = None
                account_id = None
                kit_id = None
            else:
                sample_id = row["sample_id"]
                source_id = row["source_id"]
                account_id = row["account_id"]
                kit_id = row["kit_id"]

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
        TMI_PROJECTS = {'The Microsetta Initiative', 'American Gut Project',
                        'British Gut Project'}
        if len(TMI_PROJECTS & set(projects)) > 0:
            is_tmi = True
        else:
            is_tmi = False

        with self._transaction.cursor() as cur:
            # get existing projects
            cur.execute("SELECT project, project_id "
                        "FROM barcodes.project")
            known_projects = {prj.lower(): id_ for prj, id_ in cur.fetchall()}
            for name in projects:
                if name.lower() not in known_projects:
                    raise KeyError("%s does not exist" % name)

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
                    prj_id = known_projects[project.lower()]
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
            cur.execute("SELECT kit_id, "
                        "       kit_uuid, "
                        "       array_agg(barcode) as sample_barcodes "
                        "FROM barcodes.kit "
                        "LEFT JOIN barcodes.barcode USING (kit_id)"
                        "WHERE kit_id IN %s "
                        "GROUP BY (kit_id, kit_uuid)", (tuple(names), ))
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
        update_args = (
            scan_info['sample_status'],
            scan_info['technician_notes'],
            date.today(),  # TODO: Do we need date or datetime here?
            sample_barcode
        )

        with self._transaction.cursor() as cur:
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
