class SurveyTemplateQuestion:
    def __init__(self, localized_text, short_name,
                 response_type, valid_responses, triggers):
        self.localized_text = localized_text
        self.short_name = short_name
        self.response_type = response_type
        self.valid_responses = valid_responses
        self.triggers = triggers
