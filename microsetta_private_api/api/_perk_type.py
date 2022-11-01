from flask import jsonify

from microsetta_private_api.repo.perk_type_repo import PerkTypeRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.config_manager import SERVER_CONFIG


def add_perk_type_to_campaign(body, token_info):
    """Add a fundazr perk type to a campaign

        Parameters
        ----------
        campaign_id : str
            A fundrazr campaign ID
        perk : Item
            An instance of a campaign Item
        """
    # TODO : Map these titles with the original titles
    with Transaction() as t:
        pt = PerkTypeRepo(t)
        if body['perk_id'] == SERVER_CONFIG["Perks_type_ffq"]:
            perk_type = "FFQ"

        elif body['perk_id'] == SERVER_CONFIG["Perks_type_ffq_kit"]:
            perk_type = "FFQ_SAMPLE_KIT"

        elif body['perk_id'] == SERVER_CONFIG["Perks_type_ffq_one_year"]:
            perk_type = "FFQ_ONE_YEAR"
            pt.add_subscription(body['contact_email'], body['transaction_id'])

        else:
            # default case
            # TODO : Have to confirm whether need to raise exception
            perk_type = ''

        pt.add_perk_type_to_campaign(body['perk_id'], perk_type)
        pt.add_activation_code(body['campaign_id'], body['perk_id'],
                               perk_type, body['contact_email'],
                               body['payer_name'])


def get_perk_type(body, token_info):
    """Get perk type from the perk id
        Parameters
        ----------
        perk_id : String
            An instance of a campaign Item+
        """
    with Transaction() as t:
        pt = PerkTypeRepo(t)
        return jsonify(pt.get_perk_type(body['perk_id'])), 200
