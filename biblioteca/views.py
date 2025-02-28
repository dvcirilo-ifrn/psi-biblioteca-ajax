from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import JsonResponse
import time
from .models import Livro
from .forms import GeneroForm
from contas.models import Usuario

def index(request):
    livros = Livro.objects.all().order_by("?")[:6]
    return render(request, "biblioteca/index.html", {"livros": livros})

def livros(request):
    filtro = request.GET.get("f")
    if filtro and filtro in Livro.GENEROS:
        livros = Livro.objects.filter(genero=filtro).order_by("id")
    else:
        livros = Livro.objects.all().order_by("id")
    paginator = Paginator(livros, 6)
    numero_da_pagina = request.GET.get('p')  # Pega o número da página da URL
    livros_paginados = paginator.get_page(numero_da_pagina)  # Pega a página específica
    return render(request, "biblioteca/livros.html", {"livros": livros_paginados, "opcoes": Livro.GENEROS.items()})

def detalhar_livro(request, id_livro):
    livro = get_object_or_404(Livro, id=id_livro)
    return render(request, "biblioteca/detalhar_livro.html", {"livro": livro})

def ajax_detalhar_livro(request, id_livro):
    livro = get_object_or_404(Livro, id=id_livro)
    time.sleep(2) # simula atraso da rede
    return render(request, "biblioteca/partials/_detalhar_livro.html", {"livro": livro})

def pesquisa(request):
    pesquisa = request.GET.get("q")
    if pesquisa:
        livros_autor = Livro.objects.filter(autor__icontains=pesquisa)
        livros_titulo = Livro.objects.filter(titulo__icontains=pesquisa)
        livros_sinopse = Livro.objects.filter(sinopse__icontains=pesquisa)
        livros = livros_autor | livros_titulo | livros_sinopse
        livros.distinct()
    
    paginator = Paginator(livros, 6)
    numero_da_pagina = request.GET.get('p')  # Pega o número da página da URL
    livros_paginados = paginator.get_page(numero_da_pagina)  # Pega a página específica
    return render(request, "biblioteca/pesquisa.html", {"livros": livros_paginados})

@login_required
def meus_livros(request):
    livros = Livro.objects.filter(favoritos__id=request.user.id).order_by("id")
    paginator = Paginator(livros, 6)
    numero_da_pagina = request.GET.get('p')  # Pega o número da página da URL
    livros_paginados = paginator.get_page(numero_da_pagina)  # Pega a página específica
    return render(request, "biblioteca/meus_livros.html", {"livros": livros_paginados})

@login_required
def favoritar(request, id_livro):
    if request.POST:
        livro = get_object_or_404(Livro, id=id_livro)
        if request.user in livro.favoritos.all():
            livro.favoritos.remove(request.user)
            messages.success(request, "Livro removido com sucesso!")
        else:
            livro.favoritos.add(request.user)
            messages.success(request, "Livro favoritado com sucesso!")
    else:
        messages.erros(request, "Falha ao favoritar o livro!")

    return redirect("biblioteca:meus-livros")

@login_required
def ajax_favoritar(request, id_livro):
    like = False
    if request.POST:
        livro = get_object_or_404(Livro, id=id_livro)
        if request.user in livro.favoritos.all():
            livro.favoritos.remove(request.user)
            messages.success(request, "Livro removido com sucesso!")
        else:
            livro.favoritos.add(request.user)
            like = True
            messages.success(request, "Livro favoritado com sucesso!")
    else:

        messages.erros(request, "Falha ao favoritar o livro!")

    return JsonResponse({
        "favoritos": livro.favoritos.count(), 
        "like": like, 
        "id_livro": id_livro
    })