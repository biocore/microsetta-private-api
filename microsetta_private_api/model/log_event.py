import datetime
import uuid

from microsetta_private_api.model.model_base import ModelBase
from enum import Enum, unique

# NOTE: The string values of these enums are persisted to the database
#  therefore. They MUST NOT BE CHANGED.
@unique
class EventType(Enum):
    # The event type indicating an email was sent to an end user
    EMAIL = "email"


@unique
class EventSubtype(Enum):
    # Email event subtypes refer to the various email templates we can send out

    # indicate a sample was received, and is good, but is being banked
    EMAIL_SAMPLE_RECEIVED_BANKED = "sample_received_banked"
    # indicate a sample was received, is good, and is being plated
    EMAIL_SAMPLE_RECEIVED_PLATED = "sample_received_plated"
    # indicate a previously banked sample is now being plated
    EMAIL_BANKED_SAMPLE_NOW_PLATED = "banked_sample_plated"
    # indicate if there is a problem with a sample
    # (messaging should be tailored to the problem)
    EMAIL_SAMPLE_RECEIVED_WITH_PROBLEMS = "sample_received_with_problems"


class LogEvent(ModelBase):
    def __init__(self,
                 event_id: uuid.UUID,
                 event_type: EventType,
                 event_subtype: EventSubtype,
                 event_time: datetime,
                 event_state: dict):
        self.event_id = event_id
        self.event_type = event_type
        self.event_subtype = event_subtype
        self.event_time = event_time
        self.event_state = event_state

    def to_api(self):
        return {
            "event_id": str(self.event_id),
            "event_type": self.event_type.value,
            "event_subtype": self.event_subtype.value,
            "event_time": self.event_time,
            "event_state": self.event_state
        }
