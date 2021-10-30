from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Estudiante(models.Model):
    gen = (
    ("FEMENINO","FEMENINO"),
    ("MASCULINO","MASCULINO"),
    )
    tp = (
    ("VIEJO","VIEJO"),
    ("NUEVO","NUEVO"),
    )
    sc = (
    ("A","A"),
    ("B","B"),
    ("C","C"),
    )
    nombre=models.CharField(max_length=50) 
    apellido=models.CharField(max_length=50) 
    direccion=models.CharField(max_length=20) 
    email=models.CharField(max_length=20) 
    telefono=models.CharField(max_length=20) 
    genero=models.CharField(
        max_length=20,
        choices=gen,
        default="M") 
    tipo=models.CharField(
        max_length=20,
        choices=tp,
        default="N") 
    seccion=models.CharField(
        max_length=20,
        choices=sc,
        default="A") 


    def __str__(self):
        return '%s %s %s %s' % (self.nombre,self.apellido,self.seccion,self.genero,)     
 
