from microsetta_private_api.celery_utils import celery
from microsetta_private_api.tasks import send_email
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.perk_fulfillment_repo import\
    PerkFulfillmentRepo
from microsetta_private_api.localization import EN_US
from microsetta_private_api.config_manager import SERVER_CONFIG


@celery.task(ignore_result=True)
def fulfill_new_transactions():
    error_report = []

    with Transaction() as t:
        pfr = PerkFulfillmentRepo(t)
        pf_active = pfr.check_perk_fulfillment_active()

    if pf_active:
        with Transaction() as t:
            pfr = PerkFulfillmentRepo(t)
            ftp_ids = pfr.get_pending_fulfillments()

        for ftp_id in ftp_ids:
            with Transaction() as t:
                pfr = PerkFulfillmentRepo(t)
                error_list = pfr.process_pending_fulfillment(ftp_id)
                if len(error_list) > 0:
                    for error in error_list:
                        error_report.append(error)

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
    error_report = []

    with Transaction() as t:
        pfr = PerkFulfillmentRepo(t)
        pf_active = pfr.check_perk_fulfillment_active()

    if pf_active:
        with Transaction() as t:
            pfr = PerkFulfillmentRepo(t)
            fulfillment_ids = pfr.get_subscription_fulfillments()

        for fulfillment_id in fulfillment_ids:
            with Transaction() as t:
                pfr = PerkFulfillmentRepo(t)
                error_list = pfr.process_subscription_fulfillment(
                    fulfillment_id
                )

                if len(error_list) > 0:
                    for error in error_list:
                        error_report.append(error)

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
        emails_sent, error_report = pfr.check_for_shipping_updates()

        if emails_sent > 0 or len(error_report) > 0:
            t.commit()

            email_content = f"Emails sent: {emails_sent}\n"\
                            f"Errors: {error_report}"
            try:
                send_email(SERVER_CONFIG['pester_email'], "pester_daniel",
                           {"what": "Automated Tracking Updates Output",
                            "content": email_content},
                           EN_US)
            except:  # noqa
                # try our best to email
                pass


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
