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
import uuid

from flask import jsonify, render_template, session, redirect
import jwt
import requests
from requests.auth import AuthBase

# Authrocket uses RS256 public keys, so you can validate anywhere and safely
# store the key in code. Obviously using this mechanism, we'd have to push code
# to roll the keys, which is not ideal, but you can instead hold this in a
# config somewhere and reload

# Python is dumb, don't put spaces anywhere in this string.
PUB_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAp68T9XnX7d53Zo8pt072
y+W0sV51EDZi7f2zeBbw5qvht9coFX4LF/p9Rcac7TajVJj+YE64vHm+YAL3ToJq
XOOF/6tmPYMbbg3DRdvUopH3URCR8o7cQXN//gDKruB9+xpB3v1Wq5SCX6t8SRFw
ixw3mKgpPoh+Ou5OohxmtJ+D7lr5R2DDW8QWAWpBdGgttdnex1OqDIsprJihx/SW
sHK4ql+H4MzX5PvY7S/XF2Ibl1xWsYLPvSzV/eJoG4hIwf7efUrXiVkwqFKNYzpL
YzmOf3F/k7TdpWqzic9y0ejMKzYu0ozGlKytxp3PbpI7B18nklVkGF07g/jNPwHN
7QIDAQAB
-----END PUBLIC KEY-----"""


# Client might not technically care who the user is, but if they do, they
# get the token, validate it, and pull email out of it.
def parse_jwt(token):
    decoded = jwt.decode(token, PUB_KEY, algorithm='RS256', verify=True)
    return decoded["name"]


def rootpath():
    return redirect("/home")


def home():
    if 'token' in session:
        user = parse_jwt(session['token'])
    else:
        user = None

    acct_id = None
    if user:
        accts = ApiRequest.get("/accounts")
        print(accts)
        if len(accts) > 0:
            acct_id = accts[0]

    # Note: home.jinja2 sends the user directly to authrocket to complete the
    # login if they aren't logged in yet.
    return render_template('home.jinja2', user=user, acct_id=uuid.uuid4())


def authrocket_callback(token):
    session['token'] = token
    return redirect("/home")


def logout():
    del session['token']
    return redirect("/home")


# States
NEEDS_ACCOUNT = 101
NEEDS_HUMAN_SOURCE = 102
NEEDS_SAMPLE = 103

def determine_workflow_state(token_info):
    current_state = {}
    # Do they need to make an account? YES-> create_acct.html
    accts = ApiRequest.get("/accounts")
    if len(accts) == 0:
        return NEEDS_ACCOUNT, current_state
    acct_id = accts[0].account_id
    current_state['account_id'] = acct_id

    # Do they have a human source? NO-> consent.html
    sources = ApiRequest.get("/accounts/%s/sources" % (acct_id,), params={
        "source_type": "human"
    })
    if len(sources) == 0:
        return NEEDS_HUMAN_SOURCE, current_state
    current_state['human_source_id'] = sources[0].id

    # Does the human source have any samples? NO-> ???.html
    # Have you taken the primary survey? NO-> main_survey.html
    # ???COVID Survey??? -> covid_survey.html
    # --> home.html
    pass


def workflow(token_info):
    next_state = determine_workflow_state(token_info)
    if next_state == CREATE_ACCOUNT:
        return redirect("/workflow_create_account")
    else:
        return redirect("/home")


def get_workflow_create_acct(token_info):
    return render_template('create_acct.html')


def post_workflow_create_acct(body, token_info):
    # session['kit_id'] = body['kit_id']
    # resp = ApiRequest.post("/accounts", params=somethingsomething(body))
    return redirect("/workflow")

def get_workflow_create_human_source(body, token_info):
    pass

def workflow_claim_samples(body, token_info):
    pass


def workflow_fill_primary_survey(body, token_info):
    # DAN
    pass


def workflow_assign_sample_metadata(body, token_info):
    # DAN
    pass


class BearerAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = "Bearer " + self.token
        return r


class ApiRequest:
    API_URL = "http://localhost:8082/api"
    DEFAULT_PARAMS = {'language_tag': 'en-US'}

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
    def get(cls, path, params=None):
        return requests.get(ApiRequest.API_URL + path,
                            auth=BearerAuth(session['token']),
                            params=cls.build_params(params)).json()

    @classmethod
    def put(cls, path, params=None):
        return requests.put(ApiRequest.API_URL + path,
                            auth=BearerAuth(session['token']),
                            params=cls.build_params(params)).json()

    @classmethod
    def post(cls, path, params=None):
        return requests.post(ApiRequest.API_URL + path,
                             auth=BearerAuth(session['token']),
                             params=cls.build_params(params)).json()
