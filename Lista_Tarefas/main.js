const ok = '<img src="./ok.png" alt="Tarefa Concluída"/>'
const fal ='<img src="./false.png" alt="Tarefa não Concluída"/>'
$(document).ready(function(){

    $('form').on('submit', function(e){
        e.preventDefault();
        const novaTarefa = $('#nome_tarefa').val();
        const novoItem = $(`<li style = "display: none"> ${novaTarefa} ${fal}</li>`);
        $(novoItem).appendTo('ul');
        $(novoItem).fadeIn(1000);
        $('#nome_tarefa').val('');

        $('li').click(function(){
            $(this).css("text-decoration", "line-through");
        })
    });
});