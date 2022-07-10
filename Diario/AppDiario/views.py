from django.shortcuts import render
from .models import *
from django.http import request
# Create your views here.

def inicio(request):
    return render(request, "AppDiario/inicio.html")

def usuarios(request):
    return render(request, "AppDiario/usuarios.html")

def staff(request):
    return render(request, "AppDiario/staff.html")

def colaborador(request):
    return render(request, "AppDiario/colaborador.html")