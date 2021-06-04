from werkzeug.exceptions import NotFound

from microsetta_private_api import localization
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.model.survey_template import SurveyTemplate, \
    SurveyTemplateLinkInfo
from microsetta_private_api.model.survey_template_group import \
        SurveyTemplateGroup
from microsetta_private_api.model.survey_template_question import \
        SurveyTemplateQuestion
from microsetta_private_api.model.survey_template_trigger import \
        SurveyTemplateTrigger
import copy
import secrets

from microsetta_private_api.repo.sample_repo import SampleRepo


class SurveyTemplateRepo(BaseRepo):

    VIOSCREEN_ID = 10001
    SURVEY_INFO = {
        1: SurveyTemplateLinkInfo(
            1,
            "Primary",
            "1.0",
            "local"
        ),
        2: SurveyTemplateLinkInfo(
            2,
            "Pet Information",
            "1.0",
            "local"
        ),
        3: SurveyTemplateLinkInfo(
            3,
            "Fermented Foods Questionnaire",
            "1.0",
            "local"
        ),
        4: SurveyTemplateLinkInfo(
            4,
            "Surfer Questionnaire",
            "1.0",
            "local"
        ),
        5: SurveyTemplateLinkInfo(
            5,
            "Personal Microbiome Information",
            "1.0",
            "local"
        ),
        6: SurveyTemplateLinkInfo(
            6,
            "COVID-19 Questionnaire",
            "1.0",
            "local"
        ),
        VIOSCREEN_ID: SurveyTemplateLinkInfo(
            VIOSCREEN_ID,
            "Vioscreen Food Frequency Questionnaire",
            "1.0",
            "remote"
        )
    }

    def __init__(self, transaction):
        super().__init__(transaction)

    def list_survey_ids(self):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT DISTINCT survey_id from surveys")
            rows = cur.fetchall()
        return [x[0] for x in rows]

    @staticmethod
    def get_survey_template_link_info(survey_id):
        return copy.deepcopy(SurveyTemplateRepo.SURVEY_INFO[survey_id])

    def get_survey_template(self, survey_id, language_tag):
        tag_to_col = {
            localization.EN_US: "survey_question.american",
            localization.EN_GB: "survey_question.british",
            localization.ES_MX: "survey_question.spanish"
        }

        if language_tag not in tag_to_col:
            raise NotFound("Survey localization unavailable: %s" %
                           language_tag)

        with self._transaction.cursor() as cur:

            cur.execute(
                "SELECT count(*) FROM surveys WHERE survey_id=%s",
                (survey_id,)
            )
            if cur.fetchone()[0] == 0:
                raise NotFound("No such survey")

            cur.execute(
                "SELECT "
                "group_questions.survey_group, "
                "survey_question.survey_question_id, " +
                tag_to_col[language_tag] + ", " +
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
                                                                cur_group_id,
                                                                language_tag)
                        all_groups.append(SurveyTemplateGroup(
                            group_localized_text,
                            cur_questions))
                    cur_group_id = group_id
                    cur_questions = []

                responses = self._get_question_valid_responses(question_id,
                                                               language_tag)
                triggers = self._get_question_triggers(question_id)

                # Quick  fix to correctly sort country names in Spanish
                if language_tag == localization.ES_MX and \
                        (question_id == 110 or question_id == 148):
                    responses[1:len(responses)] = \
                        sorted(responses[1:len(responses)])

                question = SurveyTemplateQuestion(question_id,
                                                  localized_text,
                                                  short_name,
                                                  response_type,
                                                  responses,
                                                  triggers)
                cur_questions.append(question)

            if cur_group_id is not None:
                group_localized_text = self._get_group_localized_text(
                    cur_group_id,
                    language_tag)
                all_groups.append(SurveyTemplateGroup(
                    group_localized_text,
                    cur_questions))

            return SurveyTemplate(survey_id, language_tag, all_groups)

    def _get_group_localized_text(self, group_id, language_tag):
        tag_to_col = {
            localization.EN_US: "american",
            localization.EN_GB: "british",
            localization.ES_MX: "spanish"
        }
        with self._transaction.cursor() as cur:
            cur.execute("SELECT " +
                        tag_to_col[language_tag] + " " +
                        "FROM survey_group "
                        "WHERE "
                        "group_order = %s", (group_id,))
            row = cur.fetchone()
            if row is None:
                return None
            return row[0]

    def _get_question_valid_responses(self, survey_question_id, language_tag):
        tag_to_col = {
            localization.EN_US: "survey_response.american",
            localization.EN_GB: "survey_response.british",
            localization.ES_MX: "survey_response.spanish",
        }

        with self._transaction.cursor() as cur:
            cur.execute("SELECT " +
                        tag_to_col[language_tag] + " "
                        "FROM "
                        "survey_question_response "
                        "LEFT JOIN "
                        "survey_response "
                        "ON "
                        "survey_question_response.response = "
                        "survey_response.american "
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

    def create_vioscreen_id(self, account_id, source_id,
                            vioscreen_ext_sample_id):
        with self._transaction.cursor() as cur:
            # test if an existing ID is available
            existing = self.get_vioscreen_id_if_exists(account_id, source_id,
                                                       vioscreen_ext_sample_id)
            if existing is None:
                vioscreen_id = secrets.token_hex(8)
                # Put a survey with status -1 into ag_login_surveys
                cur.execute("INSERT INTO ag_login_surveys("
                            "ag_login_id, "
                            "survey_id, "
                            "vioscreen_status, "
                            "source_id) "
                            "VALUES(%s, %s, %s, %s)",
                            (account_id, vioscreen_id, -1, source_id))
                # Immediately attach that survey to the specified sample
                sample_repo = SampleRepo(self._transaction)
                s = sample_repo.get_sample(account_id,
                                           source_id,
                                           vioscreen_ext_sample_id)

                if s is None:
                    raise KeyError(f"{vioscreen_ext_sample_id} does not exist")

                cur.execute("INSERT INTO source_barcodes_surveys "
                            "(barcode, survey_id) "
                            "VALUES(%s, %s)", (s.barcode, vioscreen_id))

                # And add it to the registry to keep track of the survey if
                # user quits out then wants to resume the survey.
                cur.execute("INSERT INTO vioscreen_registry("
                            "account_id, source_id, sample_id, vio_id) "
                            "VALUES(%s, %s, %s, %s)",
                            (account_id, source_id, vioscreen_ext_sample_id,
                             vioscreen_id))
            else:
                vioscreen_id = existing
        return vioscreen_id

    def get_vioscreen_id_if_exists(self, account_id, source_id,
                                   vioscreen_ext_sample_id):
        """Obtain a vioscreen ID if it exists"""
        with self._transaction.cursor() as cur:
            # Find an active vioscreen survey for this account+source+sample
            # (deleted surveys are not active)
            cur.execute("SELECT vio_id FROM vioscreen_registry WHERE "
                        "account_id=%s AND "
                        "source_id=%s AND "
                        "sample_id=%s AND "
                        "deleted=false",
                        (account_id, source_id, vioscreen_ext_sample_id))
            rows = cur.fetchall()
            if rows is None or len(rows) == 0:
                return None
            else:
                return rows[0][0]

    def fetch_user_basic_physiology(self, account_id, source_id):
        """Given an account and source ID, obtain basic physiology properties

        Parameters
        ----------
        account_id : str, UUID
            The account UUID
        source_id : str, UUID
            The source UUID

        Notes
        -----
        The original intention with this method was to provide basic host
        detail to Viocare for the reports they produce. By default,
        Viocare interprets height and weight as standard.

        Returns
        -------
            tuple, (int or None, int or None, float or None, float or None)
            The tuple contents are (birth year, gender, height, weight).
        """
        UNSPECIFIED = 'Unspecified'

        with self._transaction.cursor() as cur:
            # from survey_answers for non-free text fields
            cur.execute("""SELECT question_shortname, q.response
                           FROM ag_login_surveys AS s
                           JOIN survey_answers AS q
                             ON s.survey_id = q.survey_id
                           JOIN survey_question
                             USING (survey_question_id)
                           WHERE question_shortname IN (
                                 'HEIGHT_UNITS',
                                 'WEIGHT_UNITS',
                                 'BIRTH_YEAR',
                                 'GENDER')
                             AND s.ag_login_id = %s
                             and s.source_id = %s""",
                        (account_id, source_id))

            results = {name: value for name, value in cur.fetchall()}
            birth_year = results.get('BIRTH_YEAR')
            gender = results.get('GENDER')
            height_units = results.get('HEIGHT_UNITS')
            weight_units = results.get('WEIGHT_UNITS')

            # from survey_answers_other for height/weight
            cur.execute("""SELECT question_shortname, q.response
                           FROM ag_login_surveys AS s
                           JOIN survey_answers_other AS q
                             ON s.survey_id = q.survey_id
                           JOIN survey_question
                             USING (survey_question_id)
                           WHERE question_shortname IN (
                                 'HEIGHT_CM',
                                 'WEIGHT_KG')
                             AND s.ag_login_id = %s
                             and s.source_id = %s""",
                        (account_id, source_id))

            results = {name: value for name, value in cur.fetchall()}
            height = results.get('HEIGHT_CM')
            weight = results.get('WEIGHT_KG')

            # normalize the return values
            if birth_year is not None and birth_year.isdigit():
                birth_year = int(birth_year)
            else:
                birth_year = None

            if gender is not None and gender == UNSPECIFIED:
                gender = None

            # This sucks.
            if height == UNSPECIFIED or weight_units == UNSPECIFIED:
                height = None
            elif height is not None:
                # all survey_answers_other responses are of the form
                # '["foo"]' :/
                height = height[2:-2]
                if height == "":
                    height = None
                else:
                    height = int(height)
                    if height_units == 'centimeters':
                        # to inches
                        height = height / 2.54
            else:
                # should not occur but just in case
                height = None

            if weight == UNSPECIFIED or weight_units == UNSPECIFIED:
                weight = None
            elif weight is not None:
                # all survey_answers_other responses are of the form
                # '["foo"]' :/
                weight = weight[2:-2]
                if weight == "":
                    weight = None
                else:
                    weight = int(weight)
                    if weight_units == 'kilograms':
                        # to pounds
                        weight = weight * 2.20462
            else:
                # should not occur but just in case
                weight = None

        return (birth_year, gender, height, weight)
