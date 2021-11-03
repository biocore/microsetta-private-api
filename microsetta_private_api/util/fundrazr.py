from microsetta_private_api.celery_utils import celery
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.fundrazr import FundRazr as FundRazrRepo
from microsetta_private_api.client.fundrazr import FundRazrClient


@celery.task(ignore_result=True)
def get_fundrazr_transactions():
    c = FundRazrClient()
    with Transaction() as t:
        fr = FundRazrRepo(t)
        last_transaction = fr.last_transaction()
        for payment in c.payments(since_id=last_transaction):
            fr.add_transaction(payment)
        t.commit()
