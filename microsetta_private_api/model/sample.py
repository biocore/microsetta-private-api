from datetime import datetime
from microsetta_private_api.model.model_base import ModelBase


class Sample(ModelBase):
    def __init__(self, sample_id, datetime_collected, site, notes, barcode,
                 latest_scan_timestamp, sample_projects):
        self.id = sample_id
        # NB: datetime_collected may be None if sample not yet used
        self.datetime_collected = datetime_collected
        self.barcode = barcode
        # NB: notes may be None
        self.notes = notes
        # NB: site may be None if sample not yet used
        self.site = site
        # NB: _latest_scan_timestamp may be None if not yet returned to lab
        self._latest_scan_timestamp = latest_scan_timestamp
        self.sample_projects = sample_projects

    @property
    def is_locked(self):
        # If a sample has been scanned into the system, that means its
        # attributes can't be changed
        return self._latest_scan_timestamp is not None

    @classmethod
    def from_db(cls, sample_id, date_collected, time_collected,
                site, notes, barcode, latest_scan_timestamp, sample_projects):
        datetime_collected = None
        # NB a sample may NOT have date and time collected if it has been sent
        # out but not yet used
        if date_collected is not None and time_collected is not None:
            datetime_collected = datetime.combine(date_collected,
                                                  time_collected)
        return cls(sample_id, datetime_collected, site, notes, barcode,
                   latest_scan_timestamp, sample_projects)

    def to_api(self):
        return {
            "sample_id": self.id,
            "sample_barcode": self.barcode,
            "sample_site": self.site,
            "sample_locked": self.is_locked,
            "sample_datetime": self.datetime_collected,
            "sample_notes": self.notes,
            "sample_projects": list(self.sample_projects)
        }


# A SampleInfo represents the set of end user editable fields whose lifetime
# matches that of the association between a sample and a source
class SampleInfo:
    def __init__(self, sample_id, datetime_collected, site, notes):
        self.id = sample_id
        # NB: datetime_collected may be None if sample not yet used
        self.datetime_collected = datetime_collected
        # NB: notes may be None
        self.notes = notes
        # NB: site may be None if sample not yet used
        self.site = site
