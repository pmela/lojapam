from django.urls import path
from .views import *

app_name = "apploja"

urlpatterns = [
    path('telaDeLogin', chamandohtml, name='telaDeLogin'),
    path('telainicial', chamandotelainicial, name='telainicial')
]
