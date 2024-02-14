from datetime import datetime

HUMAN_CONSENT_TODDLER = "0-6"
HUMAN_CONSENT_CHILD = "7-12"
HUMAN_CONSENT_ADOLESCENT = "13-17"
HUMAN_CONSENT_ADULT = "18-plus"
HUMAN_CONSENT_AGE_GROUPS = (
    HUMAN_CONSENT_TODDLER,
    HUMAN_CONSENT_CHILD,
    HUMAN_CONSENT_ADOLESCENT,
    HUMAN_CONSENT_ADULT
)


class ConsentDocument:
    @staticmethod
    def from_dict(input_dict, account_id, consent_id):
        consent_type = input_dict["consent_type"]
        locale = input_dict["locale"]
        date_time = datetime.now()
        consent = input_dict["consent"]
        reconsent = input_dict["reconsent"]
        version = input_dict["version"]
        return ConsentDocument(
            consent_id, consent_type, locale,
            date_time, consent, account_id,
            reconsent, version
        )

    def __init__(self, consent_id, consent_type, locale,
                 date_time, consent_content,
                 account_id, reconsent, version):
        self.consent_id = consent_id
        self.consent_type = consent_type
        self.locale = locale
        self.date_time = date_time
        self.consent_content = consent_content
        self.account_id = account_id
        self.reconsent = reconsent
        self.version = version

    def to_api(self):
        result = {
            "consent_id": self.consent_id,
            "consent_type": self.consent_type,
            "locale": self.locale,
            "document": self.consent_content,
            "reconsent_required": self.reconsent,
            "version": self.version
        }

        return result


class ConsentSignature:
    @staticmethod
    def from_dict(input_dict, source_id, signature_id):
        date_time = datetime.now()

        parent_name_1 = input_dict.get("parent_1_name")
        parent_name_2 = input_dict.get("parent_2_name")
        deceased_parent = input_dict.get("deceased_parent")
        assent_obtainer = input_dict.get("assent_obtainer")
        assent_id = input_dict.get("assent_id")
        consent_content = input_dict.get("consent_content")
        assent_content = input_dict.get("assent_content")
        consent_type = input_dict.get("consent_type")

        return ConsentSignature(
            signature_id,
            input_dict["consent_id"],
            source_id,
            date_time,
            parent_name_1,
            parent_name_2,
            deceased_parent,
            assent_obtainer,
            assent_id,
            consent_content,
            assent_content,
            consent_type
        )

    def __init__(self, signature_id, consent_id, source_id,
                 date_time, parent_1_name, parent_2_name,
                 deceased_parent, assent_obtainer, assent_id,
                 consent_content, assent_content, consent_type):
        self.signature_id = signature_id
        self.consent_id = consent_id
        self.source_id = source_id
        self.date_time = date_time
        self.parent_1_name = parent_1_name
        self.parent_2_name = parent_2_name
        self.deceased_parent = deceased_parent
        self.assent_obtainer = assent_obtainer
        self.assent_id = assent_id
        self.consent_content = consent_content
        self.assent_content = assent_content
        self.consent_type = consent_type

    def to_api(self):
        return {'signature_id': self.signature_id,
                'consent_id': self.consent_id,
                'source_id': self.source_id,
                'date_time': self.date_time,
                'parent_1_name': self.parent_1_name,
                'parent_2_name': self.parent_2_name,
                'deceased_parent': self.deceased_parent,
                'assent_obtainer': self.assent_obtainer,
                'assent_id': self.assent_id,
                'consent_content': self.consent_content,
                'assent_content': self.assent_content,
                'consent_type': self.consent_type
                }
