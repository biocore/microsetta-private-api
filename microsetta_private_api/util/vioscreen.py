from Crypto.Cipher import AES
from Crypto import Random
from base64 import b64decode, b64encode
from werkzeug.exceptions import BadRequest
from werkzeug.urls import url_encode

from microsetta_private_api.config_manager import AMGUT_CONFIG, SERVER_CONFIG
from microsetta_private_api.LEGACY.locale_data import american_gut, british_gut


def wrap_survey_url(survey_id, language_tag, survey_redirect_url):
    # TODO: Is this the right way to do localization here?
    if language_tag == "en_us":
        text_locale = american_gut.text_locale
    elif language_tag == "en_gb":
        text_locale = british_gut.text_locale
    else:
        raise BadRequest("Unknown Locale: " + language_tag)

    """Return a formatted text block and URL for the external survey"""
    tl = text_locale['human_survey_completed.html']
    embedded_text = tl['SURVEY_VIOSCREEN']
    url = gen_survey_url(survey_id, language_tag)
    return embedded_text % url


def gen_survey_url(survey_id, language_tag, survey_redirect_url):
    if not survey_redirect_url:
        raise BadRequest("Food Frequency Questionnaire Requires "
                         "survey_redirect_url")

    regcode = SERVER_CONFIG["vioscreen_regcode"]
    # TODO: If we have problems getting the ciphertext to be accepted by
    #  vioscreen, it could be due to switching to use of werkzeugs url_encode
    #  rather than tornado's url_escape.  But that has to wait until I can
    #  test with the actual key and registration code.
    url = SERVER_CONFIG["vioscreen_endpoint"] + "/remotelogin.aspx?%s" % \
          url_encode(
              {
                  b"Key": encrypt_key(survey_id,
                                      language_tag,
                                      survey_redirect_url),
                  b"RegCode": regcode.encode()
              }, charset='utf-16'
          )
    return url


def pkcs7_pad_message(in_message):
    # http://stackoverflow.com/questions/14179784/python-encrypting-with-pycrypto-aes  # noqa
    length = 16 - (len(in_message) % 16)
    return in_message + chr(length) * length


def pkcs7_unpad_message(in_message, ):
    return in_message[:-ord(in_message[-1])]


def encrypt_key(survey_id, language_tag, survey_redirect_url):
    # TODO: Is this the right way to do localization here?
    if language_tag == "en_us":
        media_locale = american_gut.media_locale
    elif language_tag == "en_gb":
        media_locale = british_gut.media_locale
    else:
        raise BadRequest("Unknown Locale: " + language_tag)

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
    key = AMGUT_CONFIG.vioscreen_cryptokey
    iv = Random.new().read(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return pkcs7_unpad_message(cipher.decrypt(b64decode(encoded))[16:])
