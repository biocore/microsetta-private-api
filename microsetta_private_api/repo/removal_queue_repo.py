from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.exceptions import RepoException


class RemovalQueueRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def _check_account_is_admin(self, admin_email):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT count(id) FROM account WHERE account_type = "
                        "'admin' and email = %s", (admin_email,))
            count = cur.fetchone()[0]

            return False if count == 0 else True

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

    def update_queue(self, account_id, admin_email, disposition):
        if not self.check_request_remove_account(account_id):
            raise RepoException("Account is not in removal queue")

        if not self._check_account_is_admin(admin_email):
            raise RepoException("That is not an admin email address")

        if disposition not in ['ignored', 'deleted']:
            raise RepoException("Disposition must be either 'ignored' or "
                                "'deleted'")

        with self._transaction.cursor() as cur:
            # preserve the time account removal was requested by the user.
            cur.execute("SELECT requested_on FROM delete_account_queue "
                        "WHERE account_id = %s", (account_id,))
            requested_on = cur.fetchone()[0]

            # get the account id of the admin that authorized this account
            # to be deleted or ignored.
            cur.execute("SELECT id FROM account WHERE email = %s",
                        (admin_email,))
            admin_id = cur.fetchone()[0]

            # add an entry to the log detailing who reviewed the account
            # and when.
            cur.execute("INSERT INTO account_removal_log (account_id, "
                        "admin_id, disposition, requested_on) VALUES (%s,"
                        " %s, %s, %s)", (account_id, admin_id, disposition,
                                         requested_on))

            # delete the entry from queue. Note that reviewed entries are
            # deleted from the queue whether or not they were approved
            # (deleted) or not (ignored).

            # For clarity:
            # allow_removal_request() will call this method and then call
            # delete_account() immediately after.
            # ignore_removal_request() will call this method and do nothing
            # after.
            cur.execute("DELETE FROM delete_account_queue WHERE account_id"
                        " = %s", (account_id,))
