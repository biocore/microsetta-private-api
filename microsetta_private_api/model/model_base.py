class ModelBase:
    def to_api(self):
        """ Converts a model object to a dictionary matching the yaml spec """
        raise NotImplementedError

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
