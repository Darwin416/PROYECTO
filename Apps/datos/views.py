from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class infoView(TemplateView):
    template_name='info.html'
