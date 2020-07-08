from enum import Enum
from flask import render_template
from werkzeug.exceptions import BadRequest
from microsetta_private_api.model.log_event import EventType, EventSubtype


class EmailTemplate:
    def __init__(self, filepath, required):
        self.filepath = filepath
        self.required = required

    def render(self, template_args):
        for key in self.required:
            if key not in template_args:
                raise BadRequest("Missing Required Argument: " + str(key))
        return render_template(self.filepath, **template_args)


class EmailMessage(Enum):
    incorrect_sample_type = (
        "Incorrect Sample Type",
        "email/incorrect_sample_type.jinja2",
        "email/incorrect_sample_type.plain",
        ("username", "sample_barcode", "recorded_type", "received_type",
         "resolution_url"),
        EventType.EMAIL,
        EventSubtype.EMAIL_INCORRECT_SAMPLE_TYPE
    )
    missing_sample_info = (
        "Missing Sample Info",
        "email/missing_sample_info.jinja2",
        "email/missing_sample_info.plain",
        ("username", "sample_barcode", "received_type", "resolution_url"),
        EventType.EMAIL,
        EventSubtype.EMAIL_MISSING_SAMPLE_INFO
    )

    def __init__(self, subject, html, plain, required, event_type, event_sub):
        self.subject = subject
        self.html = EmailTemplate(html, required)
        self.plain = EmailTemplate(plain, required)
        self.event_type = event_type
        self.event_subtype = event_sub
