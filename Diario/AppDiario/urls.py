from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path("staff/", staff),
    path('colaborador/',colaborador),
    path('usuarios/',usuarios),
    
]