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

                # see if it's the Polyphenol FFQ
                try:
                    uuid.UUID(survey_answers_id)
                    cur.execute("""SELECT EXISTS (
                                   SELECT polyphenol_ffq_id
                                   FROM ag.polyphenol_ffq_registry
                                   WHERE polyphenol_ffq_id=%s)""",
                                (survey_answers_id, ))
                    if cur.fetchone()[0] is True:
                        return SurveyTemplateRepo.POLYPHENOL_FFQ_ID, None
                except ValueError:
                    # Note: we don't care about the error, just means it's not
                    # the Polyphenol FFQ
                    pass

                # see if it's the Spain FFQ
                try:
                    uuid.UUID(survey_answers_id)
                    cur.execute("""SELECT EXISTS (
                                   SELECT spain_ffq_id
                                   FROM ag.spain_ffq_registry
                                   WHERE spain_ffq_id=%s)""",
                                (survey_answers_id, ))
                    if cur.fetchone()[0] is True:
                        return SurveyTemplateRepo.SPAIN_FFQ_ID, None
                except ValueError:
                    # Note: we don't care about the error, just means it's not
                    # the Spain FFQ
                    pass

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
                        "WHERE survey_question_id = %s and retired is false",
                        (arbitrary_question_id,))

            survey_template_id = cur.fetchone()[0]
            # Can define statuses for our internal surveys later if we want
            return survey_template_id, None

    def get_template_ids_from_survey_ids(self, survey_ids):
        '''
        returns a list of (template_id, survey_id) tuples.
        :param survey_ids: A list of survey ids.
        :return: A list of (survey_id, survey_template_id) tuples.
        '''
        if not isinstance(survey_ids, list):
            raise ValueError("survey_ids is not a list of survey ids")

        if len(survey_ids) == 0 or '' in survey_ids or None in survey_ids:
            raise ValueError("survey_ids is an empty list or contains invalid"
                             " values")

        res = self._local_survey_template_ids_from_survey_ids(survey_ids)

        # check to see if any of the survey ids are associated with a remote
        # survey.
        for survey_id in survey_ids:
            res += self._remote_survey_template_id_from_survey_id(survey_id)

        return res

    def migrate_responses(self, barcode):
        '''
        migrates filled answers from legacy surveys associated w/a barcode into current templates and saves them as new surveys.
        :param survey_ids: A barcode.
        :return: A list of (account_id, survey_id) tuples representing the new surveys.
        '''
        if barcode is None or barcode is '':
            raise ValueError("invalid barcode")

        # to keep _migrate_responses() simple, it generates a set of new
        # templates based on latest responses of both retired and new
        # surveys. If the user already has one or more surveys of the newer
        # variety (for whatever reason), then we don't want to create migrated
        # versions for those surveys as they'd be redundant.
        results, all_meta = self._migrate_responses(barcode)

        sql = """SELECT a.survey_template_id
                 FROM   ag.ag_login_surveys a 
                        JOIN ag.source_barcodes_surveys b 
                          ON a.survey_id = b.survey_id 
                 WHERE  survey_template_id NOT IN ( 1, 2, 3, 4, 
                                                    5, 6, 7, 10000, 
                                                    10001, 10002, 10003, 10004 ) 
                        AND b.barcode = %s
                 ORDER  BY survey_template_id"""

        filter_flag = []

        with self._transaction.cursor() as cur:
            cur.execute(sql, (barcode,))

            filter_flag = [str(x[0]) for x in cur.fetchall()]

            # remove all redundant templates.
            for template_id in set(filter_flag):
                results.pop(template_id)

            new_survey_ids = []

            # submit each new survey to the system.
            for template_id in results:
                meta = all_meta[template_id]

                new_survey_id = self.submit_answered_survey(meta['account_id'],
                                                            meta['source_id'],
                                                            localization.EN_US,
                                                            template_id,
                                                            results[template_id],
                                                            creation_time=meta['creation_time'])

                self.associate_answered_survey_with_sample(meta['account_id'],
                                                           meta['source_id'],
                                                           meta['sample_id'],
                                                           new_survey_id)

                new_survey_ids.append((meta['account_id'], new_survey_id))

            return new_survey_ids

    def _migrate_responses(self, barcode):
        '''
        Get all survey responses associated with a barcode and migrate them into new survey templates.
        :param barcode: A barcode.
        :return: A dict of filled survey_templates, A dict of survey metadata.
        TODO: Union with survey_questions_other
        '''
        if barcode is None or barcode is '':
            raise ValueError("invalid barcode")

        sql = """SELECT
                        a.survey_question_id, 
                        a.response, 
                        d.survey_id as survey_template_id, 
                        e.ag_login_id as account_id,
                        e.source_id, 
                        e.creation_time,
                        f.survey_response_type,
						g.ag_kit_barcode_id as sample_id
                 FROM   ag.survey_answers a 
                        JOIN ag.source_barcodes_surveys b 
                          ON a.survey_id = b.survey_id 
                        JOIN ag.group_questions c 
                          ON a.survey_question_id = c.survey_question_id 
                        JOIN ag.surveys d 
                          ON c.survey_group = d.survey_group 
                        JOIN ag.ag_login_surveys e 
                          ON a.survey_id = e.survey_id
                        JOIN ag.survey_question_response_type f
                          ON a.survey_question_id = f.survey_question_id
						JOIN ag.ag_kit_barcodes g
						  ON b.barcode = g.barcode
                 WHERE  a.response != 'Unspecified' 
                        AND b.barcode = %s
                        AND d.retired = false
                 ORDER  BY d.survey_id asc, e.creation_time asc"""

        with self._transaction.cursor() as cur:
            cur.execute(sql, (barcode,))

            rows = cur.fetchall()

            # create a set of empty templates to fill-in.
            results = self._generate_empty_surveys()
            dirty_flag = []
            meta = {}

            for row in rows:
                question_id = str(row[0])
                response = row[1]
                template_id = str(row[2])
                account_id = str(row[3])
                source_id = str(row[4])
                creation_time = row[5]
                response_type = row[6]
                sample_id = str(row[7])

                # template n is now dirty.
                dirty_flag.append(template_id)
        
                # responses are from earliest to latest thus older answers
                # will be overwritten with newer ones as need be.
                if response_type == 'MULTIPLE':
                    results[template_id][question_id].append(response)
                    try:
                        # remove will raise an exception if 'Unspecified' has
                        # already been removed. Handle this quietly.
                        results[template_id][question_id].remove("Unspecified")
                    except ValueError:
                        pass
                else:
                    results[template_id][question_id] = response

                meta[template_id] = {'creation_time': creation_time,
                                     'account_id': account_id,
                                     'sample_id': sample_id,
                                     'source_id': source_id }

            # remove all templates that remain empty.
            for template_id in set(results.keys()) - set(dirty_flag):
                results.pop(template_id)

            return results, meta

    def _generate_empty_surveys(self):
        '''
        Generate a set of empty templates for all non-retired surveys.
        Fill in the responses with 'Unspecified' and similar as needed.
        :return: A list of empty templates for all non-retired surveys.
        TODO: Union with survey_questions_other
        '''
        sql = """SELECT a.survey_id, 
                        b.survey_question_id, 
                        c.survey_response_type 
                 FROM   ag.surveys a 
                        JOIN ag.group_questions b 
                          ON a.survey_group = b.survey_group 
                        JOIN ag.survey_question_response_type c 
                          ON b.survey_question_id = c.survey_question_id 
                        JOIN ag.survey_question d 
                          ON d.survey_question_id = b.survey_question_id 
                 WHERE  a.retired = false 
                        AND d.retired = false 
                 ORDER  BY survey_id, 
                           survey_question_id"""

        with self._transaction.cursor() as cur:
            cur.execute(sql)

            rows = cur.fetchall()

            results = {}
            for row in rows:
                template_id = str(row[0])
                question_id = str(row[1])
                response_type = row[2]

                if not template_id in results:
                    results[template_id] = {}

                if response_type == 'MULTIPLE':
                    results[template_id][question_id] = ["Unspecified"]
                else:
                    results[template_id][question_id] = "Unspecified"

            return results

    def _remote_survey_template_id_from_survey_id(self, survey_id):
        # VIOscreen
        vioscreen_repo = VioscreenRepo(self._transaction)
        status = vioscreen_repo._get_vioscreen_status(survey_id)
        if status is not None:
            return [(survey_id, SurveyTemplateRepo.VIOSCREEN_ID)]

        with self._transaction.cursor() as cur:
            try:
                # If survey_id isn't a valid UUID, a ValueError will be
                # raised.
                uuid.UUID(survey_id)
            except ValueError:
                # assume a survey_id that isn't a valid UUID is a myfoodrepo
                # survey.
                cur.execute("SELECT EXISTS (SELECT myfoodrepo_id FROM "
                            "myfoodrepo_registry WHERE myfoodrepo_id=%s)",
                            (survey_id,))

                if cur.fetchone()[0] is True:
                    return [(survey_id, SurveyTemplateRepo.MYFOODREPO_ID)]
                else:
                    return []

            # survey_id must be a proper UUID formatted string, or else the
            # queries below will fail.

            # Polyphenol FFQ
            cur.execute("SELECT EXISTS (SELECT polyphenol_ffq_id FROM "
                        "ag.polyphenol_ffq_registry WHERE "
                        "polyphenol_ffq_id=%s)", (survey_id,))

            if cur.fetchone()[0] is True:
                return [(survey_id, SurveyTemplateRepo.POLYPHENOL_FFQ_ID)]

            # Spain FFQ
            cur.execute("SELECT EXISTS (SELECT spain_ffq_id FROM "
                        "ag.spain_ffq_registry WHERE spain_ffq_id=%s)",
                        (survey_id,))

            if cur.fetchone()[0] is True:
                return [(survey_id, SurveyTemplateRepo.SPAIN_FFQ_ID)]

        return []

    def _local_survey_template_ids_from_survey_ids(self, survey_ids):
        with self._transaction.cursor() as cur:
            # note these ids are unique string ids, not integer ids.
            cur.execute("SELECT survey_id, survey_template_id "
                        "FROM ag.ag_login_surveys WHERE survey_id IN %s",
                        (tuple(survey_ids),))

            return [(x[0], x[1]) for x in cur.fetchall()]

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
                               survey_answers_id=None,
                               creation_time=None):
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
            if creation_time:
                cur.execute("INSERT INTO ag_login_surveys "
                            "(ag_login_id, survey_id, source_id, "
                            "creation_time, survey_template_id) "
                            "VALUES(%s, %s, %s, %s, %s)",
                            (ag_login_id, survey_answers_id, source_id,
                             creation_time, survey_template_id))
            else:
                cur.execute("INSERT INTO ag_login_surveys "
                            "(ag_login_id, survey_id, source_id, "
                            "survey_template_id) "
                            "VALUES(%s, %s, %s, %s)",
                            (ag_login_id, survey_answers_id, source_id,
                             survey_template_id))

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
            try:
                uuid.UUID(survey_id)
                cur.execute("UPDATE polyphenol_ffq_registry SET "
                            "deleted = true, "
                            "source_id = NULL "
                            "WHERE "
                            "account_id = %s AND polyphenol_ffq_id = %s",
                            (acct_id, survey_id))
            except ValueError:
                # Note: we don't care about the error, just means it's not
                # the Polyphenol FFQ
                pass
            try:
                uuid.UUID(survey_id)
                cur.execute("UPDATE spain_ffq_registry SET "
                            "deleted = true, "
                            "source_id = NULL "
                            "WHERE "
                            "account_id = %s AND spain_ffq_id = %s",
                            (acct_id, survey_id))
            except ValueError:
                # Note: we don't care about the error, just means it's not
                # the Spain FFQ
                pass
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
            # Also delete from vioscreen, myfoodrepo, polyphenol, and Spain
            # registries
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
            try:
                uuid.UUID(survey_id)
                cur.execute("UPDATE polyphenol_ffq_registry "
                            "SET deleted = true "
                            "WHERE "
                            "account_id = %s AND "
                            "source_id = %s AND "
                            "polyphenol_ffq_id = %s",
                            (account_id, source_id, survey_id))
            except ValueError:
                # Note: we don't care about the error, just means it's not
                # the Polyphenol FFQ
                pass
            try:
                uuid.UUID(survey_id)
                cur.execute("UPDATE spain_ffq_registry "
                            "SET deleted = true "
                            "WHERE "
                            "account_id = %s AND "
                            "source_id = %s AND "
                            "spain_ffq_id = %s",
                            (account_id, source_id, survey_id))
            except ValueError:
                # Note: we don't care about the error, just means it's not
                # the Spain FFQ
                pass

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
                                   WHERE survey_response_type in ('TEXT',
                                   'STRING')
                                       AND survey_id=%s
                                   )""",
                        (text, survey_id, survey_id))
