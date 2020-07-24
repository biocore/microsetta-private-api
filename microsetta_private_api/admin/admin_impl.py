import uuid
from flask import jsonify
import datetime

from microsetta_private_api.admin.email_templates import EmailMessage
from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.model.log_event import LogEvent
from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.event_log_repo import EventLogRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.util.email import SendEmail
from microsetta_private_api.util.redirects import build_login_redirect
from werkzeug.exceptions import Unauthorized, BadRequest


def search_barcode(token_info, sample_barcode):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        diag = admin_repo.retrieve_diagnostics_by_barcode(sample_barcode)
        if diag is None:
            return jsonify(code=404, message="Barcode not found"), 404
        return jsonify(diag), 200


def search_kit_id(token_info, kit_id):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        diag = admin_repo.retrieve_diagnostics_by_kit_id(kit_id)
        if diag is None:
            return jsonify(code=404, message="Kit ID not found"), 404
        return jsonify(diag), 200


def search_email(token_info, email):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        diag = admin_repo.retrieve_diagnostics_by_email(email)
        if diag is None:
            return jsonify(code=404, message="Email not found"), 404
        return jsonify(diag), 200


def scan_barcode(token_info, sample_barcode, body):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        scan_id = admin_repo.scan_barcode(sample_barcode, body)
        t.commit()

    response = jsonify({"scan_id": scan_id})
    response.status_code = 201
    response.headers['Location'] = '/api/admin/search/samples/%s' % \
                                   sample_barcode
    return response


def sample_pulldown_single_survey(token_info,
                                  sample_barcode,
                                  survey_template_id):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        sample_pulldown = admin_repo.get_survey_metadata(
            sample_barcode,
            survey_template_id=survey_template_id)
    return jsonify(sample_pulldown), 200


def sample_pulldown_multiple_survey(token_info,
                                    sample_barcode):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        sample_pulldown = admin_repo.get_survey_metadata(sample_barcode)
    return jsonify(sample_pulldown), 200


def project_statistics_summary(token_info):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        summary = admin_repo.get_project_summary_statistics()
        return jsonify(summary), 200


def project_statistics_detailed(token_info, project_id):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        summary = admin_repo.get_project_detailed_statistics(project_id)
        return jsonify(summary), 200


def token_grants_admin_access(token_info):
    with Transaction() as t:
        account_repo = AccountRepo(t)
        account = account_repo.find_linked_account(token_info['iss'],
                                                   token_info['sub'])
        return account is not None and account.account_type == 'admin'


def validate_admin_access(token_info):
    if not token_grants_admin_access(token_info):
        raise Unauthorized()


def create_project(body, token_info):
    validate_admin_access(token_info)

    project_name = body['project_name']
    is_microsetta = body['is_microsetta']
    bank_samples = body['bank_samples']
    plating_start_date = body.get('plating_start_date')

    if plating_start_date is not None:
        try:
            plating_start_date = datetime.datetime.strptime(
                plating_start_date, "%Y-%m-%d")
        except ValueError:
            raise BadRequest(
                "plating start date '{0}' is not a valid date in YYYY-MM-DD "
                "format".format(plating_start_date))

    if len(project_name) == 0:
        return jsonify(code=400, message="No project name provided"), 400

    if not bank_samples and plating_start_date is not None:
        raise RepoException("Plating start date cannot be set for"
                            " unbanked projects")

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        admin_repo.create_project(project_name, is_microsetta, bank_samples,
                                  plating_start_date)
        t.commit()

    return {}, 201


def create_kits(body, token_info):
    validate_admin_access(token_info)

    number_of_kits = body['number_of_kits']
    number_of_samples = body['number_of_samples']
    kit_prefix = body.get('kit_id_prefix', None)
    projects = body['projects']

    with Transaction() as t:
        admin_repo = AdminRepo(t)

        try:
            kits = admin_repo.create_kits(number_of_kits, number_of_samples,
                                          kit_prefix, projects)
        except KeyError:
            return jsonify(code=422, message="Unable to create kits"), 422
        else:
            t.commit()

    return jsonify(kits), 201


def get_account_events(account_id, token_info):
    validate_admin_access(token_info)

    with Transaction() as t:
        events = EventLogRepo(t).get_events_by_account(account_id)
        return jsonify([x.to_api() for x in events]), 200


def send_email(body, token_info):
    validate_admin_access(token_info)

    with Transaction() as t:
        account_id = None
        email = None
        resolution_url = None
        contact_name = None

        # Depending on issue type, determine what email to send to and
        # what account is involved, as well as what link to send user to
        # address the problem if that is required by the email template
        if body["issue_type"] == "sample":
            # TODO:  Building resolution url is very tricky, and it's not clear
            #  what component should be responsible for doing it.  It requires
            #  knowing what endpoint the client minimal interface is hosted at,
            #  as well as a sample barcode's associated
            #       account_id,
            #       source_id,
            #       sample_id
            #  which generally requires lookup in the db with admin privilege.

            diag = AdminRepo(t).retrieve_diagnostics_by_barcode(
                       body["template_args"]["sample_barcode"],
                       grab_kit=False)
            account_id = diag["account"].id
            source_id = diag["source"].id
            sample_id = diag["sample"].id
            email = diag["account"].email
            contact_name = diag["account"].first_name + " " + \
                diag["account"].last_name
            contact_name = contact_name.strip()
            endpoint = SERVER_CONFIG["endpoint"]
            resolution_url = build_login_redirect(
                endpoint + "/accounts/%s/sources/%s/samples/%s" %
                (account_id, source_id, sample_id)
            )
        else:
            raise Exception("Update Admin Impl to support more issue types")

        # Determine what template must be sent, and build the template args
        # from whatever is in the body and the resolution url we determined
        template = EmailMessage[body['template']]
        template_args = dict(body['template_args'])
        template_args['resolution_url'] = resolution_url
        template_args['contact_name'] = contact_name

        # Send the email
        SendEmail.send(email, template, template_args)

        # Add an event to the log that we sent this email successfully
        event = LogEvent(
            uuid.uuid4(),
            template.event_type,
            template.event_subtype,
            None,
            {
                # account_id and email are necessary to allow searching the
                # event log.
                "account_id": account_id,
                "email": email,
                "template": body["template"],
                "template_args": body["template_args"]
            })
        EventLogRepo(t).add_event(event)

        t.commit()

    return '', 204
