from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="inicio"),
    path("staff/", staff, name="staff"),    
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
    path('nuevoPosteo/', nuevoPosteo, name="nuevoPosteo"),
#ULTIMAS NOTICIAS
    path('ultimasnoticias/', leerUltimasNoticias, name='ultimasnoticias'),
    path('editarUltimasNoticias/<post>', editarUltimasNoticias, name="editarUltimasNoticias"),
    path('elminarUltimasNoticias/<titulo>', eliminarUltimasNoticias, name="eliminarUltimasNoticias"),
    path('nuevoUltimasNoticias/', nuevoUltimasNoticias, name="nuevoUltimasNoticias"),
#ECONOMIA
    path('economia/', leerEconomia, name='economia'),
    path('editarEconomia/<post>', editarEconomia, name="editarEconomia"),
    path('elminarEconomia/<titulo>', eliminarEconomia, name="eliminarEconomia"),
    path('nuevoEconomia/', nuevoEconomia, name="nuevoEconomia"),
#DEPORTES
    path('deportes/', leerDeportes, name='deportes'),
    path('editarDeportes/<post>', editarDeportes, name="editarDeportes"),
    path('elminarDeportes/<titulo>', eliminarDeportes, name="eliminarDeportes"),
    path('nuevoDeportes/', nuevoDeportes, name="nuevoDeportes"),
#ESPECTACULOS
    path('espectaculos/', leerEspectaculos, name='espectaculos'),
    path('editarEspectaculos/<post>', editarEspectaculos, name="editarEspectaculos"),
    path('elminarEspectaculos/<titulo>', eliminarEspectaculos, name="eliminarEspectaculos"),
    path('nuevoEspectaculos/', nuevoEspectaculos, name="nuevoEspectaculos"),


]