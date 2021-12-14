from django import forms
from django.forms.widgets import RadioSelect, Widget
from django.forms import BooleanField, CharField, EmailField
# from django.db import models

#Clase para guardar la información enviada de cliente a servidor a través del formulario, de manera oculta (POST)

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", error_messages={'required': 'Por favor, introduzca su nombre.'}, max_length=50)
    apellido = forms.CharField(label="Apellidos", error_messages={'required': 'Por favor, introduzca su apellido.'}, max_length=50)
    correo = forms.EmailField(label="Correo electrónico", error_messages={'required': 'Por favor, introduzca su correo.'}, max_length=50) 
    descripcion = forms.CharField(label="¿Por qué estás interesado/a?:", error_messages={'required': 'Por favor, introduzca sus motivos.'}, max_length=50)
    condiciones = forms.BooleanField(required=False,initial=False,label='Acepto el tratamiento de mis datos')
    
    # ACEPT =[('acepto','Acepto el tratamiento de mis datos'),]
    
    # condiciones= forms.BooleanField(initial=ACEPT, default=False, label="Condiciones", required=True) #TODO no funciona

    # ACEPT=[('acepto','Acepto el tratamiento de mis datos'),
    #         ('no_acepto', 'No acepto el tratamiento de mis datos'),]

    # condiciones = forms.ChoiceField(label="Condiciones", choices=ACEPT)   #funciona

    # condiciones = forms.ChoiceField(choices=ACEPT, widget=forms.RadioSelect)    #funciona

