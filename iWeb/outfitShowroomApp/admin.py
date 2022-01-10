from django.contrib import admin
from .models import Prenda, Outfit, Ocasion, Estilo, OutfitShowroom
from django.contrib.auth.models import Group
from django.urls import path

"""
TODO En el panel de administración cuando añadimos un outfit, tenemos que asociarlo a uno/varios estilos y una/varias prendas.
Problema-> a la hora de asignar a que prendas y estilos pertenecen, solo sale el id de estas. Tenemos que conseguir que salga el id y su nombre
MIRAR IMAGEN para entenderlo mejor -> outfitShowroomApp/static/problema_en_admin.png 
"""

class PrendaAdmin(admin.ModelAdmin):
    list_display=("id_pr", "nombre", "tipo_prenda", "talla", "precio", "materiales",)
    search_fields=("id_pr", "nombre", "tipo_prenda","talla", "precio", "materiales",)
    list_filter=("talla", "tipo_prenda",)
    ordering = ("id_pr",)

class OcasionAdmin(admin.ModelAdmin):
    list_display=("id_oc", "nombre", "desc",)
    search_fields=("id_oc", "nombre", "desc",)
    list_filter=("nombre",)
    ordering = ("id_oc",)

class EstiloAdmin(admin.ModelAdmin):
    list_display=("id_est", "nombre", "desc",)
    search_fields=("id_est", "nombre", "desc",)
    list_filter=("nombre",)
    ordering = ("id_est",)

class OutfitAdmin(admin.ModelAdmin):
    list_display=("id_out", "nombre", "desc", "precio",) #TODO "estilo", "ocasiones", "prendas",)
    search_fields=("id_out", "nombre", "desc", "precio",) #TODO "estilo", "ocasiones", "prendas",)
    list_filter=("nombre",) #TODO "estilo", "ocasiones", "prendas",)
    ordering = ("id_out",)
    
class OutfitShowroomAdmin(admin.ModelAdmin):
    list_display=("id_out", "nombre", "eslogan",)
    search_fields=("id_out", "nombre", "eslogan",)
    list_filter=("nombre",)
    ordering = ("id_out",)

# Register your models here.
admin.site.register(Prenda, PrendaAdmin)
admin.site.register(Ocasion, OcasionAdmin)
admin.site.register(Estilo, EstiloAdmin)
admin.site.register(Outfit, OutfitAdmin)
admin.site.register(OutfitShowroom, OutfitShowroomAdmin)

admin.site.site_header = 'Admin Tutorial Dashboard'
#admin.site.register(Snippet, SnippetAdmin)
admin.site.unregister(Group)