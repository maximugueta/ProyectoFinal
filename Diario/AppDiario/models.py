from ssl import Options
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    edad=models.IntegerField()
    pais=models.CharField(max_length=50)

    def __str__(self):
        return "nombre:"+" "+self.nombre+" "+"E-mail:"+" "+self.email+" "+"Edad:"+" "+str(self.edad)+" "+"País:"+" "+self.pais

class Colaborador(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    edad=models.IntegerField()
    especialidad=models.CharField(max_length=50)

    def __str__(self):
        return "nombre:"+" "+self.nombre+" "+"E-mail:"+" "+self.email+" "+"Edad:"+" "+str(self.edad)+" "+"Especialidad:"+" "+self.especialidad

class Staff(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    edad=models.IntegerField()
    categoria=models.CharField(max_length=50)
    
    def __str__(self):
        return "nombre:"+" "+self.nombre+" "+"E-mail:"+" "+self.email+" "+"Edad:"+" "+str(self.edad)+" "+"Categoria:"+" "+self.categoria


class Avatar(models.Model):
    
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)   

class Categoria(models.Model):
     name= models.CharField(max_length=100)

     def __str__(self) -> str:
          return self.name

class Posteo(models.Model):

    class ObjetosPublicados(models.Manager):
        
        def get_queryset(self):
            return super().get_queryset().filter(status="publicados")
        
    opciones= (("borrador","borrador"),("publicado","publicado"))

    categoria= models.ForeignKey(Categoria, on_delete=models.PROTECT, default=1)
    titulo= models.CharField(max_length=100)
    descripcion= models.TextField(null=True)
    contenido= models.TextField()
    slug= models.SlugField(max_length=250, unique_for_date="publicado", null=False, unique=True)
    publicado= models.DateTimeField(default=timezone.now)
    autor= models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    estado= models.CharField(max_length=10, choices=opciones, default="borrador")
    objetos= models.Manager()
    objetos_publicados= ObjetosPublicados()

    def __str__(self):
        return self.titulo

class Comentarios(models.Model):
    posteo= models.ForeignKey(Posteo, on_delete=models.CASCADE, related_name="comentarios")
    nombre= models.CharField(max_length=50)
    email= models.EmailField()
    contenido= models.TextField()
    publicado= models.DateTimeField(auto_now_add=True)
    estado= models.BooleanField(default=True)

    def __str__(self):
        return f"Comentario de {self.nombre}"
