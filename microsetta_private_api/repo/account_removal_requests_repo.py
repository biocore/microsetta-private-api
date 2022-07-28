from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.account_removal_requests import \
        AccountRemovalRequest


class AccountRemovalRequestsRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def _row_to_account_removal_request(self, r):
        return AccountRemovalRequest(r['id'], r['account_id'], r['email'],
                                     r['first_name'], r['last_name'],
                                     r['requested_on'])

    def get_all_account_removal_requests(self):
        with self._transaction.dict_cursor() as cur:
            cur.execute(("SELECT a.id, a.account_id, b.email, b.first_name, "
                         "b.last_name, a.requested_on FROM delete_account_"
                         "queue a, account b WHERE a.account_id = b.id ORDER"
                         " BY id"))
            rows = cur.fetchall()

            return [self._row_to_account_removal_request(r) for r in rows]
