from microsetta_private_api.celery_utils import celery
from microsetta_private_api.util.email import SendEmail
from microsetta_private_api.model.log_event import EventType, EventSubtype
from microsetta_private_api.admin.email_templates import EmailMessage, \
    BasicEmailMessage
import flask_babel


@celery.task(ignore_result=True)
def send_email(email, template_name, template_args, language):
    template = EmailMessage[template_name]

    with flask_babel.force_locale(language):
        SendEmail.send(email, template, template_args)


@celery.task(ignore_result=True)
def send_basic_email(to_email, subject, template_base_fp, req_template_keys,
                     msg_args, event_type_name, event_subtype_name,
                     from_email=None):
    event_type = EventType[event_type_name]
    event_subtype = EventSubtype[event_subtype_name]
    msg_obj = BasicEmailMessage(subject, template_base_fp, req_template_keys,
                                event_type, event_subtype)
    SendEmail.send(to_email, msg_obj, msg_args, from_email)
