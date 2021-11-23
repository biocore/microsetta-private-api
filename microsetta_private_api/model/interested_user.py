from microsetta_private_api.model.model_base import ModelBase


class InterestedUser(ModelBase):
    def __init__(self, interested_user_id, campaign_id, acquisition_source,
                 first_name, last_name, email, phone, address_1, address_2,
                 city, state, postal_code, country, latitude, longitude,
                 confirm_consent, ip_address, creation_timestamp,
                 update_timestamp, address_checked, address_valid,
                 converted_to_account, converted_to_account_timestamp):
        self.interested_user_id = interested_user_id
        self.campaign_id = campaign_id
        self.acquisition_source = acquisition_source
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.confirm_consent = confirm_consent
        self.ip_address = ip_address
        self.creation_timestamp = creation_timestamp
        self.update_timestamp = update_timestamp
        self.address_checked = address_checked
        self.address_valid = address_valid
        self.converted_to_account = converted_to_account
        self.converted_to_account_timestamp = converted_to_account_timestamp

    def to_api(self):
        return self.__dict__.copy()
