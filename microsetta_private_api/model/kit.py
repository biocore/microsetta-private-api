from microsetta_private_api.model.model_base import ModelBase


class Kit(ModelBase):
    def __init__(self, kit_id, samples):
        self.id = kit_id
        self.samples = samples

    def to_api(self):
        # Notice: read_kit requires an array of the unused samples -
        # ensure you have pulled the kit from the database correctly.
        if self.samples is None:
            return []
        else:
            return [s.to_api() for s in self.samples]
