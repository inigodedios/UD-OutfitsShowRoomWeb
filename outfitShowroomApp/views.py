from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from django.template import Template, Context, context 
from .models import Estilo, Ocasion, Outfit, Prenda


# Create your views here.
def index(request):
	return HttpResponse("Hello, world!")

def prueba(request): #prueba
	nombre = 'Prueba'
	context = {
		'login': True,
		'nombre': nombre
	}	
	return render(request, prueba.html, context)

def prueba(request):
	departamentos = get_list_or_404(Prenda.objects.order_by('nombre'))
	context = {'lista_departamentos': departamentos }
	return render(request, 'index.html', context)



#def nombreEmpresa(request, nombre_empresa):
#	lista_empresas = get_list_or_404(Outfit, nombre=Outfit.nombre)
    #context = {}
#	return render(request, 'listaEmpresas.html', context)	#render busca internamente en carpeta llamada templates, si no tendríamos que añadir la ruta completa
	#cambiar render por EmpresaDetailView