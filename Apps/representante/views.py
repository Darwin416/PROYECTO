from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import  Representante
from .forms import RepresentantesForm
from django.urls import reverse_lazy


# Create your views here.
class representativoView(TemplateView):
    template_name='representante.html'

# Create ListarRepresentantes.

class ListarRepresentantes(ListView):
    template_name = 'listadorepresentante.html'
    model = Representante

    def get_queryset(self):
        return Representante.objects.all()

# Create crear Representantes.
class CrearRepresentantes(CreateView):
    template_name = 'representante.html'
    form_class =  RepresentantesForm
    success_url = reverse_lazy('rpt:listadorepresentante') 

