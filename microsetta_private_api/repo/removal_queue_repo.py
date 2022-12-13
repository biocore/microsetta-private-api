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
            cur.execute("SELECT account_id from delete_account_queue where "
                        "account_id = %s", (account_id,))
            result = cur.fetchone()

            if result is not None:
                raise RepoException("Account is already in removal queue")

            cur.execute(
                "INSERT INTO delete_account_queue (account_id) VALUES (%s)",
                (account_id,))

    def cancel_request_remove_account(self, account_id):
        if not self.check_request_remove_account(account_id):
            raise RepoException("Account is not in removal queue")

        with self._transaction.cursor() as cur:
            cur.execute("DELETE FROM delete_account_queue WHERE account_id ="
                        " %s", (account_id,))

    def update_queue(self, account_id, admin_sub, disposition):
        if not self.check_request_remove_account(account_id):
            raise RepoException("Account is not in removal queue")

        with self._transaction.cursor() as cur:
            # preserve the time account removal was requested by the user.
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

            # delete the entry from queue. account_delete() will fail
            # w/out this.
            cur.execute("DELETE FROM delete_account_queue WHERE account_id"
                        " = %s", (account_id,))

