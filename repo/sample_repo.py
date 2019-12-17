from repo.base_repo import BaseRepo
from model.sample import Sample
from model.kit import Kit


class SampleRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)
