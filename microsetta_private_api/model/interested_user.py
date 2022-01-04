from microsetta_private_api.model.model_base import ModelBase


class InterestedUser(ModelBase):
    def __init__(self, **kwargs):
        # interested_user_id won't exist yet on incoming new users
        self.interested_user_id = kwargs.get('interested_user_id')

        # absolute minimum fields required for an interested user
        self.campaign_id = kwargs['campaign_id']
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
        self.email = kwargs['email']

        # remaining fields are either optional or auto-created later
        self.acquisition_source = kwargs.get('acquisition_source')
        self.phone = kwargs.get('phone')
        self.address_1 = kwargs.get('address_1')
        self.address_2 = kwargs.get('address_2')
        self.city = kwargs.get('city')
        self.state = kwargs.get('state')
        self.postal_code = kwargs.get('postal_code')
        self.country = kwargs.get('country')
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')
        self.confirm_consent = kwargs.get('confirm_consent', False)
        self.ip_address = kwargs.get('ip_address')
        self.creation_timestamp = kwargs.get('creation_timestamp')
        self.update_timestamp = kwargs.get('update_timestamp')
        self.address_checked = kwargs.get('address_checked', False)
        self.address_valid = kwargs.get('address_valid', False)
        self.converted_to_account = kwargs.get('converted_to_account', False)
        self.converted_to_account_timestamp = \
            kwargs.get('converted_to_account_timestamp')
        self.over_18 = kwargs.get('over_18', False)

    def to_api(self):
        return self.__dict__.copy()

    @classmethod
    def from_dict(cls, values_dict):
        return cls(**values_dict)
