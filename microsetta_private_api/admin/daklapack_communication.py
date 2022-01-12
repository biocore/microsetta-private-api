from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from flask import Response
from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.tasks import send_basic_email as celery_send_email

DAK_HEADERS = {
    SERVER_CONFIG["daklapack_subscription_key_name"]:
        SERVER_CONFIG["daklapack_subscription_key_val"]
}


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


def _convert_to_flask_response(requests_response):
    return Response(
        response=requests_response.content,
        status=requests_response.status_code,
        headers=dict(requests_response.headers)
    )


def post_daklapack_orders(payload):
    return _post_to_daklapack_api("/api/Orders/List", payload, raise_err=False)


def post_daklapack_order_archive(payload):
    return _post_to_daklapack_api("/api/Orders/Archive", payload)


def _post_to_daklapack_api(url_suffix, payload, raise_err=True):
    oauth_session = _get_daklapack_oauth2_session()

    dak_order_post_url = f"{SERVER_CONFIG['daklapack_api_base_url']}" \
                         f"{url_suffix}"

    # the json parameter sets the content-type in the headers
    # to application/json, whereas if used data parameter, would have to set
    # content-type manually
    requests_response = oauth_session.post(
        dak_order_post_url, json=payload, headers=DAK_HEADERS)
    result = _convert_to_flask_response(requests_response)

    if result.status_code >= 300:
        if raise_err:
            raise ValueError(f"Posting {payload} to {url_suffix} received "
                             f"status code {result.status_code}: "
                             f"{result.json}")
    return result


def send_daklapack_order_errors_report_email(errors_list):
    result = None
    if len(errors_list) > 0:
        template_args = {"errors": errors_list}
        email_subject = "Daklapack order errors"

        result = _send_daklapack_email(template_args, email_subject,
                                       "daklapack_errors_report_email",
                                       "email/daklapack_order_errors_report",
                                       "DAK_ORDER_ERRORS_REPORT")
    return result


def send_daklapack_polling_errors_report_email(errors_list):
    result = None
    if len(errors_list) > 0:
        template_args = {"errors": errors_list}
        email_subject = "Daklapack polling code errors"

        result = _send_daklapack_email(template_args, email_subject,
                                       "daklapack_errors_report_email",
                                       "email/daklapack_polling_errors_report",
                                       "DAK_POLLING_ERRORS_REPORT")
    return result


def _send_daklapack_email(template_args, email_subject, email_config_key,
                          template_path, email_subtype):
    try:
        errors_report_email = SERVER_CONFIG[email_config_key]
        celery_send_email.apply_async(
            args=[errors_report_email, email_subject, template_path,
                  list(template_args.keys()), template_args,
                  "EMAIL", email_subtype])
        email_success = True
    except Exception:  # noqa
        email_success = False

    return email_success


def get_daklapack_orders_status(page_num):
    return _get_from_daklapack_api(f"/api/orders?Page={int(page_num)}")


def get_daklapack_order_details(order_id):
    return _get_from_daklapack_api(f"/api/orders/{order_id}")


def _get_from_daklapack_api(url_suffix):
    oauth_session = _get_daklapack_oauth2_session()
    dak_order_get_url = f"{SERVER_CONFIG['daklapack_api_base_url']}" \
                        f"{url_suffix}"

    requests_response = oauth_session.get(dak_order_get_url,
                                          headers=DAK_HEADERS)
    result = _convert_to_flask_response(requests_response)

    if result.status_code >= 300:
        raise ValueError(f"Getting {url_suffix} received status code "
                         f"{result.status_code}: {result.json}")

    return result
