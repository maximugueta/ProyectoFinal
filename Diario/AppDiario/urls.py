from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path("staff/", staff, name="staff"),
    path('colaboradores/', colaborador, name="colaboradores"),
    path('usuarios/', usuarios, name="usuarios"),
    path('busquedaUsuario/', busquedaUsuario, name='busquedaUsuario'),
    path('buscarUsuario/', buscarUsuario, name='buscarUsuario'),
    path('busquedaStaff/', busquedaStaff, name='busquedaStaff'),
    path('buscarStaff/', buscarStaff, name='buscarStaff'),
    path('busquedaColaborador/', busquedaColaborador, name='busquedaColaborador'),
    path('buscarColaborador/', buscarColaborador, name='buscarColaborador'),
    
]