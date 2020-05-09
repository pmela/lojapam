from django.shortcuts import render
from .models import *


def chamandohtml(request):
    return render(request, 'telaDeLogin.html')


def chamandotelainicial(request):
    produtos= Produto.objects.all()
    contexto= {'produtos':produtos}
    return render(request, 'telainicial.html', contexto)

