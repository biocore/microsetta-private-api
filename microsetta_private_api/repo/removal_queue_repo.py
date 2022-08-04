import psycopg2
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.exceptions import RepoException


class RemovalQueueRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def check_request_remove_account(self, account_id):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT count(id) FROM delete_account_queue WHERE "
                        "account_id = %s", (account_id,))
            count = cur.fetchone()[0]

            return False if count == 0 else True

    def request_remove_account(self, account_id):
        with self._transaction.cursor() as cur:
            try:
                cur.execute("INSERT INTO delete_account_queue (account_id) "
                            "VALUES (%s)", (account_id,))
            except psycopg2.errors.UniqueViolation:
                raise RepoException("Account is already in removal queue")

            if cur.rowcount == 1:
                self._transaction.commit()

            return cur.rowcount == 1

    def cancel_request_remove_account(self, account_id):
        if self.check_request_remove_account(account_id):
            with self._transaction.cursor() as cur:
                sql = ("DELETE FROM delete_account_queue WHERE account_id "
                       "= %s", (account_id,))

                cur.execute(sql)

                if cur.rowcount == 1:
                    self._transaction.commit()

                return cur.rowcount == 1
        else:
            raise RepoException("Account is not in removal queue")

    def update_queue(self, account_id, admin_sub, disposition):
        if self.check_request_remove_account(account_id):
            with self._transaction.cursor() as cur:
                # preserve the time the account removal was requested by the
                # user.
                cur.execute("SELECT requested_on FROM delete_account_queue "
                            "WHERE account_id = %s", (account_id,))
                requested_on = cur.fetchone()[0]

                # get the account id of the admin that authorized this account
                # to be deleted.
                cur.execute("SELECT id FROM account WHERE auth_sub = %s",
                            (admin_sub,))
                admin_id = cur.fetchone()[0]

                # add an entry to the log detailing who deleted the account,
                # why, and when.

                cur.execute("INSERT INTO account_removal_log (account_id, "
                            "admin_id, disposition, requested_on) VALUES (%s,"
                            " %s, %s, %s)", (account_id, admin_id, disposition,
                                             requested_on))

                # we don't expect the first two commands to fail. However,
                # the insert should be confirmed.
                if cur.rowcount != 1:
                    raise RepoException("Failed to insert entry into log.")

                # delete the entry from queue. account_delete() will fail
                # w/out this.
                cur.execute("DELETE FROM delete_account_queue WHERE account_id"
                            " = %s", (account_id,))

                self._transaction.commit()
        else:
            raise RepoException("Account is not in removal queue")
