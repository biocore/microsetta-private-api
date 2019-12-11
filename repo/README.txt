We are approximating a Repository pattern:
    Each repository maps one object to a set of one or more tables in the db
    The repository exposes methods for querying, saving, updating objects
    Repositories do all db access within a specified transaction
Example Usage:

from repo.transaction import Transaction
from repo.kit_repo import KitRepo

with Transaction() as t:
    kit_repo = KitRepo(t)
    kit = kit_repo.get_kit("eba20873-b88d-33cc-e040-8a80115d392c")
    print(kit.id)
    for s in kit.samples:
        print(s.id)
        print(s.barcode)
        print(s.notes)
        print(s.deposited)
    t.commit() # If changes were made, you must commit the transaction
