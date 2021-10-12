from microsetta_private_api.model.model_base import ModelBase


class Campaign(ModelBase):
    def __init__(self, campaign_id, title, instructions, header_image,
                 permitted_countries, language_key, accepting_participants,
                 associated_projects, language_key_alt, title_alt,
                 instructions_alt):
        self.campaign_id = campaign_id
        self.title = title
        self.instructions = instructions
        self.header_image = header_image
        self.permitted_countries = permitted_countries
        self.language_key = language_key
        self.accepting_participants = accepting_participants
        self.associated_projects = associated_projects
        self.language_key_alt = language_key_alt
        self.title_alt = title_alt
        self.instructions_alt = instructions_alt

    def to_api(self):
        return {
            "campaign_id": self.campaign_id,
            "title": self.title,
            "instructions": self.instructions,
            "header_image": self.header_image,
            "permitted_countries": self.permitted_countries,
            "language_key": self.language_key,
            "accepting_participants": self.accepting_participants,
            "associated_projects": self.associated_projects,
            "language_key_alt": self.language_key_alt,
            "title_alt": self.title_alt,
            "instructions_alt": self.instructions_alt
        }
