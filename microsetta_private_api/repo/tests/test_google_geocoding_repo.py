import unittest
import json

from microsetta_private_api.model.address import Address
from microsetta_private_api.repo.google_geocoding_repo import\
    GoogleGeocodingRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.util.google_geocoding import\
    _construct_request_address, _parse_response


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
    def test_create_record(self):
        with Transaction() as t:
            gg_repo = GoogleGeocodingRepo(t)
            request_address = _construct_request_address(UCSD_ADDRESS)

            request_id = gg_repo.create_record(request_address)

            self.assertNotEqual(request_id, None)

    def test_update_record(self):
        with Transaction() as t:
            gg_repo = GoogleGeocodingRepo(t)
            request_address = _construct_request_address(UCSD_ADDRESS)

            request_id = gg_repo.create_record(request_address)

            obs = gg_repo.update_record(
                request_id,
                json.dumps(UCSD_GEOCODING_RESULTS)
            )

            self.assertEqual(obs, 1)

    def test_get_record(self):
        with Transaction() as t:
            gg_repo = GoogleGeocodingRepo(t)
            request_address = _construct_request_address(UCSD_ADDRESS)

            request_id = gg_repo.create_record(request_address)

            _ = gg_repo.update_record(
                request_id,
                json.dumps(UCSD_GEOCODING_RESULTS)
            )

            obs = gg_repo.get_record(request_id)

            self.assertEqual(obs, UCSD_GEOCODING_RESULTS)

    def test_check_duplicate(self):
        with Transaction() as t:
            gg_repo = GoogleGeocodingRepo(t)
            request_address = _construct_request_address(UCSD_ADDRESS)

            request_id = gg_repo.create_record(request_address)

            _ = gg_repo.update_record(
                request_id,
                json.dumps(UCSD_GEOCODING_RESULTS)
            )

            obs = gg_repo.check_duplicate(request_address)

            self.assertEqual(obs, request_id)


if __name__ == '__main__':
    unittest.main()
