from flask import jsonify
from microsetta_private_api.repo.campaign_repo import CampaignRepo
from microsetta_private_api.repo.transaction import Transaction


def get_campaign_information(campaign_id):
    with Transaction() as t:
        campaign_repo = CampaignRepo(t)
        campaign = campaign_repo.get_campaign_by_id(campaign_id)

        # rather than return an error on a bad campaign id, we'll return
        # a code indicating that so the signup form can handle it gracefully
        if campaign is None:
            return jsonify(campaign_id="BADID"), 200
        else:
            return campaign, 200
