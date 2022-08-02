from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="inicio"),
    path("staff/", staff, name="staff"),
    path('ultimasnoticias/', ultimasnoticias, name="ultimasnoticias"),
    path('economia/', economia, name="economia"),
    path('deportes/', deportes, name="deportes"),
    path('espectaculos/', espectaculos, name="espectaculos"),
    path('usuarios/', usuarios, name="usuarios"),
    path('busquedaUsuario/', busquedaUsuario, name='busquedaUsuario'),
    path('buscarUsuario/', buscarUsuario, name='buscarUsuario'),
    path('busquedaStaff/', busquedaStaff, name='busquedaStaff'),
    path('buscarStaff/', buscarStaff, name='buscarStaff'),
    path('leerStaff/', leerStaff, name='leerStaf'),
    path('elminarStaff/<miembro_staff>', eliminarStaff, name="eliminarStaff"),
    path('editarStaff/<miembro_staff>', editarStaff, name="editarStaff"),
    path('leerUsuarios/', leerUsuarios, name='leerUsuarios'),
    path('eliminarUsuario/<nombre_usuario>', eliminarUsuario, name="eliminarUsuario"),
    path('editarUsuario/<nombre_usuario>', editarUsuario, name="editarUsuario"),
    path('posteo1/', posteo1, name="posteo1"),

    path('login/', login_request, name="login"),
    path('register/', register, name="register"),
    path("logout/", LogoutView.as_view(template_name="AppDiario/logout.html"), name="logout" ),
    path("editarPerfil/", editarPerfil, name="editarPerfil" ),
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),
    

    path('leerPosteo/', leerPosteo, name='leerPosteo'),
    path('editarPosteo/<post>', editarPosteo, name="editarPosteo"),
    path('elminarPosteo/<titulo>', eliminarPosteo, name="eliminarPosteo"),
    path('nuevoPosteo/', nuevoPosteo, name="nuevoPosteoPosteo"),

]