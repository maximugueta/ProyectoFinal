from django.shortcuts import render
from AppDiario.forms import *
from AppDiario.models import *



def inicio(request):
    posteo= Posteo.objects.all()
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url
    return render(request, "AppDiario/inicio.html",{"imagen":imagen, "posteo":posteo})
