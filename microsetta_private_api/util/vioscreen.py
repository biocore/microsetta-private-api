import base64
import uuid
from urllib.parse import urljoin

from Crypto.Cipher import AES
from Crypto import Random
from base64 import b64decode, b64encode

from celery import Task
from microsetta_private_api.celery_utils import celery
from werkzeug.exceptions import BadRequest
from werkzeug.urls import url_encode
import requests

from microsetta_private_api.config_manager import SERVER_CONFIG


def gen_survey_url(user_id, language_tag, survey_redirect_url):
    if not survey_redirect_url:
        raise BadRequest("Food Frequency Questionnaire Requires "
                         "survey_redirect_url")

    regcode = SERVER_CONFIG["vioscreen_regcode"]
    url = SERVER_CONFIG["vioscreen_endpoint"] + "/remotelogin.aspx?%s" % \
        url_encode(
              {
                  b"Key": encrypt_key(user_id,
                                      language_tag,
                                      survey_redirect_url),
                  b"RegCode": regcode.encode()
              }, charset='utf-16'
          )
    return url


def pkcs7_pad_message(in_message):
    # http://stackoverflow.com/questions/14179784/python-encrypting-with-pycrypto-aes  # noqa
    length = 16 - (len(in_message) % 16)
    return (in_message + chr(length) * length).encode('ascii')


def pkcs7_unpad_message(in_message):
    padding = in_message[-1]
    if padding > 16:
        # Not padded.
        return in_message
    in_message = in_message[:-padding]
    return in_message


def encrypt_key(survey_id, language_tag, survey_redirect_url):
    """Encode minimal required vioscreen information to AES key"""
    firstname = "NOT"
    lastname = "IDENTIFIED"
    gender_id = 2
    dob = '01011800'

    regcode = SERVER_CONFIG["vioscreen_regcode"]

    returnurl = survey_redirect_url
    assess_query = ("FirstName=%s&LastName=%s"
                    "&RegCode=%s"
                    "&Username=%s"
                    "&DOB=%s"
                    "&Gender=%d"
                    "&AppId=1&Visit=1&EncryptQuery=True&ReturnUrl={%s}" %
                    (firstname, lastname, regcode, survey_id, dob, gender_id,
                     returnurl))

    # PKCS7 add bytes equal length of padding
    pkcs7_query = pkcs7_pad_message(assess_query)

    # Generate AES encrypted information string
    key = SERVER_CONFIG["vioscreen_cryptokey"]
    iv = Random.new().read(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    encoded = b64encode(iv + cipher.encrypt(pkcs7_query))
    return encoded


def decode_key(encoded):
    """decode AES and remove IV and PKCS#7 padding"""
    key = SERVER_CONFIG['vioscreen_cryptokey']
    iv = Random.new().read(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return pkcs7_unpad_message(cipher.decrypt(b64decode(encoded))[16:])


# In addition to the ciphered protocol that lets users interact through their
# own browsers, vioscreen supports a server to server communications channel
# for generation and retrieval of reports.  We wrap this comms channel in
# celery for async functionality.

# Note:  We expect the VioscreenAdminAPIAgent class to be instantiated once per
# celery worker process.  That per process instance maintains its own requests
# session and acquires vioscreen admin credentials upon instantiation.

# Calls out to vioscreen are expected to be bound to the singleton instance,
# and should thus reuse connections and tokens across multiple requests.
# This class is not expected to be instantiated by the main flask application
class VioscreenAdminAPIAgent(Task):
    def __init__(self):
        print("Initializing Vioscreen Communications Task")
        self.baseurl = urljoin('https://api.viocare.com',
                               SERVER_CONFIG["vioscreen_regcode"]) + '/'
        self.user = SERVER_CONFIG["vioscreen_admin_username"]
        self.password = SERVER_CONFIG["vioscreen_admin_password"]
        self.session = requests.Session()
        self.headers = None

    def update_headers(self):
        data = {"username": self.user,
                "password": self.password}

        url = urljoin(self.baseurl, 'auth/login')
        req = self.session.post(url, data=data)
        if req.status_code != 200:
            # TODO: Check if this can send back 3XX redirects or anything
            #  else that we have to handle to get tokens robustly
            raise ValueError("Failed to obtain token")
        else:
            token = req.json()['token']
            self.headers = {'Accept': 'application/json',
                            'Authorization': 'Bearer %s' % token}

    def refresh_token(self):
        if self.headers is None:
            print("Cannot refresh, no headers set")
        refresh_url = urljoin(self.baseurl, 'auth/refreshtoken')
        req = self.session.get(refresh_url, headers=self.headers)
        if req.status_code != 200:
            print("Failed to refresh vioscreen token!  Status Code:",
                  req.status_code)
        else:
            token = req.json()['token']
            self.headers = {'Accept': 'application/json',
                            'Authorization': 'Bearer %s' % token}


# In flagrant disregard for celery's own documentation, three functions that
# declare the same task base class do not appear to share the same instance
# of that class.  So we implement our own singleton.
VIOSCREEN_API = VioscreenAdminAPIAgent()


@celery.task
def refresh_headers():
    if VIOSCREEN_API.headers is None:
        VIOSCREEN_API.update_headers()
    else:
        VIOSCREEN_API.refresh_token()


@celery.task(
    bind=True,  # This function is bound to a Task instance
    ignore_result=False,  # We need the results back
    default_retry_delay=5  # Default policy: wait 5 seconds on failure
)
def make_vioscreen_request(self, method, url, **kwargs):
    if VIOSCREEN_API.headers is None:
        VIOSCREEN_API.update_headers()

    if method == "GET":
        method = VIOSCREEN_API.session.get
    elif method == "POST":
        method = VIOSCREEN_API.session.post
    else:
        raise Exception("Unknown Method")

    url = urljoin(VIOSCREEN_API.baseurl, url)

    def handle_response(req):
        if req.status_code != 200:
            data = req.json()
            code = data.get('Code')

            if code == 1016:
                # need a new token
                return None, True
            elif code == 1002:
                # unknown user
                return {'error': 'unknown user'}, False
            elif code == 1000:
                # ffq isn't taken
                return {'error': 'ffq not taken'}, False
            else:
                # Unknown exception type, requeue the celery task (up to
                # max retries times)
                exc = ValueError(str(req.status_code) + " ::: " +
                                 str(req.content))
                raise self.retry(exc=exc)
        else:
            if 'Content-Type' in req.headers:
                ct = req.headers['Content-Type']
                cts = ct.split(';')
                cts = [s.strip() for s in cts]
                if "application/json" in cts:
                    return req.json(), False
                elif "application/pdf" in cts:
                    # Well this is maddening.  Since celery is an RPC framework
                    # you can't just send bytes back and forth, so we have to
                    # encode it as a string across the redis server to get back
                    # to flask
                    return base64.b64encode(req.content).decode("utf-8"), False
                else:
                    raise Exception("Unhandled response content type")
            else:
                raise Exception("Unknown response content type")

    req = method(url, headers=VIOSCREEN_API.headers, **kwargs)
    result, auth_failure = handle_response(req)
    if auth_failure:
        VIOSCREEN_API.update_headers()
        req = method(url, headers=VIOSCREEN_API.headers, **kwargs)
        result, auth_failure = handle_response(req)

    if auth_failure:
        # Got code 1016 (unauthenticated), then logged in, then got code 1016
        # again!
        exc = ValueError(str(req.status_code) + " ::: " + str(req.content))
        raise self.retry(exc=exc)

    return result


# This object provides a cleaner facade atop the RPC interface to celery
# and lets you do all the standard vioscreen api operations we support
class VioscreenAdminAPI:
    def get(self, url, **kwargs):
        return make_vioscreen_request.delay(
            "GET",
            url,
            **kwargs)

    def post(self, url, **kwargs):
        return make_vioscreen_request.delay(
            "POST",
            url,
            **kwargs)

    def _get_session_data(self, id_, name):
        url = 'sessions/%s/%s' % (id_, name)
        result = self.get(url)
        if 'error' in result:
            return {}
        else:
            return result

    def foodcomponents(self, id_):
        return self._get_session_data(id_, 'foodcomponents').get('data')

    def percentenergy(self, id_):
        return self._get_session_data(id_, 'percentenergy').get('calculations')

    def mpeds(self, id_):
        return self._get_session_data(id_, 'mpeds').get('data')

    def eatingpatterns(self, id_):
        return self._get_session_data(id_, 'eatingpatterns').get('data')

    def foodconsumption(self, id_):
        return self._get_session_data(id_, 'foodconsumption')\
            .get('foodConsumption')

    def dietaryscore(self, id_):
        return self._get_session_data(id_, 'dietaryscore').get('dietaryScore')

    def users(self):
        return self.get('users')['users']

    def sessions(self, vioscreen_user):
        detail = self.get('users/%s/sessions' % vioscreen_user)

        # TODO: Can we push waiting for the async result out to flask to
        #  free up the flask worker for more requests?
        detail = detail.get()  # Wait for async result

        if 'error' in detail:
            return []
        else:
            return detail['sessions']

    def session_detail(self, session_id):
        return self.get('sessions/%s/detail' % session_id)

    def get_ffq(self, session_id):
        errors = []
        name_func = [('foodcomponents', self.foodcomponents),
                     ('percentenergy', self.percentenergy),
                     ('mpeds', self.mpeds),
                     ('eatingpatterns', self.eatingpatterns),
                     ('foodconsumption', self.foodconsumption),
                     ('dietaryscore', self.dietaryscore)]
        results = {}
        for name, f in name_func:
            data = f(session_id)
            if data is None:
                errors.append("FFQ appears incomplete or not taken")
                break

            results[name] = data

        return errors, results

    def top_food_report(self, session_id):
        async_result = self.post(
            "report/topfoodreport",
            data={
                "requestId": str(uuid.uuid4()),
                "sessionId": session_id,
                "companyName": "The Microsetta Initiative",
                "providerName": "The Microsetta Initiative"
            })

        # TODO: Celery becomes a lot harder to use when you need to wait for
        #  answers and encode/decode things.  Blah.
        return base64.b64decode(async_result.get().encode("utf-8"))
