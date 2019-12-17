class MockJinja:
    r"""
    Simple mock lets you display jinja templates that expect dictionaries
    without having all the necessary keys and values, simultaneously allows
    visual inspection of escaping.

    Items followed by <escaped> are escaped and secure against html injection
    Items not followed by <escaped> are insecure against html injection, but
    allow the inserted item to contain html tags for formatting
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "PUT " + self.name + " <escaped> HERE"

    def __getitem__(self, key):
        return "PUT " + self.name + '["' + key + '"]' + "<escaped> HERE"
