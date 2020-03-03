from microsetta_private_api.model.model_base import ModelBase
from werkzeug.exceptions import BadRequest


def info_from_api(api_obj):
    if api_obj["source_type"] == Source.SOURCE_TYPE_HUMAN:
        # Note: consent_date and date_revoked aren't sent over the api
        # so will be lost in translation
        return human_info_from_api(api_obj,
                                   consent_date=None,
                                   date_revoked=None)
    elif api_obj["source_type"] == Source.SOURCE_TYPE_ANIMAL:
        return animal_decoder(api_obj)
    elif api_obj["source_type"] == Source.SOURCE_TYPE_ENVIRONMENT:
        return environment_decoder(api_obj)
    else:
        raise BadRequest("Unknown source_type: " + str(api_obj["source_type"]))


def human_info_from_api(human_source, consent_date, date_revoked):
    consent = human_source["consent"]
    age_range = consent['age_range']
    is_juvenile = age_range in ['0-6', '7-12', '13-17']
    if is_juvenile:
        child_info = consent.get("child_info")
    else:
        child_info = {}

    return HumanInfo(
        human_source["source_name"],
        consent["participant_email"],
        is_juvenile,
        child_info.get("parent_1_name"),
        child_info.get("parent_2_name"),
        child_info.get("deceased_parent"),
        consent_date,
        date_revoked,
        child_info.get("obtainer_name"),
        age_range)


def human_decoder(obj):
    if isinstance(obj, dict):
        return HumanInfo(
            obj["source_name"],
            obj["email"],
            obj["is_juvenile"],
            obj["parent1_name"],
            obj["parent2_name"],
            obj["deceased_parent"],
            obj["consent_date"],
            obj["date_revoked"],
            obj["assent_obtainer"],
            obj["age_range"])
    return obj


def animal_decoder(obj):
    if isinstance(obj, dict):
        return AnimalInfo(obj["source_name"], obj["source_description"])
    return obj


def environment_decoder(obj):
    if isinstance(obj, dict):
        return EnvironmentInfo(obj["source_name"], obj["source_description"])
    return obj


class HumanInfo:
    def __init__(self, name, email, is_juvenile,
                 parent1_name, parent2_name, deceased_parent,
                 consent_date, date_revoked, assent_obtainer, age_range):
        self.name = name
        self.email = email
        self.is_juvenile = is_juvenile
        self.parent1_name = parent1_name
        self.parent2_name = parent2_name
        self.deceased_parent = deceased_parent
        self.consent_date = consent_date
        self.date_revoked = date_revoked
        self.assent_obtainer = assent_obtainer
        self.age_range = age_range


class AnimalInfo:
    def __init__(self, name, description):
        self.name = name
        self.description = description


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
        result = {
                    "source_type": self.source_type,
                    "source_name": self.source_data.name,
                    "source_id": self.id
                 }

        if self.source_type == Source.SOURCE_TYPE_HUMAN:
            consent = None
            if self.source_data.consent_date is not None:
                if self.source_data.is_juvenile:
                    consent = {
                        "participant_name": self.source_data.name,
                        "participant_email": self.source_data.email,
                        "parent_1_name": self.source_data.parent1_name,
                        "parent_2_name": self.source_data.parent2_name,
                        "deceased_parent": self.source_data.deceased_parent,
                        "obtainer_name": self.source_data.assent_obtainer
                    }
                else:
                    consent = {
                        "participant_name": self.source_data.name,
                        "participant_email": self.source_data.email
                    }
            result["consent"] = consent
        elif self.source_type in [Source.SOURCE_TYPE_ANIMAL,
                                  Source.SOURCE_TYPE_ENVIRONMENT]:
            result["source_description"] = self.source_data.description

        return result

    @classmethod
    def create_human(cls, source_id, account_id, human_info):
        return cls(
            source_id,
            account_id,
            Source.SOURCE_TYPE_HUMAN,
            human_info)

    @classmethod
    def create_animal(cls, source_id, account_id, animal_info):
        return cls(
            source_id,
            account_id,
            Source.SOURCE_TYPE_ANIMAL,
            animal_info)

    @classmethod
    def create_environment(cls, source_id, account_id, env_info):
        return cls(
            source_id,
            account_id,
            Source.SOURCE_TYPE_ENVIRONMENT,
            env_info)

    @classmethod
    def build_source(cls, source_id, account_id, source_info_dict):
        decoder_hook = DECODER_HOOKS[source_info_dict["source_type"]]
        return cls(source_id,
                   account_id,
                   source_info_dict["source_type"],
                   decoder_hook(source_info_dict))


DECODER_HOOKS = {
    Source.SOURCE_TYPE_HUMAN: human_decoder,
    Source.SOURCE_TYPE_ANIMAL: animal_decoder,
    Source.SOURCE_TYPE_ENVIRONMENT: environment_decoder
}
