from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.template import Template, Context, context
from .models import Prenda, Ocasion, Estilo, Outfit, OutfitShowroom
from .forms import FormularioContacto
from django.core.mail import send_mail, EmailMessage
    
#DETAIL VIEWS
# class PrendaDetailView(DetailView):
#     model=Prenda
#     template_name= 'prueba_detail.html'

class OcasionDetailView(DetailView):
    model=Ocasion
    template_name= 'ocasion.html'        
    context_object_name = "ocasion"
    # {%block ocasion_info%}
	# 				<h2>{{ocasion.nombre}}</h2>
	# 				<p>{{ocasion.desc}}</p>
	# 				{%for i in ocasion.outfit_set.all%}
	# 					{{i.nombre}}
	# 					{%endfor%}
	# 				{%endblock%}
    
class EstiloDetailView(DetailView):
    template_name= 'estilo.html'
    context_object_name = "estilo" #Si no como se llamaria? porque estilo_list no funciona
    model=Estilo
    # def get_queryset(self):
    #     return self.queryset.filter(outfits=self.model.id_est)
    
class OutfitDetailView(DetailView):
    template_name= 'outfit.html'
    model=Outfit
    context_object_name = "outfit"
    
 

#DETAIL LISTS
class HomeListView(ListView):
    template_name= 'home.html'
    model = OutfitShowroom
    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['ocasion_list'] = Ocasion.objects.order_by('id_oc')
        context['outfit_list'] = Outfit.objects.order_by('nombre')
        return context

class OcasionListView(ListView):
    template_name= 'ocasiones.html'
    model=Ocasion
    queryset = Ocasion.objects.order_by('nombre')
    
class EstiloListView(ListView):
    template_name= 'estilos.html'
    model=Estilo
    #queryset = Estilo.objects.order_by('nombre')
    
class OutfitListView(ListView):
    model=Outfit
    template_name= 'outfits.html'
    queryset = Outfit.objects.order_by('nombre')
	# def get_queryset(self):
	# 	return self.queryset.filter(Outfit.precio>35)



#MODELO IMPORTADO DE FORM
def contacto(request):
    if request.method == "POST":  #POST oculta los datos (enviados a través del formulario), a diferencia del GET que los muestra en la URL 
        form = FormularioContacto(request.POST)
        if form.is_valid(): #si los datos son correctos (están validados) = true
            infForm = form.cleaned_data #guardar en infForm los datos del formulario
            
            sub = "Contacto"
            msg = "Contacto recibido: " + infForm['nombre'] + " " + infForm['apellido'] + " - " + infForm['correo']   
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


# #VISTA PARA AGENDA VUE
# def agenda(request):
#     return render(request, "index.html")

