from django.contrib import admin
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import Admin, Salon, Seccion
from .models import Curso,Periodo

from .forms import AdminsForm, CursoForm ,PeriodoForm,SeccionForm,SalonForm
from django.urls import reverse_lazy


# Create your views here.

class adminView(TemplateView):
    template_name='admin.html'

class periodoView(TemplateView):
    template_name='periodo.html'

class temaView(TemplateView):
    template_name='tema.html'


class seccionView(TemplateView):
    template_name='seccion.html'    

class salonView(TemplateView):
    template_name='salon.html'   

# Listar Administradores 

class ListarAdmins(ListView):
    template_name = 'listadm.html'
    model = Admin

    def get_queryset(self):
        return Admin.objects.all()

# Listar Curso.

class ListarCursos(ListView):
    template_name = 'listadocurso.html'
    model = Curso

    def get_queryset(self):
        return Curso.objects.all()

# Listar seccion.

class ListarSeccion(ListView):
    template_name = 'listadoseccion.html'
    model = Seccion

    def get_queryset(self):
        return Seccion.objects.all()

# Listar Periodo.

class ListarPeriodo(ListView):
    template_name = 'listadoperiodo.html'
    model = Periodo

    def get_queryset(self):
        return Periodo.objects.all()
# Listar salon.

class ListarSalon(ListView):
    template_name = 'listadosalon.html'
    model = Salon

    def get_queryset(self):
        return Salon.objects.all()


# Crear vista  Administradores 

class CrearAdmins(CreateView):
    template_name = 'admin.html'
    form_class =  AdminsForm
    success_url = reverse_lazy('add:listadm') 

# Crear vista  Curso.


class CrearCurso(CreateView):
    template_name = 'tema.html'
    form_class =  CursoForm
    success_url = reverse_lazy('add:listadocurso') 

# Crear vista  Periodo.

class CrearPeriodo(CreateView):
    template_name = 'periodo.html'
    form_class =  PeriodoForm
    success_url = reverse_lazy('add:listadoperiodo')


# Crear vista  Seccion.

class CrearSeccion(CreateView):
    template_name = 'seccion.html'
    form_class =  SeccionForm
    success_url = reverse_lazy('add:listadoseccion')

    # Crear vista  Seccion.

class CrearSalon(CreateView):
    template_name = 'salon.html'
    form_class =  SalonForm
    success_url = reverse_lazy('add:listadosalon')

