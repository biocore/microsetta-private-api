from microsetta_private_api.model.model_base import ModelBase


class Subscription(ModelBase):
    def __init__(self, **kwargs):
        # subscription_id won't exist yet on new subscriptions
        self.subscription_id = kwargs.get('subscription_id')

        # absolute minimum fields required for a subscription
        self.transaction_id = kwargs['transaction_id']

        # remaining fields are either optional or auto-created later
        self.account_id = kwargs.get('account_id')
        self.cancelled = kwargs.get('cancelled', False)

    def to_api(self):
        return self.__dict__.copy()

    @classmethod
    def from_dict(cls, values_dict):
        return cls(**values_dict)
