class ModelBase:
    def to_api(self):
        """ Converts a model object to a dictionary matching the yaml spec """
        raise NotImplementedError
