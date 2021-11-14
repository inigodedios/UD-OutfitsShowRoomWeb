from django import forms

# TODO HACER EN MODELS?

class FormularioContacto(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()

    ACEPT=[('Acepto el tratamiento de mis datos.','Acepto el tratamiento de mis datos.'),]

    condiciones = forms.ChoiceField(choices=ACEPT, widget=forms.RadioSelect)

