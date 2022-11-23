from microsetta_private_api.celery_utils import celery
from microsetta_private_api.tasks import send_email
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.perk_fulfillment_repo import\
    PerkFulfillmentRepo
from microsetta_private_api.localization import EN_US
from microsetta_private_api.config_manager import SERVER_CONFIG


@celery.task(ignore_result=True)
def fulfill_new_transactions():
    with Transaction() as t:
        pfr = PerkFulfillmentRepo(t)
        error_report = pfr.process_pending_fulfillments()
        t.commit()

    if len(error_report) > 0:
        try:
            send_email(SERVER_CONFIG['pester_email'], "pester_daniel",
                       {"what": "Perk Fulfillment Errors",
                        "content": error_report},
                       EN_US)
        except:  # noqa
            # try our best to email
            pass


@celery.task(ignore_result=True)
def process_subscription_fulfillments():
    with Transaction() as t:
        pfr = PerkFulfillmentRepo(t)
        error_report = pfr.process_subscription_fulfillments()
        t.commit()

    if len(error_report) > 0:
        try:
            send_email(SERVER_CONFIG['pester_email'], "pester_daniel",
                       {"what": "Subscription Fulfillment Errors",
                        "content": error_report},
                       EN_US)
        except:  # noqa
            # try our best to email
            pass


@celery.task(ignore_result=True)
def check_shipping_updates():
    with Transaction() as t:
        pfr = PerkFulfillmentRepo(t)
        pfr.check_for_shipping_updates()


@celery.task(ignore_result=True)
def perks_without_fulfillment_details():
    with Transaction() as t:
        pfr = PerkFulfillmentRepo(t)
        perk_log = pfr.find_perks_without_fulfillment_details()

    if len(perk_log) > 0:
        try:
            send_email(SERVER_CONFIG['pester_email'], "pester_daniel",
                       {"what": "Perks Without Fulfillment Details",
                        "content": perk_log},
                       EN_US)
        except:  # noqa
            # try our best to email
            pass
