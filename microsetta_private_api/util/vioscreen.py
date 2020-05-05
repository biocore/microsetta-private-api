import secrets

from Crypto.Cipher import AES
from Crypto import Random
from base64 import b64decode, b64encode
from werkzeug.exceptions import BadRequest
from werkzeug.urls import url_encode

from microsetta_private_api.config_manager import SERVER_CONFIG


def gen_survey_url(language_tag, survey_redirect_url):
    if not survey_redirect_url:
        raise BadRequest("Food Frequency Questionnaire Requires "
                         "survey_redirect_url")

    regcode = SERVER_CONFIG["vioscreen_regcode"]
    url = SERVER_CONFIG["vioscreen_endpoint"] + "/remotelogin.aspx?%s" % \
        url_encode(
              {
                  b"Key": encrypt_key(secrets.token_hex(8),
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
