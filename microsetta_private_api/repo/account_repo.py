import psycopg2

from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.account import Account
from microsetta_private_api.exceptions import RepoException


class AccountRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    read_cols = "id, email, " \
                "account_type, auth_issuer, auth_sub, " \
                "first_name, last_name, " \
                "street, city, state, post_code, country_code, " \
                "creation_time, update_time"

    write_cols = "id, email, " \
                 "account_type, auth_issuer, auth_sub, " \
                 "first_name, last_name, " \
                 "street, city, state, post_code, country_code"

    @staticmethod
    def _row_to_addr(r):
        return {
            "street": r["street"],
            "city": r["city"],
            "state": r["state"],
            "post_code": r["post_code"],
            "country_code": r["country_code"]
        }

    @staticmethod
    def _addr_to_row(addr):
        return (addr.street,
                addr.city,
                addr.state,
                addr.post_code,
                addr.country_code)

    @staticmethod
    def _row_to_account(r):
        return Account(
            r['id'], r['email'],
            r['account_type'], r['auth_issuer'], r['auth_sub'],
            r['first_name'], r['last_name'],
            AccountRepo._row_to_addr(r),
            r['creation_time'], r['update_time'])

    @staticmethod
    def _account_to_row(a):
        return (a.id, a.email,
                a.account_type, a.auth_issuer, a.auth_sub,
                a.first_name, a.last_name) + \
               AccountRepo._addr_to_row(a.address)

    def get_account(self, account_id):
        with self._transaction.dict_cursor() as cur:
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
            row = AccountRepo._account_to_row(account)

            # Shift id to end since it appears in the WHERE clause
            row_id = row[0:1]
            row_email_to_cc = row[1:]
            final_row = row_email_to_cc + row_id

            try:
                cur.execute("UPDATE account "
                            "SET "
                            "email = %s, "
                            "account_type = %s, "
                            "auth_issuer = %s, "
                            "auth_sub = %s, "
                            "first_name = %s, "
                            "last_name = %s, "
                            "street = %s, "
                            "city = %s, "
                            "state = %s, "
                            "post_code = %s, "
                            "country_code = %s "
                            "WHERE "
                            "account.id = %s",
                            final_row
                            )
                return cur.rowcount == 1
            except psycopg2.errors.UniqueViolation as e:
                if e.diag.constraint_name == 'idx_account_email':
                    # TODO: Ugh. Localization of error messages is needed.
                    raise RepoException("Email %s is not available"
                                        % account.email) from e
                if e.diag.constraint_name == 'idx_account_issuer_sub':
                    # Ugh.  This is really difficult to explain to an end user.
                    raise RepoException("Cannot claim more than one account")
                # Unknown exception, re raise it.
                raise e

    def create_account(self, account):
        try:
            with self._transaction.cursor() as cur:
                cur.execute("INSERT INTO account (" +
                            AccountRepo.write_cols +
                            ") "
                            "VALUES("
                            "%s, %s, "
                            "%s, %s, %s, "
                            "%s, %s, "
                            "%s, %s, %s, %s, %s)",
                            AccountRepo._account_to_row(account))
                return cur.rowcount == 1
        except psycopg2.errors.UniqueViolation as e:
            if e.diag.constraint_name == 'idx_account_email':
                # TODO: Ugh. Localization of error messages is needed someday.
                raise RepoException("Email %s is not available"
                                    % account.email) from e
            if e.diag.constraint_name == 'idx_account_issuer_sub':
                # Ugh.  This is really difficult to explain to an end user.
                raise RepoException("Cannot create two accounts on the same "
                                    "email")

            # Unknown exception, re raise it.
            raise e

    def delete_account(self, account_id):
        with self._transaction.cursor() as cur:
            cur.execute("DELETE FROM account WHERE account.id = %s",
                        (account_id,))
            return cur.rowcount == 1

    def delete_account_by_email(self, email):
        with self._transaction.cursor() as cur:
            cur.execute("DELETE FROM account WHERE account.email = %s",
                        (email,))
            return cur.rowcount == 1
