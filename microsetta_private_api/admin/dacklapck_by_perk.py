from datetime import datetime
from microsetta_private_api.admin.admin_impl import _create_daklapack_order
from microsetta_private_api.model.daklapack_order import DaklapackOrder
from microsetta_private_api.repo.perk_type_repo import PerkTypeRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.celery_utils import celery


@celery.task(ignore_result=False)
def poll_dak_orders_for_perk():
    """
    For perk one_year_subscription plan we have to send 4 kits in a year.
    Create a dacklapack order for each 4 kits in between 3 months.
    """

    try:
        with Transaction() as t:
            pt = PerkTypeRepo(t)
            pending_shipments = pt.get_pending_shipments()
            for shipment in pending_shipments:
                days_till_now = datetime.now() - \
                                shipment['planned_send_date'].\
                                strftime(DaklapackOrder.DATE_FORMAT)
                # if last planned_send_date is 90 days older then it's
                # time dispatch the next article create a new
                # new daklapack order when last order delivered date
                # reaches 90 days.
                if days_till_now.days >= 90:
                    if shipment['no_of_kits_sent'] <= 4:
                        account = pt.get_account_details(shipment['email'])
                        order_struct = {
                            'articles': [
                                {  # TODO: Once UI is ready we will
                                    # get ArticleCode
                                    'articleCode': "350205",
                                    'addresses': [
                                        {
                                            'firstName': account['first_name'],
                                            'lastName': account['last_name'],
                                            'address1': account['street'],
                                            'address2': '',
                                            'postalCode': account[
                                                'postal_code'],
                                            'city': account['city'],
                                            'state': account['state'],
                                            'country': account['country'],
                                            'countryCode': account['country'],
                                            'phone': account['phone'],
                                            'creationDate': datetime.now().
                                            strftime(
                                                DaklapackOrder.
                                                DATESTAMP_FORMAT),
                                            'companyName':
                                                account['company_name']
                                        }
                                    ]
                                }
                            ],
                            'shippingProvider': 'FedEx',
                            'shippingType': 'FEDEX_2_DAY',
                            'shippingProviderMetadata': [
                                {'key': 'Reference 1',
                                 'value': 'Bill Ted'}
                            ],
                        }
                response_msg = _create_daklapack_order(order_struct)
                if response_msg.order_success:
                    pt.update_shipment(shipment['subscription_id'],
                                       shipment['no_of_kits_sent'] - 1)

    except Exception as outer_ex:
        response_msg["Code Error"] = str(outer_ex)

    return response_msg
