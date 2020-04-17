from werkzeug.exceptions import NotFound

from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.repo.account_repo import AccountRepo
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.repo.sample_repo import SampleRepo
from microsetta_private_api.repo.source_repo import SourceRepo
from hashlib import sha512

from microsetta_private_api.repo.survey_answers_repo import SurveyAnswersRepo


class AdminRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def _get_ids_relevant_to_barcode(self, sample_barcode):
        # TODO: This refactor won't merge nicely with some of the other PRs
        #  need to revisit to add kit information.  Can then remove the code
        #  duplication
        with self._transaction.dict_cursor() as cur:
            cur.execute(
                "SELECT "
                "ag_kit_barcodes.ag_kit_barcode_id as sample_id, "
                "source.id as source_id, "
                "account.id as account_id "
                "FROM "
                "ag.ag_kit_barcodes "
                "LEFT OUTER JOIN "
                "source "
                "ON "
                "ag_kit_barcodes.source_id = source.id "
                "LEFT OUTER JOIN "
                "account "
                "ON "
                "account.id = source.account_id "
                "WHERE "
                "ag_kit_barcodes.barcode = %s",
                (sample_barcode,))
            return cur.fetchone()

    def retrieve_diagnostics_by_barcode(self, sample_barcode):
        with self._transaction.dict_cursor() as cur:
            ids = self._get_ids_relevant_to_barcode(sample_barcode)

            if ids is None:
                sample_id = None
                source_id = None
                account_id = None
            else:
                sample_id = ids["sample_id"]
                source_id = ids["source_id"]
                account_id = ids["account_id"]

            account = None
            source = None
            sample = None

            if sample_id is not None:
                sample_repo = SampleRepo(self._transaction)
                sample = sample_repo._get_sample_by_id(sample_id)

            if source_id is not None and account_id is not None:
                account_repo = AccountRepo(self._transaction)
                source_repo = SourceRepo(self._transaction)
                account = account_repo.get_account(account_id)
                source = source_repo.get_source(account_id, source_id)

            cur.execute("SELECT * from barcodes.barcode "
                        "LEFT OUTER JOIN barcodes.project_barcode "
                        "USING (barcode) "
                        "LEFT OUTER JOIN barcodes.project "
                        "USING (project_id) "
                        "where barcode=%s",
                        (sample_barcode,))
            barcode_info = cur.fetchall()

            # How to unwrap a psycopg2 DictRow.  I feel dirty.
            barcode_info = [{k: v for k, v in x.items()}
                            for x in barcode_info]  # Get Inceptioned!!
            diagnostic = {
                "barcode": sample_barcode,
                "account": account,
                "source": source,
                "sample": sample,
                "barcode_info": barcode_info
            }

            return diagnostic

    def get_survey_metadata(self, sample_barcode, survey_template_id=None):
        ids = self._get_ids_relevant_to_barcode(sample_barcode)

        if ids is None:
            raise NotFound("No such barcode")

        account_id = ids['account_id']
        source_id = ids['source_id']
        sample_id = ids['sample_id']
        source = None
        if source_id is not None and account_id is not None:
            source_repo = SourceRepo(self._transaction)
            source = source_repo.get_source(account_id, source_id)

        if source is None:
            raise RepoException("Barcode is not associated with a source")

        # TODO: This is my best understanding of how the data must be
        #  transformed to get the host_subject_id, needs verification that it
        #  generates the expected values for preexisting samples.
        prehash = account_id + source.source_data.name.lower()
        host_subject_id = sha512(prehash.encode()).hexdigest()

        survey_answers_repo = SurveyAnswersRepo(self._transaction)
        answer_ids = survey_answers_repo.list_answered_surveys_by_sample(
            account_id, source_id, sample_id)

        # if a survey template is specified, filter the returned surveys
        if survey_template_id is not None:
            # TODO: This schema is so awkward for this type of query...
            answers = []
            for answer_id in answer_ids:
                template_id = survey_answers_repo.find_survey_template_id(
                    answer_id)
                if template_id == survey_template_id:
                    answers.append(answer_id)

            if len(answers) == 0:
                raise NotFound("This barcode is not associated with any surveys "
                               "matching this template id")
            if len(answers) > 1:
                #  I really hope this can't happen.  (x . x)
                raise RepoException("This barcode is associated with more than one"
                                    " survey matching this template id")
            answer_ids = answers

        metadata_map = survey_answers_repo.build_metadata_map()

        all_survey_answers = []
        for answer_id in answer_ids:
            answer_model = survey_answers_repo.get_answered_survey(
                account_id,
                source_id,
                answer_id,
                "en-US"
            )

            survey_answers = {}
            for k in answer_model:
                new_k = metadata_map[int(k)]
                survey_answers[new_k] = answer_model[k]

            all_survey_answers.append(survey_answers)

        pulldown = {
            "sample_barcode": sample_barcode,
            "host_subject_id": host_subject_id,
            "survey_answers": all_survey_answers
        }

        return pulldown