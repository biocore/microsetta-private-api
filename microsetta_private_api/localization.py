from microsetta_private_api.LEGACY.locale_data \
    import (american_gut, british_gut, spanish_gut, spain_spanish_gut)

EN_US = "en_US"
EN_GB = "en_GB"
ES_MX = "es_MX"
ES_ES = "es_ES"
JA_JP = "ja_JP"

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
    },
    ES_ES: {
        NEW_PARTICIPANT_KEY: spain_spanish_gut._NEW_PARTICIPANT,
        LANG_NAME_KEY: "spain_spanish"
    }
}
