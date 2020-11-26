from microsetta_private_api.model.model_base import ModelBase


# A particular sample (indicated by its barcode), can be examined multiple
# times.  This involves preparing the sample in a particular way
# (16S or shotgun...), then running the prepared sample through the sequencer.
# This object indicates a preparation that a sample has gone through, and the
# results of sequencing that prep.
class Preparation(ModelBase):
    def __init__(self,
                 barcode,
                 preparation_id,
                 preparation_type,
                 num_sequences):
        self.barcode = barcode
        self.preparation_id = preparation_id
        self.preparation_type = preparation_type
        self.num_sequences = num_sequences

    def to_api(self):
        return self.__dict__.copy()
