
function preclude_whitespace(selector)
{
    <!--https://stackoverflow.com/questions/12010275/strip-white-spaces-on-input-->
    $(selector).bind('input', function(){
        $(this).val(function(_, v){
            return v.replace(/\s+/g, '');
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

function select_class(input_selector, destination_selector, input_to_class)
{
    $(input_selector).change(function(){
        $(this).val(function(_, v){
            $(destination_selector).removeClass()
            $(destination_selector).addClass(input_to_class(v))
            return v
        });
    });
}
