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
            staff= Colaborador(nombre=nombre, email=email, edad=edad, categoria=categoria)
            staff.save()
            return render (request, "AppDiario/inicio.html")
    else:
        form= StaffForm()
    return render(request, "AppDiario/staff.html", {"form":form})