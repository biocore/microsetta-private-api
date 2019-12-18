from repo.base_repo import BaseRepo


class SampleRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def get_samples(self, account_id, source_id):
        pass

