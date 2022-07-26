from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

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
    path('leerStaff/', leerStaff, name='leerStaf'),
    path('elminarStaff/<miembro_staff>', eliminarStaff, name="eliminarStaff"),
    path('editarStaff/<miembro_staff>', editarStaff, name="editarStaff"),
    path('leerColaboradores/', leerColaborador, name='leerColaborador'),
    path('elminarColaborador/<colab>', eliminarColaborador, name="eliminarColaborador"),
    path('editarColaborador/<colab>', editarColaborador, name="editarColaborador"),
    path('leerUsuarios/', leerUsuarios, name='leerUsuarios'),
    path('eliminarUsuario/<nombre_usuario>', eliminarUsuario, name="eliminarUsuario"),
    path('editarUsuario/<nombre_usuario>', editarUsuario, name="editarUsuario"),

    path('login/', login_request, name="login"),
    path('register/', register, name="register"),
    path("logout/", LogoutView.as_view(template_name="AppDiario/logout.html"), name="logout" ),
    path("editarPerfil/", editarPerfil, name="editarPerfil" ),
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),



]