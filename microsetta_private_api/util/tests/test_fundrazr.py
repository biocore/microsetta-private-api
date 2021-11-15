from unittest import TestCase, skipIf, main

from microsetta_private_api.config_manager import SERVER_CONFIG


class FundRazrTests(TestCase):
    @skipIf(SERVER_CONFIG['fundrazr_url'] in ('', 'fr_url_placeholder'),
            "Fundrazr secrets not provided")
    def test_get_payments(self):
        self.fail()


if __name__ == '__main__':
    main()
