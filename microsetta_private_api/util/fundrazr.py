from microsetta_private_api.celery_utils import celery
from microsetta_private_api.tasks import send_email
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.campaign_repo import UserTransaction
from microsetta_private_api.client.fundrazr import FundrazrClient
from microsetta_private_api.localization import EN_US


@celery.task(ignore_result=True)
def get_fundrazr_transactions():
    c = FundrazrClient()
    added = 0
    amount = 0
    with Transaction() as t:
        tr = UserTransaction(t)
        latest = tr.most_recent_transaction(transaction_source=tr.TRN_TYPE_FUNDRAZR,  # noqa
                                            include_anonymous=True)

        # if we do not have any transactions, we don't have anything recent
        if latest is None:
            unixtimestamp = None
        else:
            unixtimestamp = latest.created_as_unixts()

        for payment in c.payments(since=unixtimestamp):
            tr.add_transaction(payment)
            added += 1
            amount += payment.amount

        t.commit()

    payload = f"Number added: {added}\nTotaling: ${amount}"
    send_email("danielmcdonald@ucsd.edu", "pester_daniel",
               {"what": "FundRazr transactions added",
                "content": payload},
               EN_US)
