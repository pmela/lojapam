from django.urls import path
from .views import *

app_name = "apploja"

urlpatterns = [
    path('telaDeLogin', chamandohtml, name='telaDeLogin'),
    path('telainicial/<str:nome_categoria>', chamandotelainicial, name='telainicial'),
    path('', chamandotelainicial, name='telainicialall'),
    path('menu', chamandomenu, name='menu'),
    path('cadastraUsuario', cadastraUsuario, name='cadastraUsuario')
]
