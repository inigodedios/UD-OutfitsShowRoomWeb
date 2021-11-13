from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.template import Template, Context, context
from .models import Prenda, Ocasion, Estilo, Outfit



#DETAIL VIEWS
# class PrendaDetailView(DetailView):
#     model=Prenda
#     template_name= 'prueba_detail.html'

class OcasionDetailView(DetailView):
    model=Ocasion
    template_name= 'ocasion.html'        
    def get_context_data(self, **kwargs):
        context = super(OcasionDetailView, self).get_context_data(**kwargs)
        context['outfit_list'] = Outfit.objects.order_by('nombre').select_related('ocasiones')
        return context
    
    

class EstiloDetailView(DetailView):
    template_name= 'estilo.html'
    model=Estilo
    

class OutfitDetailView(DetailView):
    template_name= 'outfit.html'
    model=Outfit
    def get_context_data(self, **kwargs):
        context = super(OutfitDetailView, self).get_context_data(**kwargs)
        context['ocasion_list'] = Ocasion.objects.filter(outfitsocasiones=self.object.id_out) #Preguntar, no entiendo al 100% como hace la relacion entre las tabals intermedias
        context['estilo_list'] = Estilo.objects.filter(outfits=self.object.id_out)
        return context


#DETAIL LISTS
class HomeListView(ListView):
    # Añadir en la base de datos una tabla con la la descripcion, logo... de la empresa para asignarle un model infoEmppresa, no estilo --> sería mas correcto
    template_name= 'home.html'
    model = Estilo
    

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['ocasion_list'] = Ocasion.objects.order_by('id_oc')
        context['outfit_list'] = Outfit.objects.order_by('nombre')
        return context
    

    

# class PrendaListView(ListView):
# 	model=Prenda
# 	queryset = Prenda.objects.order_by('nombre') #Recuerda! -> Por convencion -> prenda_list
# 	# def get_queryset(self):
# 	# 	return self.queryset.filter(Prenda.precio>35)	

# class OcasionListView(ListView):
#     template_name= 'ocasion.html'
#     model=Ocasion
#     queryset = Ocasion.objects.order_by('nombre')
    
# class EstiloListView(ListView):
#     template_name= 'index.html'
#     model=Estilo
#     queryset = Estilo.objects.order_by('nombre')
    
# class OutfitListView(ListView):
#     model=Outfit
#     queryset = Outfit.objects.order_by('nombre')
# 	# def get_queryset(self):
# 	# 	return self.queryset.filter(Outfit.precio>35)
