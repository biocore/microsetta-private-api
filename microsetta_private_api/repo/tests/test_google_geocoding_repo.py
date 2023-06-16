import unittest
import json
import uuid

from microsetta_private_api.model.address import Address
from microsetta_private_api.repo.google_geocoding_repo import\
    GoogleGeocodingRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.util.google_geocoding import\
    _construct_request_address


UCSD_ADDRESS = Address(
            "9500 Gilman DrENSURETHISISTOTALLYUNIQUE",
            "La Jolla",
            "CA",
            "92093",
            "US"
        )
UCSD_GEOCODING_RESULTS = {
   "results": [
      {
         "address_components": [
            {
               "long_name": "9500",
               "short_name": "9500",
               "types": ["street_number"]
            },
            {
               "long_name": "Gilman Drive",
               "short_name": "Gilman Dr",
               "types": ["route"]
            },
            {
               "long_name": "La Jolla",
               "short_name": "La Jolla",
               "types": ["neighborhood", "political"]
            },
            {
               "long_name": "San Diego",
               "short_name": "San Diego",
               "types": ["locality", "political"]
            },
            {
               "long_name": "San Diego County",
               "short_name": "San Diego County",
               "types": ["administrative_area_level_2", "political"]
            },
            {
               "long_name": "California",
               "short_name": "CA",
               "types": ["administrative_area_level_1", "political"]
            },
            {
               "long_name": "United States",
               "short_name": "US",
               "types": ["country", "political"]
            },
            {
               "long_name": "92093",
               "short_name": "92093",
               "types": ["postal_code"]
            }
         ],
         "formatted_address": "9500 Gilman Dr, La Jolla, CA 92093, USA",
         "geometry": {
            "location": {
               "lat": 32.8798916,
               "lng": -117.2363115
            },
            "location_type": "ROOFTOP",
            "viewport": {
               "northeast": {
                  "lat": 32.8813956302915,
                  "lng": -117.2347271697085
               },
               "southwest": {
                  "lat": 32.8786976697085,
                  "lng": -117.2374251302915
               }
            }
         },
         "place_id": "ChIJ1UVfx8YG3IAR56yE9txtrNA",
         "plus_code": {
            "compound_code": "VQH7+XF La Jolla, San Diego, CA",
            "global_code": "8544VQH7+XF"
         },
         "types": ["street_address"]
      }
   ],
   "status": "OK"
}


class GoogleGeocodingRepoTests(unittest.TestCase):
    def test_get_or_create_record_create(self):
        # Checking the UC San Diego address for the first time, so we should
        # observe return values indicating a new record
        with Transaction() as t:
            gg_repo = GoogleGeocodingRepo(t)
            request_address = _construct_request_address(UCSD_ADDRESS)

            new_request, request_id, _ = gg_repo.get_or_create_record(
                request_address
            )

            self.assertTrue(new_request)
            self.assertTrue(self._is_uuid(request_id))

    def test_get_or_create_record_get(self):
        # We're going to create a record for the UC San Diego address, then
        # check it again, so we should observe return values indicating an
        # existing record
        with Transaction() as t:
            gg_repo = GoogleGeocodingRepo(t)
            request_address = _construct_request_address(UCSD_ADDRESS)

            _, _, _ = gg_repo.get_or_create_record(
                request_address
            )

            new_request, _, _ = gg_repo.get_or_create_record(
                request_address
            )

            self.assertFalse(new_request)

    def test_update_record(self):
        with Transaction() as t:
            gg_repo = GoogleGeocodingRepo(t)
            request_address = _construct_request_address(UCSD_ADDRESS)

            _, request_id, _ = gg_repo.get_or_create_record(request_address)

            obs = gg_repo.update_record(
                request_id,
                json.dumps(UCSD_GEOCODING_RESULTS)
            )

            self.assertEqual(obs, 1)

    def _is_uuid(self, value_to_test):
        try:
            uuid.UUID(str(value_to_test))
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    unittest.main()
