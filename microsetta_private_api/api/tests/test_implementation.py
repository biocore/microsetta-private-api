from unittest import TestCase, main
from microsetta_private_api.api.implementation import verify_and_decode_token


class ImplementationTests(TestCase):
    def test_verify_and_decode_token_invalid(self):
        real_output = verify_and_decode_token('fake token')


if __name__ == "__main__":
    main()
