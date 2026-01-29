const spinner = `
<div class="d-flex justify-content-center align-items-center" style="height: 200px;">
    <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
    </div>
</div>`

document.querySelectorAll(".detalharLivro").forEach(function(elemento) {
    elemento.addEventListener("click", function() {
        document.querySelector("#modal-livro .modal-body").innerHTML = spinner;
        // Pega a URL do livro a partir do atributo data-url
        const dataUrl = this.dataset.url;
        fetch(dataUrl)
            .then((response) => response.text())
            .then((html) => {
                document.querySelector("#modal-livro .modal-body").innerHTML = html;
            });
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

  $("#generos-select").change(function() {
    const urlFiltrada = `${livrosUrl}?f=${$(this).val()}`;
    $(".album").html(spinner);
    $.get(
      urlFiltrada,
      (resposta) => {
        $(".album").html(resposta);
      }
    );
  });

  function criarEventoPaginacao() {
    $(".page-link").click(function(evento) {
      evento.preventDefault();
      const url = $(this).data("url");
      $(".album").html(spinner);
      $.get(
        url,
        (resposta) => {
          $(".album").html(resposta);
          criarEventoPaginacao();
        }
      );
    });
  }
  criarEventoPaginacao();