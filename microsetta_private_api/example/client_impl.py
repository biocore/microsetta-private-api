import flask
from flask import render_template, session, redirect
import jwt
import requests
from requests.auth import AuthBase
from urllib.parse import quote
from os import path
from datetime import datetime

# Authrocket uses RS256 public keys, so you can validate anywhere and safely
# store the key in code. Obviously using this mechanism, we'd have to push code
# to roll the keys, which is not ideal, but you can instead hold this in a
# config somewhere and reload

# Python is dumb, don't put spaces anywhere in this string.
from werkzeug.exceptions import BadRequest

from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.model.source import Source
import importlib.resources as pkg_resources


PUB_KEY = pkg_resources.read_text(
    'microsetta_private_api',
    "authrocket.pubkey")

TOKEN_KEY_NAME = 'token'
ADMIN_MODE_KEY = 'admin_mode'
HOME_URL = "/home"
HELP_EMAIL = "microsetta@ucsd.edu"
REROUTE_KEY = "reroute"

KIT_NAME_KEY = "kit_name"
EMAIL_CHECK_KEY = "email_checked"
ACCT_FNAME_KEY = "first_name"
ACCT_LNAME_KEY = "last_name"
ACCT_EMAIL_KEY = "email"
ACCT_ADDR_KEY = "address"
ACCT_WRITEABLE_KEYS = [ACCT_FNAME_KEY, ACCT_LNAME_KEY, ACCT_EMAIL_KEY,
                       ACCT_ADDR_KEY]
ACCT_ADDR_STREET_KEY = "street"
ACCT_ADDR_CITY_KEY = "city"
ACCT_ADDR_STATE_KEY = "state"
ACCT_ADDR_POST_CODE_KEY = "post_code"
ACCT_ADDR_COUNTRY_CODE_KEY = "country_code"

# States
NEEDS_REROUTE = "NeedsReroute"
NEEDS_LOGIN = "NeedsLogin"
NEEDS_ACCOUNT = "NeedsAccount"
NEEDS_EMAIL_CHECK = "NeedsEmailCheck"
NEEDS_SURVEY = "NeedsSurvey"
HOME_PREREQS_MET = "TokenPrereqsMet"
ACCT_PREREQS_MET = "AcctPrereqsMet"
SOURCE_PREREQS_MET = "SourcePrereqsMet"

# TODO FIXME HACK:  VIOSCREEN_ID is just hardcoded.  Api does not specify what
#  special handling is required.  API must specify per-sample survey templates
#  in some way, as well as any special handling for external surveys.
VIOSCREEN_ID = 10001

# TODO FIXME HACK:  In the future, we will want to be able to persist these
#  messages, or tie them to dates of specific events like system downtime.
#  Placing them in memory here is a stopgap until the minimal interface can be
#  properly separated out.
SYSTEM_MSG = None
SYSTEM_MSG_STYLE = None


def _get_req_survey_templates_by_source_type(source_type):
    if source_type == Source.SOURCE_TYPE_HUMAN:
        return [1, 6]
    elif source_type == Source.SOURCE_TYPE_ANIMAL:
        return []
    elif source_type == Source.SOURCE_TYPE_ENVIRONMENT:
        return []
    else:
        raise ValueError("Unknown source type: '%s'" % source_type)


def _make_path(account_id=None, source_id=None, suffix=None):
    result = "/accounts"
    if account_id is not None:
        result = path.join(result, account_id)
        if source_id is not None:
            result = path.join(result, "sources", source_id)

    if suffix is not None:
        result = path.join(result, suffix)

    return result


def _make_acct_path(account_id, suffix=None):
    return _make_path(account_id=account_id, suffix=suffix)


def _make_source_path(account_id, source_id, suffix=None):
    return _make_path(account_id=account_id, source_id=source_id,
                      suffix=suffix)


def _check_home_prereqs():
    current_state = {}
    if TOKEN_KEY_NAME not in session:
        return NEEDS_LOGIN, current_state

    if not session[ADMIN_MODE_KEY]:
        # Do they need to make an account? YES-> create_acct.html
        needs_reroute, accts_output, _ = ApiRequest.get("/accounts")
        # if there's an error, reroute to error page
        if needs_reroute:
            current_state[REROUTE_KEY] = accts_output
            return NEEDS_REROUTE, current_state

        if len(accts_output) == 0:
            # NB: Overwriting outputs from get call above
            needs_reroute, accts_output, _ = ApiRequest.post(
                "/accounts/legacies")
            if needs_reroute:
                current_state[REROUTE_KEY] = accts_output
                return NEEDS_REROUTE, current_state
            # if no legacy account found, need new account
            if len(accts_output) == 0:
                return NEEDS_ACCOUNT, current_state

    # If you got here, you have a token and you have (at least one) account
    # (True even of admins who skipped the above account check, as you can't
    # be an admin unless you have a microsetta account that says you are)
    return HOME_PREREQS_MET, current_state


def _check_acct_prereqs(account_id, current_state=None):
    current_state = {} if current_state is None else current_state
    current_state['account_id'] = account_id

    # If we haven't yet checked for email mismatches and gotten user decision,
    # and the user isn't an admin (who could be looking at another person's
    # account and thus have that email not match their login one):
    if not session.get(EMAIL_CHECK_KEY, False) and not session[ADMIN_MODE_KEY]:
        # Does email in our accounts table match email in authrocket?
        needs_reroute, email_match, _ = ApiRequest.get(
            '/accounts/{0}/email_match'.format(account_id))
        if needs_reroute:
            current_state[REROUTE_KEY] = email_match
            return NEEDS_REROUTE, current_state
        # if they don't match AND the user hasn't already refused update
        if not email_match["email_match"]:
            return NEEDS_EMAIL_CHECK, current_state

        session[EMAIL_CHECK_KEY] = True

    # IF we decide that every acct needs at least one source,
    # this is where that check would go

    return ACCT_PREREQS_MET, current_state


def _check_source_prereqs(acct_id, source_id, current_state=None):
    SURVEY_TEMPLATE_ID_KEY = "survey_template_id"
    current_state = {} if current_state is None else current_state
    current_state['source_id'] = source_id

    if not session[ADMIN_MODE_KEY]:
        # Get the input source
        has_error, source_output, _ = ApiRequest.get(
            '/accounts/%s/sources/%s' %
            (acct_id, source_id))
        if has_error:
            return source_output

        # Get all required survey template ids for this source type
        req_survey_template_ids = _get_req_survey_templates_by_source_type(
            source_output["source_type"])

        # Get all the current answered surveys for this source
        needs_reroute, surveys_output, _ = ApiRequest.get(
            '/accounts/{0}/sources/{1}/surveys'.format(acct_id, source_id))
        if needs_reroute:
            current_state[REROUTE_KEY] = surveys_output
            return NEEDS_REROUTE, current_state
        template_ids_of_answered_surveys = [x[SURVEY_TEMPLATE_ID_KEY] for x
                                            in surveys_output]

        # For each required survey template id for this source type
        for curr_req_survey_template_id in req_survey_template_ids:
            # Does this source LACK an answered survey with this template id?
            if curr_req_survey_template_id not in \
                    template_ids_of_answered_surveys:
                current_state["needed_survey_template_id"] = \
                    curr_req_survey_template_id
                return NEEDS_SURVEY, current_state

    return SOURCE_PREREQS_MET, current_state


def _check_relevant_prereqs(acct_id=None, source_id=None):
    prereq_step, current_state = _check_home_prereqs()
    if prereq_step == HOME_PREREQS_MET:
        if acct_id is not None:
            prereq_step, current_state = _check_acct_prereqs(
                acct_id, current_state)
            if prereq_step == ACCT_PREREQS_MET:
                if source_id is not None:
                    prereq_step, current_state = _check_source_prereqs(
                        acct_id, source_id, current_state)
                # end if there is a source id
            # end if acct prereqs are met
        # end if there is an acct id
    # end if home prereqs are met

    return prereq_step, current_state


# Client might not technically care who the user is, but if they do, they
# get the token, validate it, and pull email out of it.
def _parse_jwt(token):
    decoded = jwt.decode(token, PUB_KEY, algorithms=['RS256'], verify=True)
    email_verified = decoded.get('email_verified', False)
    return decoded["email"], email_verified


def _route_to_closest_sink(prereqs_step, current_state):
    print("Current Prereq Step:", prereqs_step)
    acct_id = current_state.get("account_id", None)
    source_id = current_state.get("source_id", None)

    if prereqs_step == NEEDS_REROUTE:
        # where you get rerouted to depends on why you need
        # rerouting: api authorization errors go back to home page,
        # all other api errors go to error page
        return current_state[REROUTE_KEY]
    elif prereqs_step == NEEDS_LOGIN or prereqs_step == HOME_PREREQS_MET:
        return redirect(HOME_URL)
    elif prereqs_step == NEEDS_ACCOUNT:
        return redirect("/create_account")
    elif prereqs_step == NEEDS_EMAIL_CHECK:
        return redirect(_make_acct_path(acct_id, suffix="update_email"))
    elif prereqs_step == NEEDS_SURVEY:
        needed_survey_template_id = current_state["needed_survey_template_id"]
        return redirect(_make_source_path(
            acct_id, source_id, suffix="take_survey?survey_template_id=%s"
                                       % needed_survey_template_id))
    elif prereqs_step == ACCT_PREREQS_MET:
        # redirect to the account details page (showing all the sources)
        return redirect(_make_acct_path(acct_id))
    elif prereqs_step == SOURCE_PREREQS_MET:
        # redirect to the source details page (showing all samples)
        return redirect(_make_source_path(acct_id, source_id))
    else:
        return get_show_error_page(
            "Unknown prereq_step: '{0}'".format(prereqs_step))


def _refresh_state_and_route_to_sink(account_id=None, source_id=None):
    prereqs_step, curr_state = _check_relevant_prereqs(account_id, source_id)
    return _route_to_closest_sink(prereqs_step, curr_state)


def _get_kit(kit_name):
    unable_to_validate_msg = "Unable to validate the kit name; please " \
                             "reload the page."
    error_msg = None
    response = None

    try:
        # call api and find out if kit name has unclaimed samples.
        # NOT doing this through ApiRequest.get bc in this case
        # DON'T want the automated error-handling

        response = requests.get(
            ApiRequest.API_URL + '/kits/',  # appending slash saves a 308 redir
            auth=BearerAuth(session[TOKEN_KEY_NAME]),
            verify=ApiRequest.CAfile,
            params=ApiRequest.build_params({KIT_NAME_KEY: kit_name}))

        if response.status_code == 404:
            error_msg = ("The provided kit id is not valid or has "
                         "already been used; please re-check your entry.")
        elif response.status_code > 200:
            error_msg = unable_to_validate_msg
    except:  # noqa
        error_msg = unable_to_validate_msg

    if error_msg is not None:
        if response is None:
            return None, error_msg, 500
        else:
            return None, error_msg, response.status_code

    return response.json(), None, response.status_code


def _get_invalid_survey_state_reroute(account_id, source_id,
                                      survey_template_id,
                                      addtl_allowed_steps=None):
    """ Get reroute if user isn't allowed to take this survey in current state.

    Check if the user is in one of the externally-specified allowed states or,
    if not, if they are the NEEDS_SURVEY state AND the survey they need is
    the one whose survey_template_id is passed in.  If either of these
    conditions is met, the user is allowed to take this survey now, so they
    don't need to be rerouted, so this method returns None.  However, if
    neither of these criteria is met, determine where the user should be
    rerouted to and return that info.

    """
    if addtl_allowed_steps is None:
        addtl_allowed_steps = []
    prereqs_step, curr_state = _check_relevant_prereqs(account_id, source_id)
    if prereqs_step not in addtl_allowed_steps:
        needed_template_id = curr_state.get("needed_survey_template_id")
        request_is_needed_template = needed_template_id == survey_template_id
        if not (prereqs_step == NEEDS_SURVEY and request_is_needed_template):
            return _route_to_closest_sink(prereqs_step, curr_state)

    return None


def _associate_sample_to_survey(account_id, source_id, sample_id, survey_id):
    # Associate the input answered surveys with this sample.
    has_error, sample_survey_output, _ = ApiRequest.post(
        '/accounts/{0}/sources/{1}/samples/{2}/surveys'.format(
            account_id, source_id, sample_id
        ), json={"survey_id": survey_id}
    )
    if has_error:
        return sample_survey_output

    return None


# Error display does not require any prereqs, so this method doesn't check any
def get_show_error_page(error_msg):
    # output is general error page
    error_txt = quote(error_msg)
    mailto_url = "mailto:{0}?subject={1}&body={2}".format(
        HELP_EMAIL, quote("minimal interface error"), error_txt)

    output = render_template('error.jinja2',
                             admin_mode=session.get(ADMIN_MODE_KEY, False),
                             mailto_url=mailto_url,
                             error_msg=error_msg,
                             endpoint=SERVER_CONFIG["endpoint"],
                             authrocket_url=SERVER_CONFIG["authrocket_url"])

    return output


# FAQ display does not require any prereqs, so this method doesn't check any
def get_show_faq():
    output = render_template('faq.jinja2',
                             admin_mode=session.get(ADMIN_MODE_KEY, False),
                             authrocket_url=SERVER_CONFIG["authrocket_url"],
                             endpoint=SERVER_CONFIG["endpoint"])
    return output


def get_home():
    user = None
    email_verified = False
    accts_output = None

    if TOKEN_KEY_NAME in session:
        try:
            # If user leaves the page open, the token can expire before the
            # session, so if our token goes back we need to force them to login
            # again.
            user, email_verified = _parse_jwt(session[TOKEN_KEY_NAME])
        except jwt.exceptions.ExpiredSignatureError:
            return redirect('/logout')

        if email_verified:
            home_step, curr_state = _check_home_prereqs()
            if home_step == NEEDS_REROUTE:
                return curr_state[REROUTE_KEY]

            has_error, accts_output, _ = ApiRequest.get("/accounts")
            # if there's an error, reroute to error page
            if has_error:
                return accts_output

    # Switch out home page in administrator mode
    if session.get(ADMIN_MODE_KEY, False):
        return render_template('admin_home.jinja2',
                               admin_mode=session.get(ADMIN_MODE_KEY, False),
                               accounts=[],
                               endpoint=SERVER_CONFIG["endpoint"],
                               authrocket_url=SERVER_CONFIG["authrocket_url"])

    # Note: home.jinja2 sends the user directly to authrocket to complete the
    # login if they aren't logged in yet.
    return render_template('home.jinja2',
                           admin_mode=session.get(ADMIN_MODE_KEY, False),
                           user=user,
                           email_verified=email_verified,
                           accounts=accts_output,
                           endpoint=SERVER_CONFIG["endpoint"],
                           authrocket_url=SERVER_CONFIG["authrocket_url"])


def get_rootpath():
    return redirect(HOME_URL)


def get_authrocket_callback(token):
    session[TOKEN_KEY_NAME] = token
    do_return, accts_output, _ = ApiRequest.get('/accounts')
    if do_return:
        return accts_output

    # new authrocket logins do not have an account yet
    if len(accts_output) > 0:
        session[ADMIN_MODE_KEY] = accts_output[0]['account_type'] == 'admin'
    else:
        session[ADMIN_MODE_KEY] = False

    return redirect(HOME_URL)


def get_signup_intermediate():
    output = render_template('signup_intermediate.jinja2',
                             authrocket_url=SERVER_CONFIG["authrocket_url"],
                             endpoint=SERVER_CONFIG["endpoint"])
    return output


def get_logout():
    session.clear()
    return redirect(HOME_URL)


def get_create_account():
    prereqs_step, curr_state = _check_relevant_prereqs()
    if prereqs_step != NEEDS_ACCOUNT:
        return _route_to_closest_sink(prereqs_step, curr_state)

    email, _ = _parse_jwt(session[TOKEN_KEY_NAME])
    # TODO:  Need to support other countries
    #  and not default to US and California
    default_account_values = {
            ACCT_EMAIL_KEY: email,
            ACCT_FNAME_KEY: '',
            ACCT_LNAME_KEY: '',
            ACCT_ADDR_KEY: {
                ACCT_ADDR_STREET_KEY: '',
                ACCT_ADDR_CITY_KEY: '',
                ACCT_ADDR_STATE_KEY: 'CA',
                ACCT_ADDR_POST_CODE_KEY: '',
                ACCT_ADDR_COUNTRY_CODE_KEY: 'US'
            }
        }

    return render_template('account_details.jinja2',
                           CREATE_ACCT=True,
                           admin_mode=session.get(ADMIN_MODE_KEY, False),
                           authorized_email=email,
                           account=default_account_values)


def post_create_account(body):
    new_acct_id = None
    prereqs_step, curr_state = _check_relevant_prereqs()
    if prereqs_step == NEEDS_ACCOUNT:
        kit_name = body[KIT_NAME_KEY]
        session[KIT_NAME_KEY] = kit_name

        api_json = {
            ACCT_FNAME_KEY: body['first_name'],
            ACCT_LNAME_KEY: body['last_name'],
            ACCT_EMAIL_KEY: body['email'],
            ACCT_ADDR_KEY: {
                ACCT_ADDR_STREET_KEY: body['street'],
                ACCT_ADDR_CITY_KEY: body['city'],
                ACCT_ADDR_STATE_KEY: body['state'],
                ACCT_ADDR_POST_CODE_KEY: body['post_code'],
                ACCT_ADDR_COUNTRY_CODE_KEY: body['country_code']
            },
            KIT_NAME_KEY: kit_name
        }

        has_error, accts_output, _ = \
            ApiRequest.post("/accounts", json=api_json)
        if has_error:
            return accts_output

        new_acct_id = accts_output["account_id"]

    return _refresh_state_and_route_to_sink(new_acct_id)


def get_update_email(account_id):
    prereqs_step, curr_state = _check_relevant_prereqs(account_id)
    if prereqs_step != NEEDS_EMAIL_CHECK:
        return _route_to_closest_sink(prereqs_step, curr_state)

    return render_template("update_email.jinja2",
                           admin_mode=session.get(ADMIN_MODE_KEY, False),
                           account_id=account_id)


def post_update_email(account_id, body):
    prereqs_step, curr_state = _check_relevant_prereqs(account_id)
    if prereqs_step == NEEDS_EMAIL_CHECK:
        # if the customer wants to update their email:
        update_email = body["do_update"] == "Yes"
        if update_email:
            # get the existing account object
            has_error, acct_output, _ = ApiRequest.get(
                '/accounts/%s' % account_id)
            if has_error:
                return acct_output

            # change the email to the one in the authrocket account
            authrocket_email, _ = _parse_jwt(session[TOKEN_KEY_NAME])
            acct_output[ACCT_EMAIL_KEY] = authrocket_email
            # retain only writeable fields; KeyError if any of them missing
            mod_acct = {k: acct_output[k] for k in ACCT_WRITEABLE_KEYS}

            # write back the updated account details
            has_error, put_output, _ = ApiRequest.put(
                '/accounts/%s' % account_id, json=mod_acct)
            if has_error:
                return put_output

        # even if they decided NOT to update, don't ask again this session
        session[EMAIL_CHECK_KEY] = True

    return _refresh_state_and_route_to_sink(account_id)


def get_account(account_id):
    prereqs_step, curr_state = _check_relevant_prereqs(account_id)
    if prereqs_step != ACCT_PREREQS_MET:
        return _route_to_closest_sink(prereqs_step, curr_state)

    has_error, account, _ = ApiRequest.get('/accounts/%s' % account_id)
    if has_error:
        return account

    has_error, sources, _ = ApiRequest.get('/accounts/%s/sources' % account_id)
    if has_error:
        return sources

    return render_template('account_overview.jinja2',
                           admin_mode=session.get(ADMIN_MODE_KEY, False),
                           account=account,
                           sources=sources)


def get_account_details(account_id):
    prereqs_step, curr_state = _check_relevant_prereqs(account_id)
    if prereqs_step != ACCT_PREREQS_MET:
        return _route_to_closest_sink(prereqs_step, curr_state)

    has_error, account, _ = ApiRequest.get('/accounts/%s' % account_id)
    if has_error:
        return account

    return render_template('account_details.jinja2',
                           CREATE_ACCT=False,
                           admin_mode=session.get(ADMIN_MODE_KEY, False),
                           account=account)


def post_account_details(account_id, body):
    prereqs_step, curr_state = _check_relevant_prereqs(account_id)
    if prereqs_step == ACCT_PREREQS_MET:
        acct = {
            ACCT_FNAME_KEY: body['first_name'],
            ACCT_LNAME_KEY: body['last_name'],
            ACCT_EMAIL_KEY: body['email'],
            ACCT_ADDR_KEY: {
                ACCT_ADDR_STREET_KEY: body['street'],
                ACCT_ADDR_CITY_KEY: body['city'],
                ACCT_ADDR_STATE_KEY: body['state'],
                ACCT_ADDR_POST_CODE_KEY: body['post_code'],
                ACCT_ADDR_COUNTRY_CODE_KEY: body['country_code']
            }
        }

        do_return, sample_output, _ = ApiRequest.put('/accounts/%s' %
                                                     account_id, json=acct)
        if do_return:
            return sample_output

    return _refresh_state_and_route_to_sink(account_id)


def get_create_human_source(account_id):
    prereqs_step, curr_state = _check_relevant_prereqs(account_id)
    if prereqs_step != ACCT_PREREQS_MET:
        return _route_to_closest_sink(prereqs_step, curr_state)

    endpoint = SERVER_CONFIG["endpoint"]
    relative_post_url = _make_acct_path(account_id,
                                        suffix="create_human_source")
    post_url = endpoint + relative_post_url
    has_error, consent_output, _ = ApiRequest.get(
        "/accounts/{0}/consent".format(account_id),
        params={"consent_post_url": post_url})

    if has_error:
        return consent_output

    # NB: this get does not render a jinja template because
    # *the private api has already rendered a jinja template*
    # and returns straight html ...
    return consent_output["consent_html"]


def post_create_human_source(account_id, body):
    new_source_id = None
    prereqs_step, curr_state = _check_relevant_prereqs(account_id)
    if prereqs_step == ACCT_PREREQS_MET:
        has_error, consent_output, _ = ApiRequest.post(
            "/accounts/{0}/consent".format(account_id), json=body)
        if has_error:
            return consent_output

        new_source_id = consent_output["source_id"]

    return _refresh_state_and_route_to_sink(account_id, new_source_id)


def get_create_nonhuman_source(account_id):
    prereqs_step, curr_state = _check_relevant_prereqs(account_id)
    if prereqs_step != ACCT_PREREQS_MET:
        return _route_to_closest_sink(prereqs_step, curr_state)

    return render_template('create_nonhuman_source.jinja2',
                           account_id=account_id)


def post_create_nonhuman_source(account_id, body):
    prereqs_step, curr_state = _check_relevant_prereqs(account_id)
    if prereqs_step == ACCT_PREREQS_MET:
        has_error, sources_output, _ = ApiRequest.post(
            "/accounts/{0}/sources".format(account_id), json=body)
        if has_error:
            return sources_output

    return _refresh_state_and_route_to_sink(account_id)


def get_fill_local_source_survey(account_id, source_id, survey_template_id):
    # if we are filling out a source-level survey, it must come before the
    # source prerequisites are met; if a sample-level one, it can come after
    reroute = _get_invalid_survey_state_reroute(account_id, source_id,
                                                survey_template_id)
    if reroute is not None:
        return reroute

    has_error, survey_output, _ = ApiRequest.get(
        '/accounts/%s/sources/%s/survey_templates/%s' %
        (account_id, source_id, survey_template_id))
    if has_error:
        return survey_output

    return render_template("survey.jinja2",
                           admin_mode=session.get(ADMIN_MODE_KEY, False),
                           endpoint=SERVER_CONFIG["endpoint"],
                           account_id=account_id,
                           source_id=source_id,
                           survey_template_id=survey_template_id,
                           survey_schema=survey_output[
                               'survey_template_text'])


def post_ajax_fill_local_source_survey(account_id, source_id,
                                       survey_template_id, body):
    reroute = _get_invalid_survey_state_reroute(account_id, source_id,
                                                survey_template_id)
    if reroute is not None:
        return reroute

    has_error, surveys_output, _ = ApiRequest.post(
        "/accounts/%s/sources/%s/surveys" % (account_id, source_id),
        json={
            "survey_template_id": survey_template_id,
            "survey_text": body
        })
    if has_error:
        return surveys_output

    return _refresh_state_and_route_to_sink(account_id, source_id)


def get_fill_vioscreen_remote_sample_survey(account_id, source_id, sample_id,
                                            survey_template_id):
    if survey_template_id != VIOSCREEN_ID:
        return get_show_error_page("Non-vioscreen remote surveys are "
                                   "not yet supported")

    # if we are filling out a source-level survey, it must come before the
    # source prerequisites are met, but a sample-level one can come after
    reroute = _get_invalid_survey_state_reroute(account_id, source_id,
                                                VIOSCREEN_ID,
                                                [SOURCE_PREREQS_MET])
    if reroute is not None:
        return reroute

    suffix = "samples/%s/vspassthru" % sample_id
    redirect_url = SERVER_CONFIG["endpoint"] + \
        _make_source_path(account_id, source_id, suffix=suffix)
    params = {'survey_redirect_url': redirect_url}
    has_error, survey_output, _ = ApiRequest.get(
        '/accounts/%s/sources/%s/survey_templates/%s' %
        (account_id, source_id, VIOSCREEN_ID), params=params)
    if has_error:
        return survey_output

    # remote surveys go to an external url, not our jinja2 template
    return redirect(survey_output['survey_template_text']['url'])


# NB: There is no post_fill_sample_survey because right now the ONLY
# per-sample survey we have is the remote food frequency questionnaire
# administered through vioscreen, and saving that requires its own special
# handling (this function).
def get_to_save_vioscreen_remote_sample_survey(account_id, source_id,
                                               sample_id, key):
    reroute = _get_invalid_survey_state_reroute(account_id, source_id,
                                                VIOSCREEN_ID,
                                                [SOURCE_PREREQS_MET])
    if reroute is not None:
        return reroute

    # TODO FIXME HACK:  This is insanity.  I need to see the vioscreen docs
    #  to interface with our API...
    has_error, surveys_output, surveys_headers = ApiRequest.post(
        "/accounts/%s/sources/%s/surveys" % (account_id, source_id),
        json={
            "survey_template_id": VIOSCREEN_ID,
            "survey_text": {"key": key}
        })
    if has_error:
        return surveys_output

    answered_survey_id = surveys_headers['Location']
    answered_survey_id = answered_survey_id.split('/')[-1]

    # associate this answered vioscreen survey to this sample
    sample_survey_output = _associate_sample_to_survey(
        account_id, source_id, sample_id, answered_survey_id)
    if sample_survey_output is not None:
        return sample_survey_output

    return _refresh_state_and_route_to_sink(account_id, source_id)


def get_source(account_id, source_id):
    prereqs_step, curr_state = _check_relevant_prereqs(account_id,
                                                       source_id)
    if prereqs_step != SOURCE_PREREQS_MET:
        return _route_to_closest_sink(prereqs_step, curr_state)

    # Retrieve the account to determine which kit it was created with
    has_error, account_output, _ = ApiRequest.get(
        '/accounts/%s' % account_id)
    if has_error:
        return account_output

    # Check if there are any unclaimed samples in the kit
    original_kit, _, kit_status = _get_kit(account_output['kit_name'])
    if kit_status == 404:
        claim_kit_name_hint = None
    else:
        claim_kit_name_hint = account_output['kit_name']

    # Retrieve the source
    has_error, source_output, _ = ApiRequest.get(
        '/accounts/%s/sources/%s' %
        (account_id, source_id))
    if has_error:
        return source_output

    # Retrieve all samples from the source
    has_error, samples_output, _ = ApiRequest.get(
        '/accounts/%s/sources/%s/samples' % (account_id, source_id))
    if has_error:
        return samples_output

    # Retrieve all surveys available to the source
    has_error, surveys_output, _ = ApiRequest.get(
        '/accounts/%s/sources/%s/survey_templates' % (account_id, source_id))
    if has_error:
        return surveys_output

    per_sample = []
    per_source = []
    restrict_to = _get_req_survey_templates_by_source_type(
        source_output["source_type"])
    for survey in surveys_output:
        if survey['survey_template_id'] in restrict_to:
            per_source.append(survey)
        if survey['survey_template_id'] == VIOSCREEN_ID:
            per_sample.append(survey)

    # Identify answered surveys for the source
    has_error, survey_answers, _ = ApiRequest.get(
        '/accounts/%s/sources/%s/surveys' % (account_id, source_id))
    if has_error:
        return survey_answers

    # TODO: Would be nice to know when the user took the survey instead of a
    #  boolean
    for answer in survey_answers:
        template_id = answer['survey_template_id']
        for template in per_source:
            if template['survey_template_id'] == template_id:
                template['answered'] = True

    # Identify answered surveys for the samples
    for sample in samples_output:
        sample['ffq'] = False
        sample_id = sample['sample_id']
        # TODO:  This is a really awkward and slow way to get this information
        has_error, per_sample_answers, _ = ApiRequest.get(
            '/accounts/%s/sources/%s/samples/%s/surveys' %
            (account_id, source_id, sample_id))
        if has_error:
            return per_sample_answers

        for answer in per_sample_answers:
            if answer['survey_template_id'] == VIOSCREEN_ID:
                sample['ffq'] = True

    # prettify datetime
    needs_assignment = False
    for sample in samples_output:
        if sample['sample_datetime'] is None:
            needs_assignment = True
        else:
            dt = datetime.fromisoformat(sample['sample_datetime'])
            sample['sample_datetime'] = dt.strftime("%b-%d-%Y %-I:%M %p")

    needs_assignment = any([sample['sample_datetime'] is None
                            for sample in samples_output])

    is_human = source_output['source_type'] == Source.SOURCE_TYPE_HUMAN
    return render_template('source.jinja2',
                           admin_mode=session.get(ADMIN_MODE_KEY, False),
                           account_id=account_id,
                           source_id=source_id,
                           is_human=is_human,
                           needs_assignment=needs_assignment,
                           samples=samples_output,
                           surveys=per_source,
                           source_name=source_output['source_name'],
                           vioscreen_id=VIOSCREEN_ID,
                           claim_kit_name_hint=claim_kit_name_hint)


def get_update_sample(account_id, source_id, sample_id):
    prereqs_step, curr_state = _check_relevant_prereqs(account_id, source_id)
    if prereqs_step != SOURCE_PREREQS_MET:
        return _route_to_closest_sink(prereqs_step, curr_state)

    has_error, source_output, _ = ApiRequest.get(
        '/accounts/%s/sources/%s' %
        (account_id, source_id)
    )
    if has_error:
        return source_output

    has_error, sample_output, _ = ApiRequest.get(
        '/accounts/%s/sources/%s/samples/%s' %
        (account_id, source_id, sample_id))
    if has_error:
        return sample_output

    source_type = source_output['source_type']
    is_environmental = source_type == Source.SOURCE_TYPE_ENVIRONMENT
    is_human = source_type == Source.SOURCE_TYPE_HUMAN

    if is_human:
        # Human Settings
        sample_sites = ["Blood (skin prick)", "Stool", "Mouth", "Nares",
                        "Nasal mucus", "Right hand", "Left hand",
                        "Forehead", "Torso", "Right leg", "Left leg",
                        "Vaginal mucus", "Tears", "Ear wax", "Hair", "Fur"]
        site_hint = None
    elif is_environmental:
        # Environment settings
        sample_sites = [None]
        site_hint = "As we cannot enumerate all possible sampling sites for " \
            "environmental sources, we recommend describing the site " \
            "the sample was taken from in as much detail as " \
            "possible below"
    else:
        raise BadRequest("Sources of type %s are not supported at this time"
                         % source_output['source_type'])

    if sample_output['sample_datetime'] is not None:
        dt = datetime.fromisoformat(sample_output['sample_datetime'])
        sample_output['date'] = dt.strftime("%m/%d/%Y")
        sample_output['time'] = dt.strftime("%-I:%M %p")
    else:
        sample_output['date'] = ""
        sample_output['time'] = ""

    return render_template('sample.jinja2',
                           admin_mode=session.get(ADMIN_MODE_KEY, False),
                           account_id=account_id,
                           source_id=source_id,
                           source_name=source_output['source_name'],
                           sample=sample_output,
                           sample_sites=sample_sites,
                           site_hint=site_hint,
                           is_environmental=is_environmental)


# TODO: guess we should also rewrite as ajax post for sample vue form?
def put_update_sample(account_id, source_id, sample_id):
    prereqs_step, curr_state = _check_relevant_prereqs(account_id, source_id)
    # Checking for only SOURCE_PREREQS_MET here because there are currently no
    # sample-specific prerequisites
    if prereqs_step != SOURCE_PREREQS_MET:
        return _route_to_closest_sink(prereqs_step, curr_state)

    model = {}
    for x in flask.request.form:
        model[x] = flask.request.form[x]

    date = model.pop('sample_date')
    time = model.pop('sample_time')
    date_and_time = date + " " + time
    sample_datetime = datetime.strptime(date_and_time, "%m/%d/%Y %I:%M %p")
    model['sample_datetime'] = sample_datetime.isoformat()

    has_error, sample_output, _ = ApiRequest.put(
        '/accounts/%s/sources/%s/samples/%s' %
        (account_id, source_id, sample_id),
        json=model)

    if has_error:
        return sample_output

    return _refresh_state_and_route_to_sink(account_id, source_id)


def get_ajax_check_kit_valid(kit_name):
    kit, error, _ = _get_kit(kit_name)
    result = True if error is None else error
    return flask.jsonify(result)


def get_ajax_list_kit_samples(kit_name):
    kit, error, code = _get_kit(kit_name)
    result = kit if error is None else error
    return flask.jsonify(result), code


# NB: associating surveys with samples when samples are claimed means that any
# surveys added to this source AFTER these samples are claimed will NOT be
# associated with these samples.  This behavior is by design.
def post_claim_samples(account_id, source_id, body):
    prereqs_step, curr_state = _check_relevant_prereqs(account_id, source_id)
    if prereqs_step == SOURCE_PREREQS_MET:
        sample_ids_to_claim = body.get('sample_id')
        if sample_ids_to_claim is None:
            # User claimed no samples ... shrug
            return _route_to_closest_sink(prereqs_step, curr_state)

        has_error, survey_output, _ = ApiRequest.get(
            '/accounts/{0}/sources/{1}/surveys'.format(account_id, source_id))
        if has_error:
            return survey_output

        # TODO: this will have to get more nuanced when we add animal surveys?
        # Grab all primary and covid surveys from the source and associate with
        # newly claimed samples; non-human sources always have none of these
        survey_ids_to_associate_with_samples = [
            x['survey_id'] for x in survey_output
            if x['survey_template_id'] in [1, 6]
        ]

        # TODO:  Any of these requests may fail independently, but we don't
        #  have a good policy to deal with partial failures.  Currently, we
        #  abort early but that will result in some set of associations being
        #  already made, one association failing, and the remaining
        #  associations not attempted.
        for curr_sample_id in sample_ids_to_claim:
            # Claim sample
            has_error, sample_output, _ = ApiRequest.post(
                '/accounts/{0}/sources/{1}/samples'.format(
                    account_id, source_id),
                json={"sample_id": curr_sample_id})
            if has_error:
                return sample_output

            # Associate the input answered surveys with this sample.
            for survey_id in survey_ids_to_associate_with_samples:
                sample_survey_output = _associate_sample_to_survey(
                        account_id, source_id, curr_sample_id, survey_id)
                if sample_survey_output is not None:
                    return sample_survey_output

    return _refresh_state_and_route_to_sink(account_id, source_id)


# Administrator Mode Functionality
def get_interactive_account_search(email_query):
    do_return, email_diagnostics, _ = ApiRequest.get(
        '/admin/search/account/%s' % (email_query,))
    if do_return:
        return email_diagnostics

    accounts = [{"email": acct['email'], "account_id": acct['id']}
                for acct in email_diagnostics['accounts']]
    return render_template('admin_home.jinja2',
                           admin_mode=session.get(ADMIN_MODE_KEY, False),
                           accounts=accounts,
                           endpoint=SERVER_CONFIG["endpoint"],
                           authrocket_url=SERVER_CONFIG["authrocket_url"])


def get_system_message():
    return render_template('admin_system_panel.jinja2',
                           admin_mode=session.get(ADMIN_MODE_KEY, False))


def post_system_message():
    pass


class BearerAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = "Bearer " + self.token
        return r


class ApiRequest:
    API_URL = SERVER_CONFIG["endpoint"] + "/api"
    DEFAULT_PARAMS = {'language_tag': 'en-US'}
    CAfile = SERVER_CONFIG["CAfile"]

    @classmethod
    def build_params(cls, params):
        all_params = {}
        for key in ApiRequest.DEFAULT_PARAMS:
            all_params[key] = ApiRequest.DEFAULT_PARAMS[key]
        if params:
            for key in params:
                all_params[key] = params[key]
        return all_params

    @classmethod
    def _check_response(cls, response):
        error_code = response.status_code
        output = None
        headers = None

        if response.status_code == 401 or response.status_code == 403:
            # output is redirect to home page for login or email verification
            output = redirect(HOME_URL)
        elif response.status_code >= 400:
            # output is general error page
            output = get_show_error_page(response.text)
        else:
            error_code = 0  # there is a response code but no *error* code
            headers = response.headers
            if response.text:
                output = response.json()

        return error_code, output, headers

    @classmethod
    def get(cls, input_path, params=None):
        response = requests.get(
            ApiRequest.API_URL + input_path,
            auth=BearerAuth(session[TOKEN_KEY_NAME]),
            verify=ApiRequest.CAfile,
            params=cls.build_params(params))

        return cls._check_response(response)

    @classmethod
    def put(cls, input_path, params=None, json=None):
        response = requests.put(
            ApiRequest.API_URL + input_path,
            auth=BearerAuth(session[TOKEN_KEY_NAME]),
            verify=ApiRequest.CAfile,
            params=cls.build_params(params),
            json=json)

        return cls._check_response(response)

    @classmethod
    def post(cls, input_path, params=None, json=None):
        response = requests.post(
            ApiRequest.API_URL + input_path,
            auth=BearerAuth(session[TOKEN_KEY_NAME]),
            verify=ApiRequest.CAfile,
            params=cls.build_params(params),
            json=json)
        return cls._check_response(response)
