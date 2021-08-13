from microsetta_private_api.LEGACY.locale_data \
    import (american_gut, british_gut, spanish_gut)

EN_US = "en_US"
EN_GB = "en_GB"
ES_MX = "es_MX"

NEW_PARTICIPANT_KEY = "new_participant"
LANG_NAME_KEY = "lang_name"
LANG_TAG_KEY = "language_tag"

LANG_SUPPORT = {
    EN_US: {
        NEW_PARTICIPANT_KEY: american_gut._NEW_PARTICIPANT,
        LANG_NAME_KEY: "american"
    },
    EN_GB: {
        NEW_PARTICIPANT_KEY: british_gut._NEW_PARTICIPANT,
        LANG_NAME_KEY: "british"
    },
    ES_MX: {
        NEW_PARTICIPANT_KEY: spanish_gut._NEW_PARTICIPANT,
        LANG_NAME_KEY: "spanish"
    }
}


def normalize(tag):
    tag = tag.replace('-', '_')
    for lang in LANG_SUPPORT:
        if tag.lower() == lang.lower():
            return lang
    raise ValueError(f"Unrecognized language_tag: {tag}")

