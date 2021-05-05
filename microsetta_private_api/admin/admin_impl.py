import uuid
from collections import defaultdict

from flask import jsonify, Response

from microsetta_private_api.config_manager import SERVER_CONFIG
from microsetta_private_api.model.log_event import LogEvent
from microsetta_private_api.model.source import Source
from microsetta_private_api.model.project import Project
from microsetta_private_api.model.daklapack_order import DaklapackOrder, \
    ORDER_ID_KEY, SUBMITTER_ACCT_KEY
from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.activation_repo import ActivationRepo
from microsetta_private_api.repo.event_log_repo import EventLogRepo
from microsetta_private_api.repo.kit_repo import KitRepo
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.repo.source_repo import SourceRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo
from microsetta_private_api.repo.metadata_repo import (retrieve_metadata,
                                                       drop_private_columns)
from microsetta_private_api.tasks import send_email as celery_send_email
from microsetta_private_api.admin.email_templates import EmailMessage
from microsetta_private_api.util.redirects import build_login_redirect
from microsetta_private_api.admin.daklapack_communication import \
    post_daklapack_order, send_daklapack_hold_email
from werkzeug.exceptions import Unauthorized


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


def qiita_compatible_metadata(token_info, include_private, body):
    validate_admin_access(token_info)

    samples = body.get('sample_barcodes')
    if samples is None:
        return jsonify(code=404, message='No samples provided'), 404

    # TODO: this call constructs transactions implicitly. It would be
    # better for the transaction to be established and passed in,
    # similar to how other "repo" objects are managed
    df, errors = retrieve_metadata(samples)

    if errors:
        return jsonify(code=404, message=str(errors)), 404

    if not include_private:
        df = drop_private_columns(df)

    return jsonify(df.to_dict(orient='index')), 200


def token_grants_admin_access(token_info):
    with Transaction() as t:
        account_repo = AccountRepo(t)
        account = account_repo.find_linked_account(token_info['iss'],
                                                   token_info['sub'])
        return account is not None and account.account_type == 'admin'


def validate_admin_access(token_info):
    if not token_grants_admin_access(token_info):
        raise Unauthorized()


def get_projects(token_info, include_stats, is_active=None):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        projects_list = admin_repo.get_projects(include_stats, is_active)
        result = [x.to_api() for x in projects_list]
        return jsonify(result), 200


def create_project(body, token_info):
    validate_admin_access(token_info)

    try:
        project = Project.from_dict(body)
    except ValueError as e:
        raise RepoException(e)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        proj_id = admin_repo.create_project(project)
        t.commit()

    response = Response()
    response.status_code = 201
    response.headers['Location'] = '/api/admin/projects/%s' % (proj_id,)
    return response


def update_project(project_id, body):
    project = Project.from_dict(body)
    with Transaction() as t:
        admin_repo = AdminRepo(t)
        admin_repo.update_project(project_id, project)
        t.commit()

        return '', 204


def create_kits(body, token_info):
    validate_admin_access(token_info)

    number_of_kits = body['number_of_kits']
    number_of_samples = body['number_of_samples']
    kit_prefix = body.get('kit_id_prefix', None)
    project_ids = body['project_ids']

    with Transaction() as t:
        admin_repo = AdminRepo(t)

        try:
            kits = admin_repo.create_kits(number_of_kits, number_of_samples,
                                          kit_prefix, project_ids)
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
        activation_code = None

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
            account_id = None
            email = None
            contact_name = None
            if diag["account"] is not None:
                account_id = diag["account"].id
                email = diag["account"].email
                contact_name = diag["account"].first_name + " " + \
                    diag["account"].last_name
                contact_name = contact_name.strip()

            source_id = None
            if diag["source"] is not None:
                source_id = diag["source"].id

            sample_id = None
            if diag["sample"] is not None:
                sample_id = diag["sample"].id
            endpoint = SERVER_CONFIG["endpoint"]

            if sample_id is not None and \
               source_id is not None and \
               account_id is not None:
                resolution_url = build_login_redirect(
                    endpoint + "/accounts/%s/sources/%s/samples/%s" %
                    (account_id, source_id, sample_id)
                )
            elif account_id is not None and source_id is not None:
                resolution_url = build_login_redirect(
                    endpoint + "/accounts/%s/sources/%s" %
                    (account_id, source_id)
                )
            elif account_id is not None:
                resolution_url = build_login_redirect(
                    endpoint + "/accounts/%s" % (account_id,)
                )
            else:
                resolution_url = build_login_redirect(
                    endpoint + "/"
                )
        elif body["issue_type"] == "activation":
            # If we are sending activation emails, we won't have
            # anything in our database- no account id, no contact name
            # no known email.  All we actually can do is read out the email
            # and append an activation code to the set of arguments
            if body["template"] == EmailMessage.send_activation_code.name:
                email = body['template_args']['new_account_email']
                activations = ActivationRepo(t)
                activation_code = activations.get_activation_code(email)
            else:
                raise Exception("Support more activation subtypes")
        else:
            raise Exception("Update Admin Impl to support more issue types")

        # Determine what template must be sent, and build the template args
        # from whatever is in the body and the resolution url we determined
        template_name = body['template']
        template = EmailMessage[template_name]

        template_args = dict(body['template_args'])
        if resolution_url is not None:
            template_args['resolution_url'] = resolution_url
        if contact_name is not None:
            template_args['contact_name'] = contact_name
        if activation_code is not None:
            template_args['new_account_code'] = activation_code
        celery_send_email.apply_async(args=[email, template_name,
                                            template_args])

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


def get_daklapack_articles(token_info):
    validate_admin_access(token_info)

    with Transaction() as t:
        admin_repo = AdminRepo(t)
        dak_article_dicts = admin_repo.get_daklapack_articles()
        return jsonify(dak_article_dicts), 200


def query_email_stats(body, token_info):
    validate_admin_access(token_info)

    email_list = body.get("emails", [])
    project = body.get("project")

    results = []
    with Transaction() as t:
        account_repo = AccountRepo(t)
        kit_repo = KitRepo(t)
        source_repo = SourceRepo(t)
        sample_repo = SampleRepo(t)

        for email in email_list:
            result = {'email': email, 'project': project}
            results.append(result)
            # can use internal lookup by email, because we have admin access
            account = account_repo._find_account_by_email(email)  # noqa
            if account is None:
                result['summary'] = "No Account"
                continue
            else:
                result['account_id'] = account.id
                result['creation_time'] = account.creation_time
                result['kit_name'] = account.created_with_kit_id

            if account.created_with_kit_id is not None:
                unused = kit_repo.get_kit_unused_samples(
                             account.created_with_kit_id
                         )
                if unused is None:
                    result['unclaimed-samples-in-kit'] = 0
                else:
                    result['unclaimed-samples-in-kit'] = len(unused.samples)

            sample_statuses = defaultdict(int)
            sources = source_repo.get_sources_in_account(account.id)

            samples_in_project = 0
            for source in sources:
                samples = sample_repo.get_samples_by_source(account.id,
                                                            source.id)
                for sample in samples:
                    if project is not None and \
                       project != "" and \
                       project not in sample.sample_projects:
                        continue
                    samples_in_project += 1
                    sample_status = sample_repo.get_sample_status(
                        sample.barcode,
                        sample._latest_scan_timestamp  # noqa
                    )
                    if sample_status is None:
                        sample_status = "never-scanned"
                    sample_statuses[sample_status] += 1
            result.update(sample_statuses)

            if result.get('unclaimed-samples-in-kit', 0) > 0:
                result['summary'] = 'Possible Unreturned Samples'
            elif samples_in_project == 0:
                result['summary'] = "No Samples In Specified Project"
            elif result.get('sample-is-valid') == samples_in_project:
                result['summary'] = 'All Samples Valid'
            else:
                result['summary'] = 'May Require User Interaction'

    return jsonify(results), 200


def query_barcode_stats(body, token_info):
    validate_admin_access(token_info)

    barcodes = body.get("sample_barcodes")
    project = body["project"]

    summaries = []
    with Transaction() as t:
        admin_repo = AdminRepo(t)
        sample_repo = SampleRepo(t)
        template_repo = SurveyTemplateRepo(t)

        project_barcodes = admin_repo.get_project_barcodes(project)

        if barcodes is None:
            barcodes = project_barcodes
        else:
            barcodes = [b for b in barcodes if b in set(project_barcodes)]
            not_found = [b for b in barcodes if b not in set(project_barcodes)]
            if len(not_found) > 0:
                nf = ", ".join(not_found)
                message = f"The following barcodes were not found: '[{nf}]'"
                return jsonify(code=404, message=message), 404

        for barcode in barcodes:
            diag = admin_repo.retrieve_diagnostics_by_barcode(barcode)
            sample = diag['sample']
            account = diag['account']
            source = diag['source']

            account_email = None if account is None else account.email
            source_email = None
            source_type = None if source is None else source.source_type
            vio_id = None

            if source is not None and source_type is Source.SOURCE_TYPE_HUMAN:
                source_email = source.email

                vio_id = template_repo.get_vioscreen_id_if_exists(account.id,
                                                                  source.id,
                                                                  sample.id)

            sample_status = sample_repo.get_sample_status(
                sample.barcode,
                sample._latest_scan_timestamp  # noqa
            )

            summary = {
                "sampleid": barcode,
                "project": project,
                "source-type": source_type,
                "site-sampled": sample.site,
                "source-email": source_email,
                "account-email": account_email,
                "vioscreen_username": vio_id,

                # NOTE: we *do not* have accurate visibility on these statuses
                # yet so they are assumed false. This support is coming in
                # a separate pull request
                "ffq-taken": False,
                "ffq-complete": False,
                "sample-status": sample_status,
                "sample-received": sample_status is not None
            }

            for status in ["sample-is-valid",
                           "no-associated-source",
                           "no-registered-account",
                           "no-collection-info",
                           "sample-has-inconsistencies",
                           "received-unknown-validity"]:
                summary[status] = sample_status == status

            summaries.append(summary)

    return jsonify(summaries), 200


def create_daklapack_order(body, token_info):
    validate_admin_access(token_info)

    body = body.copy()
    body[ORDER_ID_KEY] = str(uuid.uuid4())

    with Transaction() as t:
        account_repo = AccountRepo(t)
        body[SUBMITTER_ACCT_KEY] = account_repo.find_linked_account(
            token_info['iss'], token_info['sub'])

        try:
            daklapack_order = DaklapackOrder.from_api(**body)
        except ValueError as e:
            raise RepoException(e)

        post_response = post_daklapack_order(daklapack_order.order_structure)
        if post_response.status_code >= 400:
            # for now, very basic error handling--just pass on dak api error
            response_msg = {"daklapack_api_error_msg": post_response.text}
            response = jsonify(response_msg)
            response.status_code = post_response.status_code
            return response

        # IFF submission is successful AND has fulfillment hold msg,
        # email hold fulfillment info and the order id to Daklapack contact
        email_success = None
        if daklapack_order.fulfillment_hold_msg:
            email_success = send_daklapack_hold_email(daklapack_order)
            # if couldn't send the fulfillment hold message for any reason,
            # still DO save order to db bc it WAS sent to Daklapack, but also
            # record the email failure to the db and return info to caller
            if not email_success:
                daklapack_order.set_last_polling_info(
                    "fulfillment hold message not sent")

        # write order to db
        admin_repo = AdminRepo(t)
        order_id = admin_repo.create_daklapack_order(daklapack_order)
        t.commit()

    # return response to caller
    response_msg = {"order_id": order_id, "email_success": email_success}
    response = jsonify(response_msg)
    response.status_code = 201
    # TODO: AB: Add this endpoint as part of support for polling dak orders
    response.headers['Location'] = f'/api/admin/daklapack_orders/{order_id}'
    return response


def search_activation(token_info, email_query=None, code_query=None):
    validate_admin_access(token_info)
    with Transaction() as t:
        activations = ActivationRepo(t)
        if email_query is not None:
            infos = activations.search_email(email_query)
        elif code_query is not None:
            infos = activations.search_code(code_query)
        else:
            raise Exception("Must specify an 'email_query' or 'code_query'")

        return jsonify([i.to_api() for i in infos]), 200


def generate_activation_codes(body, token_info):
    validate_admin_access(token_info)

    email_list = body.get("emails", [])
    with Transaction() as t:
        activations = ActivationRepo(t)
        map = activations.get_activation_codes(email_list)
        results = [{"email": email, "code": map[email]} for email in map]
        t.commit()
    return jsonify(results), 200
