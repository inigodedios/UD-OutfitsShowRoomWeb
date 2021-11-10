from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from .models import Estilo, Ocasion, Outfit, Prenda


# Create your views here.
def index(request):
	return HttpResponse("Hello, world!")

#def nombreEmpresa(request, nombre_empresa):
#	lista_empresas = get_list_or_404(Outfit, nombre=Outfit.nombre)
    #context = {}
#	return render(request, 'listaEmpresas.html', context)	#render busca internamente en carpeta llamada templates, si no tendríamos que añadir la ruta completa
	#cambiar render por EmpresaDetailView