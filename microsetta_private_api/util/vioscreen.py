import base64
import uuid
from urllib.parse import urljoin

from Crypto.Cipher import AES
from Crypto import Random
from base64 import b64decode, b64encode

from celery import Task, current_task
from microsetta_private_api.tasks import send_email
from microsetta_private_api.celery_utils import celery
from werkzeug.exceptions import BadRequest
from werkzeug.urls import url_encode
import requests

from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.vioscreen_repo import (VioscreenSessionRepo,
                                                        VioscreenRepo)
from microsetta_private_api.model.vioscreen import (VioscreenSession,
                                                    VioscreenPercentEnergy,
                                                    VioscreenDietaryScore,
                                                    VioscreenSupplements,
                                                    VioscreenFoodComponents,
                                                    VioscreenEatingPatterns,
                                                    VioscreenMPeds,
                                                    VioscreenFoodConsumption,
                                                    VioscreenComposite)
from microsetta_private_api.localization import ES_MX, EN_US

# TODO: much of the logic in this module should be migrated and placed
# under microsetta_private_api.client.vioscreen

# the country code determines which FFQ is taken. Vioscreen determines
# the FFQ based on the registration code. The US survey is only the
# regcode, so we do not need to append anything
COUNTRY_CODE_TO_FFQ = {
    'US': '',
    'MX': 'mexico',
}


def gen_survey_url(user_id,
                   language_tag,
                   survey_redirect_url,
                   birth_year=None,
                   gender=None,
                   height=None,
                   weight=None,
                   country_code=None
                   ):
    if not survey_redirect_url:
        raise BadRequest("Food Frequency Questionnaire Requires "
                         "survey_redirect_url")

    regcode = SERVER_CONFIG["vioscreen_regcode"]

    gender_map = {'Male': 1, 'Female': 2}
    gender_id = gender_map.get(gender, 2)  # default to female

    if birth_year is not None:
        dob = '0630{}'.format(birth_year)
    else:
        dob = '01011970'  # default to unix epoch

    # per clarification with Vioscreen, they interpret es_MX as es_ES
    if language_tag == ES_MX:
        language_tag = 'es-ES'

    # vioscreen only accepts "-" variants, whereas we use "_" internally
    # so replace just in case.
    language_tag = language_tag.replace('_', '-')

    # We'll default to the US version if there isn't a country specific one
    # available.
    ffq = COUNTRY_CODE_TO_FFQ.get(country_code, 'US')
    if ffq == '':
        ffq = f"{regcode}"
    else:
        ffq = f"{regcode}-{ffq}"

    url = SERVER_CONFIG["vioscreen_endpoint"] +\
        "/remotelogin.aspx?%s" % url_encode(
        {
            b"Key": encrypt_key(user_id,
                                language_tag,
                                survey_redirect_url,
                                gender_id,
                                dob,
                                height,
                                weight,
                                regcode),
            b"RegCode": ffq.encode(),
        }, charset='utf-16',
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


def encrypt_key(survey_id,
                language_tag,
                survey_redirect_url,
                gender_id,
                dob,
                height,
                weight,
                regcode,
                _testing_arguments=None
                ):
    """Encode minimal required vioscreen information to AES key"""
    firstname = "NOT"
    lastname = "IDENTIFIED"

    returnurl = survey_redirect_url
    parts = ["FirstName=%s" % firstname,
             "LastName=%s" % lastname,
             "RegCode=%s" % regcode,
             "Username=%s" % survey_id,
             "DOB=%s" % dob,
             "Gender=%d" % gender_id,
             "CultureCode=%s" % language_tag,
             "AppId=1",
             "Visit=1",
             "EncryptQuery=True",
             "ReturnUrl={%s}" % returnurl]

    if _testing_arguments is not None:
        parts.extend(_testing_arguments)

    if height is not None and weight is not None:
        parts.append("Height=%s" % height)
        parts.append("Weight=%s" % weight)

    # PKCS7 add bytes equal length of padding
    assess_query = "&".join(parts)
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
            elif code == 1017:
                # From David Blankenbush on 6.24.21, this is an edge case that
                # should not occur in production
                return {'error': 'empty ffq'}, False
            elif code == 1005:
                # From David Blankenbush on 5.26.21, we should issue a retry
                # if this code is observed
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
        # Implies something weird occured
        exc = ValueError(str(req.status_code) + " ::: " + str(req.content))
        raise self.retry(exc=exc)

    return result


# This object provides a cleaner facade atop the RPC interface to celery
# and lets you do all the standard vioscreen api operations we support
class VioscreenAdminAPI:
    def __init__(self, perform_async=True):
        self.perform_async = perform_async

    def get(self, url, **kwargs):
        if self.perform_async:
            return make_vioscreen_request.delay(
                "GET",
                url,
                **kwargs)
        else:
            return make_vioscreen_request(
                "GET",
                url,
                **kwargs)

    def post(self, url, **kwargs):
        if self.perform_async:
            return make_vioscreen_request.delay(
                "POST",
                url,
                **kwargs)
        else:
            return make_vioscreen_request(
                "POST",
                url,
                **kwargs)

    def _get_session_data(self, id_, name, **kwargs):
        url = 'sessions/%s/%s' % (id_, name)
        result = self.get(url, **kwargs)
        if 'error' in result:
            return {}
        else:
            return result

    def foodcomponents(self, id_):
        data = self._get_session_data(id_, 'foodcomponents')
        return VioscreenFoodComponents.from_vioscreen(data)

    def percentenergy(self, id_):
        data = self._get_session_data(id_, 'percentenergy')
        return VioscreenPercentEnergy.from_vioscreen(data)

    def mpeds(self, id_):
        data = self._get_session_data(id_, 'mpeds')
        return VioscreenMPeds.from_vioscreen(data)

    def eatingpatterns(self, id_):
        data = self._get_session_data(id_, 'eatingpatterns')
        return VioscreenEatingPatterns.from_vioscreen(data)

    def foodconsumption(self, id_):
        data = self._get_session_data(id_, 'foodconsumption')
        return VioscreenFoodConsumption.from_vioscreen(data)

    def dietaryscore(self, id_):
        scores = []
        for scoretype in ['Hei2010', 'Hei2015']:
            params = {'dietaryScoreType': scoretype, 'foodDatabaseId': '13'}
            req = self._get_session_data(id_, 'dietaryscore', params=params)
            scores.append(VioscreenDietaryScore.from_vioscreen(req))
        return scores

    def supplements(self, id_):
        data = self._get_session_data(id_, 'supplements')
        return VioscreenSupplements.from_vioscreen(data)

    def users(self):
        return self.get('users')['users']

    def user(self, username):
        return self.get(f'users/{username}')

    def sessions(self, vioscreen_user):
        detail = self.get('users/%s/sessions' % vioscreen_user)
        # TODO: Can we push waiting for the async result out to flask to
        #  free up the flask worker for more requests?
        if self.perform_async:
            detail = detail.get()  # Wait for async result

        if 'error' in detail:
            return []
        else:
            return detail['sessions']

    def session_detail(self, session_id):
        sess_data = self.get('sessions/%s/detail' % session_id)
        user_data = self.user(sess_data['username'])
        return VioscreenSession.from_vioscreen(sess_data, user_data)

    def get_ffq(self, session_id):
        errors = []
        name_func_key = [('foodcomponents',
                          self.foodcomponents,
                          'food_components'),
                         ('percentenergy',
                          self.percentenergy,
                          'percent_energy'),
                         ('mpeds',
                          self.mpeds,
                          'mpeds'),
                         ('eatingpatterns',
                          self.eatingpatterns,
                          'eating_patterns'),
                         ('foodconsumption',
                          self.foodconsumption,
                          'food_consumption'),
                         ('dietaryscore',
                          self.dietaryscore,
                          'dietary_scores'),
                         ('supplements',
                          self.supplements,
                          'supplements')]
        results = {'session': self.session_detail(session_id)}
        for name, f, key in name_func_key:
            try:
                data = f(session_id)
            except:  # noqa
                errors.append("FFQ appears incomplete or not taken")
                break

            results[key] = data

        if errors:
            return errors, None
        else:
            return errors, VioscreenComposite(**results)

    def top_food_report(self, session_id):
        result = self.post(
            "report/topfoodreport",
            data={
                "requestId": str(uuid.uuid4()),
                "sessionId": session_id,
                "companyName": "The Microsetta Initiative",
                "providerName": "The Microsetta Initiative"
            })

        # TODO: Celery becomes a lot harder to use when you need to wait for
        #  answers and encode/decode things.  Blah.
        if self.perform_async:
            result = result.get()

        if isinstance(result, dict):
            # the times we've observed this scenario, the content is
            # {'error': 'empty ffq'}
            return None

        return base64.b64decode(result.encode('utf-8'))


@celery.task(ignore_result=False)
def update_session_detail():
    # The interaction with the API is occuring within a celery task
    # and the recommendation from celery is to avoid depending on synchronous
    # tasks from within a task. As such, we'll use non-async calls here. See
    # http://docs.celeryq.org/en/latest/userguide/tasks.html#task-synchronous-subtasks

    # HOWEVER, we could implement a watch and monitor child tasks, but
    # not sure if that would be a particular benefit here
    vio_api = VioscreenAdminAPI(perform_async=False)
    current_task.update_state(
        state="PROGRESS",
        meta={"completion": 0,
              "status": "PROGRESS",
              "message": "Gathering unfinished sessions..."})

    # obtain our current unfinished sessions to check
    with Transaction() as t:
        r = VioscreenSessionRepo(t)
        unfinished_sessions = r.get_unfinished_sessions()

    failed_sessions = []
    n_to_get = len(unfinished_sessions)
    n_updated = 0
    for idx, sess in enumerate(unfinished_sessions, 1):
        updated = []

        # Out of caution, we'll wrap the external resource interaction within
        # a blanket try/except
        try:
            if sess.sessionId is None:
                # a session requires a mix of information from Vioscreen's
                # representation of a user and a session
                user_detail = vio_api.user(sess.username)
                details = vio_api.sessions(sess.username)

                # account for the possibility of a user having multiple
                # sessions
                updated.extend([VioscreenSession.from_vioscreen(detail,
                                                                user_detail)
                                for detail in details])
            else:
                # update our model inplace
                update = vio_api.session_detail(sess.sessionId)
                if update.status != sess.status:
                    updated.append(sess.update_from_vioscreen(update))
        except Exception as e:  # noqa
            failed_sessions.append((sess.sessionId, str(e)))
            continue

        # commit as we go along to avoid holding any individual transaction
        # open for a long period
        if len(updated) > 0:
            with Transaction() as t:
                r = VioscreenSessionRepo(t)

                for update in updated:
                    r.upsert_session(update)
                t.commit()
                n_updated += len(updated)

        current_task.update_state(
            state="PROGRESS",
            meta={"completion": (idx / n_to_get) * 100,
                  "status": "PROGRESS",
                  "message": "Gathering session data..."})

    current_task.update_state(
        state="SUCCESS",
        meta={"completion": n_to_get,
              "status": "SUCCESS",
              "message": f"{n_updated} sessions updated"})

    if len(failed_sessions) > 0:
        # ...and let's make Daniel feel bad about not having a better means to
        # log what hopefully never occurs
        payload = ''.join(['%s : %s\n' % (repr(s), m)
                           for s, m in failed_sessions])
        send_email(SERVER_CONFIG['pester_email'], "pester_daniel",
                   {"what": "Vioscreen sessions failed",
                    "content": payload},
                   EN_US)


@celery.task(ignore_result=True)
def fetch_ffqs():
    MAX_FETCH_SIZE = 100

    vio_api = VioscreenAdminAPI(perform_async=False)

    # obtain our current unfinished sessions to check
    with Transaction() as t:
        r = VioscreenSessionRepo(t)
        not_represented = r.get_unfinished_sessions()

    # collect sessions to update
    unable_to_update_session = []
    updated_sessions = []
    for sess in enumerate(not_represented):
        # update session status information
        try:
            session_detail = vio_api.session_detail(sess)
        except:  # noqa
            unable_to_update_session.append(sess)
        else:
            updated_sessions.append(session_detail)

    # perform the update after we collect everything to reduce teh length of
    # time we hold the transaction open
    with Transaction() as t:
        r = VioscreenSessionRepo(t)
        for session_detail in updated_sessions:
            r.upsert_session(session_detail)
        t.commit()

    with Transaction() as t:
        vs = VioscreenSessionRepo(t)
        ffqs_not_represented = vs.get_missing_ffqs()

    # fetch ffq data for sessions we don't yet have it from
    failed_ffqs = []
    for sess in ffqs_not_represented[:MAX_FETCH_SIZE]:
        try:
            error, ffq = vio_api.get_ffq(sess.sessionId)
        except Exception as e:  # noqa
            failed_ffqs.append((sess.sessionId, str(e)))
            continue

        if error:
            failed_ffqs.append((sess.sessionId, repr(error)))
        else:
            # the call to get_ffq is long, and the data from many ffqs is
            # large so let's insert as we go
            with Transaction() as t:
                vs = VioscreenRepo(t)
                vs.insert_ffq(ffq)
                t.commit()

    if len(failed_ffqs) > 0 or len(unable_to_update_session) > 0:
        payload = ''.join(['%s : %s\n' % (repr(s), m)
                           for s, m in failed_ffqs + unable_to_update_session])
        send_email(SERVER_CONFIG['pester_email'], "pester_daniel",
                   {"what": "Vioscreen ffq insert failed",
                    "content": payload},
                   EN_US)
