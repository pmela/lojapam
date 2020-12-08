from django.urls import path
from .views import *

app_name = "apploja"

urlpatterns = [
    path('telaDeLogin', chamandohtml, name='telaDeLogin'),
    path('telainicial/<str:nome_categoria>', chamandotelainicial, name='telainicial'),
    path('telainicial', chamandotelainicial, name='telainicial'),
    path('', chamandotelainicial, name='telainicialall'),
    path('index', chamandoindex, name='index'),
    path('menu', chamandomenu, name='menu'),
    path('venda', chamandovenda, name='venda'),
    path('telaDeDetalhe/<int:id>/', chamandodetalhe, name='telaDeDetalhe'),
    path('cadastraUsuario', cadastraUsuario, name='cadastraUsuario'),
    path('validaUsuario', validaUsuario, name='validaUsuario'),

]
