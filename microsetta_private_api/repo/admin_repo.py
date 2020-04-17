import uuid
import string
import random
from itertools import groupby

from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.repo.source_repo import SourceRepo


class AdminRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def retrieve_diagnostics_by_barcode(self, sample_barcode):
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT "
                "ag_kit_barcodes.ag_kit_barcode_id as sample_id, "
                "source.id as source_id, "
                "account.id as account_id "
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
            else:
                sample_id = row["sample_id"]
                source_id = row["source_id"]
                account_id = row["account_id"]

            account = None
            source = None
            sample = None

            if sample_id is not None:
                sample_repo = SampleRepo(self._transaction)
                sample = sample_repo._get_sample_by_id(sample_id)

            if source_id is not None and account_id is not None:
                account_repo = AccountRepo(self._transaction)
                source_repo = SourceRepo(self._transaction)
                account = account_repo.get_account(account_id)
                source = source_repo.get_source(account_id, source_id)

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

            return diagnostic

    def _generate_random_kit_name(self, name_length, prefix):
        if prefix is None:
            prefix = 'tmi_'

        # O, o, S and l removed to improve readability
        chars = 'abcdefghjkmnpqrstuvwxyz' + 'ABCDEFGHJKMNPQRTUVWXYZ'
        chars += string.digits
        rand_name = ''.join(random.choice(chars)
                            for i in range(name_length))
        return prefix + rand_name

    def create_kits(self, number_of_kits, number_of_samples, kit_prefix,
                    projects):
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

            # create a record for the new kit in ag_kit table
            ag_kit_insertions = [(str(uuid.uuid4()), name, number_of_samples)
                                 for name in names]
            cur.executemany("INSERT INTO ag.ag_kit "
                            "(ag_kit_id, supplied_kit_id, swabs_per_kit) "
                            "VALUES (%s, %s, %s)",
                            ag_kit_insertions)

            # associate the new barcode to a new sample id and
            # to the new kit in the ag_kit_barcodes table
            kit_id_to_ag_kit_id = {k: u for u, k, _ in ag_kit_insertions}
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

        return {'created': created}
