from datetime import datetime
from microsetta_private_api.model.model_base import ModelBase


class Sample(ModelBase):
    def __init__(self, sample_id, datetime_collected, site, notes, barcode,
                 scan_date):
        self.id = sample_id
        # NB: datetime_collected may be None if sample not yet used
        self.datetime_collected = datetime_collected
        self.barcode = barcode
        # NB: notes may be None
        self.notes = notes
        # NB: site may be None if sample not yet used
        self.site = site
        # NB: _scan_date may be None if sample not yet returned to lab
        self._scan_date = scan_date

    @property
    def is_locked(self):
        # If a sample has been scanned into the system, that means its
        # attributes can't be changed
        return self._scan_date is not None

    @classmethod
    def load_from_db_record(cls, sample_id, date_collected, time_collected,
                            site, notes, barcode, scan_date):
        datetime_collected = None
        # NB a sample may NOT have date and time collected if it has been sent
        # out but not yet used
        if date_collected is not None and time_collected is not None:
            datetime_collected = datetime.combine(date_collected,
                                                  time_collected)
        return cls(sample_id, datetime_collected, site, notes, barcode,
                   scan_date)

    def to_api(self):
        return {
            "sample_barcode": self.barcode,
            "sample_site": self.site,
            "sample_locked": self.is_locked(),
            "sample_datetime": self.datetime_collected,
            "sample_notes": self.notes,
            "sample_projects": None  # TODO: Where is this info?
        }
