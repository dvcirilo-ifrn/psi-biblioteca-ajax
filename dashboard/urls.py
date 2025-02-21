from django.urls import path
from . import views

# namespace para urls
# evita conflito de nomes
# permite usar urls do tipo 'app_name:name'
# Ex. 'dashboard:index'
app_name="dashboard"
urlpatterns = [
    path("", views.index, name="index"),
    path("livros/", views.listar_livros, name="livros"),
    path("livros/criar/", views.criar_livro, name="criar-livro"),
    path("livros/<int:id>/", views.ler_livro, name="ler-livro"),
    path("livros/<int:id>/editar/", views.editar_livro, name="editar-livro"),
    path("livros/<int:id>/remover/", views.remover_livro, name="remover-livro"),
    path("usuarios/", views.listar_usuarios, name="usuarios"),
    path("usuarios/criar/", views.criar_usuario, name="criar-usuario"),
    path("usuarios/<int:id>/", views.ler_usuario, name="ler-usuario"),
    path("usuarios/<int:id>/editar/", views.editar_usuario, name="editar-usuario"),
    path("usuarios/<int:id>/remover/", views.remover_usuario, name="remover-usuario"),
]
