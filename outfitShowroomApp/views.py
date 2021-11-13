from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.template import Template, Context, context
from .models import Prenda, Ocasion, Estilo, Outfit



# Create your views here.
def index(request):
	return HttpResponse("Hello, world!")

#DETAIL VIEWS
class PrendaDetailView(DetailView):
    #IMPORTANTE -> No hay que establecer la pk, ya que coge el pk de nuestro modelo no el pk automatico. Creo que no genera un pk automatico porque en el DB Browser solo aparece nuestra pk
    model=Prenda
    template_name= 'prueba_detail.html'

class OcasionDetailView(DetailView):
	model=Ocasion

class EstiloDetailView(DetailView):
	model=Estilo

class OutfitDetailView(DetailView):
	model=Outfit


#DETAIL LISTS
class PrendaListView(ListView):
	model=Prenda
	queryset = Prenda.objects.order_by('nombre') #Recuerda! -> Por convencion -> prenda_list
	# def get_queryset(self):
	# 	return self.queryset.filter(Prenda.precio>35)
	
	

class OcasionListView(ListView):
    model=Ocasion
    queryset = Ocasion.objects.order_by('nombre')
    template_name= 'prueba_list.html'



class EstiloListView(ListView):
    template_name= 'home.html'
    model=Estilo
    queryset = Estilo.objects.order_by('nombre')
    
    #Debido a que necesitamos datos de los outfits en la pagina web que corresponde a Estilo
    def get_context_data(self, **kwargs):
        context = super(EstiloListView, self).get_context_data(**kwargs)
        context['ocasion_list'] = Outfit.objects.order_by('nombre')
        context['outfit_list'] = Outfit.objects.order_by('nombre')
        return context
    

class OutfitListView(ListView):
    model=Outfit
    queryset = Outfit.objects.order_by('nombre')
    
    
	# def get_queryset(self):
	# 	return self.queryset.filter(Outfit.precio>35)
