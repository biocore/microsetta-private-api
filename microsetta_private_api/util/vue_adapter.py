from microsetta_private_api.model.vue.vue_field import (VueInputField,
                                                        VueTextAreaField,
                                                        VueSelectField,
                                                        VueRadiosField,
                                                        VueChecklistField)
from microsetta_private_api.model.vue.vue_group import VueGroup
from microsetta_private_api.model.vue.vue_schema import VueSchema
from collections import defaultdict


def to_vue_field(question, triggered_by=None):
    if question.response_type == "SINGLE":
        if len(question.valid_responses) < 13:
            vue_field = VueRadiosField(question.id,
                                       question.localized_text,
                                       question.valid_responses,
                                       question.css_classes,
                                       question.short_name)
        else:
            vue_field = VueSelectField(question.id,
                                       question.localized_text,
                                       question.valid_responses,
                                       question.css_classes,
                                       question.short_name)
    elif question.response_type == "MULTIPLE":
        vue_field = VueChecklistField(question.id,
                                      question.localized_text,
                                      question.valid_responses,
                                      question.css_classes,
                                      question.short_name)
    elif question.response_type == "STRING":
        vue_field = VueInputField(question.id,
                                  question.localized_text,
                                  question.css_classes,
                                  question.short_name)
    elif question.response_type == "TEXT":
        vue_field = VueTextAreaField(question.id,
                                     question.localized_text,
                                     question.css_classes,
                                     question.short_name)
    else:
        raise ValueError("Unknown question response_type %s" %
                         question.response_type)

    if triggered_by is not None and question.id in triggered_by:
        vue_field.set(triggered_by=triggered_by[question.id])
    return vue_field


def to_vue_group(survey_template_group, triggered_by=None):
    fields = [to_vue_field(q, triggered_by=triggered_by)
              for q in survey_template_group.questions]
    return VueGroup(survey_template_group.localized_text, fields)


def to_vue_schema(survey_template):
    triggered_by = defaultdict(list)
    # Enumerate all question triggers
    for group in survey_template.groups:
        for question in group.questions:
            for trigger in question.triggers:
                # Invert the triggers in db to generate a list of questions and
                # specific responses that trigger each particular question
                triggered_by[trigger.triggered_question_id].append(
                    {'q_id': str(question.id),
                     'response': trigger.trigger_response})

    groups = [to_vue_group(g, triggered_by=triggered_by)
              for g in survey_template.groups]
    return VueSchema(groups, None)
