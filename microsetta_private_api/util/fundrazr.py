from microsetta_private_api.celery_utils import celery
from microsetta_private_api.tasks import send_email
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.campaign_repo import UserTransaction
from microsetta_private_api.client.fundrazr import FundrazrClient
from microsetta_private_api.localization import EN_US
from microsetta_private_api.config_manager import SERVER_CONFIG


@celery.task(ignore_result=True)
def get_fundrazr_transactions(test_transaction=None):
    def _get_load(t):
        added = 0
        amount = 0

        c = FundrazrClient()
        tr = UserTransaction(t)

        # gather the most recent transaction so we can get what's newer
        latest = tr.most_recent_transaction(transaction_source=tr.TRN_TYPE_FUNDRAZR,  # noqa
                                            include_anonymous=True)

        # if we do not have any transactions, we don't have anything recent
        if latest is None:
            unixtimestamp = None
        else:
            unixtimestamp = latest.created_as_unixts()

        # gather and insert transactions
        for payment in c.payments(since=unixtimestamp):
            tr.add_transaction(payment)
            added += 1
            amount += payment.amount

        return added, amount

    if test_transaction is None:
        # if we do not have a test_transaction, we assume we are operating
        # in a commit safe environment
        with Transaction() as t:
            added, amount = _get_load(t)
            t.commit()
    else:
        # otherwise, we assume we are in tests and we do not commit
        added, amount = _get_load(test_transaction)

    payload = f"Number added: {added}\nTotaling: ${amount}"

    try:
        send_email(SERVER_CONFIG['pester_email'], "pester_daniel",
                   {"what": "FundRazr transactions added",
                    "content": payload},
                   EN_US)
    except:  # noqa
        # try our best to email
        pass
