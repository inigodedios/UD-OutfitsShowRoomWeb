from django.contrib import admin
from outfitShowroomApp.models import Prenda, Outfit, Ocasion, Estilo


class PrendaAdmin(admin.ModelAdmin):
    list_display=("id_pr", "nombre", "tipo_prenda", "talla", "precio", "materiales",)
    search_fields=("id_pr", "nombre", "tipo_prenda","talla", "precio", "materiales")
    list_filter=("talla", "tipo_prenda")
# class OcasionAdmin(admin.ModelAdmin):
#     list_display=("id_pr", "nombre", "materiales", "talla", "precio")
#     search_fields=("id_pr", "nombre", "materiales", "talla", "precio")
#     list_filter=("talla",)

# class EstiloAdmin(admin.ModelAdmin):
#     list_display=("id_pr", "nombre", "materiales", "talla", "precio")
#     search_fields=("id_pr", "nombre", "materiales", "talla", "precio")
#     list_filter=("talla",)

# class OutfitAdmin(admin.ModelAdmin):
#     list_display=("id_pr", "nombre", "materiales", "talla", "precio")
#     search_fields=("id_pr", "nombre", "materiales", "talla", "precio")
#     list_filter=("talla",)


# Register your models here.
admin.site.register(Prenda, PrendaAdmin)
# admin.site.register(Ocasion, OcasionAdmin)
# admin.site.register(Estilo, EstiloAdmin)
# admin.site.register(Outfit, OutfitAdmin)
admin.site.register(Ocasion)
admin.site.register(Estilo)
admin.site.register(Outfit)