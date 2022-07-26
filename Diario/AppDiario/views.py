from django.shortcuts import render
from .models import *
from django.http import request
from django.http import HttpResponse
from AppDiario.forms import UsuarioForm, ColaboradorForm, StaffForm, UserRegisterForm, UserEditForm, AvatarForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def inicio(request):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url
    return render(request, "AppDiario/inicio.html",{"imagen":imagen})

'''def usuarios(request):
    return render(request, "AppDiario/usuarios.html")'''

'''def staff(request):
    return render(request, "AppDiario/staff.html")'''

'''def colaborador(request):
    return render(request, "AppDiario/colaborador.html")'''

#USUARIOS
#Crear usuarios
def usuarios(request):

    if (request.method=="POST"):
        form= UsuarioForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            email= info["email"]
            edad= info["edad"]
            pais= info["pais"]
            usuario= Usuario(nombre=nombre, email=email, edad=edad, pais=pais)
            usuario.save()
            return render (request, "AppDiario/inicio.html")
    else:
        form= UsuarioForm()
    return render(request, "AppDiario/usuarios.html", {"form":form})  

#BUSQUEDA DE USUARIOS
def busquedaUsuario(request):

    return render(request, "AppDiario/busquedaUsuario.html")

def buscarUsuario(request):

    if request.GET["nombre"]:
        user= request.GET["nombre"]
        usuario= Usuario.objects.filter(nombre=user)
        return render(request, "AppDiario/resultadoBusquedaUsuarios.html", {"usuario":usuario})
    else:
        return render(request, "AppDiario/busquedaUsuario.html", {"error":"No se ingreso ningun usuario"})

#ELIMINAR Y EDITAR USUARIOS
def leerUsuarios(request):

    usuario= Usuario.objects.all()
    return render (request, "AppDiario/leerUsuarios.html", {"usuario":usuario})

def eliminarUsuario(request, nombre_usuario):

    user= Usuario.objects.get(nombre=nombre_usuario)
    user.delete()
    usuario= Usuario.objects.all()
    return render(request, "AppDiario/leerUsuarios.html", {"usuario":usuario})

def editarUsuario(request, nombre_usuario):

    user= Usuario.objects.get(nombre=nombre_usuario)
    if request.method == "POST":
        form= UsuarioForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            usuarios.nombre= info["nombre"]
            usuarios.email= info["email"]
            usuarios.edad= info["edad"]
            usuarios.pais= info["pais"]
            usuarios.save()
            return render(request, "AppDiario/inicio.html")
    else:
        form= ColaboradorForm(initial={"nombre":user.nombre, "email":user.email, "edad":user.edad, "pais":user.pais})
    return render(request, "AppDiario/editarUsuario.html", {"formulario":form, "nombre_usuario":nombre_usuario})

'''
---------------------
'''
#COLABORADORES
#CREAR COLABORADORES
def colaborador(request):

    if (request.method=="POST"):
        form= ColaboradorForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            email= info["email"]
            edad= info["edad"]
            especialidad= info["especialidad"]
            colaborador= Colaborador(nombre=nombre, email=email, edad=edad, especialidad=especialidad)
            colaborador.save()
            return render (request, "AppDiario/inicio.html")
    else:
        form= ColaboradorForm()
    return render(request, "AppDiario/colaborador.html", {"form":form}) 

#BUSCAR COLABORADORES
def busquedaColaborador(request):

    return render(request, "AppDiario/busquedaColaborador.html")

def buscarColaborador(request):

    if request.GET["nombre"]:
        user= request.GET["nombre"]
        colaborador= Colaborador.objects.filter(nombre=user)
        return render(request, "AppDiario/resultadoBusquedaColaboradores.html", {"colaborador":colaborador})
    else:
        return render(request, "AppDiario/busquedaColaborador.html", {"error":"No se ingreso ningun colaborador"})

#ELIMINAR Y EDITAR COLABORADORES
def leerColaborador(request):

    colaborador= Colaborador.objects.all()
    return render (request, "AppDiario/leerColaborador.html", {"colaborador":colaborador})

def eliminarColaborador(request, colab):

    miembro= Colaborador.objects.get(nombre=colab)
    miembro.delete()
    colaborador= Colaborador.objects.all()
    return render(request, "AppDiario/leerColaborador.html", {"colaborador":colaborador})

def editarColaborador(request, colab):

    miembro= Colaborador.objects.get(nombre=colab)
    if request.method == "POST":
        form= ColaboradorForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            colaborador.nombre= info["nombre"]
            colaborador.email= info["email"]
            colaborador.edad= info["edad"]
            colaborador.especialidad= info["especialidad"]
            colaborador.save()
            return render(request, "AppDiario/inicio.html")
    else:
        form= ColaboradorForm(initial={"nombre":miembro.nombre, "email":miembro.email, "edad":miembro.edad, "especialidad":miembro.especialidad})
    return render(request, "AppDiario/editarColaborador.html", {"formulario":form, "colab":colab})

'''
--------------------------------
'''

#STAFF
#CREAR STAFF

def staff(request):

    if (request.method=="POST"):
        form= StaffForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            email= info["email"]
            edad= info["edad"]
            categoria= info["categoria"]
            staff= Staff(nombre=nombre, email=email, edad=edad, categoria=categoria)
            staff.save()
            return render (request, "AppDiario/inicio.html")
    else:
        form= StaffForm()
    return render(request, "AppDiario/staff.html", {"form":form})

#BUSCAR STAFF

def busquedaStaff(request):

    return render(request, "AppDiario/busquedaStaff.html")

def buscarStaff(request):

    if request.GET["nombre"]:
        user= request.GET["nombre"]
        staff= Staff.objects.filter(nombre=user)
        return render(request, "AppDiario/resultadoBusquedaStaff.html", {"staff":staff})
    else:
        return render(request, "AppDiario/busquedaStaff.html", {"error":"No se ingreso ningun miembro del staff"})

#ELIMINAR Y EDITAR STAFF

def leerStaff(request):

    staff= Staff.objects.all()
    return render (request, "AppDiario/leerStaff.html", {"staff":staff})

def eliminarStaff(request, miembro_staff):

    miembro= Staff.objects.get(nombre=miembro_staff)
    miembro.delete()
    staff= Staff.objects.all()
    return render(request, "AppDiario/leerStaff.html", {"staff":staff})

def editarStaff(request, miembro_staff):

    miembro= Staff.objects.get(nombre=miembro_staff)
    if request.method == "POST":
        form= StaffForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            staff.nombre= info["nombre"]
            staff.email= info["email"]
            staff.edad= info["edad"]
            staff.categoria= info["categoria"]
            staff.save()
            return render(request, "AppDiario/inicio.html")
    else:
        form= StaffForm(initial={"nombre":miembro.nombre, "email":miembro.email, "edad":miembro.edad, "categoria":miembro.categoria})
    return render(request, "AppDiario/editarStaff.html", {"formulario":form, "miembro_staff":miembro_staff})
'''
----------------------------
'''
#LOGIN - REGISTER - PERFIL
def login_request(request):
    
    if request.method == "POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario= request.POST["username"]
            contra= request.POST["password"]
            user= authenticate(username=usuario, password=contra)            
            if user is not None:
                login(request, user)
                return render(request, "AppDiario/inicio.html", {"form":form, "mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppDiario/login.html", {"form":form, "mensaje":f"Usuario o contraseña inconrrecta"})
        else:
            return render(request, "AppDiario/login.html", {"form":form, "mensaje":f"FORMULARIO INVALIDO"})
    else:
        form= AuthenticationForm()
        return render(request, "AppDiario/login.html", {"form":form})

def register(request):

    if request.method == "POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            form.save()
            return render(request, "AppDiario/inicio.html", {"form":form, "mensaje":f"Usuario Creado: {username}"})
    else:
        form= UserRegisterForm()
    return render(request, "AppDiario/register.html", {"form":form})

def editarPerfil(request):

    usuario= request.user

    if request.method == "POST":
        formulario= UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            usuario.email= informacion["email"]
            usuario.password1= informacion["password1"]
            usuario.password2= informacion["password2"]
            usuario.save()

            return render(request, "AppDiario/inicio.html", {"usuario":usuario, "mensaje":"PERFIL EDITADO CON EXITO"})

    else:
        formulario= UserEditForm(instance=usuario)

    return render(request, "AppDiario/editarPerfil.html", {"formulario":formulario, "usuario":usuario.username})

'''
------------------------
'''
#AVATAR

def agregarAvatar(request):
    if request.method == "POST":
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.get(user=request.user)
            if(avatarViejo.imagen):
                avatarViejo.delete()
            avatar = Avatar (user=request.user, imagen=formulario.cleaned_data["imagen"])
            avatar.save()
            return render(request, "AppDiario/inicio.html", {"usuario":request.user, "mensaje":"AVATAR AGREGADO CON EXITO"})
    else:
        formulario=AvatarForm()
        return render(request, "AppDiario/agregarAvatar.html", {"formulario":formulario, "usuario":request.user})
