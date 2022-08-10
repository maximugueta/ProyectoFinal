from django.urls import path
from .views import *


urlpatterns = [

    path('mensajes/', nuevoMensaje, name='nuevoMensaje'),
    path('verMensajes/', verMensajes, name='verMensajes'),
    path('elminarMensaje/<asunto>', eliminarMensaje, name="eliminarMensaje"),
    path('contestarMensaje/<asunto>', contestarMensaje, name="contestarMensaje"),


]
