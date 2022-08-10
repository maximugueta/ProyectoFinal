from django.contrib.auth.decorators import login_required
from .models import Msj
from AppDiario.models import Avatar
from django.contrib.auth.models import User
from .forms import *
from django.shortcuts import render
from pickle import TRUE



# Create your views here.


def nuevoMensaje(request):    
    user= request.user
    if (request.method=="POST"):
        form= MensajeForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            asunto= info["asunto"]
            cuerpo= info["cuerpo"]
            destinatario= info["destinatario"]           
            emisor= user             
            mensaje= Msj(cuerpo=cuerpo, destinatario=destinatario, emisor=emisor, asunto=asunto)
            mensaje.save()
            return render(request, "mensajeria/verMensajes.html", {})
    else:
        form= MensajeForm()
    return render(request, "mensajeria/mensajes.html", {"form":form})

def verMensajes(request):
    user= request.user        
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url  
    mensaje= Msj.objects.filter(destinatario= user)
    return render (request, "mensajeria/verMensajes.html", {"mensaje":mensaje, "imagen":imagen})

def eliminarMensaje(request, asunto):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url    
    mensaje= Msj.objects.get(asunto=asunto)
    mensaje.delete()
    mensajes= Msj.objects.all()
    return render(request, "mensajeria/verMensajes.html", {"mensajes":mensajes, "imagen":imagen})

def contestarMensaje(request, asunto):
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url
    mensaje= Msj.objects.get(asunto=asunto)
    if request.method == "POST":
        form= MensajeForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            mensaje.emisor= info["emisor"]
            mensaje.cuerpo= info["cuerpo"]
            mensaje.asunto= info["asunto"]            
            mensaje.save()
            return render(request, "mensajeria/verMensajes.html", {})
    else:
        form= MensajeForm(initial={"emisor":mensaje.emisor, "cuerpo":mensaje.cuerpo, "asunto":mensaje.asunto})
    return render(request, "mensajeria/contestarMensaje.html", {"formulario":form, "asunto":asunto, "imagen":imagen})





'''
@method_decorator(login_required, name="dispatch")
class ListaHilo(TemplateView):
    template_name = "mensajeria/lista_hilo.html"

@method_decorator(login_required, name="dispatch")
class DetalleHilo(DetailView):
    model = Hilo
    
    def get_object(self):
        obj = super(DetalleHilo, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj

def agregar_mensaje(request, pk):
    json_response = {'fecha_enviado':False}
    if request.user.is_authenticated:
        content = request.GET.get('content', None)
        if content:
            hilo = get_object_or_404(Hilo, pk=pk)  
            mensaje = Mensaje.objects.create(user=request.user, content=content)
            hilo.mensajes.add(mensaje)
            json_response['fecha_enviado'] = True
            if len(mensaje.mensajes.all()) is 1:
                json_response['first'] = True
    else:
        raise Http404("Usuario no autenticado")

    return JsonResponse(json_response)

@login_required
def iniciar_hilo(request, username):
    user = get_object_or_404(User, username=username)
    hilo = Hilo.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('mensajeria:detalle', args=[hilo.pk]))'''

