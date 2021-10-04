from unittest import TestCase, main
import datetime

from microsetta_private_api.client.myfoodrepo import MFRClient, MFRException
from microsetta_private_api.config_manager import SERVER_CONFIG


class MFRTests(TestCase):
    def setUp(self):
        self.c = MFRClient('food_&_you')

    # The MFR URL and API key are encoded as github repository secrets.
    # Secrets are not passed when a fork issues a PR. This test will still
    # execute from master once a PR is merged.
    @unittest.skipIf(SERVER_CONFIG['myfoodrepo_url'] in ('', 'mfr_url_placeholder'))  # noqa
    def test_create_get_delete(self):
        cohorts = self.c.cohorts()
        self.assertTrue(len(cohorts.data.cohorts) >= 1)
        cohort = cohorts.data.cohorts[0].codename

        subj_at_creation = self.c.create_subj(cohort)
        key = subj_at_creation.data.subject.key

        subj_at_read = self.c.read_subj(cohort, key)
        self.assertEqual(subj_at_read.data.subject,
                         subj_at_creation.data.subject)

        now = datetime.datetime.now()
        subj_at_exp = self.c.update_subj(cohort, key, now)
        self.assertEqual(subj_at_exp.data.subject.key, key)
        self.assertNotEqual(subj_at_exp.data.subject,
                            subj_at_read.data.subject)

        subj_at_reread = self.c.read_subj(cohort, key)
        self.assertEqual(subj_at_exp.data.subject,
                         subj_at_reread.data.subject)

        self.c.delete_subj(cohort, key)

        with self.assertRaises(MFRException):
            self.c.read_subj(cohort, key)

    def test_json_to_model(self):
        json = """{
                    "foo": "bar",
                    "baz": {"key1": "value1"},
                    "items": [
                      "item1",
                      {"key2": "value2"}
                    ]
                  }"""
        obs = self.c._json_to_model(json)

        self.assertEqual(obs.foo, 'bar')
        self.assertEqual(obs.baz.key1, 'value1')
        self.assertEqual(obs.items[0], 'item1')
        self.assertEqual(obs.items[1].key2, 'value2')


if __name__ == '__main__':
    main()
