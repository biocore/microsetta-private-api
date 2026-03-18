from unittest import TestCase, main, skipIf

from microsetta_private_api.client.fundrazr import FundrazrClient
from microsetta_private_api.config_manager import SERVER_CONFIG


class FundrazrClientTests(TestCase):
    def setUp(self):
        self.c = FundrazrClient()

    @skipIf(SERVER_CONFIG['fundrazr_url'] in ('', 'fundrazr_url_placeholder'),
            "Fundrazr secrets not provided")
    def test_payments(self):
        # payments comeback with the most recent first
        obs_gen = self.c.payments()
        obs = next(obs_gen)
        obs2 = next(obs_gen)
        remainder = list(obs_gen)

        # staging is limited, and let's not assume its transaction state
        # will remain stable. but I _think_ all will have claimed items
        self.assertTrue(len(obs.claimed_items) > 0)
        self.assertTrue(len(obs2.claimed_items) > 0)
        self.assertTrue(obs.amount > 0)
        self.assertTrue(obs2.amount > 0)

        # we should have more than 2 transactions...
        self.assertTrue(len(remainder) > 0)

        second_to_last = obs2.created_as_unixts()
        timegen = self.c.payments(since=second_to_last)
        items = list(timegen)

        # DEBUG: gather information about timestamp precision and item counts
        print("\nDEBUG test_payments:")
        print(f"  obs (most recent):  id={obs.id!r}  "
              f"created={obs.created!r}  "
              f"unixts={obs.created_as_unixts()}")
        print(f"  obs2 (2nd recent):  id={obs2.id!r}  "
              f"created={obs2.created!r}  "
              f"unixts={obs2.created_as_unixts()}")
        print(f"  second_to_last unixts (after +1): {second_to_last + 1}")
        print(f"  len(remainder)={len(remainder)}")
        print(f"  len(items since obs2)={len(items)}")
        for i, item in enumerate(items):
            print(f"    items[{i}]: id={item.id!r}  "
                  f"created={item.created!r}  "
                  f"unixts={item.created_as_unixts()}")

        # there should only be a single transaction newer than
        # second to last
        self.assertEqual(len(items), 1)

    @skipIf(SERVER_CONFIG['fundrazr_url'] in ('', 'fundrazr_url_placeholder'),
            "Fundrazr secrets not provided")
    def test_campaigns(self):
        obs = self.c.campaigns()

        # staging has three campaigns, let's assume that's stable...
        self.assertEqual(len(obs), 3)
        self.assertTrue(len(obs[0].items) > 0)

    @skipIf(SERVER_CONFIG['fundrazr_url'] in ('', 'fundrazr_url_placeholder'),
            "Fundrazr secrets not provided")
    def test_campaign(self):
        obs = self.c.campaign('14i22')
        self.assertEqual(obs.title, 'American Gut V2')


if __name__ == '__main__':
    main()
