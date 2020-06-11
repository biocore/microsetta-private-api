
function preclude_whitespace(selector)
{
    <!--https://stackoverflow.com/questions/12010275/strip-white-spaces-on-input-->
    $(selector).bind('input', function(){
        $(this).val(function(_, v){
            return v.replace(/\s+/g, '');
        });
});
}