import json
import requests
import urllib.parse

from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.melissa_repo import MelissaRepo
from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.exceptions import RepoException


def verify_address(address_1, address_2=None, city=None, state=None,
                   postal=None, country=None):
    """
    Required parameters: address_1, postal, country
    Optional parameters: address_2, city, state

    Note - postal and country default to None as you can't have non-default
            arguments after default arguments, and preserving structural order
            makes sense for addresses
    """

    if address_1 is None or len(address_1) < 1 or postal is None or\
            len(postal) < 1 or country is None or len(country) < 1:
        raise KeyError("Must include address_1, postal, and country fields")

    with Transaction() as t:
        # The response codes we can treat as deliverable
        GOOD_CODES = ["AV25", "AV24", "AV23", "AV22"]

        melissa_repo = MelissaRepo(t)

        dupe_status = melissa_repo.check_duplicate(address_1, address_2,
                                                   postal, country)

        if dupe_status is not False:
            # duplicate record - return result with an added field noting dupe
            return_dict = {"address_1": dupe_status["result_address_1"],
                           "address_2": dupe_status['result_address_2'],
                           "city": dupe_status['result_city'],
                           "state": dupe_status['result_state'],
                           "postal": dupe_status['result_postal'],
                           "country": dupe_status['result_country'],
                           "latitude": dupe_status['result_latitude'],
                           "longitude": dupe_status['result_longitude'],
                           "valid": dupe_status['result_good'],
                           "duplicate": True}
            return return_dict
        else:
            record_id = melissa_repo.create_record(address_1, address_2,
                                                   city, state, postal,
                                                   country)

            if record_id is None:
                raise RepoException("Failed to create record in database.")

            url_params = {"id": SERVER_CONFIG["melissa_license_key"],
                          "opt": "DeliveryLines:ON",
                          "format": "JSON",
                          "t": record_id,
                          "a1": address_1,
                          "a2": address_2,
                          "loc": city,
                          "admarea": state,
                          "postal": postal,
                          "ctry": country}

            url = SERVER_CONFIG["melissa_url"] + "?%s" % \
                urllib.parse.urlencode(url_params)

            response = requests.get(url)
            if response.ok is False:
                exception_msg = "Error connecting to Melissa API."
                exception_msg += " Status Code: " + response.status_code
                exception_msg += " Status Text: " + response.reason
                raise Exception(exception_msg)

            response_raw = response.text
            response_obj = json.loads(response_raw)
            if "Records" in response_obj.keys():
                """
                Note: Melissa's Global Address API allows batch requests.
                    However, our usage is on a single-record basis. Therefore,
                    we can safely assume that the response will only include
                    one record to parse and use.
                """

                record_obj = response_obj["Records"][0]

                r_formatted_address = record_obj["FormattedAddress"]
                r_codes = record_obj["Results"]
                r_good = False

                codes = r_codes.split(",")
                for code in codes:
                    if code in GOOD_CODES:
                        r_good = True
                        break

                r_address_1 = record_obj["AddressLine1"]
                r_address_2 = record_obj["AddressLine2"]
                r_city = record_obj["Locality"]
                r_state = record_obj["AdministrativeArea"]
                r_postal = record_obj["PostalCode"]
                r_country = record_obj["CountryName"]
                r_latitude = record_obj["Latitude"]
                r_longitude = record_obj["Longitude"]

                u_success = melissa_repo.update_results(record_id, url,
                                                        response_raw, r_codes,
                                                        r_good,
                                                        r_formatted_address,
                                                        r_address_1,
                                                        r_address_2, r_city,
                                                        r_state, r_postal,
                                                        r_country, r_latitude,
                                                        r_longitude)
                t.commit()

                if u_success is False:
                    exception_msg = "Failed to update results for Melissa "
                    exception_msg += "Address Query " + record_id
                    raise ValueError(exception_msg)

                return_dict = {"address_1": r_address_1,
                               "address_2": r_address_2,
                               "city": r_city,
                               "state": r_state,
                               "postal": r_postal,
                               "country": r_country,
                               "latitude": r_latitude,
                               "longitude": r_longitude,
                               "valid": r_good}

                return return_dict
            else:
                t.commit()
                exception_msg = "Melissa Global Address API failed on "
                exception_msg += record_id

                raise Exception(exception_msg)
