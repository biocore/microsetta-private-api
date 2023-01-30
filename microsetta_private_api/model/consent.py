from datetime import datetime


class ConsentDocument:
    @staticmethod
    def from_dict(input_dict, account_id, consent_id):
        consent_type = input_dict["consent_type"]
        locale = input_dict["locale"]
        date_time = datetime.now()
        consent = input_dict["consent"]
        reconsent = input_dict["reconsent"]
        return ConsentDocument(
            consent_id, consent_type, locale,
            date_time, consent, account_id,
            reconsent
        )

    def __init__(self, consent_id, consent_type, locale,
                 date_time, consent_content,
                 account_id, reconsent):
        self.consent_id = consent_id
        self.consent_type = consent_type
        self.locale = locale
        self.date_time = date_time
        self.consent_content = consent_content
        self.account_id = account_id
        self.reconsent = reconsent

    def to_api(self):
        result = {
                    "consent_id": self.consent_id,
                    "consent_type": self.consent_type,
                    "locale": self.locale,
                    "document": self.consent_content,
                    "reconsent_required": self.reconsent
                }

        return result


class ConsentSignature:
    @staticmethod
    def from_dict(input_dict, source_id, signature_id):
        date_time = datetime.now()

        parent_name_1 = input_dict.get("parent_1_name")
        parent_name_2 = input_dict.get("parent_2_name")
        deceased_parent = input_dict.get("deceased_parent")
        assent_obtainer = input_dict.get("obtainer_name")
        assent_id = input_dict.get("assent_id")

        return ConsentSignature(
            signature_id,
            input_dict["consent_id"],
            source_id,
            date_time,
            parent_name_1,
            parent_name_2,
            deceased_parent,
            assent_obtainer,
            assent_id
        )

    def __init__(self, signature_id, consent_id, source_id,
                 date_time, parent_1_name, parent_2_name,
                 deceased_parent, assent_obtainer, assent_id):
        self.signature_id = signature_id
        self.consent_id = consent_id
        self.source_id = source_id
        self.date_time = date_time
        self.parent_1_name = parent_1_name
        self.parent_2_name = parent_2_name
        self.deceased_parent = deceased_parent
        self.assent_obtainer = assent_obtainer
        self.assent_id = assent_id

    def to_api(self):
        return {'signature_id': self.signature_id,
                'consent_id': self.consent_id,
                'source_id': self.source_id,
                'date_time': self.date_time,
                'parent_1_name': self.parent_1_name,
                'parent_2_name': self.parent_2_name,
                'deceased_parent': self.deceased_parent,
                'assent_obtainer': self.assent_obtainer,
                'assent_id': self.assent_id
                }
