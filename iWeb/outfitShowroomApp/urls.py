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
    path('ocasion/<int:pk>/', views.OcasionDetailView.as_view()),
    path('estilo/<int:pk>/', views.EstiloDetailView.as_view()),
    path('outfit/<int:pk>/', views.OutfitDetailView.as_view()),
    
    #LIST VIEWS
    path('', views.HomeListView.as_view()),
    path ('ocasion/', views.OcasionListView.as_view()),
    path ('estilo/', views.EstiloListView.as_view()),
    path ('outfit/', views.OutfitListView.as_view()),

    #FORM PATH
    path('contact/', views.contacto, name='contactForm'),

    # #AGENDA PATH
    # path('agenda/', views.agenda, name='agenda'),
]
