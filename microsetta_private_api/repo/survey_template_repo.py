from werkzeug.exceptions import NotFound

from microsetta_private_api.config_manager import SERVER_CONFIG
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
from microsetta_private_api.exceptions import RepoException
from microsetta_private_api.repo.vioscreen_repo import VioscreenRepo


class SurveyTemplateRepo(BaseRepo):

    VIOSCREEN_ID = 10001
    MYFOODREPO_ID = 10002
    POLYPHENOL_FFQ_ID = 10003
    SPAIN_FFQ_ID = 10004
    BASIC_INFO_ID = 10
    AT_HOME_ID = 11
    LIFESTYLE_ID = 12
    GUT_ID = 13
    GENERAL_HEALTH_ID = 14
    HEALTH_DIAG_ID = 15
    ALLERGIES_ID = 16
    DIET_ID = 17
    DETAILED_DIET_ID = 18
    MIGRAINE_ID = 19
    SURFERS_ID = 20
    COVID19_ID = 21
    OTHER_ID = 22

    SURVEY_INFO = {
        # For now, let's keep legacy survey info as well.
        1: SurveyTemplateLinkInfo(
            1,
            "Primary Questionnaire",
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
        7: SurveyTemplateLinkInfo(
            7,
            "Cooking Oils and Oxalate-rich Foods",
            "1.0",
            "local"
        ),
        VIOSCREEN_ID: SurveyTemplateLinkInfo(
            VIOSCREEN_ID,
            "Vioscreen Food Frequency Questionnaire",
            "1.0",
            "remote"
        ),
        MYFOODREPO_ID: SurveyTemplateLinkInfo(
            MYFOODREPO_ID,
            "MyFoodRepo Diet Tracking",
            "1.0",
            "remote"
        ),
        POLYPHENOL_FFQ_ID: SurveyTemplateLinkInfo(
            POLYPHENOL_FFQ_ID,
            "Polyphenols",
            "1.0",
            "remote"
        ),
        SPAIN_FFQ_ID: SurveyTemplateLinkInfo(
            SPAIN_FFQ_ID,
            "Spain Food Frequency Questionnaire",
            "1.0",
            "remote"
        ),
        BASIC_INFO_ID: SurveyTemplateLinkInfo(
            BASIC_INFO_ID,
            "Basic Information",
            "1.0",
            "local"
        ),
        AT_HOME_ID: SurveyTemplateLinkInfo(
            AT_HOME_ID,
            "At Home",
            "1.0",
            "local"
        ),
        LIFESTYLE_ID: SurveyTemplateLinkInfo(
            LIFESTYLE_ID,
            "Lifestyle",
            "1.0",
            "local"
        ),
        GUT_ID: SurveyTemplateLinkInfo(
            GUT_ID,
            "Gut",
            "1.0",
            "local"
        ),
        GENERAL_HEALTH_ID: SurveyTemplateLinkInfo(
            GENERAL_HEALTH_ID,
            "General Health",
            "1.0",
            "local"
        ),
        HEALTH_DIAG_ID: SurveyTemplateLinkInfo(
            HEALTH_DIAG_ID,
            "Health Diagnosis",
            "1.0",
            "local"
        ),
        ALLERGIES_ID: SurveyTemplateLinkInfo(
            ALLERGIES_ID,
            "Allergies",
            "1.0",
            "local"
        ),
        DIET_ID: SurveyTemplateLinkInfo(
            DIET_ID,
            "Diet",
            "1.0",
            "local"
        ),
        DETAILED_DIET_ID: SurveyTemplateLinkInfo(
            DETAILED_DIET_ID,
            "Detailed Diet",
            "1.0",
            "local"
        ),
        MIGRAINE_ID: SurveyTemplateLinkInfo(
            MIGRAINE_ID,
            "Migraine",
            "1.0",
            "local"
        ),
        SURFERS_ID: SurveyTemplateLinkInfo(
            SURFERS_ID,
            "Surfers",
            "1.0",
            "local"
        ),
        COVID19_ID: SurveyTemplateLinkInfo(
            COVID19_ID,
            "COVID-19",
            "1.0",
            "local"
        ),
        OTHER_ID: SurveyTemplateLinkInfo(
            OTHER_ID,
            "Other",
            "1.0",
            "local"
        )
    }

    def __init__(self, transaction):
        super().__init__(transaction)

    def local_surveys(self):
        return {k: v for k, v in self.SURVEY_INFO.items()
                if v.survey_template_type == 'local'}

    def remote_surveys(self):
        return {k: v for k, v in self.SURVEY_INFO.items()
                if v.survey_template_type == 'remote'}

    def list_survey_ids(self):
        with self._transaction.cursor() as cur:
            cur.execute("SELECT DISTINCT survey_id FROM surveys")
            rows = cur.fetchall()
        return [x[0] for x in rows]

    @staticmethod
    def get_survey_template_link_info(survey_id):
        return copy.deepcopy(SurveyTemplateRepo.SURVEY_INFO[survey_id])

    def get_survey_template(self, survey_template_id, language_tag):
        tag_to_col = {
            localization.EN_US: "survey_question.american",
            localization.EN_GB: "survey_question.british",
            localization.ES_MX: "survey_question.spanish",
            localization.ES_ES: "survey_question.spain_spanish"
        }

        if language_tag not in tag_to_col:
            raise NotFound("Survey localization unavailable: %s" %
                           language_tag)

        with self._transaction.cursor() as cur:

            cur.execute(
                "SELECT count(*) FROM surveys WHERE survey_id=%s",
                (survey_template_id,)
            )

            if cur.fetchone()[0] == 0:
                raise NotFound("No such survey")

            cur.execute(
                "SELECT "
                "group_questions.survey_group, "
                "survey_question.survey_question_id, " +
                tag_to_col[language_tag] + ", " +
                "survey_question.question_shortname, "
                "survey_question_response_type.survey_response_type, "
                "survey_question.css_classes "
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
                (survey_template_id,))

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
                css_classes = r[5]

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

                # Quick fix to correctly sort country names in Spanish
                if (language_tag == localization.ES_MX or language_tag ==
                    localization.ES_ES) and (question_id == 110 or
                                             question_id == 148):
                    responses[1:len(responses)] = \
                        sorted(responses[1:len(responses)])

                question = SurveyTemplateQuestion(question_id,
                                                  localized_text,
                                                  short_name,
                                                  response_type,
                                                  responses,
                                                  triggers,
                                                  css_classes)
                cur_questions.append(question)

            if cur_group_id is not None:
                group_localized_text = self._get_group_localized_text(
                    cur_group_id,
                    language_tag)
                all_groups.append(SurveyTemplateGroup(
                    group_localized_text,
                    cur_questions))

            return SurveyTemplate(survey_template_id, language_tag, all_groups)

    def _get_group_localized_text(self, group_id, language_tag):
        tag_to_col = {
            localization.EN_US: "american",
            localization.EN_GB: "british",
            localization.ES_MX: "spanish",
            localization.ES_ES: "spain_spanish"
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
            localization.ES_ES: "survey_response.spain_spanish",
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

    def create_myfoodrepo_entry(self, account_id, source_id):
        """Create a MyFoodRepo entry if a slot is available

        Parameters
        ----------
        account_id : str, UUID
            The account UUID
        source_id : str, UUID
            The source UUID

        Returns
        -------
        bool
            True if a slot was obtained, False otherwise
        """
        with self._transaction.cursor() as cur:
            # we are testing for availability based on entries in the
            # myfoodrepo_registry. to ensure workers see accurate state,
            # we lock the table prior to our slot and update check forcing
            # the effort in this method to be serial.
            self._transaction.lock_table("myfoodrepo_registry")
            if self.myfoodrepo_slots_available() > 0:
                # Add to the myfoodrepo_registry
                cur.execute("""INSERT INTO myfoodrepo_registry (account_id,
                                                                source_id)
                               VALUES (%s, %s)""",
                            (account_id, source_id))

                return True
            else:
                return False

    def set_myfoodrepo_id(self, account_id, source_id, mfr_id):
        """Set the MyFoodRepo ID of a registry entry

        Parameters
        ----------
        account_id : str, UUID
            The account UUID
        source_id : str, UUID
            The source UUID
        mfr_id : str
            A created MyFoodRepo subject ID

        Raises
        ------
        KeyError
            If the source already has a subject assigned
        """
        with self._transaction.cursor() as cur:
            existing, created = self.get_myfoodrepo_id_if_exists(account_id,
                                                                 source_id)

            if existing is not None:
                raise KeyError(f"{account_id} and {source_id} are already "
                               f"assigned to {existing}")

            if existing is None and created is None:
                raise KeyError(f"{account_id} and {source_id} do not have "
                               f"a slot")

            # Put a survey into ag_login_surveys
            cur.execute("INSERT INTO ag_login_surveys("
                        "ag_login_id, "
                        "survey_id, "
                        "vioscreen_status, "
                        "source_id, "
                        "survey_template_id) "
                        "VALUES(%s, %s, %s, %s, %s)",
                        (account_id, mfr_id, None, source_id,
                         SurveyTemplateRepo.MYFOODREPO_ID))

            # Add to the myfoodrepo_registry
            cur.execute("""UPDATE myfoodrepo_registry
                           SET myfoodrepo_id=%s
                           WHERE account_id=%s AND source_id=%s""",
                        (mfr_id, account_id, source_id))

    def delete_myfoodrepo(self, account_id, source_id):
        """Intended for admin use, remove MyFoodRepo entries

        This method is idempotent

        This method deletes ALL MyFoodRepo surveys associated with an account
        and source

        This is a hard delete, we REMOVE rows rather than setting a flag

        Parameters
        ----------
        account_id : str, UUID
            The account UUID
        source_id : str, UUID
            The source UUID
        """
        with self._transaction.cursor() as cur:
            existing, created = self.get_myfoodrepo_id_if_exists(account_id,
                                                                 source_id)
            if existing is not None:
                cur.execute("""DELETE FROM ag.ag_login_surveys
                               WHERE ag_login_id=%s
                                   AND source_id=%s
                                   AND survey_id=%s""",
                            (account_id, source_id, existing))

            cur.execute("""DELETE FROM ag.myfoodrepo_registry
                           WHERE account_id=%s
                               AND source_id=%s""",
                        (account_id, source_id))

    def get_myfoodrepo_id_if_exists(self, account_id, source_id):
        """Return a MyFoodRepo ID if one exists

        Parameters
        ----------
        account_id : str, UUID
            The account UUID
        source_id : str, UUID
            The source UUID

        Returns
        -------
        (str or None, datetime or None)
            The associated MyFoodRepo ID and the time it was created.
            If (None, <time>), it indicates a slot is created but the subject
            ID has not been assigned.
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT myfoodrepo_id, creation_timestamp
                           FROM myfoodrepo_registry
                           WHERE account_id=%s AND source_id=%s""",
                        (account_id, source_id))
            res = cur.fetchone()

            if res is None:
                return (None, None)
            else:
                return res

    def myfoodrepo_slots_available(self):
        """Return the available number of slots

        Returns
        -------
        int
            The number of slots available
        """
        maximum_slots = SERVER_CONFIG['myfoodrepo_slots']
        interval = "'7 days'"
        with self._transaction.cursor() as cur:
            cur.execute(f"""SELECT count(*)
                            FROM myfoodrepo_registry
                            WHERE creation_timestamp >= (
                                NOW() - INTERVAL {interval}
                            )""")
            count = cur.fetchone()[0]
            return max(0, maximum_slots - count)

    def myfoodrepo_slots_total(self):
        """Return the total number of slots

        Returns
        -------
        int
            The total number of slots
        """
        maximum_slots = SERVER_CONFIG['myfoodrepo_slots']
        return maximum_slots

    def create_polyphenol_ffq_entry(self, account_id, source_id,
                                    language_tag, study):
        """Return a newly created Polyphenol FFQ ID

        Parameters
        ----------
        account_id : str, UUID
            The account UUID
        source_id : str, UUID
            The source UUID
        language_tag: str
            The user's language tag
        study: str
            The study variable we'll pass to Danone's FFQ

        Returns
        -------
        UUID
            The newly created Polyphenol FFQ ID
        """
        with self._transaction.cursor() as cur:
            cur.execute("""INSERT INTO ag.polyphenol_ffq_registry
                           (account_id, source_id, language_tag, study)
                           VALUES (%s, %s, %s, %s)
                           RETURNING polyphenol_ffq_id""",
                        (account_id, source_id, language_tag, study))
            polyphenol_ffq_id = cur.fetchone()[0]
            if polyphenol_ffq_id is None:
                raise RepoException("Error creating Polyphenol FFQ entry")
            else:
                # Put a survey into ag_login_surveys
                cur.execute("INSERT INTO ag_login_surveys("
                            "ag_login_id, "
                            "survey_id, "
                            "vioscreen_status, "
                            "source_id, "
                            "survey_template_id) "
                            "VALUES(%s, %s, %s, %s, %s)",
                            (account_id, polyphenol_ffq_id, None, source_id,
                             SurveyTemplateRepo.POLYPHENOL_FFQ_ID))

                return polyphenol_ffq_id

    def get_polyphenol_ffq_id_if_exists(self, account_id, source_id):
        """Return a Polyphenol FFQ ID if one exists

        Parameters
        ----------
        account_id : str, UUID
            The account UUID
        source_id : str, UUID
            The source UUID

        Returns
        -------
        (UUID, str) or (None, None)
            The associated Polyphenol FFQ ID and study
            It's impossible to find one without the other
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT polyphenol_ffq_id, study
                           FROM ag.polyphenol_ffq_registry
                           WHERE account_id=%s AND source_id=%s""",
                        (account_id, source_id))
            res = cur.fetchone()

            if res is None:
                return (None, None)
            else:
                return res

    def delete_polyphenol_ffq(self, account_id, source_id):
        """Intended for admin use, remove Polyphenol FFQ entries

        This method is idempotent.

        This method deletes ALL Polyphenol FFQ surveys associated with an
        account and source

        This is a hard delete, we REMOVE rows rather than setting a flag

        Parameters
        ----------
        account_id : str, UUID
            The account UUID
        source_id : str, UUID
            The source UUID
        """
        with self._transaction.cursor() as cur:
            existing, _ = self.get_polyphenol_ffq_id_if_exists(account_id,
                                                               source_id)
            if existing is not None:
                cur.execute("""DELETE FROM ag.ag_login_surveys
                               WHERE ag_login_id=%s
                                   AND source_id=%s
                                   AND survey_id=%s""",
                            (account_id, source_id, existing))
            cur.execute("""DELETE FROM ag.polyphenol_ffq_registry
                           WHERE account_id=%s
                               AND source_id=%s""",
                        (account_id, source_id))

    def create_spain_ffq_entry(self, account_id, source_id):
        """Return a newly created Spain FFQ ID

        Parameters
        ----------
        account_id : str, UUID
            The account UUID
        source_id : str, UUID
            The source UUID

        Returns
        -------
        UUID
            The newly created Spain FFQ ID
        """
        with self._transaction.cursor() as cur:
            cur.execute("""INSERT INTO ag.spain_ffq_registry
                           (account_id, source_id)
                           VALUES (%s, %s)
                           RETURNING spain_ffq_id""",
                        (account_id, source_id))
            spain_ffq_id = cur.fetchone()[0]
            if spain_ffq_id is None:
                raise RepoException("Error creating Spain FFQ entry")
            else:
                # Put a survey into ag_login_surveys
                cur.execute("INSERT INTO ag_login_surveys("
                            "ag_login_id, "
                            "survey_id, "
                            "vioscreen_status, "
                            "source_id, "
                            "survey_template_id) "
                            "VALUES(%s, %s, %s, %s, %s)",
                            (account_id, spain_ffq_id, None, source_id,
                             SurveyTemplateRepo.SPAIN_FFQ_ID))

                return spain_ffq_id

    def get_spain_ffq_id_if_exists(self, account_id, source_id):
        """Return a Spain FFQ ID if one exists

        Parameters
        ----------
        account_id : str, UUID
            The account UUID
        source_id : str, UUID
            The source UUID

        Returns
        -------
        UUID or None
            The associated Spain FFQ ID or None
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT spain_ffq_id
                           FROM ag.spain_ffq_registry
                           WHERE account_id=%s AND source_id=%s""",
                        (account_id, source_id))
            res = cur.fetchone()

            if res is None:
                return None
            else:
                return res[0]

    def delete_spain_ffq(self, account_id, source_id):
        """Intended for admin use, remove Spain FFQ entries

        This method is idempotent

        This method deletes ALL Spain FFQ surveys associated with an account
        and source

        This is a hard delete, we REMOVE rows rather than setting a flag

        Parameters
        ----------
        account_id : str, UUID
            The account UUID
        source_id : str, UUID
            The source UUID
        """
        with self._transaction.cursor() as cur:
            existing = self.get_spain_ffq_id_if_exists(account_id,
                                                       source_id)
            if existing is not None:
                cur.execute("""DELETE FROM ag.ag_login_surveys
                               WHERE ag_login_id=%s
                                   AND source_id=%s
                                   AND survey_id=%s""",
                            (account_id, source_id, existing))

            cur.execute("""DELETE FROM ag.spain_ffq_registry
                           WHERE account_id=%s
                               AND source_id=%s""",
                        (account_id, source_id))

    def get_vioscreen_sample_to_user(self):
        """Obtain a mapping of sample barcode to vioscreen user"""
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT barcode, vio_id
                           FROM ag.vioscreen_registry
                           JOIN ag.ag_kit_barcodes
                               ON sample_id=ag_kit_barcode_id
                           WHERE vio_id IS NOT NULL""")
            return {r[0]: r[1] for r in cur.fetchall()}

    def create_vioscreen_id(self, account_id, source_id,
                            sample_id=None,
                            registration_code=None):
        with self._transaction.cursor() as cur:
            # This transaction scans for existing IDs,
            # then generates a new ID if none exist
            # To prevent workers from seeing stale state,
            # and thus each generating multiple new IDs
            # in the case of multiple workers,
            # we lock the vioscreen_registry table
            self._transaction.lock_table("vioscreen_registry")
            # test if an existing ID is available
            existing = self.get_vioscreen_id_if_exists(account_id, source_id,
                                                       sample_id,
                                                       registration_code)

            if existing is None:
                vioscreen_id = secrets.token_hex(8)

                # if they're using a registration code, we need to make sure
                # it hasn't already been used
                if registration_code is not None:
                    vio_repo = VioscreenRepo(self._transaction)
                    unused_code = vio_repo.is_code_unused(registration_code)

                    if unused_code is False:
                        # the code is either invalid or has been used
                        raise RepoException("Registration code is invalid")
                    else:
                        # the code is valid and unused, so let's mark it used
                        # and proceed
                        cur.execute(
                            "UPDATE campaign.ffq_registration_codes "
                            "SET registration_code_used = NOW() "
                            "WHERE ffq_registration_code = %s",
                            (registration_code, )
                        )

                # Put a survey with status -1 into ag_login_surveys
                cur.execute("INSERT INTO ag_login_surveys("
                            "ag_login_id, "
                            "survey_id, "
                            "vioscreen_status, "
                            "source_id, "
                            "survey_template_id) "
                            "VALUES(%s, %s, %s, %s, %s)",
                            (account_id, vioscreen_id, -1, source_id,
                             self.VIOSCREEN_ID))

                # And add it to the registry to keep track of the survey if
                # user quits out then wants to resume the survey.
                cur.execute(
                    "INSERT INTO ag.vioscreen_registry ("
                    "account_id, source_id, vio_id, sample_id, "
                    "registration_code) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (account_id, source_id, vioscreen_id, sample_id,
                     registration_code)
                )
            else:
                vioscreen_id = existing
        return vioscreen_id

    def get_vioscreen_id_if_exists(self, account_id, source_id,
                                   sample_id=None,
                                   registration_code=None,
                                   timestamp=None):
        """Obtain a vioscreen ID if it exists"""
        with self._transaction.cursor() as cur:
            # Find an active vioscreen survey for this account+source+sample
            # (deleted surveys are not active)
            if sample_id is not None:
                cur.execute("SELECT vio_id FROM "
                            "vioscreen_registry WHERE "
                            "account_id=%s AND "
                            "source_id=%s AND "
                            "sample_id=%s AND "
                            "deleted=false",
                            (account_id, source_id, sample_id))
            elif registration_code is not None:
                cur.execute("SELECT vio_id FROM "
                            "vioscreen_registry WHERE "
                            "account_id=%s AND "
                            "source_id=%s AND "
                            "registration_code=%s AND "
                            "deleted=false",
                            (account_id, source_id, registration_code))
            elif timestamp is not None:
                cur.execute("SELECT DISTINCT "
                            "vioscreen_registry.vio_id, "
                            "ag_login_surveys.creation_time "
                            "FROM vioscreen_registry "
                            "INNER JOIN ag_login_surveys "
                            "ON vioscreen_registry.vio_id = "
                            "ag_login_surveys.survey_id "
                            "WHERE vioscreen_registry.account_id = %s "
                            "AND vioscreen_registry.source_id = %s "
                            "AND deleted=false "
                            "AND ag_login_surveys.creation_time >= %s"
                            "ORDER BY ag_login_surveys.creation_time DESC ",
                            (account_id, source_id, timestamp))
            else:
                cur.execute("SELECT DISTINCT vioscreen_registry.vio_id, "
                            "ag_login_surveys.creation_time "
                            "FROM vioscreen_registry "
                            "INNER JOIN ag_login_surveys "
                            "ON vioscreen_registry.vio_id = "
                            "ag_login_surveys.survey_id "
                            "WHERE vioscreen_registry.account_id = %s "
                            "AND vioscreen_registry.source_id = %s "
                            "AND deleted=false "
                            "ORDER BY ag_login_surveys.creation_time DESC ",
                            (account_id, source_id))
            rows = cur.fetchall()
            if rows is None or len(rows) == 0:
                return None
            else:
                return rows[0][0]

    def get_vioscreen_all_ids_if_exists(self, account_id, source_id):
        """Obtain all vioscreen IDs for a source

        This method captures all IDs including IDs with the "deleted"
        flag set.

        Parameters
        ----------
        account_id : str, UUID
            The account UUID
        source_id : str, UUID
            The source UUID

        Returns
        tuple or None
            The tuple of IDs or None of there are no associated IDs
        """
        with self._transaction.cursor() as cur:
            cur.execute("""SELECT vio_id
                           FROM vioscreen_registry
                           WHERE account_id = %s
                               AND source_id = %s""",
                        (account_id, source_id))
            ids = tuple([r[0] for r in cur.fetchall()])
            if len(ids) > 0:
                return ids
            else:
                return None

    def delete_vioscreen(self, account_id, source_id):
        """Intended for admin use, remove Vioscreen entries from the system

        This method is idempotent

        This method deletes ALL Vioscreen FFQ surveys associated with an
        account and source

        This is a hard delete, we REMOVE rows rather than setting a flag

        Parameters
        ----------
        account_id : str, UUID
            The account UUID
        source_id : str, UUID
            The source UUID
        """
        with self._transaction.cursor() as cur:
            # get all vioscreen user names associated with the source
            cur.execute("""SELECT vio_id
                           FROM vioscreen_registry
                           WHERE account_id=%s
                               AND source_id=%s""",
                        (account_id, source_id))
            vio_ids = tuple([r[0] for r in cur.fetchall()])

            if len(vio_ids) == 0:
                return None

            # get all sessions associated with the vio_ids
            cur.execute("""SELECT sessionid
                           FROM ag.vioscreen_sessions
                           WHERE username IN %s""",
                        (vio_ids, ))
            sessions = tuple([r[0] for r in cur.fetchall()])

            if len(sessions) > 0:
                for tbl in ('dietaryscore', 'eatingpatterns', 'foodcomponents',
                            'foodconsumption', 'foodconsumptioncomponents',
                            'percentenergy', 'supplements', 'mpeds'):
                    tbl = f'ag.vioscreen_{tbl}'
                    cur.execute("DELETE FROM " + tbl + " " +
                                "WHERE sessionid IN %s",
                                (sessions, ))
                cur.execute("""DELETE FROM ag.vioscreen_sessions
                               WHERE sessionid IN %s""",
                            (sessions, ))

            cur.execute("""DELETE FROM ag.vioscreen_registry
                           WHERE account_id = %s
                               AND source_id = %s""",
                        (account_id, source_id))

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
                                 'GENDER',
                                 'GENDER_v2')
                             AND s.ag_login_id = %s
                             and s.source_id = %s""",
                        (account_id, source_id))

            results = {name: value for name, value in cur.fetchall()}
            birth_year = results.get('BIRTH_YEAR')
            height_units = results.get('HEIGHT_UNITS')
            weight_units = results.get('WEIGHT_UNITS')

            # If the user has responded to the new form of the gender question
            # use that. Otherwise, fall back to the old question.
            gender = results.get('GENDER_v2')
            if gender is None:
                gender = results.get('GENDER')

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
                if height.startswith('['):
                    # old survey_answers_other responses are of the form
                    # '["foo"]' :/
                    # TODO: patch all old answers to remove extraneous [""]?
                    height = height[2:-2]

                if height == "":
                    height = None
                else:
                    height = float(height)
                    if height_units == 'centimeters':
                        # to inches
                        height = height / 2.54

                    # Per email from David @ Viocare, height must be between
                    # 24 and 96 inches.
                    if height < 24.0 or height > 96.0:
                        height = None
            else:
                # should not occur but just in case
                height = None

            if weight == UNSPECIFIED or weight_units == UNSPECIFIED:
                weight = None
            elif weight is not None:
                if weight.startswith('['):
                    # old survey_answers_other responses are of the form
                    # '["foo"]' :/
                    weight = weight[2:-2]

                if weight == "":
                    weight = None
                else:
                    weight = float(weight)
                    if weight_units == 'kilograms':
                        # to pounds
                        weight = weight * 2.20462

                    # Per email from David @ Viocare, weight must be between
                    # 30 and 600 pounds.
                    if weight < 30.0 or weight > 600.0:
                        weight = None
            else:
                # should not occur but just in case
                weight = None

        return (birth_year, gender, height, weight)

    def has_external_surveys(self, account_id, source_id):
        """Test whether a source has any external surveys associated

        Parameters
        ----------
        account_id : str, UUID
            The account UUID
        source_id : str, UUID
            The source UUID

        Returns
        -------
        boolean
            True indicates the user has an external survey associated, false
            otherwise
        """
        getters = (self.get_myfoodrepo_id_if_exists,
                   self.get_polyphenol_ffq_id_if_exists,
                   self.get_spain_ffq_id_if_exists,
                   self.get_vioscreen_all_ids_if_exists)

        for get in getters:
            res = get(account_id, source_id)

            # the if_exists methods are inconsistent in return type, yay
            if isinstance(res, tuple):
                if res[0] is not None:
                    return True
            else:
                if res is not None:
                    return True

        return False

    def get_date_survey_last_taken(self, source_id, survey_template_id):
        """ Get the date that the given source last took the given
            survey_Template_id

        Parameters
        ----------
        source_id : str
            The id of the source
        survey_template_id : int or str
            The id of the survey in question

        Returns
        -------
        datetime or None
            If it finds a result, it returns the datetime. Otherwise, None.
        """
        with self._transaction.cursor() as cur:
            cur.execute("SELECT MAX(creation_time) "
                        "FROM ag.ag_login_surveys "
                        "WHERE source_id = %s AND survey_template_id = %s",
                        (source_id, survey_template_id))
            r = cur.fetchone()
            if r is None:
                return None
            else:
                return r[0]

    def migrate_responses(self, source_id, survey_template_id):
        '''
        Get all survey responses associated with a source and survey_template
         and migrate them. Will pull from past results if they are found,
         including legacy template answers.
        :param source_id: A source (the provider of a sample)
        :param survey_template_id: A survey template id.
        :return: A filled survey_template dict
        '''
        sql = """SELECT *
                 FROM  (SELECT a.survey_question_id,
                               a.response,
                               e.creation_time,
                               f.survey_response_type
                        FROM   ag.survey_answers a
                               JOIN ag.group_questions c
                                 ON a.survey_question_id = c.survey_question_id
                               JOIN ag.surveys d
                                 ON c.survey_group = d.survey_group
                               JOIN ag.ag_login_surveys e
                                 ON a.survey_id = e.survey_id
                               JOIN ag.survey_question_response_type f
                                 ON a.survey_question_id = f.survey_question_id
                               JOIN ag.survey_question g
                                 ON a.survey_question_id = g.survey_question_id
                        WHERE  e.source_id = %s
                               AND d.survey_id = %s
                               AND g.retired = false
                        UNION
                        SELECT a.survey_question_id,
                               a.response,
                               e.creation_time,
                               f.survey_response_type
                        FROM   ag.survey_answers_other a
                               JOIN ag.group_questions c
                                 ON a.survey_question_id = c.survey_question_id
                               JOIN ag.surveys d
                                 ON c.survey_group = d.survey_group
                               JOIN ag.ag_login_surveys e
                                 ON a.survey_id = e.survey_id
                               JOIN ag.survey_question_response_type f
                                 ON a.survey_question_id = f.survey_question_id
                               JOIN ag.survey_question g
                                 ON a.survey_question_id = g.survey_question_id
                        WHERE  e.source_id = %s
                                 AND d.survey_id = %s
                                 AND g.retired = false) t
                 ORDER BY creation_time ASC,
                          survey_question_id ASC"""

        with self._transaction.cursor() as cur:
            cur.execute(sql, (source_id, survey_template_id, source_id,
                              survey_template_id,))
            rows = cur.fetchall()

            # create an empty template to fill-in.
            results = self._generate_empty_survey(survey_template_id)

            multiple_timestamps = {}
            for question_id, response, creation_time, response_type in rows:
                # responses are from earliest to latest thus older answers
                # will be overwritten with newer ones as need be, according
                # to creation time ASC.
                question_id = str(question_id)

                if response_type == 'MULTIPLE':
                    # For questions that are MULTIPLE (checkbox lists), we
                    # need to keep track of which survey submission each
                    # response is from and reset the list if we find a newer
                    # survey submission
                    if len(results[question_id]) == 0:
                        results[question_id].append(response)
                        multiple_timestamps[question_id] = creation_time
                    else:
                        if creation_time == multiple_timestamps[question_id]:
                            # same survey submission, so append
                            results[question_id].append(response)
                        else:
                            # we just hit a newer survey, reset the list
                            results[question_id] = [response]
                            multiple_timestamps[question_id] = creation_time
                else:
                    # SINGLE, STRING, and TEXT types
                    results[question_id] = response

            return results

    def _generate_empty_survey(self, survey_template_id, return_tuple=False):
        """ Generate an empty survey template for a given template ID and
            fill in the responses with 'Unspecified' as needed.

        Parameters
        ----------
        survey_template_id : int or str
            The id for which we're generating a survey template
        return_tuple : bool
            If set to True, each question's value is a tuple, rather than just
            a an array/string

        Returns
        -------
        dict of questions
            If return_tuple is False, the form is
                {question_id: question_response}
            If return_tuple is True, the form is
                {question_id: (question_response, None)}
        """
        # various parts of the code base will push either int or str in
        # for survey_template_id, so we cast to int here
        survey_template_id = int(survey_template_id)

        if survey_template_id in self.SURVEY_INFO:
            if survey_template_id in [self.VIOSCREEN_ID,
                                      self.MYFOODREPO_ID,
                                      self.POLYPHENOL_FFQ_ID,
                                      self.SPAIN_FFQ_ID]:
                raise ValueError("survey_template_id must be for a local "
                                 "survey")
        else:
            raise ValueError("invalid value for survey_template_id")

        # Note a.survey_id is actually a survey_template_id
        sql = """SELECT b.survey_question_id,
                        c.survey_response_type
                 FROM   ag.surveys a
                        JOIN ag.group_questions b
                          ON a.survey_group = b.survey_group
                        JOIN ag.survey_question_response_type c
                          ON b.survey_question_id = c.survey_question_id
                        JOIN ag.survey_question d
                          ON d.survey_question_id = b.survey_question_id
                 WHERE  a.survey_id = %s
                        AND d.retired = false
                 ORDER  BY survey_id,
                           survey_question_id"""

        with self._transaction.cursor() as cur:
            cur.execute(sql, (survey_template_id,))

            rows = cur.fetchall()

            results = {}
            for row in rows:
                question_id = str(row[0])
                response_type = row[1]

                if response_type == 'MULTIPLE':
                    if return_tuple:
                        results[question_id] = ([], None)
                    else:
                        results[question_id] = []
                else:
                    if return_tuple:
                        results[question_id] = ("", None)
                    else:
                        results[question_id] = ""

            return results

    def get_template_ids_from_survey_ids(self, survey_ids):
        '''
        returns a list of (template_id, survey_id) tuples.
        :param survey_ids: A list of survey ids.
        :return: A list of (survey_id, survey_template_id) tuples.
        '''
        with self._transaction.cursor() as cur:
            # with the new survey_template_id column in ag_login_surveys,
            # retrieving the template_ids for both remote and local surveys
            # is now trivial.
            cur.execute("SELECT survey_id, survey_template_id "
                        "FROM ag.ag_login_surveys WHERE survey_id IN %s",
                        (tuple(survey_ids),))

            return [(x[0], x[1]) for x in cur.fetchall()]
