import json
from microsetta_private_api.model.model_base import ModelBase


def human_decoder(obj):
    if isinstance(obj, dict):
        return HumanInfo(
            obj["name"],
            obj["email"],
            obj["is_juvenile"],
            obj["parent1_name"],
            obj["parent1_deceased"],
            obj["parent2_name"],
            obj["parent2_deceased"],
            obj["consent_date"],
            obj["age_range"])
    return obj


def animal_decoder(obj):
    if isinstance(obj, dict):
        return AnimalInfo(obj["name"])
    return obj


def environment_decoder(obj):
    if isinstance(obj, dict):
        return EnvironmentInfo(obj["name"], obj["description"])
    return obj


class HumanInfo:
    def __init__(self, name, email, is_juvenile,
                 parent1_name, parent1_deceased,
                 parent2_name, parent2_deceased,
                 consent_date, age_range):
        self.name = name
        self.email = email
        self.is_juvenile = is_juvenile
        self.parent1_name = parent1_name
        self.parent1_deceased = parent1_deceased
        self.parent2_name = parent2_name
        self.parent2_deceased = parent2_deceased
        self.consent_date = consent_date
        self.age_range = age_range


class AnimalInfo:
    def __init__(self, name):
        self.name = name


class EnvironmentInfo:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Source(ModelBase):
    SOURCE_TYPE_HUMAN = "human"
    SOURCE_TYPE_ANIMAL = "animal"
    SOURCE_TYPE_ENVIRONMENT = "environmental"

    def __init__(self, source_id, account_id, source_type, source_data):
        self.id = source_id
        self.account_id = account_id
        self.source_type = source_type
        self.source_data = source_data

    def to_api(self):
        

        if self.source_type == Source.SOURCE_TYPE_HUMAN:
            consent = None

            if self.source_data.consent_date is not None:
                if self.source_data.is_juvenile:
                    consent = {
                        "participant_name": self.source_data.name,
                        "participant_email": self.source_data.email,
                        "parent_1_name": self.parent1_name,
                        "parent_2_name": self.parent2_name,
                        "deceased_parent": (self.parent1_deceased or
                                            self.parent2_deceased),
                        "obtainer_name": None  # TODO: What is this???
                    }
                else:
                    consent = {
                        "participant_name": self.source_data.name,
                        "participant_email": self.source_data.email
                    }

            return {
                "source_type": self.source_type,
                "source_name": self.source_name,
                "consent": consent
            }
        if self.source_type in [
                                Source.SOURCE_TYPE_ANIMAL,
                                Source.SOURCE_TYPE_ENVIRONMENT
                               ]:
            return {
                "source_type": self.source_type,
                "source_name": self.source_data.name
            }

    @classmethod
    def create_human(cls, source_id, account_id, human_info):
        return Source(
            source_id,
            account_id,
            Source.SOURCE_TYPE_HUMAN,
            human_info)

    @classmethod
    def create_animal(cls, source_id, account_id, animal_info):
        return Source(
            source_id,
            account_id,
            Source.SOURCE_TYPE_ANIMAL,
            animal_info)

    @classmethod
    def create_environment(cls, source_id, account_id, env_info):
        return Source(
            source_id,
            account_id,
            Source.SOURCE_TYPE_ENVIRONMENT,
            env_info)

    @classmethod
    def from_json(cls, source_id, account_id, typed_json_data):
        decoder_hook = DECODER_HOOKS[typed_json_data["source_type"]]
        return Source(source_id, account_id, typed_json_data["source_type"],
                      json.loads(typed_json_data, object_hook=decoder_hook))


DECODER_HOOKS = {
    Source.SOURCE_TYPE_HUMAN: human_decoder,
    Source.SOURCE_TYPE_ANIMAL: animal_decoder,
    Source.SOURCE_TYPE_ENVIRONMENT: environment_decoder
}
