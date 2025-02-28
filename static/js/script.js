const spinner = `
<div class="d-flex justify-content-center align-items-center" style="height: 200px;">
    <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
    </div>
</div>`

$(".detalharLivro").click(function() { //nesse caso não pode usar arrow function
    $("#modal-livro .modal-body").html(spinner);
    // Pega a URL do livro a partir do atributo data-url
    const dataUrl = $(this).data("url");
    $.ajax({
        url: dataUrl,
        method: "get",
        success: (response) => {
        $("#modal-livro .modal-body").html(response);
        }
    });
});

$(".form-like").submit( function (evento) {
    evento.preventDefault(); // evita a submissão "normal" do form
    $.ajax({
      url: $(this).attr("action"),
      method: "POST",
      data: $(this).serialize(),
      success: (resposta) => {
        if (resposta.like) {
          $(`#like-${resposta.id_livro}`).html(`<span>${resposta.favoritos}</span><i class="bi bi-heart-fill ms-1"></i>`);
        } else {
          $(`#like-${resposta.id_livro}`).html(`<span>${resposta.favoritos}</span><i class="bi bi-heart ms-1"></i>`);
        }
        buscarMensagens();
      },
      error: (xhr, status, error) => {
        alert(error);
      }
    });
  });

  function buscarMensagens() {
    $.get(mensagensUrl,
      (resposta) => {
        $("#div-mensagens").html(resposta);
      }
    );
  }