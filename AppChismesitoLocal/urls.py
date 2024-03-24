from django.urls import path
from AppChismesitoLocal.views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio/', inicio, name='inicio'),  
    path('logout/', exit, name='exit'),
    path('lista_publicaciones/', lista_publicaciones, name='lista_publicaciones'), 
     
]