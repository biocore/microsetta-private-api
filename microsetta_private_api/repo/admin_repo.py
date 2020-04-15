from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.repo.source_repo import SourceRepo


class AdminRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def retrieve_diagnostics_by_barcode(self, sample_barcode):
        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT "
                "ag_kit_barcodes.ag_kit_barcode_id, "
                "source.id, "
                "account.id "
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
                return None

            sample_id = row[0]
            source_id = row[1]
            account_id = row[2]

            account = None
            source = None
            sample_repo = SampleRepo(self._transaction)
            sample = sample_repo._get_sample_by_id(sample_id)

            if source_id is not None and account_id is not None:
                account_repo = AccountRepo(self._transaction)
                source_repo = SourceRepo(self._transaction)
                account = account_repo.get_account(account_id)
                source = source_repo.get_source(account_id, source_id)

            diagnostic = {
                "account": account,
                "source": source,
                "sample": sample
            }

            return diagnostic
