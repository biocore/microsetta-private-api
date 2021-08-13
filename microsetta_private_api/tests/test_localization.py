from unittest import TestCase, main
from microsetta_private_api.localization import (LANG_SUPPORT, LANG_NAME_KEY,
                                                 EN_US)


class LocalizationTests(TestCase):
    def normalize_valid(self):
        for tag in LANG_SUPPORT:
            self.assertEqual(tag, LANG_SUPPORT.normalize(tag))

    def test_normalize_offcase(self):
        for tag in LANG_SUPPORT:
            self.assertEqual(tag, LANG_SUPPORT.normalize(tag.lower()))
            self.assertEqual(tag, LANG_SUPPORT.normalize(tag.upper()))

    def test_normalize_underscore(self):
        for tag in LANG_SUPPORT:
            modified = tag.replace('_', '-')
            self.assertEqual(tag, LANG_SUPPORT.normalize(modified))
            self.assertEqual(tag, LANG_SUPPORT.normalize(modified.lower()))
            self.assertEqual(tag, LANG_SUPPORT.normalize(modified.upper()))

    def test_normalize_invalid(self):
        for bad in ['foobar', 'en_xx', 'en_XX', 'es_en', '12asd']:
            with self.assertRaises(KeyError):
                LANG_SUPPORT.normalize(bad)

    def test_getitem(self):
        self.assertEqual(LANG_SUPPORT[EN_US][LANG_NAME_KEY], 'american')

    def test_getitem_bad(self):
        for bad in ['foobar', 'en_xx', 'en_XX', 'es_en', '12asd']:
            with self.assertRaises(KeyError):
                LANG_SUPPORT[bad]


if __name__ == '__main__':
    main()
