from datetime import datetime
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.admin import daklapack_communication as dc

OUTBOUND_DEV_KEY = "outBoundDelivery"
INBOUND_DEV_KEY = "inBoundDelivery"
COLLECTION_DEVICE_TYPES = ["2point5ml_etoh_tube", "7ml_etoh_tube",
                           "neoteryx_kit"]
SENT_STATUS = "Sent"
ERROR_STATUS = "Error"


def poll_dak_orders():
    """Get open orders' status from daklapack and process accordingly"""

    with Transaction() as t:
        poll_dak_orders_using_transaction(t)


# This method exists (as a separate entity from poll_dak_orders)
# exists only to make testing easier
def poll_dak_orders_using_transaction(t):
    """Use transaction to get open orders' status from daklapack and process"""

    results = {SENT_STATUS: [], ERROR_STATUS: []}
    admin_repo = AdminRepo(t)

    # from our db, get list of daklapack orders that haven't been completed
    open_dak_order_ids = admin_repo.get_unfinished_daklapack_order_ids()
    curr_page = 0

    # as long as there are still orders we need status info on
    while len(open_dak_order_ids) > 0:
        curr_page += 1

        # call daklapack api to get another "page" of order statuses
        dak_orders_response = dc.get_daklapack_orders_status(curr_page)
        dak_orders_data = dak_orders_response.json["data"]

        # for each order for which daklapack provided a status
        for curr_datum in dak_orders_data:
            curr_order_id = curr_datum["orderId"]

            # ignore any order that is not an open order
            if curr_order_id not in open_dak_order_ids:
                continue  # to next order datum

            # record the current order status, whatever it is, to db
            curr_status = curr_datum["lastState"]["status"]
            admin_repo.set_daklapack_order_poll_info(
                curr_order_id, datetime.now(), curr_status)

            if curr_status == ERROR_STATUS or curr_status == SENT_STATUS:
                curr_creation_date = curr_datum["creationDate"]

                per_article_info = process_order_articles(
                    admin_repo, curr_order_id, curr_status,
                    curr_creation_date)

                # note extend not append--avoiding nested lists
                results[curr_status].extend(per_article_info)

                # if curr_status == ERROR_STATUS:
                # TODO: cancel the errored order w daklapack
                # end if error
            # end if error or sent

            # remove current order id from the list of order ids that we
            # want to know the status of (since now we know)
            open_dak_order_ids.remove(curr_order_id)

            # exit once we have found info on all order ids we care about
            if len(open_dak_order_ids) == 0:
                break  # out of looping over each order datum
        # next datum
    # end while

    # iff there were any errors,
    # email a list of all the failed orders to
    # an email address specified in the config
    # errors = results[ERROR_STATUS]
    # if len(errors) > 0:
    #     dc.send_daklapack_errors_report_email(errors)

    return results


def process_order_articles(admin_repo, order_id, status, create_date):
    per_article_outputs = []
    order_proj_ids = None

    if status == SENT_STATUS:
        # get projects this order belongs to (needed later for kit creation)
        order_proj_ids = admin_repo.get_projects_for_dak_order(order_id)

    # call daklapack api to get detailed info on this single order
    dak_orders_response = dc.get_daklapack_order_details(
        order_id)

    # loop over each kind of "daklapack article" in this order;
    # NOTE that although the daklapack api allows >1 type of article (i.e.,
    # more than one article code) per order,
    # as of mid-2021, microsetta does NOT: microsetta-admin allows creation of
    # daklapack orders with only a single article code, and each level of
    # fundrazr contribution maps to a perk defined by a single article code.
    dak_order_article_types = dak_orders_response.json["articles"]
    for curr_article_type in dak_order_article_types:
        article_instances = curr_article_type["articles"]

        # for each instance of this article kind in the order
        for curr_article_instance in article_instances:
            if status == SENT_STATUS:
                # (Per Daniel 2021-07-01, each instance of a daklapack article
                # represents exactly one kit, no more or less.)
                curr_output = _store_single_sent_kit(
                    admin_repo, order_proj_ids, curr_article_instance)
            elif status == ERROR_STATUS:
                curr_output = _gather_article_error_info(
                    order_id, create_date, curr_article_instance)
            else:
                raise ValueError(f"Order {order_id} has an unexpected status: "
                                 f"{status}")

            per_article_outputs.append(curr_output)
        # next article instance
    # next article type

    return per_article_outputs


def _store_single_sent_kit(admin_repo, order_proj_ids, single_article_dict):
    device_barcodes = []
    kit_name = box_id = None

    # Gather info on address and outbound/inbound fedex tracking
    # numbers for this particular article instance (i.e., kit).
    # Per Edgar and Daniel, some kits:
    # - will have outbound and inbound fedex tracking numbers
    #   (e.g., typical fundrazr kits)
    # - will have neither tracking numbers (e.g., a project just
    #   purchasing kits)
    # - will have an outbound tracking number (e.g., a project
    #   where the participant drops their kit off somewhere)
    # - will have an inbound tracking number (e.g., a hand out at
    #   a conference)

    outbound_fedex_code = inbound_fedex_code = None
    if single_article_dict[OUTBOUND_DEV_KEY] is not None:
        outbound_fedex_code = single_article_dict[
            OUTBOUND_DEV_KEY]["code"]
    if single_article_dict[INBOUND_DEV_KEY] is not None:
        inbound_fedex_code = single_article_dict[
            INBOUND_DEV_KEY]["code"]

    address_dict = single_article_dict["sendInformation"]

    # for each "scannable item" (i.e., barcoded thing) in a kit
    scannable_kit_items = single_article_dict["scannableKitItems"]
    for curr_scannable in scannable_kit_items:
        # NB: the scannable item can theoretically have a lot of internal
        # complexity, like a populated containerItems list that itself
        # contains scannable items, on to infinity.  HOWEVER, microsetta
        # has defined each article to equal exactly one kit, so it should
        # not be necessary to dig into that.

        # figure out what *kind* of barcoded thing this is and capture
        # its barcode to the right field if it is a kind we care about
        curr_scannable_type = curr_scannable["type"]
        curr_barcode = curr_scannable["barcode"]
        if curr_scannable_type in COLLECTION_DEVICE_TYPES:
            device_barcodes.append(curr_barcode)
        elif curr_scannable_type == "box":
            box_id = curr_barcode
        elif curr_scannable_type == "registration_card":
            kit_name = curr_barcode
        else:
            # Daklapack barcodes this thing but we don't care about it
            continue  # to next scannable kit item
    # next scannable item

    # create a new kit in db for this article instance
    created_kit_info = admin_repo.create_kit(
        kit_name, box_id, address_dict, outbound_fedex_code,
        inbound_fedex_code, device_barcodes, order_proj_ids)

    return created_kit_info


def _gather_article_error_info(order_id, create_date, curr_article_instance):
    # dig the info for an error report out of the article instance
    curr_error_info = {"order_id": order_id,
                       "article_code": curr_article_instance["articleCode"],
                       "sent_to_address":
                           curr_article_instance["sendInformation"],
                       # per specifications, orders submitted by microsetta api
                       # through the daklapack interface put the name of the
                       # microsetta user who submitted the order into the
                       # order's "companyName" field
                       "order_submitter":
                           curr_article_instance["sendInformation"]
                           ["companyName"],
                       "creation_date": create_date,
                       "status_description":
                           curr_article_instance["description"]
                       }

    return curr_error_info
