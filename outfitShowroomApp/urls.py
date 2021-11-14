"""outfitShowroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #DETAIL VIEWS
    path('ocasion/<int:pk>/', views.OcasionDetailView.as_view(), name='ocasion_d'),
    path('estilo/<int:pk>/', views.EstiloDetailView.as_view(), name='estilo_d'),
    path('outfit/<int:pk>/', views.OutfitDetailView.as_view(), name='outfit_d'),
    
    # path ('prenda/<int:pk>/', views.PrendaDetailView.as_view(), name='prenda_d'),
    
    #LIST VIEWS
    path('home/', views.HomeListView.as_view(), name='estilo_l'),
    
    # path ('prenda/', views.PrendaListView.as_view(), name='prenda_l'),
    # path ('ocasion', views.OcasionListView.as_view(), name='ocasion_l'),
    # path ('estilo/', views.EstiloListView.as_view(), name='estilo_l'),
    # path ('outfit/', views.OutfitListView.as_view(), name='outfit_l'),

    #FORM PATH
    path('contact/', views.contacto, name='contactForm'),
]
