from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import request
from .forms import UserRegistroForm
from django.contrib import messages

# Create your views here.

class homeView(TemplateView):
    template_name='home.html'

class loginView(TemplateView):
    template_name='login.html'

# Create registro de usuarios.

def registro(request):
    if request.method == 'POST':
        form = UserRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect ('hme:home')
    else:
        form = UserRegistroForm()
    context = { 'form': form }
    return render(request, 'registro.html',context)

