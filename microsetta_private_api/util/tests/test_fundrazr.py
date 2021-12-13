from unittest import TestCase, skipIf, main
import datetime

from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.util.fundrazr import get_fundrazr_transactions
from microsetta_private_api.repo.campaign_repo import (UserTransaction,
                                                       FundRazrCampaignRepo)
from microsetta_private_api.repo.transaction import Transaction


class FundRazrTests(TestCase):
    def setUp(self):
        # swap out the default project association for one that
        # exists in the test database
        self.old = FundRazrCampaignRepo._DEFAULT_PROJECT_ASSOCIATION
        FundRazrCampaignRepo._DEFAULT_PROJECT_ASSOCIATION = (1, )

    def tearDown(self):
        FundRazrCampaignRepo._DEFAULT_PROJECT_ASSOCIATION = self.old

    @skipIf(SERVER_CONFIG['fundrazr_url'] in ('', 'fundrazr_url_placeholder'),
            "Fundrazr secrets not provided")
    def test_get_fundrazr_transactions(self):
        # integration test, verify we can pull from fundrazr and insert
        # real obtained data

        # we should have zero transactions as test database doesn't have any
        # resident
        now = datetime.datetime.now()
        with Transaction() as t:
            ut = UserTransaction(t)
            obs = ut.get_transactions(before=now)
            self.assertEqual(obs, [])

            get_fundrazr_transactions(test_transaction=t)

            obs = ut.get_transactions(before=now)

            # staging has like 7 transactions, but let's not assume that'll be
            # true in perpetuity
            self.assertTrue(len(obs) > 0)

            # rerun to make sure we dont get more transactions, and that we
            # properly handle the lack of new transactions
            seen = len(obs)
            get_fundrazr_transactions(test_transaction=t)
            obs = ut.get_transactions(before=now)
            self.assertEqual(len(obs), seen)


if __name__ == '__main__':
    main()
