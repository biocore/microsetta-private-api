from datetime import datetime


class ConsentDocument:
    @staticmethod
    def from_dict(input_dict, account_id, consent_id):
        consent_type = input_dict["consent_type"]
        locale = input_dict["locale"]
        date_time = datetime.now()
        consent = input_dict["consent"]
        
        return ConsentDocument(
            consent_id, consent_type, locale,
            date_time, consent, account_id
        )


    def __init__(self, consent_id, consent_type, locale,
                date_time, consent_content, 
                account_id):
        self.consent_id = consent_id
        self.consent_type = consent_type
        self.locale = locale
        self.date_time = date_time
        self.consent_content = consent_content
        self.account_id = account_id

    """To be written later!"""
    def to_api(self):
        result = {
                    "consent_id" : self.consent_id,
                    "consent_type" : self.consent_type,
                    "locale" : self.locale,
                    "document" : self.consent_content
                 }

        return result

class ConsentSignature:
    @staticmethod
    def from_dict(input_dict, signature_id):
        date_time = datetime.now()

        return ConsentSignature(
            signature_id,
            input_dict["consent_id"], 
            input_dict["source_id"],
            date_time,
            input_dict["parent_1_name"],
            input_dict["parent_2_name"],
            input_dict["deceased_parent"],
            input_dict["assent_obtainer"]
        )

    def __init__(self, signature_id, consent_id, source_id,
                date_time, parent_1_name, parent_2_name,
                deceased_parent, assent_obtainer):
        self.signature_id = signature_id
        self.consent_id = consent_id
        self.source_id = source_id
        self.date_time = date_time
        self.parent_1_name = parent_1_name
        self.parent_2_name = parent_2_name
        self.deceased_parent = deceased_parent
        self.assent_obtainer = assent_obtainer

    #Will be updated later
    def to_api(self):
        return ""
    