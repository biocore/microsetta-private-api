function preclude_whitespace(selector) {
    // https://stackoverflow.com/questions/12010275/strip-white-spaces-on-input
    $(selector).bind('input', function(){
        $(this).val(function(_, v){
            return v.replace(/\s+/g, '');
        });
    });
}

// Disable implicit submission for the form with the input name (NOT id).
// While implicit submission is strongly recommended by the HTML
// standards for accessibility purposes, it is causing confusion
// and premature form submission for our user base
function preventImplicitSubmission(form_name){
    let implicit_sub_input_types = ["text", "search", "url", "tel", "email", "password", "date", "month", "week", "time",
        "datetime-local", "number"];
    let partial_selector = 'form[name ="' + form_name + '"] input[type="';
    $.each(implicit_sub_input_types, function(index, value) {
        let input_elements = $(partial_selector + value + '"]');

        // for each input element of the given type in form, disable submit on pressing Enter
        // by making the keydown event return false on presses of that key
        input_elements.each(function() {
            $(this).keydown(function (e) {
                if (e.keyCode === 13) {
                    e.preventDefault();
                    return false;
                }
            });
        });
    });
}

function replicate_text(input_selector, destination_selector)
{
    $(input_selector).bind('input', function(){
        $(this).val(function(_, v){
            $(destination_selector).html(v)
            return v
        });
    });
}

function select_class(input_selector, destination_selector, input_to_class) {
    $(input_selector).change(function(){
        $(this).val(function(_, v){
            $(destination_selector).removeClass()
            $(destination_selector).addClass(input_to_class(v))
            return v
        });
    });
}
