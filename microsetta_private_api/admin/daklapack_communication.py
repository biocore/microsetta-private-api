from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.tasks import send_basic_email as celery_send_email

ORDER_HOLD_TEMPLATE_PATH = "email/daklapack_fulfillment_hold_request"


def _get_daklapack_oauth2_session():
    # run the "Resource Owner Client Credentials Grant Type" oauth2 workflow
    client_id = SERVER_CONFIG["daklapack_client_id"]
    auth_client = BackendApplicationClient(client_id=client_id)
    auth_session = OAuth2Session(client=auth_client)
    token = auth_session.fetch_token(
        token_url=SERVER_CONFIG["daklapack_auth_url"],
        client_id=client_id,
        client_secret=SERVER_CONFIG["daklapack_client_secret"])

    dak_session = OAuth2Session(client_id, token=token)
    return dak_session


# TODO: AB: unit-test daklapack_communication.post_daklapack_order
def post_daklapack_order(payload):
    oauth_session = _get_daklapack_oauth2_session()
    # the json parameter sets the content-type in the headers
    # to application/json, whereas if used data parameter, would have to set
    # content-type manually
    dak_order_post_url = f"{SERVER_CONFIG['daklapack_api_base_url']}" \
                         f"/api/Orders"
    result = oauth_session.post(
        dak_order_post_url, json=payload,
        headers={SERVER_CONFIG["daklapack_subscription_key_name"]:
                     SERVER_CONFIG["daklapack_subscription_key_val"]})
    return result


# TODO: AB: unit-test daklapack_communication.send_daklapack_hold_email
def send_daklapack_hold_email(daklapack_order):
    try:
        template_args = {"order_id": daklapack_order.id,
                         "fulfillment_hold_msg":
                             daklapack_order.fulfillment_hold_msg}
        email_subject = f"Hold fulfillment of order {daklapack_order.id}"
        dak_service_email = SERVER_CONFIG["daklapack_service_email"]
        celery_send_email.apply_async(
            args=[dak_service_email, email_subject,
                  ORDER_HOLD_TEMPLATE_PATH,
                  list(template_args.keys()), template_args,
                  "EMAIL", "DAK_ORDER_HOLD"])
        email_success = True
    except Exception:  # noqa
        email_success = False

    return email_success
