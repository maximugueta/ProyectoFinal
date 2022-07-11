from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path("staff/", staff),
    path('colaboradores/',colaborador),
    path('usuarios/',usuarios),
    
]