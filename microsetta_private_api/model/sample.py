from datetime import datetime
from microsetta_private_api.model.model_base import ModelBase


class Sample(ModelBase):
    def __init__(self, sample_id, datetime_collected, site, notes, barcode,
                 latest_scan_timestamp, source_id, account_id,
                 sample_projects, latest_scan_status):
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
        self._latest_scan_status = latest_scan_status
        self.sample_projects = sample_projects

        self.source_id = source_id
        self.account_id = account_id

        self.accession_urls = []

    def set_accession_urls(self, accession_urls):
        self.accession_urls = accession_urls

    @property
    def edit_locked(self):
        # If a sample has been scanned and is valid, it is locked.
        return self._latest_scan_timestamp is not None and \
               self._latest_scan_status == "sample-is-valid"

    @property
    def remove_locked(self):
        # If a sample has been scanned (even if invalid), it cannot be removed
        # from a source.
        return self._latest_scan_timestamp is not None

    @classmethod
    def from_db(cls, sample_id, date_collected, time_collected,
                site, notes, barcode, latest_scan_timestamp,
                source_id, account_id, sample_projects, latest_scan_status):
        datetime_collected = None
        # NB a sample may NOT have date and time collected if it has been sent
        # out but not yet used
        if date_collected is not None and time_collected is not None:
            datetime_collected = datetime.combine(date_collected,
                                                  time_collected)
        return cls(sample_id, datetime_collected, site, notes, barcode,
                   latest_scan_timestamp, source_id,
                   account_id, sample_projects, latest_scan_status)

    def to_api(self):
        return {
            "sample_id": self.id,
            "sample_barcode": self.barcode,
            "sample_site": self.site,
            "sample_edit_locked": self.edit_locked,
            "sample_remove_locked": self.remove_locked,
            "sample_datetime": self.datetime_collected,
            "sample_notes": self.notes,
            "source_id": self.source_id,
            "account_id": self.account_id,
            "sample_projects": list(self.sample_projects),
            "accession_urls": self.accession_urls
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
