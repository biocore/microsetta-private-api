from microsetta_private_api.celery_utils import celery
from microsetta_private_api.tasks import send_email
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.campaign_repo import (UserTransaction,
                                                       FundRazrCampaignRepo)
from microsetta_private_api.client.fundrazr import FundrazrClient
from microsetta_private_api.localization import EN_US


@celery.task(ignore_result=True)
def get_fundrazr_transactions():
    c = FundrazrClient()
    added = 0
    amount = 0
    with Transaction() as t:
        tr = UserTransaction(t)
        fr = FundRazrCampaignRepo(t)

        # check if we have new campaigns or perks
        campaigns = c.campaigns()
        for campaign in campaigns:
            if not fr.campaign_exists(campaign.campaign_id):
                fr.insert_campaign(campaign)
            for item in campaign.items:
                print(campaign.campaign_id, item.id, item.title)
                if not fr.item_exists(campaign.campaign_id, item.id):
                    fr.add_perk_to_campaign(campaign.campaign_id, item)

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

        t.commit()

    payload = f"Number added: {added}\nTotaling: ${amount}"
    send_email("danielmcdonald@ucsd.edu", "pester_daniel",
               {"what": "FundRazr transactions added",
                "content": payload},
               EN_US)
