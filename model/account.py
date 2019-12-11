class Account:
    def __init__(self, account_id, email, auth_provider,
                 first_name, last_name, address):
        self.id = account_id
        self.email = email
        self.auth_provider = auth_provider
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
