from unittest import TestCase, main, skipIf

from microsetta_private_api.client.fundrazr import (FundrazrClient,
                                                    FundrazrException)
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


if __name__ == '__main__':
    main()
