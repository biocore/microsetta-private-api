function verify_kit_claim(form_name, submitHandler) {
    // Initialize form validation
    let form_selector = "form[name='" + form_name + "']";
    return function() {
        validateOptions = {
            // Specify validation rules
            rules: {
                // The key name on the left side is the name attribute
                // of an input field. Validation rules are defined
                // on the right side
                kit_name: {
                    required: true,
                    remote: {
                        url: "/check_acct_inputs",
                        type: "post"
                    }
                }
            }
        }
        if (submitHandler != null){
            validateOptions["submitHandler"] = submitHandler;
        }
        $(form_selector).validate(validateOptions);
    };
}

