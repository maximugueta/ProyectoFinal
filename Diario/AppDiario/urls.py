from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path("staff/", staff, name="staff"),
    path('colaboradores/',colaborador, name="colaboradores"),
    path('usuarios/',usuarios, name="usuarios"),
    
]