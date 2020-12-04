from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


def chamandohtml(request):
    return render(request, 'telaDeLogin.html')


def chamandoindex(request):
    return render(request, 'index.html')

def chamandotelainicial(request, nome_categoria=None):
    if nome_categoria == None:
        produtos = Produto.objects.all()
    else:
        categoria = Categoria.objects.get(nome=nome_categoria)
        produtos = Produto.objects.filter(categoria=categoria)
    estoques = Estoque.objects.all()

    for produto in produtos:
        produto.estoque = []
        for estoque in estoques:
            if produto.id == estoque.produto.id:
                produto.estoque.append(estoque)


    paginado = Paginator(produtos, 8)  # Show 25 contacts per page.

    numero_pagina = request.GET.get('page')
    produto_paginado = paginado.get_page(numero_pagina)
    contexto = {'produto_paginado': produto_paginado}

    return render(request, 'telainicial.html', contexto)


# def chamandotelainicial(request, estoque=None):
#     if estoque == None:
#         produtos = Produto.objects.all()
#     else:
#         estoque = Estoque.objects.get(nome=estoque)
#         produtos = Produto.objects.filter(estoque=estoque)
#
#     paginado = Paginator(produtos, 8)  # Show 25 contacts per page.
#
#     numero_pagina = request.GET.get('page')
#     produto_paginado = paginado.get_page(numero_pagina)
#     contexto = {'produto_paginado': produto_paginado}
#
#     return render(request, 'telainicial.html', contexto)


def chamandomenu(request):
    return render(request, 'menu.html')


def chamandovenda(request):
    return render(request, 'venda.html')


def chamandodetalhe(request, id=None):
    produto = Produto.objects.get(id=id)
    estoques = Estoque.objects.filter(produto=produto)
    contexto = {'produto': produto, 'estoques': estoques}
    return render(request, 'telaDeDetalhe.html', contexto)


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


def validaUsuario(request):
    if request.method == 'POST':
        email_logar = request.POST['email_logar']
        senha_logar = request.POST['senha_logar']
        if Usuario.objects.filter(email=email_logar).exists():
            if Usuario.objects.filter(senha=senha_logar).exists():
                return chamandotelainicial(request)
            else:
                print("senha errada")
        else:
            print("email errado")

    return render(request, 'telaDeLogin.html')
