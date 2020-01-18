from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.repo.survey_template_repo import SurveyTemplateRepo

import uuid


# TODO: It looks like there is significant mismatch between the current schema
#  and the desired yaml.  This implementation will likely need to be used
#  as a change script that converts the underlying data to a new schema rather
#  than the final implementation for retrieving survey answers.

# TODO: Survey answers associated with a sample are referenced in
#  source_barcodes_surveys, totally unclear what to do with those here.  Should
#  we disambiguate all these functions to decide whether it includes that
#  table, build out a SurveyAnswersRepo, or modify the schema so its not so
#  insane???
class SurveyAnswersRepo(BaseRepo):

    def list_answered_surveys(self, account_id, source_id):
        # TODO: No obvious way in the current schema to go from an answered
        #  survey's id back to a survey template id, preventing retrieval
        #  of the survey's title...  This should be addressed as we transform
        #  the data as well
        with self._transaction.cursor() as cur:
            cur.execute("SELECT survey_id "
                        "FROM ag_login_surveys "
                        "WHERE ag_login_id = %s "
                        "AND source_id = %s",
                        (account_id, source_id))

            rows = cur.fetchall()
            answered_surveys = [r[0] for r in rows]
        return answered_surveys

    def get_answered_survey(self, ag_login_id, survey_id):
        model = {}
        if not self._acct_owns_survey(ag_login_id, survey_id):
            return None

        with self._transaction.cursor() as cur:
            # Grab selection and multi selection responses
            cur.execute("SELECT "
                        "survey_answers.survey_question_id, "
                        "response, "
                        "survey_response_type "
                        "FROM "
                        "survey_answers "
                        "LEFT JOIN "
                        "survey_question_response_type "
                        "ON "
                        "survey_answers.survey_question_id = "
                        "survey_question_response_type.survey_question_id "
                        "WHERE "
                        "survey_id = %s",
                        (survey_id,))
            rows = cur.fetchall()

            for r in rows:
                str_id = str(r[0])

                if r[2] == "SINGLE":
                    model[str_id] = r[1]
                elif r[2] == "MULTIPLE":
                    if str_id not in model:
                        model[str_id] = []
                    model[str_id].append(r[1])

            # Grab free form responses
            cur.execute("SELECT "
                        "survey_question_id, response "
                        "FROM "
                        "survey_answers_other "
                        "WHERE "
                        "survey_id = %s",
                        (survey_id,))
            rows = cur.fetchall()
            for r in rows:
                model[str(r[0])] = r[1]

        return model

    def submit_answered_survey(self, ag_login_id, source_id,
                               locale_code, survey_template_id, survey_model):
        # This is actually pretty complicated in the current schema:
        #   We need to filter the model down to questions that are in the
        #       template
        #   We need to ensure that the account has access to write the given
        #       participant
        #   We need to generate a survey_answer id
        #   We need to log that the user submitted this survey
        #   We need to write each answer to one or more rows

        # TODO: We need to ensure that the account has access to write the
        #  given participant!?!
        survey_answers_id = str(uuid.uuid4())

        survey_template_repo = SurveyTemplateRepo(self._transaction)
        survey_template = survey_template_repo.get_survey_template(
            survey_template_id)

        with self._transaction.cursor() as cur:

            # Log that the user submitted this survey
            cur.execute("INSERT INTO ag_login_surveys "
                        "(ag_login_id, survey_id, source_id) "
                        "VALUES(%s, %s, %s)",
                        (ag_login_id, survey_answers_id, source_id))

            # Write each answer
            for survey_template_group in survey_template.groups:
                for survey_question in survey_template_group.questions:
                    survey_question_id = survey_question.id
                    if str(survey_question_id) not in survey_model:
                        # TODO: Is this supposed to leave the question blank
                        #  or write Unspecified?
                        continue
                    answer = survey_model[str(survey_question_id)]

                    q_type = survey_question.response_type
                    if q_type == "SINGLE":
                        cur.execute("INSERT INTO survey_answers "
                                    "(survey_id, "
                                    "survey_question_id, "
                                    "response) "
                                    "VALUES(%s, %s, %s)",
                                    (survey_answers_id,
                                     survey_question_id,
                                     answer))
                    if q_type == "MULTIPLE":
                        for ans in answer:
                            cur.execute("INSERT INTO survey_answers "
                                        "(survey_id, "
                                        "survey_question_id, "
                                        "response) "
                                        "VALUES(%s, %s, %s)",
                                        (survey_answers_id,
                                         survey_question_id,
                                         ans))
                    if q_type == "STRING" or q_type == "TEXT":
                        cur.execute("INSERT INTO survey_answers_other "
                                    "(survey_id, "
                                    "survey_question_id, "
                                    "response) "
                                    "VALUES(%s, %s, %s)",
                                    (survey_answers_id,
                                     survey_question_id,
                                     answer))
        return survey_answers_id

    def delete_answered_survey(self, acct_id, survey_id):
        if not self._acct_owns_survey(acct_id, survey_id):
            return False

        with self._transaction.cursor() as cur:
            cur.execute("DELETE FROM survey_answers WHERE "
                        "survey_id = %s",
                        (survey_id,))
            cur.execute("DELETE FROM survey_answers_other WHERE "
                        "survey_id = %s",
                        (survey_id,))
            cur.execute("DELETE FROM ag_login_surveys WHERE "
                        "ag_login_id = %s AND survey_id = %s",
                        (acct_id, survey_id))

    # True if this account owns this survey_answer_id, else False
    def _acct_owns_survey(self, acct_id, survey_id):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT "
                        "survey_id "
                        "FROM "
                        "ag_login_surveys "
                        "WHERE "
                        "ag_login_id = %s AND survey_id = %s",
                        (acct_id, survey_id))
            return cur.fetchone() is not None

    # True if this account + participant owns this survey_answer_id else False
    def _acct_source_owns_survey(self, acct_id, source_id, survey_id):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT "
                        "survey_id "
                        "FROM "
                        "ag_login_surveys "
                        "WHERE "
                        "ag_login_id = %s AND "
                        "source_id = %s AND "
                        "survey_id = %s",
                        (acct_id, source_id, survey_id))
            return cur.fetchone() is not None
