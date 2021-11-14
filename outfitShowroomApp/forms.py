from django import forms

#Clase para guardar la información enviada de cliente a servidor a través del formulario, de manera oculta (POST)

class FormularioContacto(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField() 
    descripcion = forms.CharField()

    ACEPT=[('Acepto el tratamiento de mis datos.','Acepto el tratamiento de mis datos.'),]

    #condiciones = forms.ChoiceField(choices=ACEPT, widget=forms.RadioSelect)    #TODO no se puede seleccionar 

