$(document).ready(function(){
    $('#tecla1').click(function(){
        var number = ('diplay').val
        $(this).html(`<input type="number" name="display" value=${number}/>`);
    })
})