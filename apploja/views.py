from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator





def chamandohtml(request):
    return render(request, 'telaDeLogin.html')


def chamandotelainicial(request, nome_categoria=None):
    if nome_categoria == None:
        produtos = Produto.objects.all()
    else:
        categoria = Categoria.objects.get(nome=nome_categoria)
        produtos = Produto.objects.filter(categoria=categoria)

    paginado = Paginator(produtos, 6)  # Show 25 contacts per page.

    numero_pagina = request.GET.get('page')
    produto_paginado = paginado.get_page(numero_pagina)
    contexto = {'produto_paginado': produto_paginado}

    return render(request, 'telainicial.html', contexto)


def chamandomenu(request):
    return render(request, 'menu.html')


def cadastraUsuario(request):
    if request.method == 'POST':
        print("oi")
        nome_cadastro = request.POST['nome_cadastro']
        email_cadastro = request.POST['email_cadastro']
        senha_cadastro = request.POST['senha_cadastro']
        confirma_senha = request.POST['confirmasenha']
        if senha_cadastro == confirma_senha:
            print("senha correta")
            if not Usuario.objects.filter(email=email_cadastro).exists():
                usuario = Usuario(nome=nome_cadastro, email=email_cadastro, senha=senha_cadastro)
                usuario.save()
            else:
                print("email ja ultilizado.")
        else:
            print("senha não confere.")

    return render(request, 'telaDeLogin.html')

