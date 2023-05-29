$(document).ready(function() {
    var result = $('#result');
    
    $('.number').click(function() {
        var val = $(this).text();
        result.val(result.val() + val);
    });
    
    $('.operator').click(function() {
        var val = $(this).text();
        result.val(result.val() + ' ' + val + ' ');
    });
    
    $('.apagaultnum').click(function(){
        result.val(result.val().slice(0, -1));
    });

    $('.clear').click(function() {
        result.val('');
    });

    $('.apagar').click(function(){
        result.val(result.val().slice(0, -1));
    });

    $('.divididopor100').click(function(){
        result.val(result.val() / 100);
    })

    $('.1dividido').click(function(){
        result.val(1 / result.val());
    });

    $('.xelemesmo').click(function(){
        result.val(result.val() * result.val());
    });

    $('.menos').click(function(){
        result.val('- ' + result.val());
    });

    $('.pontuacao').click(function(){
        result.val(result.val() + '.');
    });

    $('.calculate').click(function() {
        var expression = result.val();
        var answer = eval(expression);
        result.val(answer);
    });
});
