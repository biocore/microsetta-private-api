import unittest
from unittest import skipIf

from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.util.google_geocoding import geocode_address,\
    _construct_request_address, _parse_response
from microsetta_private_api.model.address import Address


UCSD_ADDRESS = Address(
            "9500 Gilman Dr",
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
FAILURE_GEOCODING_RESULTS = {
   "results": [],
   "status": "ZERO_RESULTS"
}
STRICT_GEOCODING_RESULTS = {
   "results": [
      {
         "address_components": [
            {
               "long_name": "New York",
               "short_name": "New York",
               "types": ["locality", "political"]
            },
            {
               "long_name": "New York",
               "short_name": "NY",
               "types": ["administrative_area_level_1", "political"]
            },
            {
               "long_name": "United States",
               "short_name": "US",
               "types": ["country", "political"]
            }
         ],
         "formatted_address": "New York, NY, USA",
         "geometry": {
            "bounds": {
               "northeast": {
                  "lat": 40.9175771,
                  "lng": -73.70027209999999
               },
               "southwest": {
                  "lat": 40.4773991,
                  "lng": -74.25908989999999
               }
            },
            "location": {
               "lat": 40.7127753,
               "lng": -74.0059728
            },
            "location_type": "APPROXIMATE",
            "viewport": {
               "northeast": {
                  "lat": 40.9175771,
                  "lng": -73.70027209999999
               },
               "southwest": {
                  "lat": 40.4773991,
                  "lng": -74.25908989999999
               }
            }
         },
         "partial_match": True,
         "place_id": "ChIJOwg_06VPwokRYv534QaPC8g",
         "types": ["locality", "political"]
      },
      {
         "address_components": [
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
            }
         ],
         "formatted_address": "San Diego, CA, USA",
         "geometry": {
            "bounds": {
               "northeast": {
                  "lat": 33.114249,
                  "lng": -116.90816
               },
               "southwest": {
                  "lat": 32.534856,
                  "lng": -117.3097969
               }
            },
            "location": {
               "lat": 32.715738,
               "lng": -117.1610838
            },
            "location_type": "APPROXIMATE",
            "viewport": {
               "northeast": {
                  "lat": 33.114249,
                  "lng": -116.90816
               },
               "southwest": {
                  "lat": 32.534856,
                  "lng": -117.3097969
               }
            }
         },
         "partial_match": True,
         "place_id": "ChIJSx6SrQ9T2YARed8V_f0hOg0",
         "types": ["locality", "political"]
      }
   ],
   "status": "OK"
}


class GoogleGeocodingTests(unittest.TestCase):
    @skipIf(SERVER_CONFIG['google_geocoding_key'] in
            ('', 'geocoding_key_placeholder'),
            "Google Geocoding secrets not provided")
    def test_geocode_address(self):
        obs_lat, obs_long, obs_error = geocode_address(UCSD_ADDRESS)

        self.assertEqual(obs_lat, 32.8798916)
        self.assertEqual(obs_long, -117.2363115)
        self.assertEqual(obs_error, False)

    def test_construct_request_address(self):
        obs = _construct_request_address(UCSD_ADDRESS)
        self.assertEqual(obs, "9500 Gilman Dr, La Jolla, CA 92093, US")

    def test_parse_response_successful(self):
        obs_lat, obs_long, obs_error = _parse_response(UCSD_GEOCODING_RESULTS)

        self.assertEqual(obs_lat, 32.8798916)
        self.assertEqual(obs_long, -117.2363115)
        self.assertEqual(obs_error, False)

    def test_parse_response_failure(self):
        obs_lat, obs_long, obs_error = _parse_response(
            FAILURE_GEOCODING_RESULTS
        )

        self.assertEqual(obs_lat, None)
        self.assertEqual(obs_long, None)
        self.assertEqual(obs_error, True)

    def test_parse_response_strict(self):
        # The results for STRICT_GEOCODING_RESULTS were generated with a query
        # of 1234 Fake St, San Diego, NY
        obs_lat, obs_long, obs_error = _parse_response(
            STRICT_GEOCODING_RESULTS, True
        )

        self.assertEqual(obs_lat, None)
        self.assertEqual(obs_long, None)
        self.assertEqual(obs_error, True)


if __name__ == '__main__':
    unittest.main()
