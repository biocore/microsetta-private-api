from repo.base_repo import BaseRepo
from model.survey_template import SurveyTemplate
from model.survey_template_group import SurveyTemplateGroup
from model.survey_template_question import SurveyTemplateQuestion
from model.survey_template_trigger import SurveyTemplateTrigger


class SurveyTemplateRepo(BaseRepo):
    def __init__(self, transaction):
        super().__init__(transaction)

    def list_survey_ids(self):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT DISTINCT survey_id from surveys")
            rows = cur.fetchall()
        return [x[0] for x in rows]

    def get_survey_template(self, survey_id):

        # TODO: Need to add support for locales, will require changing
        # the survey_question table.
        with self._transaction.cursor() as cur:
            cur.execute(
                "SELECT "
                "group_questions.survey_group, "
                "survey_question.survey_question_id, "
                "survey_question.american, "
                "survey_question.question_shortname, "
                "survey_question_response_type.survey_response_type "
                "FROM "
                "surveys "
                "LEFT JOIN group_questions ON "
                "surveys.survey_group = group_questions.survey_group "
                "LEFT JOIN survey_question ON "
                "group_questions.survey_question_id = "
                "survey_question.survey_question_id "
                "LEFT JOIN survey_question_response_type ON "
                "survey_question.survey_question_id = "
                "survey_question_response_type.survey_question_id "
                "WHERE surveys.survey_id = %s AND "
                "survey_question.retired = false "
                "ORDER BY group_questions.survey_group, "
                "group_questions.display_index",
                (survey_id,))

            rows = cur.fetchall()

            all_groups = []
            cur_group_id = None
            cur_questions = None

            for r in rows:
                group_id = r[0]
                question_id = r[1]
                localized_text = r[2]
                short_name = r[3]
                response_type = r[4]

                if group_id != cur_group_id:
                    if cur_group_id is not None:
                        group_localized_text = self._get_group_localized_text(
                                                                cur_group_id)
                        all_groups.append(SurveyTemplateGroup(
                            group_localized_text,
                            cur_questions))
                    cur_group_id = group_id
                    cur_questions = []

                responses = self._get_question_valid_responses(question_id)
                triggers = self._get_question_triggers(question_id)

                question = SurveyTemplateQuestion(question_id,
                                                  localized_text,
                                                  short_name,
                                                  response_type,
                                                  responses,
                                                  triggers)
                cur_questions.append(question)

            if cur_group_id is not None:
                group_localized_text = self._get_group_localized_text(
                    cur_group_id)
                all_groups.append(SurveyTemplateGroup(
                    group_localized_text,
                    cur_questions))

            return SurveyTemplate(survey_id, "american", all_groups)

    def _get_group_localized_text(self, group_id):
        # TODO: Localization!
        with self._transaction.cursor() as cur:
            cur.execute("SELECT american "
                        "FROM survey_group "
                        "WHERE "
                        "group_order = %s", (group_id,))
            row = cur.fetchone()
            if row is None:
                return None
            return row[0]

    def _get_question_valid_responses(self, survey_question_id):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT response "
                        "FROM "
                        "survey_question_response "
                        "WHERE "
                        "survey_question_id = %s "
                        "ORDER BY "
                        "display_index", (survey_question_id,))
            return [x[0] for x in cur.fetchall()]

    def _get_question_triggers(self, survey_question_id):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT triggering_response, triggered_question "
                        "FROM "
                        "survey_question_triggers "
                        "WHERE "
                        "survey_question_id = %s ", (survey_question_id,))

            rows = cur.fetchall()
            return [SurveyTemplateTrigger(x[0], x[1]) for x in rows]
