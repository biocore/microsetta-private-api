"""
Functions to implement OpenAPI 3.0 interface to access private PHI.

Underlies the resource server in the oauth2 workflow. "Resource Server: The
server hosting user-owned resources that are protected by OAuth2. The resource
server validates the access-token and serves the protected resources."
--https://dzone.com/articles/oauth-20-beginners-guide

Loosely based off examples in
https://realpython.com/flask-connexion-rest-api/#building-out-the-complete-api
and associated file
https://github.com/realpython/materials/blob/master/flask-connexion-rest/version_3/people.py  # noqa: E501
"""

import json
import flask
from flask import render_template, session, redirect
import jwt
import requests
from requests.auth import AuthBase
from urllib.parse import quote

# Authrocket uses RS256 public keys, so you can validate anywhere and safely
# store the key in code. Obviously using this mechanism, we'd have to push code
# to roll the keys, which is not ideal, but you can instead hold this in a
# config somewhere and reload

# Python is dumb, don't put spaces anywhere in this string.
from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.model.vue.vue_factory import VueFactory
from microsetta_private_api.model.vue.vue_field import VueInputField, \
    VueTextAreaField, VueSelectField, VueDateTimePickerField
import importlib.resources as pkg_resources


PUB_KEY = pkg_resources.read_text(
    'microsetta_private_api',
    "authrocket.pubkey")

TOKEN_KEY_NAME = 'token'
WORKFLOW_URL = '/workflow'
HELP_EMAIL = "microsetta@ucsd.edu"
KIT_NAME_KEY = "kit_name"
EMAIL_CHECK_KEY = "email_checked"

ACCT_FNAME_KEY = "first_name"
ACCT_LNAME_KEY = "last_name"
ACCT_EMAIL_KEY = "email"
ACCT_ADDR_KEY = "address"
ACCT_WRITEABLE_KEYS = [ACCT_FNAME_KEY, ACCT_LNAME_KEY, ACCT_EMAIL_KEY,
                       ACCT_ADDR_KEY]

_NEEDS_SURVEY_PREFIX = "NeedsSurvey"

# States
NEEDS_REROUTE = "NeedsReroute"
NEEDS_LOGIN = "NeedsLogin"
NEEDS_ACCOUNT = "NeedsAccount"
NEEDS_EMAIL_CHECK = "NeedsEmailCheck"
NEEDS_HUMAN_SOURCE = "NeedsHumanSource"
TOO_MANY_HUMAN_SOURCES = "TooManyHumanSources"
NEEDS_SAMPLE = "NeedsSample"
NEEDS_PRIMARY_SURVEY = _NEEDS_SURVEY_PREFIX + "1"
NEEDS_COVID_SURVEY = _NEEDS_SURVEY_PREFIX + "6"
ALL_DONE = "AllDone"

# TODO FIXME HACK:  VIOSCREEN_ID is just hardcoded.  Api does not specify what
#  special handling is required.  API must specify per-sample survey templates
#  in some way, as well as any special handling for external surveys.
VIOSCREEN_ID = 10001


# Client might not technically care who the user is, but if they do, they
# get the token, validate it, and pull email out of it.
def parse_jwt(token):
    decoded = jwt.decode(token, PUB_KEY, algorithms=['RS256'], verify=True)
    email_verified = decoded.get('email_verified', False)
    return decoded["email"], email_verified


def rootpath():
    return redirect("/home")


def home():
    user = None
    email_verified = False
    acct_id = None
    has_multiple_hs_sources = False

    if TOKEN_KEY_NAME in session:
        try:
            # If user leaves the page open, the token can expire before the
            # session, so if our token goes back we need to force them to login
            # again.
            user, email_verified = parse_jwt(session[TOKEN_KEY_NAME])
        except jwt.exceptions.ExpiredSignatureError:
            return redirect('/logout')

        if email_verified:
            workflow_needs, workflow_state = determine_workflow_state()
            if workflow_needs == NEEDS_REROUTE:
                return workflow_state["reroute"]

            acct_id = workflow_state.get("account_id", None)
            has_multiple_hs_sources = workflow_needs == TOO_MANY_HUMAN_SOURCES

    # Note: home.jinja2 sends the user directly to authrocket to complete the
    # login if they aren't logged in yet.
    return render_template('home.jinja2',
                           user=user,
                           email_verified=email_verified,
                           acct_id=acct_id,
                           has_multiple_hs_sources=has_multiple_hs_sources,
                           endpoint=SERVER_CONFIG["endpoint"],
                           authrocket_url=SERVER_CONFIG["authrocket_url"])


def authrocket_callback(token):
    session[TOKEN_KEY_NAME] = token
    return redirect("/home")


def logout():
    if TOKEN_KEY_NAME in session:
        # delete these keys if they are here, otherwise ignore
        session.pop(TOKEN_KEY_NAME, None)
        session.pop(KIT_NAME_KEY, None)
        session.pop(EMAIL_CHECK_KEY, None)
    return redirect("/home")


def determine_workflow_state():
    current_state = {}
    if TOKEN_KEY_NAME not in session:
        return NEEDS_LOGIN, current_state

    # Do they need to make an account? YES-> create_acct.html
    needs_reroute, accts_output, _ = ApiRequest.get("/accounts")
    # if there's an error, reroute to error page
    if needs_reroute:
        current_state["reroute"] = accts_output
        return NEEDS_REROUTE, current_state

    if len(accts_output) == 0:
        # NB: Overwriting outputs from get call above
        needs_reroute, accts_output, _ = ApiRequest.post("/accounts/legacies")
        if needs_reroute:
            current_state["reroute"] = accts_output
            return NEEDS_REROUTE, current_state
        # if no legacy account found, need new account
        if len(accts_output) == 0:
            return NEEDS_ACCOUNT, current_state

    acct_id = accts_output[0]["account_id"]
    current_state['account_id'] = acct_id

    # If we haven't yet checked for email mismatches and gotten user decision:
    if not session.get(EMAIL_CHECK_KEY, False):
        # Does email in our accounts table match email in authrocket?
        needs_reroute, email_match, _ = ApiRequest.get(
            "/accounts/%s/email_match" % acct_id)
        if needs_reroute:
            current_state["reroute"] = email_match
            return NEEDS_REROUTE, current_state
        # if they don't match AND the user hasn't already refused update
        if not email_match["email_match"]:
            return NEEDS_EMAIL_CHECK, current_state

        session[EMAIL_CHECK_KEY] = True

    # Do they have a human source? NO-> consent.html
    needs_reroute, sources_output, _ = ApiRequest.get(
        "/accounts/%s/sources" % (acct_id,), params={"source_type": "human"})
    if needs_reroute:
        current_state["reroute"] = sources_output
        return NEEDS_REROUTE, current_state
    if len(sources_output) == 0:
        return NEEDS_HUMAN_SOURCE, current_state
    elif len(sources_output) > 1:
        # we do not currently support displaying multiple human sources
        return TOO_MANY_HUMAN_SOURCES, current_state

    source_id = sources_output[0]["source_id"]
    current_state['human_source_id'] = source_id

    # Have you taken the primary survey? NO-> main_survey.html
    needs_reroute, surveys_output, _ = ApiRequest.get(
        "/accounts/{0}/sources/{1}/surveys".format(acct_id, source_id))
    if needs_reroute:
        current_state["reroute"] = surveys_output
        return NEEDS_REROUTE, current_state

    has_primary = False
    has_covid = False
    for survey in surveys_output:
        if survey['survey_template_id'] == 1:
            has_primary = True
            current_state["answered_primary_survey_id"] = survey["survey_id"]
        elif survey['survey_template_id'] == 6:
            has_covid = True
            current_state["answered_covid_survey_id"] = survey["survey_id"]

    if not has_primary:
        return NEEDS_PRIMARY_SURVEY, current_state

    if not has_covid:
        return NEEDS_COVID_SURVEY, current_state

    # Does the human source have any samples? NO-> kit_sample_association.html
    needs_reroute, samples_output, _ = ApiRequest.get(
        "/accounts/{0}/sources/{1}/samples".format(acct_id, source_id))
    if needs_reroute:
        current_state["reroute"] = surveys_output
        return NEEDS_REROUTE, current_state
    if len(samples_output) == 0:
        return NEEDS_SAMPLE, current_state

    current_state['sample_objs'] = samples_output

    return ALL_DONE, current_state


def workflow():
    next_state, current_state = determine_workflow_state()
    print("Next State:", next_state)
    if next_state == NEEDS_REROUTE:
        # where you get rerouted to depends on why you need
        # rerouting: api authorization errors go back to home page,
        # all other api errors go to error page
        return current_state["reroute"]
    elif next_state == NEEDS_LOGIN:
        return redirect("/home")
    elif next_state == NEEDS_ACCOUNT:
        return redirect("/workflow_create_account")
    elif next_state == NEEDS_EMAIL_CHECK:
        return redirect("/workflow_update_email")
    elif next_state == NEEDS_HUMAN_SOURCE:
        return redirect("/workflow_create_human_source")
    elif next_state == NEEDS_PRIMARY_SURVEY:
        return redirect("/workflow_take_survey?survey_template_id=" +
                        NEEDS_PRIMARY_SURVEY.replace(_NEEDS_SURVEY_PREFIX, ""))
    elif next_state == NEEDS_COVID_SURVEY:
        return redirect("/workflow_take_survey?survey_template_id=" +
                        NEEDS_COVID_SURVEY.replace(_NEEDS_SURVEY_PREFIX, ""))
    elif next_state == NEEDS_SAMPLE:
        return redirect("/workflow_claim_kit_samples")
    elif next_state == ALL_DONE:
        # redirect to the page showing all the samples for this source
        samples_url = "/accounts/{account_id}/sources/{source_id}".format(
            account_id=current_state["account_id"],
            source_id=current_state["human_source_id"])
        return redirect(samples_url)


def get_workflow_create_account():
    next_state, current_state = determine_workflow_state()
    if next_state != NEEDS_ACCOUNT:
        return redirect(WORKFLOW_URL)

    email, _ = parse_jwt(session[TOKEN_KEY_NAME])
    return render_template('create_acct.jinja2',
                           authorized_email=email)


def post_workflow_create_account(body):
    next_state, current_state = determine_workflow_state()
    if next_state == NEEDS_ACCOUNT:
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

        do_return, accts_output, _ = \
            ApiRequest.post("/accounts", json=api_json)
        if do_return:
            return accts_output

    return redirect(WORKFLOW_URL)


def get_workflow_update_email():
    next_state, current_state = determine_workflow_state()
    if next_state != NEEDS_EMAIL_CHECK:
        return redirect(WORKFLOW_URL)

    return render_template("update_email.jinja2")


def post_workflow_update_email(body):
    next_state, current_state = determine_workflow_state()
    if next_state != NEEDS_EMAIL_CHECK:
        return redirect(WORKFLOW_URL)

    # if the customer wants to update their email:
    update_email = body["do_update"] == "Yes"
    if update_email:
        # get the existing account object
        acct_id = current_state["account_id"]
        do_return, acct_output, _ = ApiRequest.get('/accounts/%s' % acct_id)
        if do_return:
            return acct_output

        # change the email to the one in the authrocket account
        authrocket_email, _ = parse_jwt(session[TOKEN_KEY_NAME])
        acct_output[ACCT_EMAIL_KEY] = authrocket_email
        # retain only writeable fields; KeyError if any of them missing
        mod_acct = {k: acct_output[k] for k in ACCT_WRITEABLE_KEYS}

        # write back the updated account info
        do_return, put_output, _ = ApiRequest.put(
            '/accounts/%s' % acct_id, json=mod_acct)
        if do_return:
            return put_output

    # even if they decided NOT to update, don't ask again this session
    session[EMAIL_CHECK_KEY] = True
    return redirect(WORKFLOW_URL)


def get_workflow_create_human_source():
    next_state, current_state = determine_workflow_state()
    if next_state != NEEDS_HUMAN_SOURCE:
        return redirect(WORKFLOW_URL)

    acct_id = current_state["account_id"]
    endpoint = SERVER_CONFIG["endpoint"]
    post_url = endpoint + "/workflow_create_human_source"
    do_return, consent_output, _ = ApiRequest.get(
        "/accounts/{0}/consent".format(acct_id),
        params={"consent_post_url": post_url})

    return_val = consent_output if do_return else \
        consent_output["consent_html"]

    return return_val


def post_workflow_create_human_source(body):
    next_state, current_state = determine_workflow_state()
    if next_state == NEEDS_HUMAN_SOURCE:
        acct_id = current_state["account_id"]
        do_return, consent_output, _ = ApiRequest.post(
            "/accounts/{0}/consent".format(acct_id), json=body)

        if do_return:
            return consent_output

    return redirect(WORKFLOW_URL)


def get_workflow_claim_kit_samples():
    next_state, current_state = determine_workflow_state()
    if next_state != NEEDS_SAMPLE:
        return redirect(WORKFLOW_URL)

    if KIT_NAME_KEY in session:
        mock_body = {KIT_NAME_KEY: session[KIT_NAME_KEY]}
        return post_workflow_claim_kit_samples(mock_body)
    else:
        return render_template("kit_sample_association.jinja2")


def post_workflow_claim_kit_samples(body):
    next_state, current_state = determine_workflow_state()
    if next_state == NEEDS_SAMPLE:
        acct_id = current_state["account_id"]
        source_id = current_state["human_source_id"]
        answered_survey_id = current_state["answered_primary_survey_id"]
        answered_covid_survey_id = current_state["answered_covid_survey_id"]

        # get all the unassociated samples in the provided kit
        kit_name = body[KIT_NAME_KEY]
        do_return, sample_output, _ = ApiRequest.get(
            '/kits', params={KIT_NAME_KEY: kit_name})
        if do_return:
            return sample_output

        # for each sample, associate it to the human source
        # and ALSO to the (single) primary and COVID survey for this human
        # source
        for curr_sample_obj in sample_output:
            curr_sample_id = curr_sample_obj["sample_id"]
            do_return, sample_output, _ = ApiRequest.post(
                '/accounts/{0}/sources/{1}/samples'.format(acct_id, source_id),
                json={"sample_id": curr_sample_id}
            )

            if do_return:
                return sample_output

            do_return, sample_survey_output, _ = ApiRequest.post(
                '/accounts/{0}/sources/{1}/samples/{2}/surveys'.format(
                    acct_id, source_id, curr_sample_id
                ), json={"survey_id": answered_survey_id}
            )

            if do_return:
                return sample_output

            do_return, sample_survey_output, _ = ApiRequest.post(
                '/accounts/{0}/sources/{1}/samples/{2}/surveys'.format(
                    acct_id, source_id, curr_sample_id
                ), json={"survey_id": answered_covid_survey_id}
            )

            if do_return:
                return sample_output

    return redirect(WORKFLOW_URL)


def get_workflow_fill_survey(survey_template_id):
    next_state, current_state = determine_workflow_state()
    if next_state != _NEEDS_SURVEY_PREFIX + str(survey_template_id):
        return redirect(WORKFLOW_URL)

    acct_id = current_state["account_id"]
    source_id = current_state["human_source_id"]
    do_return, survey_output, _ = ApiRequest.get(
        '/accounts/%s/sources/%s/survey_templates/%s' %
        (acct_id, source_id, survey_template_id))
    if do_return:
        return survey_output

    return render_template("survey.jinja2",
                           endpoint=SERVER_CONFIG["endpoint"],
                           survey_template_id=survey_template_id,
                           survey_schema=survey_output[
                               'survey_template_text'])


def post_workflow_fill_survey(survey_template_id, body):
    next_state, current_state = determine_workflow_state()
    if next_state == _NEEDS_SURVEY_PREFIX + str(survey_template_id):
        acct_id = current_state["account_id"]
        source_id = current_state["human_source_id"]

        do_return, surveys_output, _ = ApiRequest.post(
            "/accounts/%s/sources/%s/surveys" % (acct_id, source_id),
            json={
                "survey_template_id": survey_template_id,
                "survey_text": body
            }
        )

        if do_return:
            return surveys_output

    return redirect(WORKFLOW_URL)


def get_account(account_id):
    if TOKEN_KEY_NAME not in session:
        return redirect(WORKFLOW_URL)

    do_return, sources, _ = ApiRequest.get('/accounts/%s/sources' % account_id)
    if do_return:
        return sources
    return render_template('account.jinja2',
                           acct_id=account_id,
                           sources=sources)


def get_source(account_id, source_id):
    next_state, current_state = determine_workflow_state()
    if next_state != ALL_DONE:
        return redirect(WORKFLOW_URL)

    # Retrieve all samples from the source
    do_return, samples_output, _ = ApiRequest.get(
        '/accounts/%s/sources/%s/samples' % (account_id, source_id))
    if do_return:
        return samples_output

    # Retrieve all surveys available to the source
    do_return, surveys_output, _ = ApiRequest.get(
        '/accounts/%s/sources/%s/survey_templates' % (account_id, source_id))
    if do_return:
        return surveys_output

    # Limit to only the primary and COVID19 survey as that is the primary
    # data focus for TMI right now.
    per_sample = []
    per_source = []
    restrict_to = [1, 6]
    for survey in surveys_output:
        if survey['survey_template_id'] in restrict_to:
            per_source.append(survey)
        if survey['survey_template_id'] == VIOSCREEN_ID:
            per_sample.append(survey)

    # Identify answered surveys for the source
    do_return, survey_answers, _ = ApiRequest.get(
        '/accounts/%s/sources/%s/surveys' % (account_id, source_id))
    if do_return:
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
        do_return, per_sample_answers, _ = ApiRequest.get(
            '/accounts/%s/sources/%s/samples/%s/surveys' %
            (account_id, source_id, sample_id))

        if do_return:
            return per_sample_answers

        for answer in per_sample_answers:
            if answer['survey_template_id'] == VIOSCREEN_ID:
                sample['ffq'] = True

    return render_template('source.jinja2',
                           acct_id=account_id,
                           source_id=source_id,
                           samples=samples_output,
                           surveys=per_source,
                           vioscreen_id=VIOSCREEN_ID)


def show_source_survey(account_id, source_id, survey_template_id):
    return show_sample_survey(account_id, source_id, None, survey_template_id)


def show_sample_survey(account_id, source_id, sample_id, survey_template_id):
    params = {}
    if survey_template_id == VIOSCREEN_ID:
        params['survey_redirect_url'] = \
            SERVER_CONFIG["endpoint"] + \
            '/accounts/%s/sources/%s/samples/%s/vspassthru' \
            % (account_id, source_id, sample_id)

    do_return, survey_output, _ = ApiRequest.get(
        '/accounts/%s/sources/%s/survey_templates/%s' %
        (account_id, source_id, survey_template_id), params=params)
    if do_return:
        return survey_output

    # Handle remote surveys
    if survey_output['survey_template_type'] == 'remote':
        return redirect(survey_output['survey_template_text']['url'])

    # Handle local surveys
    return render_template("survey.jinja2",
                           survey_template_id=survey_template_id,
                           survey_schema=survey_output[
                               'survey_template_text'])


def finish_vioscreen(account_id, source_id, sample_id, key):
    # TODO FIXME HACK:  This is insanity.  I need to see the vioscreen docs
    #  to interface with our API...
    do_return, surveys_output, surveys_headers = ApiRequest.post(
        "/accounts/%s/sources/%s/surveys" % (account_id, source_id),
        json={
            "survey_template_id": VIOSCREEN_ID,
            "survey_text": {"key": key}
        }
    )

    if do_return:
        return surveys_output

    answered_survey_id = surveys_headers['Location']
    answered_survey_id = answered_survey_id.split('/')[-1]

    do_return, sample_survey_output, _ = ApiRequest.post(
        '/accounts/%s/sources/%s/samples/%s/surveys' %
        (account_id, source_id, sample_id),
        json={"survey_id": answered_survey_id}
    )

    if do_return:
        return sample_survey_output

    return redirect("/accounts/%s/sources/%s" % (account_id, source_id))


def finish_survey(account_id, source_id, survey_template_id):
    model = {}
    for x in flask.request.form:
        model[x] = flask.request.form[x]

    do_return, surveys_output, _ = ApiRequest.post(
        "/accounts/%s/sources/%s/surveys" % (account_id, source_id),
        json={
            "survey_template_id": survey_template_id,
            "survey_text": model
        }
    )

    if do_return:
        return surveys_output

    return redirect("/accounts/%s/sources/%s" % (account_id, source_id))


def get_sample(account_id, source_id, sample_id):
    next_state, current_state = determine_workflow_state()
    if next_state != ALL_DONE:
        return redirect(WORKFLOW_URL)

    do_return, sample_output, _ = ApiRequest.get(
        '/accounts/%s/sources/%s/samples/%s' %
        (account_id, source_id, sample_id))
    if do_return:
        return sample_output

    sample_sites = ["Blood (skin prick)", "Stool", "Mouth", "Nares",
                    "Nasal mucus", "Right hand", "Left hand",
                    "Forehead", "Torso", "Right leg",  "Left leg",
                    "Vaginal mucus", "Tears",  "Ear wax", "Hair", "Fur"]

    factory = VueFactory()

    schema = factory.start_group("Edit Sample Information")\
        .add_field(VueInputField("sample_barcode", "Barcode")
                   .set(disabled=True))\
        .add_field(VueDateTimePickerField("sample_datetime", "Date and Time")
                   .set(required=True,
                        validator="string"))\
        .add_field(VueSelectField("sample_site", "Site", sample_sites)
                   .set(required=True,
                        validator="string")) \
        .add_field(VueTextAreaField("sample_notes", "Notes")) \
        .end_group()\
        .build()

    return render_template('sample.jinja2',
                           acct_id=account_id,
                           source_id=source_id,
                           sample=sample_output,
                           schema=schema)


def put_sample(account_id, source_id, sample_id):
    next_state, current_state = determine_workflow_state()
    if next_state != ALL_DONE:
        return redirect(WORKFLOW_URL)

    model = {}
    for x in flask.request.form:
        model[x] = flask.request.form[x]

    do_return, sample_output, _ = ApiRequest.put(
        '/accounts/%s/sources/%s/samples/%s' %
        (account_id, source_id, sample_id),
        json=model)

    if do_return:
        return sample_output

    return redirect('/accounts/%s/sources/%s' %
                    (account_id, source_id))


def post_check_acct_inputs(body):
    unable_to_validate_msg = "Unable to validate the kit name; please " \
                             "reload the page."
    response_info = True
    try:
        kit_name = body[KIT_NAME_KEY]

        # call api and find out if kit name has unclaimed samples.
        # NOT doing this through ApiRequest.get bc in this case
        # DON'T want the automated error-handling

        response = requests.get(
            ApiRequest.API_URL + '/kits',
            auth=BearerAuth(session[TOKEN_KEY_NAME]),
            verify=ApiRequest.CAfile,
            params=ApiRequest.build_params({KIT_NAME_KEY: kit_name}))

        if response.status_code == 404:
            response_info = ("The provided kit id is not valid or has "
                             "already been used; please re-check your entry.")
        elif response.status_code > 200:
            response_info = unable_to_validate_msg
    except:  # noqa
        response_info = unable_to_validate_msg
    finally:
        return json.dumps(response_info)


def generate_error_page(error_msg):
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


def render_faq():
    output = render_template('faq.jinja2',
                             page_title="Frequently Asked Questions",
                             show_breadcrumbs=True,
                             show_logout=False,
                             authrocket_url=SERVER_CONFIG["authrocket_url"],
                             endpoint=SERVER_CONFIG["endpoint"])
    return output



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
            output = redirect("/home")
        elif response.status_code >= 400:
            # output is general error page
            output = generate_error_page(response.text)
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
