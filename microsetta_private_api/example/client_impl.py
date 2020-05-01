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

# States
NEEDS_REROUTE = "NeedsReroute"
NEEDS_LOGIN = "NeedsLogin"
NEEDS_ACCOUNT = "NeedsAccount"
NEEDS_EMAIL_CHECK = "NeedsEmailCheck"
NEEDS_HUMAN_SOURCE = "NeedsHumanSource"
TOO_MANY_HUMAN_SOURCES = "TooManyHumanSources"
NEEDS_SAMPLE = "NeedsSample"
NEEDS_PRIMARY_SURVEY = "NeedsPrimarySurvey"
ALL_DONE = "AllDone"


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
    needs_reroute, accts_output = ApiRequest.get("/accounts")
    # if there's an error, reroute to error page
    if needs_reroute:
        current_state["reroute"] = accts_output
        return NEEDS_REROUTE, current_state

    if len(accts_output) == 0:
        # NB: Overwriting outputs from get call above
        needs_reroute, accts_output = ApiRequest.post("/accounts/legacies")
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
        needs_reroute, email_match = ApiRequest.get(
            "/accounts/%s/email_match" % acct_id)
        if needs_reroute:
            current_state["reroute"] = email_match
            return NEEDS_REROUTE, current_state
        # if they don't match AND the user hasn't already refused update
        if not email_match["email_match"]:
            return NEEDS_EMAIL_CHECK, current_state

        session[EMAIL_CHECK_KEY] = True

    # Do they have a human source? NO-> consent.html
    needs_reroute, sources_output = ApiRequest.get(
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
    needs_reroute, surveys_output = ApiRequest.get(
        "/accounts/{0}/sources/{1}/surveys".format(acct_id, source_id))
    if needs_reroute:
        current_state["reroute"] = surveys_output
        return NEEDS_REROUTE, current_state

    has_primary = False
    for survey in surveys_output:
        if survey['survey_template_id'] == 1:
            has_primary = True
            current_state["answered_primary_survey_id"] = survey["survey_id"]
    if not has_primary:
        return NEEDS_PRIMARY_SURVEY, current_state

    # ???COVID Survey??? -> covid_survey.html

    # Does the human source have any samples? NO-> kit_sample_association.html
    needs_reroute, samples_output = ApiRequest.get(
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
        return redirect("/workflow_take_primary_survey")
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

        do_return, accts_output = ApiRequest.post("/accounts", json=api_json)
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
        do_return, acct_output = ApiRequest.get('/accounts/%s' % acct_id)
        if do_return:
            return acct_output

        # change the email to the one in the authrocket account
        authrocket_email, _ = parse_jwt(session[TOKEN_KEY_NAME])
        acct_output[ACCT_EMAIL_KEY] = authrocket_email
        # retain only writeable fields; KeyError if any of them missing
        mod_acct = {k: acct_output[k] for k in ACCT_WRITEABLE_KEYS}

        # write back the updated account info
        do_return, put_output = ApiRequest.put(
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
    do_return, consent_output = ApiRequest.get(
        "/accounts/{0}/consent".format(acct_id),
        params={"consent_post_url": post_url})

    return_val = consent_output if do_return else \
        consent_output["consent_html"]

    return return_val


def post_workflow_create_human_source(body):
    next_state, current_state = determine_workflow_state()
    if next_state == NEEDS_HUMAN_SOURCE:
        acct_id = current_state["account_id"]
        do_return, consent_output = ApiRequest.post(
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

        # get all the unassociated samples in the provided kit
        kit_name = body[KIT_NAME_KEY]
        do_return, sample_output = ApiRequest.get(
            '/kits', params={KIT_NAME_KEY: kit_name})
        if do_return:
            return sample_output

        # for each sample, associate it to the human source
        # and ALSO to the (single) primary survey for this human source
        for curr_sample_obj in sample_output:
            curr_sample_id = curr_sample_obj["sample_id"]
            do_return, sample_output = ApiRequest.post(
                '/accounts/{0}/sources/{1}/samples'.format(acct_id, source_id),
                json={"sample_id": curr_sample_id}
            )

            if do_return:
                return sample_output

            do_return, sample_survey_output = ApiRequest.post(
                '/accounts/{0}/sources/{1}/samples/{2}/surveys'.format(
                    acct_id, source_id, curr_sample_id
                ), json={"survey_id": answered_survey_id}
            )

            if do_return:
                return sample_output

    return redirect(WORKFLOW_URL)


def get_workflow_fill_primary_survey():
    next_state, current_state = determine_workflow_state()
    if next_state != NEEDS_PRIMARY_SURVEY:
        return redirect(WORKFLOW_URL)

    acct_id = current_state["account_id"]
    source_id = current_state["human_source_id"]
    primary_survey = 1
    do_return, survey_output = ApiRequest.get(
        '/accounts/%s/sources/%s/survey_templates/%s' %
        (acct_id, source_id, primary_survey))
    if do_return:
        return survey_output

    return render_template("survey.jinja2",
                           survey_schema=survey_output[
                               'survey_template_text'])


def post_workflow_fill_primary_survey():
    next_state, current_state = determine_workflow_state()
    if next_state == NEEDS_PRIMARY_SURVEY:
        acct_id = current_state["account_id"]
        source_id = current_state["human_source_id"]

        model = {}
        for x in flask.request.form:
            model[x] = flask.request.form[x]

        do_return, surveys_output = ApiRequest.post(
            "/accounts/%s/sources/%s/surveys" % (acct_id, source_id),
            json={
                "survey_template_id": 1,
                "survey_text": model
            }
        )

        if do_return:
            return surveys_output

    return redirect(WORKFLOW_URL)


def get_source(account_id, source_id):
    next_state, current_state = determine_workflow_state()
    if next_state != ALL_DONE:
        return redirect(WORKFLOW_URL)

    do_return, samples_output = ApiRequest.get(
        '/accounts/%s/sources/%s/samples' % (account_id, source_id))
    if do_return:
        return samples_output

    return render_template('source.jinja2',
                           acct_id=account_id,
                           source_id=source_id,
                           samples=samples_output)


def get_sample(account_id, source_id, sample_id):
    next_state, current_state = determine_workflow_state()
    if next_state != ALL_DONE:
        return redirect(WORKFLOW_URL)

    do_return, sample_output = ApiRequest.get(
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

    do_return, sample_output = ApiRequest.put(
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

        if response.status_code == 401 or response.status_code == 403:
            # output is redirect to home page for login or email verification
            output = redirect("/home")
        elif response.status_code >= 400:
            # output is general error page
            error_txt = quote(response.text)
            mailto_url = "mailto:{0}?subject={1}&body={2}".format(
                HELP_EMAIL, quote("minimal interface error"), error_txt)

            output = render_template('error.jinja2',
                                     mailto_url=mailto_url,
                                     error_msg=response.text)
        else:
            error_code = 0  # there is a response code but no *error* code
            if response.text:
                output = response.json()

        return error_code, output

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
