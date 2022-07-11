from django import forms


class UsuarioForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    email=forms.EmailField()
    edad=forms.IntegerField()
    pais=forms.CharField(max_length=50)
  
class ColaboradorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    email=forms.EmailField()
    edad=forms.IntegerField()
    especialidad=forms.CharField(max_length=50)
   
class StaffForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    email=forms.EmailField()
    edad=forms.IntegerField()
    categoria=forms.CharField(max_length=50)
    
    