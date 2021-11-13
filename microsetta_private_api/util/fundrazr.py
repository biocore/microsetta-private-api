from microsetta_private_api.celery_utils import celery
from microsetta_private_api.tasks import send_email
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.campaign import UserTransaction
from microsetta_private_api.client.fundrazr import FundRazrClient
from microsetta_private_api.localization import EN_US


@celery.task(ignore_result=True)
def get_fundrazr_transactions():
    c = FundRazrClient()
    added = 0
    amount = 0
    with Transaction() as t:
        tr = UserTransaction(t)
        last_transaction = tr.last_transaction(tr.TRN_TYPE_FUNDRAZR)

        for payment in c.payments(since_id=last_transaction):
            tr.add_transaction(payment)
            added += 1
            amount += payment.amount

        t.commit()

    payload = f"Number added: {added}\nTotaling: ${amount}"
    send_email("danielmcdonald@ucsd.edu", "pester_daniel",
               {"what": "FundRazr transactions added",
                "content": payload},
               EN_US)
