function verify_kit_claim() {
    // Initialize form validation on the registration form.
    // It has the name attribute "registration"
    $("form[name='kit_claim_form']").validate({
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
            },
            // Make sure the form is submitted to the destination defined
            // in the "action" attribute of the form when valid
            submitHandler: function (form) {
                form.submit();
            }
        }
    });
};

