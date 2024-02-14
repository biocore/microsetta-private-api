import unittest
from unittest import skipIf

from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.util.melissa import verify_address


class MelissaTests(unittest.TestCase):
    @skipIf(SERVER_CONFIG['melissa_license_key'] in
            ('', 'qwerty123456'),
            "Melissa secrets not provided")
    def test_verify_address_valid(self):
        # UC San Diego's address is a known and stable valid address
        obs = verify_address(
            address_1="9500 Gilman Dr",
            address_2="",
            address_3="",
            city="La Jolla",
            state="CA",
            postal="92093",
            country="US"
        )
        self.assertTrue(obs['valid'])

    @skipIf(SERVER_CONFIG['melissa_license_key'] in
            ('', 'qwerty123456'),
            "Melissa secrets not provided")
    def test_verify_address_invalid(self):
        # Non-existent street address in San Diego
        obs = verify_address(
            address_1="1234 NotAReal St",
            address_2="",
            address_3="",
            city="San Diego",
            state="CA",
            postal="92116",
            country="US"
        )
        self.assertFalse(obs['valid'])

    @skipIf(SERVER_CONFIG['melissa_license_key'] in
            ('', 'qwerty123456'),
            "Melissa secrets not provided")
    def test_verify_address_po_box_good(self):
        # Assert that PO boxes will return valid when block_po_boxes=False
        obs = verify_address(
            address_1="PO Box 9001",
            address_2="",
            address_3="",
            city="San Diego",
            state="CA",
            postal="92169",
            country="US",
            block_po_boxes=False
        )
        self.assertTrue(obs['valid'])

    @skipIf(SERVER_CONFIG['melissa_license_key'] in
            ('', 'qwerty123456'),
            "Melissa secrets not provided")
    def test_verify_address_po_box_bad(self):
        # Assert that PO boxes will return invalid when we omit block_po_boxes
        obs = verify_address(
            address_1="PO Box 9002",
            address_2="",
            address_3="",
            city="San Diego",
            state="CA",
            postal="92169",
            country="US"
        )
        self.assertFalse(obs['valid'])


if __name__ == '__main__':
    unittest.main()
