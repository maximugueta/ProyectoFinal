from django.db import models

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
    