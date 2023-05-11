const ContainerMensagemSucesso = document.querySelector('.mensagem_sucesso');
const ContainerMensagemNegativa = document.querySelector('.mensagem_erro');
const ContainerMensagemIgual = document.querySelector('.mensagem_igual');
const campoB = document.getElementById('campo_b');
let formValido = false;
const form = document.getElementById('form_html');

form.addEventListener('submit', function(e){
    e.preventDefault();

    const campoA = document.getElementById('campo_a');
    const mensagemSucesso = `Sucesso. O Segundo número <b>${campoB.value}</b> é maior que o Primeiro <b>${campoA.value}</b>.`
    const mensagemNegativa = `Falhou. Porque o Primeiro número <b>${campoA.value}</b> é maior que o Segundo número <b>${campoB.value}</b>.`
    const mensagemIgual = `Os números são Iguais Primeiro número <b>${campoA.value}</b> Segundo número <b>${campoB.value}</b>.`

    formValido = (parseInt(campoB.value) > parseInt(campoA.value));
    formIgual = (parseInt(campoB.value) == parseInt(campoA.value));

    if(formValido){
        ContainerMensagemSucesso.innerHTML = mensagemSucesso;
        campoB.style.border = '';
        ContainerMensagemSucesso.style.display = 'block';
        ContainerMensagemNegativa.style.display = 'none';
        ContainerMensagemIgual.style.display = 'none';

        campoA.value = '';
        campoB.value = '';

    }else if(formIgual){
        ContainerMensagemIgual.innerHTML = mensagemIgual;
        campoB.style.border = '';
        ContainerMensagemIgual.style.display = 'block';
        ContainerMensagemSucesso.style.display = 'none';
        ContainerMensagemNegativa.style.display = 'none';
        

        campoA.value = '';
        campoB.value = '';
    }else{
        campoB.style.border = '1px solid red';
        ContainerMensagemNegativa.innerHTML = mensagemNegativa;
        ContainerMensagemNegativa.style.display = 'block';
        ContainerMensagemSucesso.style.display = 'none';
        ContainerMensagemIgual.style.display = 'none';

        campoA.value = '';
        campoB.value = '';
    }
})

campoB.addEventListener('keyup', function(e){
    formValido = validaNome(e.target.value);

    if(formValido){
        campoB.classList.remove('error');
        document.querySelector('.mensagem_erro').style.display = 'none';
    }else{
        campoB.classList.add('error');
        document.querySelector('.mensagem_erro').style.display = 'block';
    }
})


