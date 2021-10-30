from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import Maestro
from .forms import MaestrosForm
from django.urls import reverse_lazy


from Apps.maestro.models import Maestro

# Create your views here.
class teacherView(TemplateView):
    template_name='maestro.html'

# Create Listar Maestros.

class ListarMaestros(ListView):
    template_name = 'listadomaestro.html'
    model = Maestro

    def get_queryset(self):
        return Maestro.objects.all()   

# Create crear Maestros.

class CrearMaestros(CreateView):
    template_name = 'maestro.html'
    form_class =  MaestrosForm
    success_url = reverse_lazy('mto:listadomaestro') 

