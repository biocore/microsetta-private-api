from microsetta_private_api.LEGACY.locale_data import american_gut, british_gut

EN_US = "en-US"
EN_GB = "en-GB"
ES_MX = "es-MX"

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
    }
    #,
    #ES_MX: {
    #    NEW_PARTICIPANT_KEY: spanish_gut._NEW_PARTICIPANT,
    #    LANG_NAME_KEY: "spanish"
    #}
}
