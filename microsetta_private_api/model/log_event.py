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

    # The welcome to microsetta email containing an email and
    # code to send to the new user for signup
    EMAIL_ACTIVATION = "send_activation_code"
    # indicate a sample was received, and is good, but is being banked
    EMAIL_SAMPLE_RECEIVED_BANKED = "sample_received_banked"
    # indicate a sample was received, is good, and is being plated
    EMAIL_SAMPLE_RECEIVED_PLATED = "sample_received_plated"
    # indicate a previously banked sample is now being plated
    EMAIL_BANKED_SAMPLE_NOW_PLATED = "banked_sample_plated"
    # Indicate a sample was received but doesn't match the information provided
    EMAIL_INCORRECT_SAMPLE_TYPE = "incorrect_sample_type"
    # Indicate a sample was received but necessary information was not provided
    EMAIL_MISSING_SAMPLE_INFO = "missing_sample_info"
    # A valid sample was received
    EMAIL_SAMPLE_IS_VALID = "sample_is_valid"
    # Sample is not associated with a source
    EMAIL_NO_SOURCE = "no_associated_source"
    # Fulfillment of a daklapack order must be held
    DAK_ORDER_HOLD = "daklapack_order_hold"
    # Daklapack order polling idenfitied orders with errors
    DAK_ORDER_ERRORS_REPORT = "daklapack_orders_error_report"
    # Daklapack polling encountered code errors
    DAK_POLLING_ERRORS_REPORT = "daklapack_polling_errors_report"
    # Pester daniel if for what are expected to be unusual situations
    PESTER_DANIEL = "pester_daniel"
    # for project per-sample summaries
    EMAIL_PER_PROJECT_SUMMARY = "per_project_summary"
    # for addresses that Melissa deems invalid
    EMAIL_ADDRESS_INVALID = "address_invalid"


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
