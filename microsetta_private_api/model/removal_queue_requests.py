from microsetta_private_api.model.model_base import ModelBase


class RemovalQueueRequest(ModelBase):
    def __init__(self, id, account_id, email, first_name, last_name,
                 requested_on, user_delete_reason):
        self.id = id
        self.account_id = account_id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

        # 2022-07-27 17:15:33.937458-07:00 -> 2022-07-27 17:15:33
        self.requested_on = str(requested_on).split('.')[0]
        self.user_delete_reason = user_delete_reason

    def to_api(self):
        return self.__dict__.copy()
