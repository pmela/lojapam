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
