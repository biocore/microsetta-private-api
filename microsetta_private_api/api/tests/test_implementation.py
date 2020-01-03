from unittest import TestCase, main
from microsetta_private_api.api.implementation import verify_and_decode_token


class ImplementationTests(TestCase):
    def test_verify_and_decode_token_invalid(self):
        real_output = verify_and_decode_token() #'990')
        self.assertIsNone(real_output)


if __name__ == "__main__":
    main()
