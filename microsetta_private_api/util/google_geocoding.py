import json
import requests
import urllib.parse

from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.google_geocoding_repo import\
    GoogleGeocodingRepo
from microsetta_private_api.config_manager import SERVER_CONFIG


def geocode_address(address):
    with Transaction() as t:
        gg_repo = GoogleGeocodingRepo(t)

        request_address = _construct_request_address(address)

        # Determine if we've already geocoded the address
        new_request, ret_val = gg_repo.get_or_create_record(request_address)
        if new_request is False:
            # Already geocoded, just return the parsed response
            return _parse_response(ret_val)
        else:
            # New record, so ret_val is the ID of the record in the database
            request_id = ret_val

            if request_id is None:
                # There was an error creating the DB record - we should never
                # reach this point, but if we do, mark it as failed
                return None, None, True

            url_params = {
                "address": request_address,
                "key": SERVER_CONFIG['google_geocoding_key']
            }
            request_url = SERVER_CONFIG['google_geocoding_url'] + "?%s" % \
                urllib.parse.urlencode(url_params)

            response = requests.get(request_url)
            if response.ok is False:
                exception_msg = "Error connecting to Google Geocoding API."
                exception_msg += " Status Code: " + response.status_code
                exception_msg += " Status Text: " + response.reason
                raise Exception(exception_msg)

            response_raw = response.text
            response_obj = json.loads(response_raw)

            try:
                gg_repo.update_record(request_id, response_raw)
            except:
                # Something went wrong here, but we shouldn't stop processing.
                pass

            t.commit()

            return _parse_response(response_obj)


def _construct_request_address(address):
    request_address = address.street
    if address.street2 is not None:
        request_address += " " + address.street2
    request_address += ", " + address.city
    request_address += ", " + address.state
    request_address += " " + address.post_code
    request_address += ", " + address.country_code

    return request_address


def _parse_response(geocoding_response, strict_mode=False):
    # NB: Google's Geocoding API will do it's best to find _a_ match, even if
    # it's not an ideal match. I'm implementing a strict_mode parameter that
    # can be leveraged based on how precise we need the geocoding result to be

    latitude = None
    longitude = None
    request_error = False

    if geocoding_response['status'] != "OK":
        # There was some sort of failure, either at a technical level, or no
        # records were found.
        request_error = True

    else:
        # Google's Geocoding API returns the most appropriate result first
        # so we'll default to that. If it's an approximate match, we can
        # safely assume that any other results would also be approximate
        result = geocoding_response['results'][0]

        # If the partial_match key exists and we're using strict mode, we can
        # immediately fail the address
        if 'partial_match' in result and strict_mode:
            request_error = True
        else:
            latitude = result['geometry']['location']['lat']
            longitude = result['geometry']['location']['lng']

    return latitude, longitude, request_error
