from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.account import Account
import json


class AccountRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    read_cols = "id, email, auth_provider, first_name, last_name, address, " \
                "account_type, creation_time, update_time"
    write_cols = "id, email, auth_provider, first_name, last_name, address, " \
                 "account_type"

    @classmethod
    def _row_to_account(cls, r):
        return Account(r[0], r[1], r[2], r[3], r[4],
                       json.loads(r[5]), r[6], r[7], r[8])

    @classmethod
    def _account_to_row(cls, a):
        return (a.id, a.email, a.auth_provider, a.first_name, a.last_name,
                json.dumps(a.address), a.account_type)

    def get_account(self, account_id):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT " + AccountRepo.read_cols + " FROM "
                        "account "
                        "WHERE "
                        "account.id = %s", (account_id,))
            r = cur.fetchone()
            if r is None:
                return None
            else:
                return AccountRepo._row_to_account(r)

    def update_account(self, account):
        with self._transaction.cursor() as cur:
            cur.execute("UPDATE account "
                        "SET "
                        "email = %s, auth_provider = %s, first_name = %s, "
                        "last_name = %s, address = %s, account_type = %s "
                        "WHERE "
                        "account.id = %s",
                        (account.email, account.auth_provider,
                         account.first_name, account.last_name,
                         json.dumps(account.address), account.account_type,
                         account.id)
                        )
            return cur.rowcount == 1

    def create_account(self, account):
        with self._transaction.cursor() as cur:
            cur.execute("INSERT INTO account (" + AccountRepo.write_cols + ") "
                        "VALUES(%s, %s, %s, %s, %s, %s, %s)",
                        AccountRepo._account_to_row(account))
            return cur.rowcount == 1

    def delete_account(self, account_id):
        with self._transaction.cursor() as cur:
            cur.execute("DELETE FROM account WHERE account.id = %s",
                        (account_id,))
            return cur.rowcount == 1
