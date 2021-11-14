from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.template import Template, Context, context
from .models import Prenda, Ocasion, Estilo, Outfit
from outfitShowroomApp.forms import FormularioContacto
from django.core.mail import send_mail, EmailMessage



#DETAIL VIEWS
# class PrendaDetailView(DetailView):
#     model=Prenda
#     template_name= 'prueba_detail.html'

class OcasionDetailView(DetailView):
    model=Ocasion
    template_name= 'ocasion.html'        
    def get_context_data(self, **kwargs):
        context = super(OcasionDetailView, self).get_context_data(**kwargs)
        context['outfit_list'] = Outfit.objects.filter(ocasiones=self.object.id_oc) #Funciona bien
        return context
    
class EstiloDetailView(DetailView):
    template_name= 'estilo.html'
    model=Estilo
    queryset = Estilo.objects.order_by('-nombre') #estilo_list
    def get_context_data(self, **kwargs):
        context = super(EstiloDetailView, self).get_context_data(**kwargs)
        context['outfit_list'] = Outfit.objects.filter(estilo=self.object.id_est) #ERROR No funciona
        return context
    
    # def get_queryset(self):
    #     return self.queryset.filter(outfits=self.model.id_est)
    
class OutfitDetailView(DetailView):
    template_name= 'outfit.html'
    model=Outfit
    
    def get_context_data(self, **kwargs):
        context = super(OutfitDetailView, self).get_context_data(**kwargs)
        context['ocasion_list'] = Ocasion.objects.filter(outfitsocasiones=self.object.id_out) #Funciona bien
        context['estilo_list'] = Estilo.objects.filter(outfits=self.object.estilo_id) #Funciona bien
        return context


#DETAIL LISTS
class HomeListView(ListView):
    # TODO Añadir en la base de datos una tabla con la la descripcion, logo... de la empresa para asignarle un model infoEmppresa, no estilo --> sería mas correcto
    template_name= 'home.html'
    model = Estilo
    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['ocasion_list'] = Ocasion.objects.order_by('id_oc')
        context['outfit_list'] = Outfit.objects.order_by('nombre')
        return context
    

# class PrendaListView(ListView):
# 	model=Prenda
# 	queryset = Prenda.objects.order_by('nombre') #Recuerda! -> Por convencion -> prenda_list
# 	# def get_queryset(self):
# 	# 	return self.queryset.filter(Prenda.precio>35)	

# class OcasionListView(ListView):
#     template_name= 'ocasion.html'
#     model=Ocasion
#     queryset = Ocasion.objects.order_by('nombre')
    
# class EstiloListView(ListView):
#     template_name= 'index.html'
#     model=Estilo
#     queryset = Estilo.objects.order_by('nombre')
    
# class OutfitListView(ListView):
#     model=Outfit
#     queryset = Outfit.objects.order_by('nombre')
# 	# def get_queryset(self):
# 	# 	return self.queryset.filter(Outfit.precio>35)


#MODELO IMPORTADO DE FORM
def contacto(request):
    if request.method == "POST":  #POST oculta los datos (enviados a través del formulario), a diferencia del GET que los muestra en la URL 
        form = FormularioContacto(request.POST)
        if form.is_valid(): #si los datos son correctos (están validados)
            infForm = form.cleaned_data #guardar en infForm los datos del formulario
            
            sub = "Contacto"
            msg = "Contacto recibido: " + infForm['nombre'] + " " + infForm['apellido'] + " - " + infForm['correo']   #TODO se concatenan así los strings?
            fromemail = "outfitshowroomapp@gmail.com"
            recipientlist = infForm['correo']
            

            send_mail(sub, msg, fromemail, [recipientlist])

            # email = EmailMessage(
            # "Contacto",
            # "Contacto recibido: " + infForm['nombre'] + " " + infForm['apellido'] + " - " + infForm['correo'],
            # "outfitshowroomapp@gmail.com",
            # [infForm['correo']],)

        

            return render(request, "enviado.html")
    else:
        form = FormularioContacto()
    return render(request, "contacto.html", {'form':form})



