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
	model:Prenda
	def get_context_data(self, **kwargs):
		context = super(PrendaDetailView, self).get_context_data(**kwargs) 
		context['prenda_list'] = Prenda.objects.all()
		return context

class OcasionDetailView(DetailView):
	model:Ocasion
	def get_context_data(self, **kwargs):
		context = super(OcasionDetailView, self).get_context_data(**kwargs) 
		context['ocasion_list'] = Ocasion.objects.all()
		return context

class EstiloDetailView(DetailView):
	model:Estilo
	def get_context_data(self, **kwargs):
		context = super(EstiloDetailView, self).get_context_data(**kwargs) 
		context['estilo_list'] = Estilo.objects.all()
		return context

class OutfitDetailView(DetailView):
	model:Outfit
	def get_context_data(self, **kwargs):
		context = super(OutfitDetailView, self).get_context_data(**kwargs) 
		context['outfit_list'] = Outfit.objects.all()
		return context


#DETAIL LISTS
class PrendaListView(ListView):
	model:Prenda
	queryset = Prenda.objects.order_by('-nombre') #Recuerda! -> Por convencion el objeto resultante de una queryset se queda en una variable llamada por el nombreModelo_list -> empleado_list
	def get_context_data(self, **kwargs):
		context = super(PrendaListView, self).get_context_data(**kwargs)
		context['titulo_prenda'] = 'Listado de prendas'
		return context
	def get_queryset(self):
		return self.queryset.filter(Prenda.precio>35)

class OcasionListView(ListView):
	model:Ocasion
	queryset = Ocasion.objects.order_by('-nombre')
	def get_context_data(self, **kwargs):
		context = super(OcasionListView, self).get_context_data(**kwargs)
		context['titulo_ocasion'] = 'Listado de ocasiones'
		return context
	"""def get_queryset(self): TODO
		return self.queryset.filter() #Yo no ordenaria por nada - Iñigo
	"""

class EstiloListView(ListView):
	model:Estilo
	queryset = Estilo.objects.order_by('-nombre')
	def get_context_data(self, **kwargs):
		context = super(EstiloListView, self).get_context_data(**kwargs)
		context['titulo_estilo'] = 'Listado de estilos'
		return context
	"""def get_queryset(self):
		return self.queryset.filter()
	"""	

class OutfitListView(ListView):
	model:Outfit
	queryset = Outfit.objects.order_by('-nombre')
	def get_context_data(self, **kwargs):
		context = super(OutfitListView, self).get_context_data(**kwargs)
		context['titulo_outfit'] = 'Listado de outfit'
		return context
	def get_queryset(self):
		return self.queryset.filter(Outfit.precio>35)
