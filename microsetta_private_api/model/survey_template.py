class SurveyTemplate:
    def __init__(self, survey_id, locale, groups):
        self.id = survey_id
        self.locale = locale
        self.groups = groups


class SurveyTemplateLinkInfo:
    def __init__(self, survey_template_id, survey_template_title,
                 survey_template_version, survey_template_type,
                 survey_scope, survey_is_required):
        self.survey_template_id = survey_template_id
        self.survey_template_title = survey_template_title
        self.survey_template_version = survey_template_version
        self.survey_template_type = survey_template_type
        self.survey_scope = survey_scope
        self.survey_is_required = survey_is_required

    def to_api(self, survey_answers_id):
        return {
            "survey_id": survey_answers_id,
            "survey_template_id": self.survey_template_id,
            "survey_template_title": self.survey_template_title,
            "survey_template_version": self.survey_template_version,
            "survey_template_type": self.survey_template_type,
            "survey_scope": self.survey_scope,
            "survey_is_required": self.survey_is_required
        }
