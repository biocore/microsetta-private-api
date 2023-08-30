class SurveyTemplateQuestion:
    def __init__(self, question_id, localized_text, short_name,
                 response_type, valid_responses, triggers, css_classes):
        self.id = question_id
        self.localized_text = localized_text
        self.short_name = short_name
        self.response_type = response_type
        self.valid_responses = valid_responses
        self.triggers = triggers
        self.css_classes = css_classes
