from microsetta_private_api.celery_utils import celery
from microsetta_private_api.util.email import SendEmail
from microsetta_private_api.model.log_event import EventType, EventSubtype
from microsetta_private_api.admin.email_templates import EmailMessage, \
    BasicEmailMessage
import flask_babel
from microsetta_private_api.admin.sample_summary import per_sample
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.repo.qiita_repo import QiitaRepo
# from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.localization import EN_US
from microsetta_private_api.config_manager import SERVER_CONFIG
import pandas as pd
import tempfile
import os
import datetime
import json
import io
import traceback


@celery.task(ignore_result=True)
def send_email(email, template_name, template_args, language):
    template = EmailMessage[template_name]

    with flask_babel.force_locale(language):
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
    with Transaction() as t:
        admin = AdminRepo(t)
        project_name = admin.get_project_name(project)

    summaries = per_sample(project, barcodes=None,
                           strip_sampleid=strip_sampleid)
    df = pd.DataFrame(summaries)
    _, path = tempfile.mkstemp()
    df.to_csv(path)
    date = datetime.datetime.now().strftime("%d%b%Y")
    filename = f'project-{project_name}-summary-{date}.csv'

    # NOTE: we are not using .delay so this action remains
    # within the current celery task
    template_args = {'date': date, 'project': project_name}
    send_basic_email(email,
                     f"[TMI-summary] Project {project}",
                     'email/sample_summary',
                     list(template_args),
                     template_args,
                     "EMAIL", "EMAIL_PER_PROJECT_SUMMARY",
                     attachment_filepath=path,
                     attachment_filename=filename)
    os.remove(path)


@celery.task(ignore_result=True)
def update_qiita_metadata():
    with Transaction() as t:
        qiita = QiitaRepo(t)

        try:
            n_pushed, error = qiita.push_metadata_to_qiita()
        except:  # noqa
            detail = io.StringIO()
            traceback.print_exc(file=detail)
            detail.seek(0)
            error = [{'hardfail': detail.read()}, ]

        if len(error) > 0:
            send_email(SERVER_CONFIG['pester_email'], "pester_daniel",
                       {"what": "qiita metadata push errors",
                        "content": json.dumps(error, indent=2)},
                       EN_US)


# @celery.task(ignore_result=True)
# def geocode_accounts():
#     with Transaction() as t:
#         account_repo = AccountRepo(t)
#         account_repo.geocode_accounts()
#         t.commit()
