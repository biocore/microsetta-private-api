from microsetta_private_api.repo.campaign_repo import CampaignRepo
from microsetta_private_api.repo.transaction import Transaction


def get_campaign_information(campaign_id):
    with Transaction() as t:
        campaign_repo = CampaignRepo(t)
        campaign = campaign_repo.get_campaign_by_id(campaign_id)

        # we don't want to raise an exception if the campaign isn't found
        # for signup form, we'll just display default campaign
        if campaign is None:
            return None, 200
        else:
            return campaign, 200
