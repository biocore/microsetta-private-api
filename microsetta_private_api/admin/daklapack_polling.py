import json
from datetime import datetime
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.admin import daklapack_communication as dc
from microsetta_private_api.celery_utils import celery
from microsetta_private_api.util.util import PerksType

OUTBOUND_DEV_KEY = "outBoundDelivery"
INBOUND_DEV_KEY = "inBoundDelivery"
COLLECTION_DEVICE_TYPES = ["Tube"]
BOX_TYPE = "BoxId"
REGISTRATION_CARD_TYPE = "KitId"
SENT_STATUS = "Sent"
ERROR_STATUS = "Error"
ARCHIVE_STATUS = "Archived"
CODE_ERROR = "Code Error"
BARCODE_KEY = "barcode"
CONTAINER_KEY = "Container-content"
CONTAINER_ITEMS_KEY = "containerItems"
TYPE_KEY = "type"
SINGLE_KIT_TYPES = [BOX_TYPE, REGISTRATION_CARD_TYPE]
SINGLE_KIT_TYPES.extend(COLLECTION_DEVICE_TYPES)
MULTI_ITEM_ERR_MSG = "Found multi-item content in a single-kit item"


@celery.task(ignore_result=False)
def poll_dak_orders():
    """Get open orders' status from daklapack and process accordingly"""

    results = {SENT_STATUS: [], ERROR_STATUS: [], CODE_ERROR: []}

    def make_error_str(ex):
        return f"{type(ex)}: {str(ex)}"

    try:
        # from our db, get list of daklapack orders that haven't been completed
        # NB that this transaction need not be committed because it only reads
        with Transaction() as t:
            a_repo = AdminRepo(t)
            open_dak_order_ids = a_repo.get_unfinished_daklapack_order_ids()

        # as long as there are still orders we need status info on
        curr_page = 0
        while len(open_dak_order_ids) > 0:
            # call daklapack api to get another "page" of order statuses
            dak_orders_response = dc.get_daklapack_orders_status(curr_page)
            dak_orders_data = dak_orders_response.json["data"]

            # if the page number is larger than the number of actual pages of
            # orders, the data list will be empty so break out of while loop
            if len(dak_orders_data) == 0:
                break

            # for each order for which daklapack provided a status
            for curr_datum in dak_orders_data:
                curr_order_id = curr_datum["orderId"]
                curr_status = curr_datum["lastState"]["status"]
                curr_creation_date = curr_datum["creationDate"]

                # ignore any order that is not an open order
                if curr_order_id not in open_dak_order_ids:
                    continue  # to next order datum

                try:
                    per_article_info = _process_single_order(
                        curr_order_id, curr_status, curr_creation_date)

                    if per_article_info is not None:
                        # note extend not append--avoiding nested lists
                        results[curr_status].extend(per_article_info)
                    # end if error or sent
                except Exception as per_order_ex:
                    results[CODE_ERROR].append(make_error_str(per_order_ex))

                # remove current order id from the list of order ids that we
                # want to know the status of (since now we know)
                open_dak_order_ids.remove(curr_order_id)

                # exit once we have found info on all order ids we care about
                if len(open_dak_order_ids) == 0:
                    break  # out of looping over each order datum
            # next datum

            curr_page += 1
        # end while
    except Exception as outer_ex:
        results[CODE_ERROR].append(make_error_str(outer_ex))

    # email a list of any failed orders to address in the config
    dc.send_daklapack_order_errors_report_email(results[ERROR_STATUS])

    # email a list of any encountered exceptions to address in the config
    dc.send_daklapack_polling_errors_report_email(results[CODE_ERROR])

    return results


def _process_single_order(curr_order_id, curr_status, curr_creation_date):
    per_article_info = None

    with Transaction() as per_order_t:
        per_order_admin_repo = AdminRepo(per_order_t)

        # record the current order status, whatever it is, to db
        per_order_admin_repo.set_daklapack_order_poll_info(
            curr_order_id, datetime.now(), curr_status)

        if curr_status == ERROR_STATUS or curr_status == SENT_STATUS:
            per_article_info = process_order_articles(
                per_order_admin_repo, curr_order_id, curr_status,
                curr_creation_date)

        if curr_status == ERROR_STATUS:
            # archive the errored order
            dc.post_daklapack_order_archive({"orderIds": [curr_order_id]})

            per_order_admin_repo.set_daklapack_order_poll_info(
                curr_order_id, datetime.now(), ARCHIVE_STATUS)

        per_order_t.commit()

    return per_article_info


def process_order_articles(admin_repo, order_id, status, create_date):
    per_article_outputs = []
    order_proj_ids = None
    curr_output = ""

    if status == SENT_STATUS:
        # get projects this order belongs to (needed later for kit creation)
        order_proj_ids = admin_repo.get_projects_for_dak_order(order_id)

    # call daklapack api to get detailed info on this single order
    dak_orders_response = dc.get_daklapack_order_details(order_id)

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
                if admin_repo.get_perk_type(order_id) in\
                        [PerksType.FFQ_KIT, PerksType.FFQ_ONE_YEAR]:
                    curr_output = _store_single_sent_kit(
                        admin_repo, order_proj_ids, curr_article_instance)

                # able to assume there is only one kit uuid bc
                # _store_single_sent_kit stores a single kit, by definition
                kit_uuid = curr_output["created"][0]["kit_uuid"]
                admin_repo.set_kit_uuids_for_dak_order(order_id, [kit_uuid])
                curr_output = _store_sent_kits_for_article(
                    admin_repo, order_proj_ids, order_id,
                    curr_article_instance)
            elif status == ERROR_STATUS:
                single_output = _gather_article_error_info(
                    order_id, create_date, curr_article_instance)
                curr_output = [single_output]
            else:
                raise ValueError(f"Order {order_id} has an unexpected status: "
                                 f"{status}")

            per_article_outputs.extend(curr_output)
        # next article instance
    # next article type

    return per_article_outputs


def _store_sent_kits_for_article(
        admin_repo, order_proj_ids, order_id, single_article_dict):

    created_kits = []
    is_multi_item = None

    outbound_fedex_code, inbound_fedex_code, address_dict = _get_article_info(
        single_article_dict)

    # for each "thing" in a kit
    # for each "scannable item" (i.e., barcoded thing) in a kit
    scannable_kit_items = single_article_dict["scannableKitItems"]
    for curr_scannable in scannable_kit_items:
        # figure out what *kind* of barcoded thing this is and capture
        # its barcode to the right field if it is a kind we care about
        curr_scannable_type = curr_scannable[TYPE_KEY]

        if curr_scannable_type == CONTAINER_KEY:
            curr_barcode = curr_scannable[BARCODE_KEY]
            if curr_barcode != "NoLabel":
                raise ValueError(f"Unexpected barcode for {CONTAINER_KEY}: "
                                 f"{curr_barcode}")

            # DON'T change this to "is_multi_item" bc False != None here
            if is_multi_item is False:
                raise ValueError(MULTI_ITEM_ERR_MSG)
            else:
                is_multi_item = True

            curr_items = curr_scannable[CONTAINER_ITEMS_KEY]
            for curr_item in curr_items:
                curr_item_details = curr_item["containerItemDetails"]
                # ok, NOW we should be at the level of a single kit
                curr_kit_info = _store_single_sent_kit(
                    admin_repo, order_proj_ids, order_id, outbound_fedex_code,
                    inbound_fedex_code, address_dict, curr_item_details)
                created_kits.append(curr_kit_info)

        elif curr_scannable_type in SINGLE_KIT_TYPES:
            is_multi_item = False

            # in theory, at this point I could break from the loop, but I'm
            # continuing to loop over all the kit items so I can detect if
            # single-item and multi-item info are both present (which is Bad)
        # end if
    # next scannable kit item

    # if we found out above that this scannable_kit_items is for only one kit;
    # DON'T change this to "is_multi_item" bc False != None here
    if is_multi_item is False:
        curr_kit_info = _store_single_sent_kit(
            admin_repo, order_proj_ids, order_id, outbound_fedex_code,
            inbound_fedex_code, address_dict, scannable_kit_items)
        created_kits.append(curr_kit_info)

    if len(created_kits) == 0:
        raise ValueError(f"Unable to find any kits in order {order_id}, "
                         f"article internal id "
                         f"{single_article_dict['internalId']}")

    return created_kits


def _get_article_info(single_article_dict):
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

    return outbound_fedex_code, inbound_fedex_code, address_dict


def _store_single_sent_kit(admin_repo, order_proj_ids, order_id,
                           outbound_fedex_code, inbound_fedex_code,
                           address_dict, items_list):

    device_barcodes = []
    kit_name = box_id = None

    for curr_scannable in items_list:
        # NB: the scannable item can theoretically have a lot of internal
        # complexity, like a populated containerItems list that itself
        # contains scannable items, on to infinity.  HOWEVER, microsetta
        # DOES NOT support that level of nesting, so if it is present, error.
        curr_subitems = curr_scannable.get(CONTAINER_ITEMS_KEY)
        if curr_subitems and len(curr_subitems) > 0:
            raise ValueError(MULTI_ITEM_ERR_MSG)

        # figure out what *kind* of barcoded thing this is and capture
        # its barcode to the right field if it is a kind we care about
        curr_scannable_type = curr_scannable[TYPE_KEY]
        curr_barcode = curr_scannable[BARCODE_KEY]
        if curr_scannable_type in COLLECTION_DEVICE_TYPES:
            device_barcodes.append(curr_barcode)
        elif curr_scannable_type == BOX_TYPE:
            box_id = _prevent_overwrite(box_id, curr_barcode, BOX_TYPE)
        elif curr_scannable_type == REGISTRATION_CARD_TYPE:
            kit_name = _prevent_overwrite(kit_name, curr_barcode,
                                          REGISTRATION_CARD_TYPE)
        elif curr_scannable_type == CONTAINER_KEY:
            raise ValueError(MULTI_ITEM_ERR_MSG)
        else:
            # Something we don't care about it
            continue  # to next scannable kit item
    # next scannable item

    # create a new kit in db for this article instance
    created_kit_info = admin_repo.create_kit(
        kit_name, box_id, address_dict, outbound_fedex_code,
        inbound_fedex_code, device_barcodes, order_proj_ids)

    # addresses returned from the create are strings (that in this case
    # hold representation of json); return them as json instead.
    # Not doing graceful error handling here because if any of these
    # keys/structures don't exist, something is wrong and we *should* error
    if len(created_kit_info["created"]) == 1:
        address_str = created_kit_info["created"][0]["address"]
        created_kit_info["created"][0]["address"] = json.loads(address_str)
    else:
        raise ValueError(f"Expected exactly one kit created, "
                         f"found {len(created_kit_info['created'])}")

    # can do [0] since just verified we created ONLY ONE KIT
    kit_uuid = created_kit_info["created"][0]["kit_uuid"]
    admin_repo.set_kit_uuids_for_dak_order(order_id, [kit_uuid])

    return created_kit_info


def _prevent_overwrite(old_val, new_val, val_type):
    if old_val is not None:
        raise ValueError(f"For type '{val_type}, cannot overwrite first value "
                         f"found ('{old_val}') with additional value "
                         f"'{new_val}'")
    return new_val


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
