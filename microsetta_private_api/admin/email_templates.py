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
        "Your Microsetta Initiative status update: attention needed",
        "email/incorrect_sample_type.jinja2",
        "email/incorrect_sample_type.plain",
        ("contact_name", "sample_barcode", "recorded_type", "received_type",
         "resolution_url"),
        EventType.EMAIL,
        EventSubtype.EMAIL_INCORRECT_SAMPLE_TYPE
    )
    missing_sample_info = (
        "Your Microsetta Initiative status update: information needed",
        "email/missing_sample_info.jinja2",
        "email/missing_sample_info.plain",
        ("contact_name", "sample_barcode", "received_type", "resolution_url"),
        EventType.EMAIL,
        EventSubtype.EMAIL_MISSING_SAMPLE_INFO
    )
    sample_is_valid = (
        "Your Microsetta Initiative status update and next steps",
        "email/sample_is_valid.jinja2",
        "email/sample_is_valid.plain",
        ("contact_name",),
        EventType.EMAIL,
        EventSubtype.EMAIL_SAMPLE_IS_VALID
    )
    no_associated_source = (
        ("Your Microsetta Initiative status update: "
         "critical information needed"),
        "email/no_associated_source.jinja2",
        "email/no_associated_source.plain",
        ("contact_name", "sample_barcode", "resolution_url"),
        EventType.EMAIL,
        EventSubtype.EMAIL_NO_SOURCE
    )

    def __init__(self, subject, html, plain, required, event_type, event_sub):
        self.subject = subject
        self.html = EmailTemplate(html, required)
        self.plain = EmailTemplate(plain, required)
        self.event_type = event_type
        self.event_subtype = event_sub


class BasicEmailMessage:
    def __init__(self, subject, template_base_fp, req_template_keys,
                 event_type, event_sub):
        self.subject = subject
        self.html = EmailTemplate(f"{template_base_fp}.jinja2",
                                  req_template_keys)
        self.plain = EmailTemplate(f"{template_base_fp}.plain",
                                   req_template_keys)
        self.event_type = event_type
        self.event_subtype = event_sub
