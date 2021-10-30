from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class datosView(TemplateView):
     template_name='datos.html'

class registroView(TemplateView):
     template_name='registro.html'