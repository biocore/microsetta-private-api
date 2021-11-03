from unittest import TestCase, main, skipIf

from microsetta_private_api.client.fundrazr import FundrazrClient
from microsetta_private_api.config_manager import SERVER_CONFIG


class FundrazrClientTests(TestCase):
    def setUp(self):
        self.c = FundrazrClient()

    @skipIf(SERVER_CONFIG['fundrazr_url'] in ('', 'fundrazr_url_placeholder'),
            "Fundrazr secrets not provided")
    def test_campaigns(self):
        obs = self.c.campaigns()
        obs = {(campaign.title, campaign.id) for campaign in obs}
        exp = {('The Microsetta Initiative - Mexico', 'b1q1v4'),
               ('The Microsetta Initiative', '31l0S2'),
               ('Australian Gut', '11OxG1'),
               ('Global FoodOmics Project', '11Ewye'),
               ('British Gut', '4sSf3'),
               ('American Gut', '4Tqx5')}
        self.assertTrue(exp.issubset(obs))

    @skipIf(SERVER_CONFIG['fundrazr_url'] in ('', 'fundrazr_url_placeholder'),
            "Fundrazr secrets not provided")
    def test_payments(self):
        obs_gen = self.c.payments()
        obs = next(obs_gen)
        obs2 = next(obs_gen)

        # our limit is 50 and we definitely have more than 50 transactions
        self.assertEqual(len(obs), 50)
        self.assertEqual(len(obs2), 50)
        self.assertNotEqual(obs, obs2)

        # this is pretty weak so lets do better
        self.fail()


if __name__ == '__main__':
    main()
