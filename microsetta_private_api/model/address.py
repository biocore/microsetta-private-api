from microsetta_private_api.model.model_base import ModelBase


class Address(ModelBase):
    def __init__(self, street, city, state, postcode, country_code):
        self.street = street
        self.city = city,
        self.state = state,
        self.postcode = postcode
        self.country_code = country_code

    def to_api(self):
        return {
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "postcode": self.postcode,
            "country_code": self.country_code
        }
