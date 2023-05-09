const form = document.getElementById('form_html');

form.addEventListener('submit', function(e){
    
    let formValido = false;

    e.preventDefault();

    const campoA = document.getElementById('campo_a');
    const campoB = document.getElementById('campo_b');
    const mensagemSucesso = `Sucesso. O Segundo - ${campoB.value} número é maior que o Primeiro - ${campoA.value}.`
    const mensagemNegativa = `Falhou. Porque o Primeiro número ${campoA.value} é maior que o Segundo número ${campoB.value}.`

    formValido = (campoB.value > campoA.value);

    if(formValido){
        alert(mensagemSucesso);
        campoA.value = '';
        campoB.value = '';
    }else{
        alert(mensagemNegativa);
    }
})


