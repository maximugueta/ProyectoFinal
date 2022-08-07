from ast import Delete
from multiprocessing import context
from django.shortcuts import render
from .models import *
from django.http import request
from django.http import HttpResponse
from AppDiario.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.

def inicio(request):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url
    return render(request, "AppDiario/inicio.html",{"imagen":imagen})


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

@login_required
def eliminarUsuario(request, nombre_usuario):

    user= Usuario.objects.get(nombre=nombre_usuario)
    user.delete()
    usuario= Usuario.objects.all()
    return render(request, "AppDiario/leerUsuarios.html", {"usuario":usuario})

@login_required
def editarUsuario(request, nombre_usuario):
    usuarios= Usuario.objects.get(nombre=nombre_usuario)
    if request.method=="POST":
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
        form= UsuarioForm(initial={"nombre":usuarios.nombre, "email":usuarios.email, "edad":usuarios.edad, "pais":usuarios.pais})
    return render(request, "AppDiario/editarUsuario.html", {"formulario":form, "nombre_usuario":nombre_usuario})

#--------------------------------

#SECCIONES
def ultimasnoticias(request):

    return render (request, "AppDiario/ultimasnoticias.html")


def economia(request):

    return render (request, "AppDiario/economia.html")


def deportes(request):

    return render (request, "AppDiario/deportes.html")


def espectaculos(request):

    return render (request, "AppDiario/espectaculos.html")

#---------------------------------------------------

#STAFF
#CREAR STAFF

@login_required
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

@login_required
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

@login_required
def leerStaff(request):

    staff= Staff.objects.all()
    return render (request, "AppDiario/leerStaff.html", {"staff":staff})


@login_required
def eliminarStaff(request, miembro_staff):

    miembro= Staff.objects.get(nombre=miembro_staff)
    miembro.delete()
    staff= Staff.objects.all()
    return render(request, "AppDiario/leerStaff.html", {"staff":staff})

@login_required
def editarStaff(request, miembro_staff):

    staff= Staff.objects.get(nombre=miembro_staff)
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
        form= StaffForm(initial={"nombre":staff.nombre, "email":staff.email, "edad":staff.edad, "categoria":staff.categoria})
    return render(request, "AppDiario/editarStaff.html", {"formulario":form, "miembro_staff":miembro_staff})


#----------------------------

#LOGIN - REGISTER - PERFIL
def login_request(request):
    
    if request.method=="POST":
        form= AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usu= request.POST['username']
            contra= request.POST['password']
            usuario=authenticate(username=usu, password=contra)     

            if usuario is not None:
                login(request, usuario)
                return render(request, "AppDiario/inicio.html", {"form":form, "mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppDiario/login.html", {"form":form, "mensaje":f"Usuario o contraseña incorrecta"})

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

@login_required
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

#------------------------------------------

#AVATAR

@login_required
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


#------------------------------------------------------
 

def leerPosteo(request):

    posteo= Posteo.objects.all()
    return render (request, "AppDiario/leerPosteo.html", {"posteo":posteo})

def editarPosteo(request, post):

    posteo= Posteo.objects.get(titulo=post)
    if request.method == "POST":
        form= PosteoForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            posteo.titulo= info["titulo"]
            posteo.descripcion= info["descripcion"]
            posteo.contenido= info["contenido"]
            posteo.save()
            return render(request, "AppDiario/leerPosteo.html")
    else:
        form= PosteoForm(initial={"titulo":posteo.titulo, "descripcion":posteo.descripcion, "contenido":posteo.contenido})
    return render(request, "AppDiario/editarPosteo.html", {"formulario":form, "post":post})

def eliminarPosteo(request, titulo):

    posteo= Posteo.objects.get(titulo=titulo)
    posteo.delete()
    post= Posteo.objects.all()
    return render(request, "AppDiario/inicio.html", {"post":post})

def nuevoPosteo(request):

    if (request.method=="POST"):
        form= PosteoForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            titulo= info["titulo"]
            descripcion= info["descripcion"]
            contenido= info["contenido"]               
            posteo= Posteo(titulo=titulo, descripcion=descripcion, contenido=contenido)
            posteo.save()
            return render(request, "AppDiario/inicio.html")
    else:
        form= PosteoForm()
    return render(request, "AppDiario/nuevoPosteo.html", {"form":form}) 



#POSTEOS

def posteo1(request):

    return render(request, "AppDiario/post_1.html")
#ULTIMAS NOTICIAS

def leerUltimasNoticias(request):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url
    
    posteo_ultimasNoticias= PosteoUltimasNoticias.objects.all()
    return render (request, "AppDiario/ultimasnoticias.html", {"posteo_ultimasNoticias":posteo_ultimasNoticias, "imagen":imagen})

def editarUltimasNoticias(request, post):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url

    posteo_ultimasNoticias= PosteoUltimasNoticias.objects.get(titulo=post)
    if request.method == "POST":
        form= PosteoUltimasNoticiasForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            posteo_ultimasNoticias.titulo= info["titulo"]
            posteo_ultimasNoticias.descripcion= info["descripcion"]
            posteo_ultimasNoticias.contenido= info["contenido"]
            posteo_ultimasNoticias.save()
            return render(request, "AppDiario/UltimasNoticias.html", {"imagen":imagen})
    else:
        form= PosteoUltimasNoticiasForm(initial={"titulo":posteo_ultimasNoticias.titulo, "descripcion":posteo_ultimasNoticias.descripcion, "contenido":posteo_ultimasNoticias.contenido})
    return render(request, "AppDiario/editarUltimasNoticias.html", {"formulario":form, "post":post, "imagen":imagen})

def eliminarUltimasNoticias(request, titulo):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url

    posteo_ultimasNoticias= PosteoUltimasNoticias.objects.get(titulo=titulo)
    posteo_ultimasNoticias.delete()
    post= PosteoUltimasNoticias.objects.all()
    return render(request, "AppDiario/inicio.html", {"post":post, "imagen":imagen})

def nuevoUltimasNoticias(request):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url
    user= request.user

    if (request.method=="POST"):
        form= PosteoUltimasNoticiasForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            titulo= info["titulo"]
            descripcion= info["descripcion"]
            contenido= info["contenido"]  
            autor= user             
            posteo_ultimasNoticias= PosteoUltimasNoticias(titulo=titulo, descripcion=descripcion, contenido=contenido, autor=autor)
            posteo_ultimasNoticias.save()
            return render(request, "AppDiario/inicio.html", {"imagen":imagen})
    else:
        form= PosteoUltimasNoticiasForm()
    return render(request, "AppDiario/nuevoUltimasNoticias.html", {"form":form, "imagen":imagen}) 


#ECONOMIA

def leerEconomia(request):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url
    
    posteo_economia= PosteoEconomia.objects.all()
    return render (request, "AppDiario/economia.html", {"posteo_economia":posteo_economia, "imagen":imagen})

def editarEconomia(request, post):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url

    posteo_economia= PosteoEconomia.objects.get(titulo=post)
    if request.method == "POST":
        form= PosteoEconomiaForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            posteo_economia.titulo= info["titulo"]
            posteo_economia.descripcion= info["descripcion"]
            posteo_economia.contenido= info["contenido"]
            posteo_economia.save()
            return render(request, "AppDiario/economia.html", {"imagen":imagen})
    else:
        form= PosteoEconomiaForm(initial={"titulo":posteo_economia.titulo, "descripcion":posteo_economia.descripcion, "contenido":posteo_economia.contenido})
    return render(request, "AppDiario/editarEconomia.html", {"formulario":form, "post":post, "imagen":imagen})

def eliminarEconomia(request, titulo):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url

    posteo_economia= PosteoEconomia.objects.get(titulo=titulo)
    posteo_economia.delete()
    post= PosteoEconomia.objects.all()
    return render(request, "AppDiario/inicio.html", {"post":post, "imagen":imagen})

def nuevoEconomia(request):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url
    user= request.user

    if (request.method=="POST"):
        form= PosteoEconomiaForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            titulo= info["titulo"]
            descripcion= info["descripcion"]
            contenido= info["contenido"]  
            autor= user             
            posteo_economia= PosteoEconomia(titulo=titulo, descripcion=descripcion, contenido=contenido, autor=autor)
            posteo_economia.save()
            return render(request, "AppDiario/inicio.html", {"imagen":imagen})
    else:
        form= PosteoEconomiaForm()
    return render(request, "AppDiario/nuevoEconomia.html", {"form":form, "imagen":imagen}) 

#DEPORTES

def leerDeportes(request):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url
    posteo_deportes= PosteoDeportes.objects.all()
    return render (request, "AppDiario/deportes.html", {"posteo_deportes":posteo_deportes, "imagen":imagen})

def editarDeportes(request, post):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url

    posteo_deportes= PosteoDeportes.objects.get(titulo=post)
    if request.method == "POST":
        form= PosteoDeportesForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            posteo_deportes.titulo= info["titulo"]
            posteo_deportes.descripcion= info["descripcion"]
            posteo_deportes.contenido= info["contenido"]
            posteo_deportes.autor= info["autor"]
            posteo_deportes.save()
           
            return render(request, "AppDiario/deportes.html", {"imagen":imagen})
    else:
        form= PosteoDeportesForm(initial={"titulo":posteo_deportes.titulo, "descripcion":posteo_deportes.descripcion, "contenido":posteo_deportes.contenido})
    return render(request, "AppDiario/editarDeportes.html", {"formulario":form, "post":post, "imagen":imagen})

def eliminarDeportes(request, titulo):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url

    posteo_deportes= PosteoDeportes.objects.get(titulo=titulo)
    posteo_deportes.delete()
    post= PosteoDeportes.objects.all()
    return render(request, "AppDiario/inicio.html", {"post":post, "imagen":imagen})

def nuevoDeportes(request):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url

    user= request.user

    if (request.method=="POST"):
        form= PosteoDeportesForm(request.POST)        
        if form.is_valid():
            info= form.cleaned_data
            titulo= info["titulo"]
            descripcion= info["descripcion"]
            contenido= info["contenido"]   
            autor= user       
            posteo_deportes= PosteoDeportes(titulo=titulo, descripcion=descripcion, contenido=contenido, autor=autor)
            posteo_deportes.save()
            
            return render(request, "AppDiario/inicio.html", {"imagen":imagen})
    else:
        form= PosteoDeportesForm()
    return render(request, "AppDiario/nuevoDeportes.html", {"form":form, "imagen":imagen}) 


#ESPECTACULOS

def leerEspectaculos(request):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url
    
    posteo_espectaculos= PosteoEspectaculos.objects.all()
    return render (request, "AppDiario/espectaculos.html", {"posteo_espectaculos":posteo_espectaculos, "imagen":imagen})

def editarEspectaculos(request, post):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url

    posteo_espectaculos= PosteoEspectaculos.objects.get(titulo=post)
    if request.method == "POST":
        form= PosteoEspectaculosForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            posteo_espectaculos.titulo= info["titulo"]
            posteo_espectaculos.descripcion= info["descripcion"]
            posteo_espectaculos.contenido= info["contenido"]
            posteo_espectaculos.save()
            return render(request, "AppDiario/espectaculos.html", {"imagen":imagen})
    else:
        form= PosteoEspectaculosForm(initial={"titulo":posteo_espectaculos.titulo, "descripcion":posteo_espectaculos.descripcion, "contenido":posteo_espectaculos.contenido})
    return render(request, "AppDiario/editarEspectaculos.html", {"formulario":form, "post":post, "imagen":imagen})

def eliminarEspectaculos(request, titulo):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url

    posteo_espectaculos= PosteoEspectaculos.objects.get(titulo=titulo)
    posteo_espectaculos.delete()
    post= PosteoEspectaculos.objects.all()
    return render(request, "AppDiario/inicio.html", {"post":post, "imagen":imagen})

def nuevoEspectaculos(request):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url
    user= request.user

    if (request.method=="POST"):
        form= PosteoEspectaculosForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            titulo= info["titulo"]
            descripcion= info["descripcion"]
            contenido= info["contenido"] 
            autor= user              
            posteo_espectaculos= PosteoEspectaculos(titulo=titulo, descripcion=descripcion, contenido=contenido, autor=autor)
            posteo_espectaculos.save()
            return render(request, "AppDiario/inicio.html", {"imagen":imagen})
    else:
        form= PosteoEspectaculosForm()
    return render(request, "AppDiario/nuevoEspectaculos.html", {"form":form, "imagen":imagen}) 