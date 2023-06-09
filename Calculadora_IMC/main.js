$(document).ready(function() {
    var result = $('#result');
    var result2 = $('#result2');

    buttons2 = $('.buttons2').css('display', 'none');
    buttons = $('.buttons').css('display', 'flex');
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
    $('.calculate1').click(function(){
        $('.mensagem').css('display', 'block')
    });

    $('#result2').click(function(){
        buttons = $('.buttons').css('display', 'none');
        buttons2 = $('.buttons2').css('display', 'flex');
        $('.number2').click(function() {
            var val2 = $(this).text();
            result2.val(result2.val() + val2);
        });
        $('.clear2').click(function() {
            result2.val('');
        });
        $('.apagar2').click(function(){
            result2.val(result2.val().slice(0, -1));
        });
        $('.pontuacao2').click(function(){
            result2.val(result2.val() + '.');
        });
        $('.calculate2').click(function() {
            var resultado = result.val() / (result2.val() * result2.val());
            
            if(result.val() == 0){
                $('.mensagem').css('display', 'block')
            }else{
                if(resultado < 17){
                    resultado = $('.mensagem1').css('display', 'block');
                }else if(resultado == 17 || resultado <= 18.49){
                    resultado = $('.mensagem2').css('display', 'block');
                }else if(resultado == 18.5  || resultado <= 24.99){
                    resultado = $('.mensagem3').css('display', 'block');
                }else if(resultado == 25 || resultado <= 29.99){
                    resultado = $('.mensagem4').css('display', 'block');
                }else if(resultado == 30 || resultado <= 34.99){
                    resultado = $('.mensagem5').css('display', 'block');
                }else if(resultado == 35 || resultado <= 39.99){
                    resultado = $('.mensagem6').css('display', 'block');
                }else{
                    resultado = $('.mensagem7').css('display', 'block');
                }
            }
        });
    });

    $('.clear_tudo').click(function(){
        result.val('');
        result2.val('');
        resultado = $('.mensagem1, .mensagem2, .mensagem3, .mensagem4, .mensagem5, .mensagem6, .mensagem7').css('display', 'none');
    });
});