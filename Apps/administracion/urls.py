"""Administracion Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import   CrearSeccion,ListarSalon, adminView, periodoView,temaView,seccionView,salonView,ListarAdmins,CrearAdmins,ListarCursos,CrearCurso,ListarPeriodo,CrearPeriodo,ListarSeccion,ListarSalon, CrearSalon

app_name='add'


urlpatterns = [
    path('admin/', adminView.as_view(), name='administracion'),
    path('periodo/', periodoView.as_view(), name='periodo'),
    path('tema/',temaView.as_view(), name='tema'),
    path('seccion/', seccionView.as_view(), name='seccion'),
    path('salon/',salonView.as_view(), name='salon'),
    
    path('listado_admin/',ListarAdmins.as_view(), name='listadm'),
    path('crearadmin/',CrearAdmins.as_view(), name='crearadmin'),

    path('listadocurso/',ListarCursos.as_view(), name='listadocurso'),
    path('crearcurso/', CrearCurso.as_view(), name='crearcurso'),

    path('listadoperiodo/',ListarPeriodo.as_view(), name='listadoperiodo'),
    path('crearperiodo/',CrearPeriodo.as_view(), name='crearperiodo'),

    path('listadoseccion/',ListarSeccion.as_view(), name='listadoseccion'),
    path('crearseccion/',CrearSeccion.as_view(), name='crearseccion'),

    path('listadosalon /',ListarSalon.as_view(), name='listadosalon'),
    path('crearsalon/', CrearSalon.as_view(), name='crearsalon'),


    


    







]
