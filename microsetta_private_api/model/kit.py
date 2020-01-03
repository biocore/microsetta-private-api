from microsetta_private_api.model.model_base import ModelBase


class Kit(ModelBase):
    def __init__(self, kit_id, samples):
        self.id = kit_id
        self.samples = samples

    def to_api(self):
        # API requires an array of the unused samples
        unused = []
        for s in self.samples:
            if not s.deposited:
                unused.append(s.to_api())
        return unused
