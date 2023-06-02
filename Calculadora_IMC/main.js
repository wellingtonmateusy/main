$(document).ready(function() {
    var result = $('#result');
    var result2 = $('#result2');
    
    $('#result').click(function(){
        $('.number').click(function() {
            var val = $(this).text();
            result.val(result.val() + val);
        });
        $('.clear').click(function() {
            result.val('');
        });
        $('.apagar').click(function(){
            result.val(result.val().slice(0, -1));
        });
        $('.pontuacao').click(function(){
            result.val(result.val() + '.');
        });
    });

    $('#result2').click(function(){
        $('.number').click(function() {
            var val2 =+ $(this).text();
            result2.val(result2.val() + val2);
        });
        $('.clear').click(function() {
            result2.val('');
        });
        $('.apagar').click(function(){
            result2.val(result2.val().slice(0, -1));
        });
        $('.pontuacao').click(function(){
            result2.val(result2.val() + '.');
        });
    });

    $('.clear_tudo').click(function(){
        result.val('');
        result2.val('');
    })

    $('.calculate').click(function() {
        var resultado = result.val() / (result2.val() * result2.val());
        console.log(resultado);
    });
});