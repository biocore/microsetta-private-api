from microsetta_private_api.model.model_base import ModelBase


class Account(ModelBase):
    def __init__(self, account_id, email,
                 account_type, auth_issuer, auth_sub,
                 first_name, last_name,
                 address,
                 creation_time=None, update_time=None):
        self.id = account_id
        self.email = email
        self.account_type = account_type
        self.auth_issuer = auth_issuer
        self.auth_sub = auth_sub
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.creation_time = creation_time
        self.update_time = update_time

    def to_api(self):
        # api is not given the auth_issuer or auth_sub
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
