from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Msj(models.Model):
    asunto= models.CharField(max_length=75)
    emisor= models.ForeignKey(User, on_delete=models.CASCADE) 
    destinatario= models.CharField(max_length=25)
    cuerpo= models.TextField()
    fecha_enviado= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Asunto: {self.asunto}, de {self.emisor} para {self.destinatario}"



'''class Mensaje(models.Model):

    emisor= models.ForeignKey(User, on_delete=models.CASCADE)     
    cuerpo= models.TextField()
    fecha_enviado= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['fecha_enviado']

class HiloManager(models.Manager):

    def find(self, user1, user2):
        queryset = self.filter(users=user1).filter(users=user2)
        if len(queryset) > 0:
            return queryset[0]
        return None

    def find_or_create(self, user1, user2):
        hilo = self.find(user1, user2)
        if hilo is None:
            hilo= Hilo.objects.create()
            hilo.users.add(user1, user2)
        return hilo

class Hilo(models.Model):
    users = models.ManyToManyField(User, related_name='hilos')
    mensajes = models.ManyToManyField(Mensaje)
    updated = models.DateTimeField(auto_now=True)

    objects = HiloManager()

    class Meta:
        ordering = ['-updated']'''



   


   
