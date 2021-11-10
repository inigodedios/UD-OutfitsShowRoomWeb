from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from .models import Estilo, Ocasion, Outfit, Prenda

# Create your views here.
def index(request):
    return HttpResponse("Hello world")