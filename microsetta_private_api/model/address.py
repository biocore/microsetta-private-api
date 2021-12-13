from microsetta_private_api.model.model_base import ModelBase


class Address(ModelBase):
    def __init__(self, street, city, state, post_code, country_code,
                 street2=None):
        self.street = street
        self.city = city
        self.state = state
        self.post_code = post_code
        self.country_code = country_code
        self.street2 = street2

    def to_api(self):
        cp = self.__dict__.copy()
        if self.street2 is None:
            cp.pop('street2')
        return cp
