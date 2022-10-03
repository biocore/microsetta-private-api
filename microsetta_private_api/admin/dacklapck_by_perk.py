from datetime import datetime
from microsetta_private_api.admin.admin_impl import _create_daklapack_order
from microsetta_private_api.model.daklapack_order import DaklapackOrder
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.admin import daklapack_communication as dc
from microsetta_private_api.celery_utils import celery


@celery.task(ignore_result=False)
def poll_dak_orders_for_perk():
    """
    For perk type 3 we have to send 4 kits in a year.
    Create a dacklapack order for each 4 kits in between 3 months.
    """
    response_msg = {}
    try:

        with Transaction() as t:
            a_repo = AdminRepo(t)
            open_dak_order_ids = a_repo.get_perk_type3_orders()
            for order in open_dak_order_ids:
                days_till_now = datetime.now() - order['planned_send_date'].strftime(DaklapackOrder.DATE_FORMAT)

                # if last planned_send_date is 90 days older then it's time dispatch the next article create a new
                # new daklapack order when last order delivered date reaches 90 days
                # TODO: we don't know exact
                #  response of dak_order, once we get the sample response we can change accordingly
                if days_till_now.days >= 90:
                    if order['no_of_kits'] <= 4:
                        dak_orders_response = dc.get_daklapack_order_details(order['dak_order_id'])

                        order_struct = {
                            'articles': [
                                {
                                    'articleCode': '350102', # we have to map the correct article code
                                    'addresses': dak_orders_response['articles']['addresses']
                                }
                            ],
                            'shippingProvider': dak_orders_response['shipping_provider'],
                            'shippingType': dak_orders_response['shipping_type'],
                            'shippingProviderMetadata': dak_orders_response['shipping_provider_metadata'],
                            "plannedSendDate": datetime.date.today()
                        }
                        response_msg = _create_daklapack_order(order_struct, no_of_kits=order['no_of_kits'] + 1)
    except Exception as outer_ex:
        response_msg["Code Error"] = str(outer_ex)

    return response_msg
