from flask import jsonify
from microsetta_private_api.repo.campaign_repo import CampaignRepo
from microsetta_private_api.repo.transaction import Transaction


def get_campaign_information(campaign_id):
    with Transaction() as t:
        campaign_repo = CampaignRepo(t)
        campaign = campaign_repo.get_campaign_by_id(campaign_id)

        if campaign is None:
            return jsonify(code=404, message="Campaign not found"), 404
        else:
            return campaign, 200
