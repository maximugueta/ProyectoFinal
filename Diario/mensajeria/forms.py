from django import forms
from .models import *
from django.contrib.auth.models import User




class MensajeForm(forms.Form):
    asunto= forms.CharField(max_length=75)
    cuerpo= forms.CharField()
    destinatario= forms.CharField(max_length=25)
    