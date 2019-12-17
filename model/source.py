import json


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


def canine_decoder(obj):
    if isinstance(obj, dict):
        return CanineInfo(obj["name"])
    return obj


def environment_decoder(obj):
    if isinstance(obj, dict):
        return EnvironmentInfo(obj["name"], obj["description"])
    return obj


DECODER_HOOKS = {
    'human': human_decoder,
    'canine': canine_decoder,
    'environment': environment_decoder
}


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


class CanineInfo:
    def __init__(self, name):
        self.name = name


class EnvironmentInfo:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Source:
    SOURCE_TYPE_HUMAN = "human"
    SOURCE_TYPE_CANINE = "canine"
    SOURCE_TYPE_ENVIRONMENT = "environment"

    def __init__(self, source_id, account_id, source_type, source_data):
        self.id = source_id
        self.account_id = account_id
        self.source_type = source_type
        self.source_data = source_data

    @classmethod
    def create_human(cls, source_id, account_id, human_info):
        return Source(source_id, account_id, 'human', human_info)

    @classmethod
    def create_canine(cls, source_id, account_id, canine_info):
        return Source(source_id, account_id, 'canine', canine_info)

    @classmethod
    def create_environment(cls, source_id, account_id, env_info):
        return Source(source_id, account_id, 'environment', env_info)

    @classmethod
    def from_json(cls, source_id, account_id, typed_json_data):
        decoder_hook = DECODER_HOOKS[typed_json_data["source_type"]]
        return Source(source_id, account_id, typed_json_data["source_type"],
                      json.loads(typed_json_data, object_hook=decoder_hook))
