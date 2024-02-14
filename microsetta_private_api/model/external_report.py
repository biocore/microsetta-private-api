from microsetta_private_api.model.model_base import ModelBase


class ExternalReport(ModelBase):
    def __init__(self, **kwargs):
        self.external_report_id = kwargs['external_report_id']
        self.source_id = kwargs['source_id']
        self.report_type = kwargs['report_type']
        self.file_name = kwargs['file_name']
        self.file_title = kwargs['file_title']
        self.file_type = kwargs['file_type']
        self.file_contents = kwargs['file_contents']

    def to_api(self):
        return self.__dict__.copy()

    @classmethod
    def from_dict(cls, values_dict):
        return cls(**values_dict)
