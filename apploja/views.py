from django.shortcuts import render
from .models import *


def chamandohtml(request):
    return render(request, 'telaDeLogin.html')


def chamandotelainicial(request, nome_categoria=None):
    if nome_categoria == None:
        produtos = Produto.objects.all()
    else:
        categoria = Categoria.objects.get(nome=nome_categoria)
        produtos = Produto.objects.filter(categoria=categoria)
    contexto = {'produtos': produtos}

    return render(request, 'telainicial.html', contexto)


def chamandomenu(request):
    return render(request, 'menu.html')


