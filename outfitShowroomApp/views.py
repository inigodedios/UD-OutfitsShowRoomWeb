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
    #IMPORTANTE -> No hay que establecer la pk, ya que coge el pk de nuestro modelo no el pk automatico. Creo que no genera un pk automatico porque hemos establecido que uno de nuestros atributo sea el pk (en el DB Browser solo aparece nuestra pk)
    model=Prenda
    template_name= 'prueba.html'

class OcasionDetailView(DetailView):
	model=Ocasion

class EstiloDetailView(DetailView):
	model=Estilo

class OutfitDetailView(DetailView):
	model=Outfit


#DETAIL LISTS
class PrendaListView(ListView):
	model=Prenda
	queryset = Prenda.objects.order_by('-nombre') #Recuerda! -> Por convencion el objeto resultante de una queryset se queda en una variable llamada por el nombreModelo_list -> empleado_list
	def get_queryset(self):
		return self.queryset.filter(Prenda.precio>35)

class OcasionListView(ListView):
	model=Ocasion
	queryset = Ocasion.objects.order_by('-nombre')


class EstiloListView(ListView):
	model=Estilo
	queryset = Estilo.objects.order_by('-nombre')

class OutfitListView(ListView):
	model=Outfit
	queryset = Outfit.objects.order_by('-nombre')
	def get_queryset(self):
		return self.queryset.filter(Outfit.precio>35)
