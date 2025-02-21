from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from contas.models import Usuario
from biblioteca.models import Livro
from .forms import LivroForm
from contas.forms import UsuarioChangeForm, UsuarioCreationForm

@login_required
@permission_required("biblioteca.add_livro", raise_exception=True)
def index(request):

    context = {
        "num_livros": Livro.objects.count(),
        "num_usuarios": Usuario.objects.count(),
        "num_favoritos": Livro.favoritos.through.objects.count(),
    }

    return render(request, "dashboard/index.html", context)

@login_required
@permission_required("biblioteca.add_livro", raise_exception=True)
def listar_livros(request):
    ordenar = request.GET.get("ordenar")
    if ordenar:
        livros = Livro.objects.all().order_by(ordenar)
    else:
        livros = Livro.objects.all().order_by("id")

    paginator = Paginator(livros, 10)
    numero_da_pagina = request.GET.get('p')  # Pega o número da página da URL
    livros_paginados = paginator.get_page(numero_da_pagina)  # Pega a página específica
    return render(request, "dashboard/livros.html", {"livros": livros_paginados})

@login_required
@permission_required("biblioteca.add_livro", raise_exception=True)
def criar_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Livro criado com sucesso!")
            return redirect("dashboard:livros")
        else:
            messages.error(request, "Falha ao criar livro!")
    else:
        form = LivroForm()
    return render(request, "dashboard/criar_livro.html", {"form": form})

@login_required
@permission_required("biblioteca.view_livro", raise_exception=True)
def ler_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    return render(request, "dashboard/detalhar_livro.html", {"livro": livro})

@login_required
@permission_required("biblioteca.change_livro", raise_exception=True)
def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            form.save()
            messages.success(request, "Livro atualizado!")
            return redirect("dashboard:livros")
        else:
            messages.error(request, "Falha ao criar livro!")
    else:
        form = LivroForm(instance=livro)
    return render(request, "dashboard/editar_livro.html", {"form": form})

def remover_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == "POST":
        livro.delete()
        messages.success(request, "Livro removido com sucesso!")
        return redirect("dashboard:livros")
    else:
        return render(request, "dashboard/remover_livro.html")

def listar_usuarios(request):
    ordenar = request.GET.get("ordenar")
    if ordenar:
        usuarios = Usuario.objects.all().order_by(ordenar)
    else:
        usuarios = Usuario.objects.all().order_by("id")
    paginator = Paginator(usuarios, 10)
    numero_da_pagina = request.GET.get('p')  # Pega o número da página da URL
    usuarios_paginados = paginator.get_page(numero_da_pagina)  # Pega a página específica
    return render(request, "dashboard/usuarios.html", {"usuarios": usuarios_paginados})

def criar_usuario(request):
    if request.method == "POST":
        form = UsuarioCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criado com sucesso!")
            return redirect("dashboard:usuarios")
        else:
            messages.error(request, "Falha ao criar usuário!")
    else:
        form = UsuarioCreationForm()
    return render(request, "dashboard/criar_usuario.html", {"form": form})

def ler_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    return render(request, "dashboard/detalhar_usuario.html", {"usuario": usuario})

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == "POST":
        form = UsuarioChangeForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário atualizado!")
            return redirect("dashboard:usuarios")
        else:
            messages.error(request, "Falha ao criar usuário!")
    else:
        form = UsuarioChangeForm(instance=usuario)
    return render(request, "dashboard/editar_usuario.html", {"form": form})

def remover_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == "POST":
        if usuario.id == request.user.id:
            messages.error(request, "Não é possível remover o usuário logado!")
        else:
            usuario.delete()
            messages.success(request, "Usuário removido com sucesso!")
        return redirect("dashboard:usuarios")
    else:
        return render(request, "dashboard/remover_usuario.html")
