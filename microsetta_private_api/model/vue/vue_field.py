class VueField:

    # Field properties include:
    # type, label, model, id, inputName, featured, visible, disabled,
    # required, multi, default, hint, help, validator,
    # validateDebounceTime, styleClasses, buttons, attributes
    # https://vue-generators.gitbook.io/vue-generators/fields/field_properties
    #
    # There are also additional properties dependent on the type
    def __init__(self, type_, label, model, id_, input_name, featured, visible,
                 disabled, required, multi, default, hint, help_, validator,
                 validate_debounce_time, style_classes, buttons, attributes,
                 shortname):
        # Type of Vue field displayed to user
        self.type = type_
        # Label of the field
        self.label = label
        # id determining default value from the model
        self.model = model
        # id of the field
        self.id = id_
        # name attribute of the field
        self.inputName = input_name
        # Should the field/label be bold
        self.featured = featured
        # Should the field be visible
        self.visible = visible
        # Should the field be disabled
        self.disabled = disabled
        # Should the field be required
        self.required = required
        # If true, visible only if multiple is true on the component attr
        self.multi = multi
        # Default value of the field
        self.default = default
        # Hint shown below the field to help user fill in the field
        self.hint = hint
        # Tooltip on hover to help the user fill in the field
        self.help = help_
        # Validation function: Built in validators are:
        # "number", "integer", "double", "string", "array", "date", "regexp",
        # "email", "url", "creditCard", "alpha", "alphaNumeric"
        self.validator = validator
        # Time in milliseconds before alerting the user when validation fails
        # If set, overrides the default for this particular field
        self.validateDebounceTime = validate_debounce_time
        # Additional css classes
        self.styleClasses = style_classes
        # Additional buttons associated with field
        # (generate password/link etc)
        self.buttons = buttons
        # Additional attributes to add to the field
        self.attributes = attributes
        # the question shortname if appicable
        self.shortname = shortname

    def set(self, **attributes):
        for key in attributes:
            setattr(self, key, attributes[key])
        return self


class VueInputField(VueField):
    def __init__(self, question_id, question_text, question_shortname=None):
        super().__init__(
            type_="input",
            label=question_text,
            model=str(question_id),
            id_=str(question_id),
            input_name=str(question_id),
            featured=False,
            visible=True,
            disabled=False,
            required=False,
            multi=False,
            default=None,
            hint=None,
            help_=None,
            validator="string",
            validate_debounce_time=None,
            style_classes=None,
            buttons=None,
            attributes=None,
            shortname=question_shortname
        )
        self.inputType = "text"


class VueTextAreaField(VueField):
    def __init__(self, question_id, question_text, question_shortname=None):
        super().__init__(
            type_="textArea",
            label=question_text,
            model=str(question_id),
            id_=str(question_id),
            input_name=str(question_id),
            featured=False,
            visible=True,
            disabled=False,
            required=False,
            multi=False,
            default=None,
            hint=None,
            help_=None,
            validator="string",
            validate_debounce_time=None,
            style_classes=None,
            buttons=None,
            attributes=None,
            shortname = question_shortname
        )
        self.autocomplete = None
        self.max = None
        self.min = None
        self.placeholder = None
        self.readonly = False
        self.rows = 5


class VueSelectField(VueField):
    def __init__(self, question_id, question_text, valid_responses,
                 question_shortname=None):
        super().__init__(
            type_="select",
            label=question_text,
            model=str(question_id),
            id_=str(question_id),
            input_name=str(question_id),
            featured=False,
            visible=True,
            disabled=False,
            required=False,
            multi=False,
            default=valid_responses[0],
            hint=None,
            help_=None,
            validator=None,
            validate_debounce_time=None,
            style_classes=None,
            buttons=None,
            attributes=None,
            shortname=question_shortname
        )
        self.values = valid_responses
        self.selectOptions = {
            "hideNoneSelectedText": True,
            "value": valid_responses[0]
        }


class VueChecklistField(VueField):
    def __init__(self, question_id, question_text, valid_responses,
                 question_shortname=None):
        super().__init__(
            type_="checklist",
            label=question_text,
            model=str(question_id),
            id_=str(question_id),
            input_name=str(question_id),
            featured=False,
            visible=True,
            disabled=False,
            required=False,
            multi=True,
            default=None,
            hint=None,
            help_=None,
            validator=None,
            validate_debounce_time=None,
            style_classes=None,
            buttons=None,
            attributes=None,
            shortname=question_shortname
        )
        self.listBox = False
        self.values = valid_responses
        self.selectOptions = {}


class VueDateTimePickerField(VueField):
    def __init__(self, question_id, question_text, question_shortname=None):
        super().__init__(
            type_="dateTimePicker",
            label=question_text,
            model=str(question_id),
            id_=str(question_id),
            input_name=str(question_id),
            featured=False,
            visible=True,
            disabled=False,
            required=False,
            multi=False,
            default=None,
            hint=None,
            help_=None,
            validator=None,
            validate_debounce_time=None,
            style_classes=None,
            buttons=None,
            attributes=None,
            shortname=question_shortname
        )
        self.dateTimePickerOptions = {
            "format": "YYYY-MM-DD HH:mm:ss"
        }
