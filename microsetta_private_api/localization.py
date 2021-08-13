from microsetta_private_api.LEGACY.locale_data \
    import (american_gut, british_gut, spanish_gut)

EN_US = "en_US"
EN_GB = "en_GB"
ES_MX = "es_MX"

NEW_PARTICIPANT_KEY = "new_participant"
LANG_NAME_KEY = "lang_name"
LANG_TAG_KEY = "language_tag"


class _LANG_SUPPORT(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getitem__(self, language_tag):
        language_tag = self.normalize(language_tag)
        return super().__getitem__(language_tag)

    def normalize(self, tag):
        tag = tag.replace('-', '_')
        for lang in self:
            if tag.lower() == lang.lower():
                return lang
        raise KeyError(f"Unrecognized language_tag: {tag}")


LANG_SUPPORT = _LANG_SUPPORT({
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
})
