from datetime import date

from microsetta_private_api.exceptions import RepoException
from werkzeug.exceptions import NotFound

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

    def get_project_summary_statistics(self):
        with self._transaction.dict_cursor() as cur:
            # TODO:  I don't see a clean way to get the number of kits easily.
            #  postpone showing number of kits for now?
            cur.execute(
                "SELECT "
                "project_id, project, count(barcode) "
                "FROM project LEFT JOIN "
                "project_barcode "
                "USING(project_id) "
                "GROUP BY project_id "
                "ORDER BY count DESC "
            )
            rows = cur.fetchall()

            proj_stats = [
                {
                    'project_id': row['project_id'],
                    'project_name': row['project'],
                    'number_of_samples': row['count']
                    # 'number_of_kits': ???  Profit.
                }
                for row in rows]

            return proj_stats

    def get_project_detailed_statistics(self, project_id):
        with self._transaction.dict_cursor() as cur:
            # TODO:  I don't see a clean way to get the number of kits easily.
            #  postpone showing number of kits for now?
            cur.execute(
                "SELECT "
                "project_id, project, count(barcode) "
                "FROM project LEFT JOIN "
                "project_barcode "
                "USING(project_id) "
                "WHERE project_id = %s "
                "GROUP BY project_id ",
                (project_id,)
            )
            row = cur.fetchone()

            if row is None:
                raise NotFound("No such project")

            project_id = row['project_id']
            project_name = row['project']
            number_of_samples = row['count']
            # number_of_kits = ???

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
                'number_of_samples': number_of_samples,
                'number_of_samples_scanned_in': number_of_samples_scanned_in,
                'sample_status_counts': sample_status_counts
            }

            return detailed_stats
