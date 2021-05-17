from microsetta_private_api.celery_utils import celery
from microsetta_private_api.util.email import SendEmail
from microsetta_private_api.model.log_event import EventType, EventSubtype
from microsetta_private_api.admin.email_templates import EmailMessage, \
    BasicEmailMessage
from microsetta_private_api.admin.sample_summary import per_sample
import pandas as pd
import tempfile
import os
import datetime


@celery.task(ignore_result=True)
def send_email(email, template_name, template_args):
    template = EmailMessage[template_name]
    SendEmail.send(email, template, template_args)


@celery.task(ignore_result=True)
def send_basic_email(to_email, subject, template_base_fp, req_template_keys,
                     msg_args, event_type_name, event_subtype_name,
                     from_email=None, **kwargs):
    event_type = EventType[event_type_name]
    event_subtype = EventSubtype[event_subtype_name]
    msg_obj = BasicEmailMessage(subject, template_base_fp, req_template_keys,
                                event_type, event_subtype)
    SendEmail.send(to_email, msg_obj, msg_args, from_email, **kwargs)


@celery.task(ignore_result=True)
def per_sample_summary(email, project, strip_sampleid):
    summaries = per_sample(project, barcodes=None,
                           strip_sampleid=strip_sampleid)
    df = pd.DataFrame(summaries)
    _, path = tempfile.mkstemp()
    df.to_csv(path)
    date = datetime.datetime.now().strftime("%d%b%Y")
    filename = f'project-{project}-summary-{date}.csv'

    # NOTE: we are not using .delay so this action remains
    # within the current celery task
    template_args = {'date': date, 'project': project}
    send_basic_email(email,
                     f"[TMI-summary] Project {project}",
                     'email/sample_summary',
                     list(template_args),
                     template_args,
                     "EMAIL", "EMAIL_PER_PROJECT_SUMMARY",
                     attachment_filepath=path,
                     attachment_filename=filename)
    os.remove(path)
