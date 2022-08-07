from django.contrib import admin
from .models import *


admin.site.register(Staff)
admin.site.register(Colaborador)
admin.site.register(Usuario)
admin.site.register(Avatar)
admin.site.register(PosteoEconomia)
admin.site.register(PosteoDeportes)
admin.site.register(PosteoEspectaculos)
admin.site.register(PosteoUltimasNoticias)
#admin.site.register(Categoria)

@admin.register(Posteo)
class AutorAdmin(admin.ModelAdmin):
    list_display= ("titulo", "id", "autor")
    

@admin.register(Comentarios)
class ComentariosAdmin(admin.ModelAdmin):
    list_display= ("posteo", "nombre", "email", "publicado", "estado")
    list_filter= ("estado", "publicado")
    search_fields= ("nombre", "email", "contenido")






# Register your models here.
