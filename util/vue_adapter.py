from model.vue.vue_field import VueInputField, VueTextAreaField, \
                                VueSelectField, VueChecklistField
from model.vue.vue_group import VueGroup
from model.vue.vue_schema import VueSchema


def to_vue_field(question):
    if question.response_type == "SINGLE":
        return VueSelectField(question.id,
                              question.localized_text,
                              question.valid_responses)
    elif question.response_type == "MULTIPLE":
        return VueChecklistField(question.id,
                                 question.localized_text,
                                 question.valid_responses)
    elif question.response_type == "STRING":
        return VueInputField(question.id, question.localized_text)
    elif question.response_type == "TEXT":
        return VueTextAreaField(question.id, question.localized_text)


def to_vue_group(survey_template_group):
    fields = [to_vue_field(q) for q in survey_template_group.questions]
    return VueGroup(survey_template_group.localized_text, fields)


def to_vue_schema(survey_template):
    groups = [to_vue_group(g) for g in survey_template.groups]
    return VueSchema(groups, None)
