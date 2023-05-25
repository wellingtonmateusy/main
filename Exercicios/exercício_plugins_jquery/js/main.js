$(document).ready(function(){

    $('#nome').bind('keyup blur', function(){
        let i = $(this);
        i.val(i.val().replace(/[^a-z A-Z]/g, ''));
    })

    $('#telefone').mask('(00) 00000-0000', {
        placeholder: '(12)99345-8901'
    })

    $('#cpf').mask('000.000.000-00', {
        placeholder: '087.154.820-81'
    })

    $('#cep').mask('00000-000', {
        placeholder: '72800-175'
    })

    $('form').validate({
        rules: {
            nome: {
                required: true,
            },
            email: {
                required: true,
                email: true
            },
            telefone: {
                required: true
            },
            cpf: {
                required: true
            },
            endereco: {
                required: true
            },
            cep: {
                required: true
            }
        },
        messages: {
            nome: 'Por favor, informe seu nome!',
            email: 'Por favor, informe seu e-mail!',
            telefone: 'Por favor, informe seu telefone!',
            cpf: 'Por favor, informe seu CPF!',
            endereco: 'Por favor, informe seu endereço!',
            cep: 'Por favor, informe seu CEP!'
        },
        submitHandler: function(form){
            console.log(form)
        },
        invalidHandler: function(validador){
            let camposIncorretos = validador.numberOfInvalids();
            if(camposIncorretos){
                alert(`Existem ${camposIncorretos} campos incorretos!`);
            }
        }
    })
})