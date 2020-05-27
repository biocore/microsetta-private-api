import flask
from flask import render_template, session, redirect
import jwt
import requests
from requests.auth import AuthBase
from urllib.parse import quote
from os import path

# Authrocket uses RS256 public keys, so you can validate anywhere and safely
# store the key in code. Obviously using this mechanism, we'd have to push code
# to roll the keys, which is not ideal, but you can instead hold this in a
# config somewhere and reload

# Python is dumb, don't put spaces anywhere in this string.
from werkzeug.exceptions import BadRequest

from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.model.source import Source
from microsetta_private_api.model.vue.vue_factory import VueFactory
from microsetta_private_api.model.vue.vue_field import VueInputField, \
    VueTextAreaField, VueSelectField, VueDateTimePickerField
import importlib.resources as pkg_resources


PUB_KEY = pkg_resources.read_text(
    'microsetta_private_api',
    "authrocket.pubkey")

TOKEN_KEY_NAME = 'token'
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


def _get_required_survey_templates_by_source_type(source_type):
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

    # Do they need to make an account? YES-> create_acct.html
    needs_reroute, accts_output, _ = ApiRequest.get(_make_path())
    # if there's an error, reroute to error page
    if needs_reroute:
        current_state[REROUTE_KEY] = accts_output
        return NEEDS_REROUTE, current_state

    if len(accts_output) == 0:
        # NB: Overwriting outputs from get call above
        needs_reroute, accts_output, _ = ApiRequest.post(
            _make_path(suffix="legacies"))
        if needs_reroute:
            current_state[REROUTE_KEY] = accts_output
            return NEEDS_REROUTE, current_state
        # if no legacy account found, need new account
        if len(accts_output) == 0:
            return NEEDS_ACCOUNT, current_state

    # If you got here, you have a token and you have (at least one) account
    return HOME_PREREQS_MET, current_state


def _check_acct_prereqs(account_id, current_state=None):
    current_state = {} if current_state is None else current_state
    current_state['account_id'] = account_id

    # If we haven't yet checked for email mismatches and gotten user decision:
    if not session.get(EMAIL_CHECK_KEY, False):
        # Does email in our accounts table match email in authrocket?
        needs_reroute, email_match, _ = ApiRequest.get(
            _make_acct_path(account_id, suffix="email_match"))
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

    # Get the input source
    has_error, source_output, _ = ApiRequest.get(
        '/accounts/%s/sources/%s' %
        (acct_id, source_id))
    if has_error:
        return source_output

    # Get all required survey template ids for this source type
    req_survey_template_ids = _get_required_survey_templates_by_source_type(
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
        if curr_req_survey_template_id not in template_ids_of_answered_surveys:
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
        # TODO: theoretically could route this to the front end /error ..
        # but kind of a waste?  Do we need to reroute all these to front end?
        # Guess doing so means we can't accidentally change front end behavior
        # but not back-end behavior here ...
        return get_show_error_page(
            "Unknown prereq_step: '{0}'".format(prereqs_step))


def _update_state_and_route_to_sink(account_id=None, source_id=None):
    prereqs_step, current_state = _check_relevant_prereqs(account_id,
                                                          source_id)
    return _route_to_closest_sink(prereqs_step, current_state)


def _get_kit(kit_name):
    unable_to_validate_msg = "Unable to validate the kit name; please " \
                             "reload the page."
    error_msg = None
    response_status_code = None

    try:
        # call api and find out if kit name has unclaimed samples.
        # NOT doing this through ApiRequest.get bc in this case
        # DON'T want the automated error-handling

        response = requests.get(
            ApiRequest.API_URL + '/kits/',  # appending slash saves a 308 redir
            auth=BearerAuth(session[TOKEN_KEY_NAME]),
            verify=ApiRequest.CAfile,
            params=ApiRequest.build_params({KIT_NAME_KEY: kit_name}))

        response_status_code = response.status_code

        if response_status_code == 404:
            error_msg = ("The provided kit id is not valid or has "
                         "already been used; please re-check your entry.")
        elif response_status_code > 200:
            error_msg = unable_to_validate_msg
    except:  # noqa
        error_msg = unable_to_validate_msg

    if error_msg is not None:
        return None, error_msg, response_status_code

    return response.json(), None, response_status_code


def _check_survey_allowed(account_id, source_id, survey_template_id,
                          addtl_allowed_steps=None):
    addtl_allowed_steps = [] if addtl_allowed_steps is None \
        else addtl_allowed_steps
    prereqs_step, current_state = _check_relevant_prereqs(account_id,
                                                          source_id)
    if prereqs_step not in addtl_allowed_steps:
        needed_template_id = current_state.get("needed_survey_template_id", "")
        request_is_needed_template = needed_template_id == survey_template_id
        if not (prereqs_step == NEEDS_SURVEY and request_is_needed_template):
            return _route_to_closest_sink(prereqs_step, current_state)

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
                             mailto_url=mailto_url,
                             error_msg=error_msg,
                             endpoint=SERVER_CONFIG["endpoint"],
                             authrocket_url=SERVER_CONFIG["authrocket_url"])

    return output


# FAQ display does not require any prereqs, so this method doesn't check any
def get_show_faq():
    output = render_template('faq.jinja2',
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
            home_step, current_state = _check_home_prereqs()
            if home_step == NEEDS_REROUTE:
                return current_state[REROUTE_KEY]

            has_error, accts_output, _ = ApiRequest.get("/accounts")
            # if there's an error, reroute to error page
            if has_error:
                return accts_output

    # Note: home.jinja2 sends the user directly to authrocket to complete the
    # login if they aren't logged in yet.
    return render_template('home.jinja2',
                           user=user,
                           email_verified=email_verified,
                           accounts=accts_output,
                           endpoint=SERVER_CONFIG["endpoint"],
                           authrocket_url=SERVER_CONFIG["authrocket_url"])


def get_rootpath():
    return redirect(HOME_URL)


def get_authrocket_callback(token):
    session[TOKEN_KEY_NAME] = token
    return redirect(HOME_URL)


def get_logout():
    if TOKEN_KEY_NAME in session:
        # delete these keys if they are here, otherwise ignore
        session.pop(TOKEN_KEY_NAME, None)
        session.pop(KIT_NAME_KEY, None)
        session.pop(EMAIL_CHECK_KEY, None)
    return redirect(HOME_URL)


def get_create_account():
    prereqs_step, current_state = _check_relevant_prereqs()
    if prereqs_step != NEEDS_ACCOUNT:
        return _route_to_closest_sink(prereqs_step, current_state)

    email, _ = _parse_jwt(session[TOKEN_KEY_NAME])
    return render_template('create_acct.jinja2',
                           authorized_email=email)


def post_create_account(body):
    prereqs_step, current_state = _check_relevant_prereqs()
    if prereqs_step == NEEDS_ACCOUNT:
        kit_name = body[KIT_NAME_KEY]
        session[KIT_NAME_KEY] = kit_name

        api_json = {
            ACCT_FNAME_KEY: body['first_name'],
            ACCT_LNAME_KEY: body['last_name'],
            ACCT_EMAIL_KEY: body['email'],
            ACCT_ADDR_KEY: {
                "street": body['street'],
                "city": body['city'],
                "state": body['state'],
                "post_code": body['post_code'],
                "country_code": body['country_code']
            },
            KIT_NAME_KEY: kit_name
        }

        has_error, accts_output, _ = \
            ApiRequest.post("/accounts", json=api_json)
        if has_error:
            return accts_output

    new_acct_id = accts_output["account_id"]
    return _update_state_and_route_to_sink(new_acct_id)


def get_update_email(account_id):
    prereqs_step, current_state = _check_relevant_prereqs(account_id)
    if prereqs_step != NEEDS_EMAIL_CHECK:
        return _route_to_closest_sink(prereqs_step, current_state)

    return render_template("update_email.jinja2", account_id=account_id)


def post_update_email(account_id, body):
    prereqs_step, current_state = _check_relevant_prereqs(account_id)
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

            # write back the updated account info
            has_error, put_output, _ = ApiRequest.put(
                '/accounts/%s' % account_id, json=mod_acct)
            if has_error:
                return put_output

        # even if they decided NOT to update, don't ask again this session
        session[EMAIL_CHECK_KEY] = True

    return _update_state_and_route_to_sink(account_id)


def get_account(account_id):
    prereqs_step, current_state = _check_relevant_prereqs(account_id)
    if prereqs_step != ACCT_PREREQS_MET:
        return _route_to_closest_sink(prereqs_step, current_state)

    has_error, sources, _ = ApiRequest.get('/accounts/%s/sources' % account_id)
    if has_error:
        return sources

    return render_template('account.jinja2',
                           account_id=account_id,
                           sources=sources)


def get_create_human_source(account_id):
    prereqs_step, current_state = _check_relevant_prereqs(account_id)
    if prereqs_step != ACCT_PREREQS_MET:
        return _route_to_closest_sink(prereqs_step, current_state)

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
    prereqs_step, current_state = _check_relevant_prereqs(account_id)
    if prereqs_step == ACCT_PREREQS_MET:
        has_error, consent_output, _ = ApiRequest.post(
            "/accounts/{0}/consent".format(account_id), json=body)
        if has_error:
            return consent_output

    new_source_id = consent_output["source_id"]
    return _update_state_and_route_to_sink(account_id, new_source_id)


def get_create_nonhuman_source(account_id):
    prereqs_step, current_state = _check_relevant_prereqs(account_id)
    if prereqs_step != ACCT_PREREQS_MET:
        return _route_to_closest_sink(prereqs_step, current_state)

    return render_template('create_nonhuman_source.jinja2',
                           account_id=account_id)


def post_create_nonhuman_source(account_id, body):
    prereqs_step, current_state = _check_relevant_prereqs(account_id)
    if prereqs_step == ACCT_PREREQS_MET:
        has_error, sources_output, _ = ApiRequest.post(
            "/accounts/{0}/sources".format(account_id), json=body)
        if has_error:
            return sources_output

    return _update_state_and_route_to_sink(account_id)


def get_fill_local_source_survey(account_id, source_id, survey_template_id):
    # if we are filling out a source-level survey, it must come before the
    # source prerequisites are met; if a sample-level one, it can come after
    reroute = _check_survey_allowed(account_id, source_id, survey_template_id)
    if reroute is not None:
        return reroute

    has_error, survey_output, _ = ApiRequest.get(
        '/accounts/%s/sources/%s/survey_templates/%s' %
        (account_id, source_id, survey_template_id))
    if has_error:
        return survey_output

    return render_template("survey.jinja2",
                           endpoint=SERVER_CONFIG["endpoint"],
                           account_id=account_id,
                           source_id=source_id,
                           survey_template_id=survey_template_id,
                           survey_schema=survey_output[
                               'survey_template_text'])


def post_ajax_fill_local_source_survey(account_id, source_id,
                                       survey_template_id, body):
    reroute = _check_survey_allowed(account_id, source_id, survey_template_id)
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

    return _update_state_and_route_to_sink(account_id, source_id)


def get_fill_vioscreen_remote_sample_survey(account_id, source_id, sample_id,
                                            survey_template_id):
    if survey_template_id != VIOSCREEN_ID:
        return get_show_error_page("Non-vioscreen remote surveys are "
                                   "not yet supported")

    # if we are filling out a source-level survey, it must come before the
    # source prerequisites are met, but a sample-level one can come after
    reroute = _check_survey_allowed(account_id, source_id, VIOSCREEN_ID,
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
def get_to_save_vioscreen_remote_sample_survey(account_id, source_id, sample_id, key):
    reroute = _check_survey_allowed(account_id, source_id, VIOSCREEN_ID,
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

    return _update_state_and_route_to_sink(account_id, source_id)


def get_source(account_id, source_id):
    prereqs_step, current_state = _check_relevant_prereqs(account_id, source_id)
    if prereqs_step != SOURCE_PREREQS_MET:
        return _route_to_closest_sink(prereqs_step, current_state)

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
    restrict_to = _get_required_survey_templates_by_source_type(
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

    needs_assignment = any([sample['sample_datetime'] is None
                            for sample in samples_output])

    is_human = source_output['source_type'] == Source.SOURCE_TYPE_HUMAN
    return render_template('source.jinja2',
                           account_id=account_id,
                           source_id=source_id,
                           is_human=is_human,
                           needs_assignment=needs_assignment,
                           samples=samples_output,
                           surveys=per_source,
                           source_name=source_output['source_name'],
                           vioscreen_id=VIOSCREEN_ID)


def get_update_sample(account_id, source_id, sample_id):
    prereqs_step, current_state = _check_relevant_prereqs(account_id, source_id)
    if prereqs_step != SOURCE_PREREQS_MET:
        return _route_to_closest_sink(prereqs_step, current_state)

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
    factory = VueFactory()

    schema = factory.start_group("Edit Sample Information")\
        .add_field(VueInputField("sample_barcode", "Barcode")
                   .set(disabled=True))\
        .add_field(VueDateTimePickerField("sample_datetime", "Date and Time")
                   .set(required=True,
                        validator="string"))\
        .add_field(VueSelectField("sample_site", "Site", sample_sites)
                   .set(required=not is_environmental,
                        validator="string",
                        disabled=is_environmental,
                        hint=site_hint)) \
        .add_field(VueTextAreaField("sample_notes", "Notes")) \
        .end_group()\
        .build()

    return render_template('sample.jinja2',
                           account_id=account_id,
                           source_id=source_id,
                           source_name=source_output['source_name'],
                           sample=sample_output,
                           schema=schema)


# TODO: guess we should also rewrite as ajax post for sample vue form?
def put_update_sample(account_id, source_id, sample_id):
    prereqs_step, current_state = _check_relevant_prereqs(account_id, source_id)
    # TODO: here we might want a "sample prereqs met"?
    if prereqs_step != SOURCE_PREREQS_MET:
        return _route_to_closest_sink(prereqs_step, current_state)

    model = {}
    for x in flask.request.form:
        model[x] = flask.request.form[x]

    has_error, sample_output, _ = ApiRequest.put(
        '/accounts/%s/sources/%s/samples/%s' %
        (account_id, source_id, sample_id),
        json=model)

    if has_error:
        return sample_output

    return _update_state_and_route_to_sink(account_id, source_id)


def get_ajax_check_kit_valid(kit_name):
    kit, error, _ = _get_kit(kit_name)
    result = True if error is None else error
    return flask.jsonify(result)


def get_ajax_list_kit_samples(kit_name):
    kit, error, code = _get_kit(kit_name)
    result = kit if error is None else error
    return flask.jsonify(result), code


# TODO: Note that associating surveys with samples when samples are claimed
#  means that any surveys added to this source AFTER these samples are claimed
#  will NOT be associated with these samples.  This might be the right behavior
#  but we should probably make an explicit policy decision about that :)
def post_claim_samples(account_id, source_id, body):
    prereqs_step, current_state = _check_relevant_prereqs(account_id, source_id)
    if prereqs_step == SOURCE_PREREQS_MET:
        sample_ids_to_claim = body.get('sample_id', None)
        if sample_ids_to_claim is None:
            # User claimed no samples ... shrug
            return _route_to_closest_sink(prereqs_step, current_state)

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
                '/accounts/{0}/sources/{1}/samples'.format(account_id, source_id),
                json={"sample_id": curr_sample_id})
            if has_error:
                return sample_output

            # Associate the input answered surveys with this sample.
            for survey_id in survey_ids_to_associate_with_samples:
                sample_survey_output = _associate_sample_to_survey(
                        account_id, source_id, curr_sample_id, survey_id)
                if sample_survey_output is not None:
                    return sample_survey_output

    return _update_state_and_route_to_sink(account_id, source_id)


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
    def get(cls, path, params=None):
        response = requests.get(
            ApiRequest.API_URL + path,
            auth=BearerAuth(session[TOKEN_KEY_NAME]),
            verify=ApiRequest.CAfile,
            params=cls.build_params(params))

        return cls._check_response(response)

    @classmethod
    def put(cls, path, params=None, json=None):
        response = requests.put(
            ApiRequest.API_URL + path,
            auth=BearerAuth(session[TOKEN_KEY_NAME]),
            verify=ApiRequest.CAfile,
            params=cls.build_params(params),
            json=json)

        return cls._check_response(response)

    @classmethod
    def post(cls, path, params=None, json=None):
        response = requests.post(
            ApiRequest.API_URL + path,
            auth=BearerAuth(session[TOKEN_KEY_NAME]),
            verify=ApiRequest.CAfile,
            params=cls.build_params(params),
            json=json)
        return cls._check_response(response)
