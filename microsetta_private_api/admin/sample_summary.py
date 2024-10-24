from microsetta_private_api.model.source import Source
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo
from werkzeug.exceptions import NotFound


def get_barcodes_by_project_id(project_id):
    with Transaction() as t:
        return AdminRepo(t).get_project_barcodes(project_id)


def get_barcodes_by_kit_ids(kit_ids):
    with Transaction() as t:
        return AdminRepo(t).get_barcodes_filter(kit_ids=kit_ids)


def get_barcodes_by_emails(emails):
    with Transaction() as t:
        return AdminRepo(t).get_barcodes_filter(emails=emails)


def get_barcodes_by_outbound_tracking_numbers(outbound_tracking_numbers):
    with Transaction() as t:
        return AdminRepo(t).get_barcodes_filter(
            outbound_tracking_numbers=outbound_tracking_numbers)


def get_barcodes_by_inbound_tracking_numbers(inbound_tracking_numbers):
    with Transaction() as t:
        return AdminRepo(t).get_barcodes_filter(
            inbound_tracking_numbers=inbound_tracking_numbers)


def per_sample(project, barcodes, strip_sampleid):
    summaries = []
    with Transaction() as t:
        admin_repo = AdminRepo(t)
        sample_repo = SampleRepo(t)
        template_repo = SurveyTemplateRepo(t)

        # all associated projects returned for each barcode,
        # so no universal project needed
        if barcodes is None:
            if project is None:
                return summaries
            barcodes = admin_repo.get_project_barcodes(project)

        for barcode in barcodes:
            diag = admin_repo.retrieve_diagnostics_by_barcode(barcode)
            if diag is None:
                raise NotFound(f"Barcode not found: {barcode}")

            sample = diag['sample']
            account = diag['account']
            source = diag['source']
            first_scans_info = diag['scans_info']
            last_scans_info = diag['latest_scan']
            if first_scans_info:
                first_scan_timestamp = first_scans_info[0]['scan_timestamp']
                first_scan_status = first_scans_info[0]['sample_status']
            else:
                first_scan_timestamp = None
                first_scan_status = None
            if last_scans_info:
                latest_scan_timestamp = last_scans_info['scan_timestamp']
                latest_scan_status = last_scans_info['sample_status']
            else:
                latest_scan_timestamp = None
                latest_scan_status = None

            account_email = None if account is None else account.email
            source_type = None if source is None else source.source_type
            vio_id = None

            # find all projects for barcode
            projects_info = diag['projects_info']
            all_projects = [proj_obj['project'] for proj_obj in projects_info]
            barcode_project = '; '.join(sorted(all_projects))

            if source is not None and source_type == Source.SOURCE_TYPE_HUMAN:
                vio_id = template_repo.get_vioscreen_id_if_exists(account.id,
                                                                  source.id,
                                                                  sample.id)
                # fall back on matching with source id
                if not vio_id:
                    vio_id = \
                        template_repo.get_vioscreen_id_if_exists(account.id,
                                                                 source.id,
                                                                 None)
                if vio_id:
                    ffq_complete, ffq_taken, _ = \
                        vs_repo.get_ffq_status_by_vio_id(vio_id)
                else:
                    ffq_complete = False
                    ffq_taken = False
            else:
                ffq_complete = False
                ffq_taken = False

            # at least one sample has been observed that "is_microsetta",
            # described in the barcodes.project_barcode table, but which is
            # unexpectedly not present in ag.ag_kit_barcodes
            if sample is None:
                sample_status = None
                sample_site = None
                sample_date = None
                sample_time = None
                ffq_complete = None
                ffq_taken = None
            else:
                sample_status = sample_repo.get_sample_status(
                    sample.barcode,
                    sample._latest_scan_timestamp
                )
                sample_site = sample.site

                # get sample date, time
                sample_datetime = sample.datetime_collected
                if sample_datetime is not None:
                    sample_date = sample_datetime.date().isoformat()
                    sample_time = sample_datetime.time().isoformat()
                else:
                    sample_date = None
                    sample_time = None

            kit_by_barcode = admin_repo.get_kit_by_barcode([barcode])

            if kit_by_barcode and len(kit_by_barcode) > 0:
                info = kit_by_barcode[0]

                kit_id_name = info['kit_id']
                outbound_fedex_tracking = info['outbound_tracking']
                inbound_fedex_tracking = info['inbound_tracking']
            else:
                kit_id_name = None
                outbound_fedex_tracking = None
                inbound_fedex_tracking = None

            summary = {
                "sampleid": None if strip_sampleid else barcode,
                "project": barcode_project,
                "source-type": source_type,
                "site-sampled": sample_site,
                "sample-date": sample_date,
                "sample-time": sample_time,
                "account-email": account_email,
                "vioscreen_username": vio_id,
                "ffq-taken": ffq_taken,
                "ffq-complete": ffq_complete,
                "sample-status": sample_status,
                "sample-received": sample_status is not None,
                "first-scan-timestamp": first_scan_timestamp,
                "first-scan-status": first_scan_status,
                "latest-scan-timestamp": latest_scan_timestamp,
                "latest-scan-status": latest_scan_status,
                "kit-id": kit_id_name,
                "outbound-tracking": outbound_fedex_tracking,
                "inbound-tracking": inbound_fedex_tracking,
            }

            for status in ["sample-is-valid",
                           "no-associated-source",
                           "no-registered-account",
                           "no-collection-info",
                           "sample-has-inconsistencies",
                           "received-unknown-validity"]:
                summary[status] = sample_status == status

            summaries.append(summary)
    return summaries
