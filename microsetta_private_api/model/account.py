from microsetta_private_api.model.model_base import ModelBase
from microsetta_private_api.model.address import Address


class Account(ModelBase):
    @staticmethod
    def from_dict(input_dict):
        result = Account(
            input_dict["id"],
            input_dict['email'],
            "standard",
            "GLOBUS",  # TODO: This is dependent on their login token!
            input_dict['first_name'],
            input_dict['last_name'],
            Address(
                input_dict['address']['street'],
                input_dict['address']['city'],
                input_dict['address']['state'],
                input_dict['address']['post_code'],
                input_dict['address']['country_code'],
            )
        )
        return result

    def __init__(self, account_id, email,
                 account_type, auth_provider,
                 first_name, last_name,
                 address,
                 creation_time=None, update_time=None):
        self.id = account_id
        self.email = email
        self.account_type = account_type
        self.auth_provider = auth_provider
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.creation_time = creation_time
        self.update_time = update_time

    def to_api(self):
        # api users are not given the auth_provider
        return {
            "account_id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "address": self.address,
            "account_type": self.account_type,
            "creation_time": self.creation_time,
            "update_time": self.update_time
        }
