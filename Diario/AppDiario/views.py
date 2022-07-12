from django.shortcuts import render
from .models import *
from django.http import request
from django.http import HttpResponse
from AppDiario.forms import UsuarioForm, ColaboradorForm, StaffForm

# Create your views here.

def inicio(request):
    return render(request, "AppDiario/inicio.html")

'''def usuarios(request):
    return render(request, "AppDiario/usuarios.html")'''

'''def staff(request):
    return render(request, "AppDiario/staff.html")'''

'''def colaborador(request):
    return render(request, "AppDiario/colaborador.html")'''

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

def busquedaUsuario(request):

    return render(request, "AppDiario/busquedaUsuario.html")

def buscarUsuario(request):

    if request.GET["nombre"]:
        user= request.GET["nombre"]
        usuario= Usuario.objects.filter(nombre=user)
        return render(request, "AppDiario/resultadoBusquedaUsuarios.html", {"usuario":usuario})
    else:
        return render(request, "AppDiario/busquedaUsuario.html", {"error":"No se ingreso ningun usuario"})

def busquedaStaff(request):

    return render(request, "AppDiario/busquedaStaff.html")

def buscarStaff(request):

    if request.GET["nombre"]:
        user= request.GET["nombre"]
        staff= Staff.objects.filter(nombre=user)
        return render(request, "AppDiario/resultadoBusquedaStaff.html", {"staff":staff})
    else:
        return render(request, "AppDiario/busquedaStaff.html", {"error":"No se ingreso ningun miembro del staff"})

def busquedaColaborador(request):

    return render(request, "AppDiario/busquedaColaborador.html")

def buscarColaborador(request):

    if request.GET["nombre"]:
        user= request.GET["nombre"]
        colaborador= Colaborador.objects.filter(nombre=user)
        return render(request, "AppDiario/resultadoBusquedaColaboradores.html", {"colaborador":colaborador})
    else:
        return render(request, "AppDiario/busquedaColaborador.html", {"error":"No se ingreso ningun colaborador"})