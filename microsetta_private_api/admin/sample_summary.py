from microsetta_private_api.model.source import Source
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo
from microsetta_private_api.repo.vioscreen_repo import VioscreenSessionRepo
from werkzeug.exceptions import NotFound


def get_barcodes_for(project_id):
    if project_id is None:
        raise ValueError("project_id must be defined.")

    with Transaction() as t:
        return AdminRepo(t).get_project_barcodes(project_id)


def per_sample(project, barcodes, strip_sampleid):
    summaries = []
    with Transaction() as t:
        admin_repo = AdminRepo(t)
        sample_repo = SampleRepo(t)
        template_repo = SurveyTemplateRepo(t)
        vs_repo = VioscreenSessionRepo(t)

        if project is not None:
            project_barcodes = admin_repo.get_project_barcodes(project)
        else:
            project = 'Unspecified'

        if barcodes is None:
            barcodes = project_barcodes

        for barcode in barcodes:
            diag = admin_repo.retrieve_diagnostics_by_barcode(barcode)
            if diag is None:
                raise NotFound(f"Barcode not found: {barcode}")

            sample = diag['sample']
            account = diag['account']
            source = diag['source']

            account_email = None if account is None else account.email
            source_email = None
            source_type = None if source is None else source.source_type
            vio_id = None

            if source is not None and source_type == Source.SOURCE_TYPE_HUMAN:
                source_email = source.source_data.email

                vio_id = template_repo.get_vioscreen_id_if_exists(account.id,
                                                                  source.id,
                                                                  sample.id)

            # at least one sample has been observed that "is_microsetta",
            # described in the barcodes.project_barcode table, but which is
            # unexpectedly not present in ag.ag_kit_barcodes
            if sample is None:
                sample_status = None
                sample_site = None
                ffq_complete = None
                ffq_taken = None
            else:
                sample_status = sample_repo.get_sample_status(
                    sample.barcode,
                    sample._latest_scan_timestamp
                )
                sample_site = sample.site
                ffq_complete, ffq_taken, _ = vs_repo.get_ffq_status_by_sample(
                    sample.id
                )

            summary = {
                "sampleid": None if strip_sampleid else barcode,
                "project": project,
                "source-type": source_type,
                "site-sampled": sample_site,
                "source-email": source_email,
                "account-email": account_email,
                "vioscreen_username": vio_id,
                "ffq-taken": ffq_taken,
                "ffq-complete": ffq_complete,
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
    return summaries
