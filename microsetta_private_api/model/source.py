from microsetta_private_api.model.model_base import ModelBase


class HumanInfo:
    @staticmethod
    def from_dict(input_dict, consent_date, date_revoked):
        consent = input_dict["consent"]
        age_range = consent['age_range']
        is_juvenile = age_range in ['0-6', '7-12', '13-17']
        if is_juvenile:
            child_info = consent.get("child_info")
        else:
            child_info = {}

        return HumanInfo(
            consent["participant_email"],
            is_juvenile,
            child_info.get("parent_1_name"),
            child_info.get("parent_2_name"),
            child_info.get("deceased_parent"),
            consent_date,
            date_revoked,
            child_info.get("obtainer_name"),
            age_range)

    def __init__(self, email, is_juvenile,
                 parent1_name, parent2_name, deceased_parent,
                 consent_date, date_revoked, assent_obtainer, age_range):
        self.email = email
        self.is_juvenile = is_juvenile
        self.parent1_name = parent1_name
        self.parent2_name = parent2_name
        self.deceased_parent = deceased_parent
        self.consent_date = consent_date
        self.date_revoked = date_revoked
        self.assent_obtainer = assent_obtainer
        self.age_range = age_range

    def to_api(self):
        consent = {"participant_email": self.email,
                   "age_range": self.age_range}

        if self.is_juvenile:
            consent.update({
                "participant_email": self.email,
                "parent_1_name": self.parent1_name,
                "parent_2_name": self.parent2_name,
                "deceased_parent": self.deceased_parent,
                "obtainer_name": self.assent_obtainer
            })

        result = {"consent": consent}
        return result


class NonHumanInfo:
    @staticmethod
    def from_dict(input_dict):
        return NonHumanInfo(input_dict["source_description"])

    def __init__(self, description):
        self.description = description

    def to_api(self):
        result = {"source_description": self.description}
        return result


class Source(ModelBase):
    SOURCE_TYPE_HUMAN = "human"
    SOURCE_TYPE_ANIMAL = "animal"
    SOURCE_TYPE_ENVIRONMENT = "environmental"

    def __init__(self, source_id, account_id, source_type,
                 source_name, source_data):
        self.id = source_id
        self.account_id = account_id
        self.source_type = source_type
        self.name = source_name
        self.source_data = source_data

    def to_api(self):
        result = {
                    "source_type": self.source_type,
                    "source_name": self.name,
                    "source_id": self.id
                 }

        result.update(self.source_data.to_api())
        return result
