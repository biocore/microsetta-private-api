from microsetta_private_api.model.model_base import ModelBase


class Kit(ModelBase):
    def __init__(self, kit_id, samples):
        self.id = kit_id
        self.samples = samples

    def to_api(self):
        # API requires an array of the unused samples
        # TODO: Null sample site may just be an approximation of unused,
        #  what should we use as the exact policy here?
        return [s.to_api() for s in self.samples if s.site is None]
