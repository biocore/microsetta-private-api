import psycopg2
import werkzeug
from werkzeug.exceptions import BadRequest

from microsetta_private_api import localization
from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.repo.base_repo import BaseRepo
from microsetta_private_api.repo.sample_repo import SampleRepo
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
from microsetta_private_api.repo.vioscreen_repo import VioscreenRepo


class SurveyAnswersRepo(BaseRepo):

    def survey_template_id_and_status(self, survey_answers_id):
        # TODO FIXME HACK:  There has GOT TO BE an easier way!
        with self._transaction.cursor() as cur:
            cur.execute("SELECT survey_id, survey_question_id "
                        "FROM survey_answers "
                        "WHERE survey_id=%s "
                        "LIMIT 1",
                        (survey_answers_id,))

            rows = cur.fetchall()

            cur.execute("SELECT survey_id, survey_question_id "
                        "FROM survey_answers_other "
                        "WHERE survey_id=%s "
                        "LIMIT 1",
                        (survey_answers_id,))
            rows += cur.fetchall()

            if len(rows) == 0:
                # see if it's vioscreen
                vioscreen_repo = VioscreenRepo(self._transaction)
                status = vioscreen_repo._get_vioscreen_status(
                    survey_answers_id)
                if status is not None:
                    return SurveyTemplateRepo.VIOSCREEN_ID, status

                # see if it's myfoodrepo
                cur.execute("""SELECT EXISTS (
                                   SELECT myfoodrepo_id
                                   FROM myfoodrepo_registry
                                   WHERE myfoodrepo_id=%s)""",
                            (survey_answers_id, ))
                if cur.fetchone()[0] is True:
                    return SurveyTemplateRepo.MYFOODREPO_ID, None
                else:
                    # not vioscreen and not myfoodrepo?

                    return None, None
                    # TODO: Maybe this should throw an exception, but doing so
                    #  locks the end user out of the minimal implementation
                    #  if they submit an empty survey response.
                    # raise RepoException("No answers in survey: %s" %
                    #                     survey_answers_id)

            arbitrary_question_id = rows[0][1]
            cur.execute("SELECT surveys.survey_id FROM "
                        "group_questions "
                        "LEFT JOIN surveys USING (survey_group) "
                        "WHERE survey_question_id = %s",
                        (arbitrary_question_id,))

            survey_template_id = cur.fetchone()[0]
            # Can define statuses for our internal surveys later if we want
            return survey_template_id, None

    def list_answered_surveys(self, account_id, source_id):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT survey_id, vioscreen_status "
                        "FROM ag_login_surveys "
                        "WHERE ag_login_id = %s "
                        "AND source_id = %s",
                        (account_id, source_id))

            rows = cur.fetchall()
            # Now that vioscreen_status is sent down to client, we can consider
            # vioscreen surveys to be answered regardless of their status.
            answered_surveys = [r[0] for r in rows]
        return answered_surveys

    def list_answered_surveys_by_sample(
            self, account_id, source_id, sample_id):
        sample_repo = SampleRepo(self._transaction)

        # Note: Retrieving sample in this way validates permissions.
        sample = sample_repo.get_sample(account_id, source_id, sample_id)
        if sample is None:
            raise werkzeug.exceptions.NotFound("No sample with id %s" %
                                               sample_id)

        with self._transaction.cursor() as cur:
            cur.execute("SELECT "
                        "survey_id "
                        "FROM "
                        "ag_kit_barcodes "
                        "LEFT JOIN source_barcodes_surveys "
                        "USING (barcode)"
                        "WHERE "
                        "ag_kit_barcode_id = %s",
                        (sample_id,))
            rows = cur.fetchall()
            answered_surveys = [r[0] for r in rows if r[0] is not None]
        return answered_surveys

    def get_answered_survey(self, ag_login_id, source_id,
                            survey_id, language_tag):
        model = {}
        if not self._acct_source_owns_survey(ag_login_id,
                                             source_id,
                                             survey_id):
            return None

        localization_info = localization.LANG_SUPPORT[language_tag]
        lang_name = localization_info[localization.LANG_NAME_KEY]

        with self._transaction.cursor() as cur:
            # Grab selection and multi selection responses
            cur.execute("SELECT "
                        "survey_answers.survey_question_id, "
                        + lang_name + ", "
                        "survey_response_type "
                        "FROM "
                        "survey_answers "
                        "LEFT JOIN "
                        "survey_question_response_type "
                        "ON "
                        "survey_answers.survey_question_id = "
                        "survey_question_response_type.survey_question_id "
                        "LEFT JOIN "
                        "survey_response "
                        "ON "
                        "survey_answers.response = survey_response.american "
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
                               language_tag, survey_template_id, survey_model,
                               survey_answers_id=None):
        # note that "ag_login_id" is the same as account_id

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

        if survey_answers_id is None:
            survey_answers_id = str(uuid.uuid4())

        survey_template_repo = SurveyTemplateRepo(self._transaction)
        survey_template = survey_template_repo.get_survey_template(
            survey_template_id, language_tag)

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
                    q_type = survey_question.response_type

                    # TODO FIXME HACK: Modify DB to make this unnecessary!
                    # We MUST record at least ONE answer for each survey
                    # (even if the user answered nothing)
                    #  or we can't properly track the survey template id later.
                    # Therefore, if the user answered NOTHING, store an empty
                    # string for the first string or text question in the
                    # survey, just so something is recorded.
                    if len(survey_model) == 0 and \
                            (q_type == "STRING" or q_type == "TEXT"):
                        survey_model[str(survey_question_id)] = ""

                    if str(survey_question_id) not in survey_model:
                        # TODO: Is this supposed to leave the question blank
                        #  or write Unspecified?
                        continue
                    answer = survey_model[str(survey_question_id)]

                    if q_type == "SINGLE":
                        # Normalize localized answer
                        normalized_answer = self._unlocalize(answer,
                                                             survey_question_id,  # noqa
                                                             language_tag)

                        try:
                            cur.execute("INSERT INTO survey_answers "
                                        "(survey_id, "
                                        "survey_question_id, "
                                        "response) "
                                        "VALUES(%s, %s, %s)",
                                        (survey_answers_id,
                                         survey_question_id,
                                         normalized_answer))
                        except psycopg2.errors.ForeignKeyViolation:
                            raise BadRequest(
                                "Invalid single survey response: %s" % answer)

                    if q_type == "MULTIPLE":
                        for ans in answer:
                            normalized_answer = self._unlocalize(ans,
                                                                 survey_question_id,  # noqa
                                                                 language_tag)
                            try:
                                cur.execute("INSERT INTO survey_answers "
                                            "(survey_id, "
                                            "survey_question_id, "
                                            "response) "
                                            "VALUES(%s, %s, %s)",
                                            (survey_answers_id,
                                             survey_question_id,
                                             normalized_answer))
                            except psycopg2.errors.ForeignKeyViolation:
                                raise BadRequest(
                                    "Invalid multiple survey response: %s" % ans)  # noqa

                    if q_type == "STRING" or q_type == "TEXT":
                        # Note:  Can't convert language on free text...
                        cur.execute("INSERT INTO survey_answers_other "
                                    "(survey_id, "
                                    "survey_question_id, "
                                    "response) "
                                    "VALUES(%s, %s, %s)",
                                    (survey_answers_id,
                                     survey_question_id,
                                     answer))

        if len(survey_model) == 0:
            # we should not have gotten to the end without recording at least
            # ONE answer (even an empty one) ... but it could happen if this
            # survey template includes NO text or string questions AND the
            # user doesn't answer any of the questions it does include. Not
            # worth making the code robust to this case, as this whole "include
            # one empty answer" is a temporary hack, but at least ensure we
            # know this problem occurred if it ever does
            raise RepoException("No answers provided for survey template %s "
                                "and not able to add an empty string default" %
                                survey_template_id)

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
            cur.execute("DELETE FROM source_barcodes_surveys WHERE "
                        "survey_id = %s",
                        (survey_id,))
            cur.execute("DELETE FROM ag_login_surveys WHERE "
                        "ag_login_id = %s AND survey_id = %s",
                        (acct_id, survey_id))
            # Also unlink any vioscreen external surveys.
            cur.execute("UPDATE vioscreen_registry SET "
                        "source_id = NULL, "
                        "deleted = true "
                        "WHERE "
                        "account_id = %s AND vio_id = %s",
                        (acct_id, survey_id))
            cur.execute("UPDATE myfoodrepo_registry SET "
                        "deleted=true, "
                        "source_id = NULL "
                        "WHERE "
                        "account_id = %s AND myfoodrepo_id = %s",
                        (acct_id, survey_id))
        return True

    def associate_answered_survey_with_sample(self, account_id, source_id,
                                              sample_id, survey_id):
        sample_repo = SampleRepo(self._transaction)

        if not self._acct_owns_survey(account_id, survey_id):
            raise werkzeug.exceptions.NotFound("No survey ID: %s" % survey_id)

        s = sample_repo.get_sample(account_id, source_id, sample_id)

        if s is None:
            raise werkzeug.exceptions.NotFound("No sample ID: %s" % sample_id)

        # Switching to insert if not exists semantics since vioscreen IDs will
        # be associated with samples prior to being filled out.
        with self._transaction.cursor() as cur:
            cur.execute("SELECT * FROM source_barcodes_surveys "
                        "WHERE barcode=%s AND survey_id=%s",
                        (s.barcode, survey_id))
            if cur.fetchone() is None:
                cur.execute("INSERT INTO source_barcodes_surveys "
                            "(barcode, survey_id) "
                            "VALUES(%s, %s)", (s.barcode, survey_id))

    def dissociate_answered_survey_from_sample(self, account_id, source_id,
                                               sample_id, survey_id):
        sample_repo = SampleRepo(self._transaction)

        if not self._acct_source_owns_survey(account_id, source_id, survey_id):
            raise werkzeug.exceptions.NotFound("No survey ID: %s" % survey_id)

        s = sample_repo.get_sample(account_id, source_id, sample_id)

        if s is None:
            raise werkzeug.exceptions.NotFound("No sample ID: %s" % sample_id)

        with self._transaction.cursor() as cur:
            cur.execute("DELETE FROM source_barcodes_surveys "
                        "WHERE "
                        "barcode = %s AND "
                        "survey_id = %s",
                        (s.barcode, survey_id))
            # Also delete from vioscreen and myfoodrepo registries
            cur.execute("UPDATE vioscreen_registry "
                        "SET deleted=true "
                        "WHERE "
                        "account_id = %s AND "
                        "source_id = %s AND "
                        "sample_id = %s AND "
                        "vio_id = %s",
                        (account_id, source_id, sample_id, survey_id))
            cur.execute("UPDATE myfoodrepo_registry "
                        "SET deleted=true "
                        "WHERE "
                        "account_id = %s AND "
                        "source_id = %s AND "
                        "myfoodrepo_id = %s",
                        (account_id, source_id, survey_id))

    def build_metadata_map(self):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT survey_question_id, question_shortname "
                        "FROM "
                        "survey_question")
            rows = cur.fetchall()
            metamap = {row[0]: row[1] for row in rows}
        return metamap

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

    def _unlocalize(self, answer, survey_question_id, language_tag):
        localization_info = localization.LANG_SUPPORT[language_tag]
        lang_name = localization_info[localization.LANG_NAME_KEY]

        with self._transaction.cursor() as cur:
            # Normalize localized answer
            cur.execute("""SELECT american
                           FROM survey_response
                             JOIN survey_question_response
                             ON response=american
                           WHERE survey_question_id=%s
                             AND """ + lang_name + "=%s",
                        (survey_question_id, answer))
            row = cur.fetchone()
            if row is None:
                raise BadRequest("Invalid unlocalization: %s" % answer)
            normalized_answer = row[0]
            return normalized_answer

    def _get_survey_sample_associations(self, answered_survey_id):
        """ Do not use from api layer, you must validate account and source."""
        with self._transaction.cursor() as cur:
            cur.execute("SELECT barcode "
                        "FROM source_barcodes_surveys "
                        "WHERE survey_id = %s",
                        (answered_survey_id,))

            sample_rows = cur.fetchall()
            if sample_rows is None:
                return []
            else:
                return [r[0] for r in sample_rows]

    def scrub(self, account_id, source_id, survey_id):
        """Replace free text with scrubbed text"""
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT survey_id
                           FROM ag.ag_login_surveys
                           WHERE ag_login_id = %s AND
                               source_id = %s AND
                               survey_id = %s""",
                        (account_id, source_id, survey_id))
            res = cur.fetchone()
            if res is None:
                raise RepoException("Invalid account / source / survey "
                                    "relation")

            text = 'scrubbed'
            cur.execute("""UPDATE survey_answers_other
                           SET response=%s
                           WHERE survey_id=%s
                               AND survey_question_id IN (
                                   SELECT survey_question_id
                                   FROM survey_answers_other
                                       JOIN survey_question_response_type
                                           USING (survey_question_id)
                                   WHERE survey_response_type='TEXT'
                                       AND survey_id=%s
                                   )""",
                        (text, survey_id, survey_id))
