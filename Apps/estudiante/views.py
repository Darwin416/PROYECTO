from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import Estudiante
from .forms import EstudiantesForm
from django.urls import reverse_lazy





# Create your views here.

class estudianteView(TemplateView):
    template_name='estudiante.html'

# Create Listado   Estudiantes.

class ListarEstudiantes(ListView):
    template_name = 'listestudiante.html'
    model = Estudiante

    def get_queryset(self):
        return Estudiante.objects.all()

# Create Listado   Estudiantes.

class CrearEstudiantes(CreateView):
    template_name = 'estudiante.html'
    form_class =  EstudiantesForm
    success_url = reverse_lazy('est:listest')         


