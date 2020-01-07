from microsetta_private_api.model.model_base import ModelBase


class Address(ModelBase):
    def __init__(self, street, city, state, post_code, country_code):
        self.street = street
        self.city = city
        self.state = state
        self.post_code = post_code
        self.country_code = country_code

    def to_api(self):
        return self.__dict__.copy()
