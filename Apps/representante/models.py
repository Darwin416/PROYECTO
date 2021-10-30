from django.db import models

# Create your models here.
class Representante(models.Model):
    gen = (
    ("FEMENINO","FEMENINO"),
    ("MASCULINO","MASCULINO"),
    )
    nombre=models.CharField(max_length=50) 
    apellido=models.CharField(max_length=50) 
    direccion=models.CharField(max_length=200) 
    email=models.CharField(max_length=200) 
    telefono=models.CharField(max_length=200) 
    ocupacion=models.CharField(max_length=200) 
    genero=models.CharField(
        max_length=20,
        choices=gen,
        default="M") 

    def __str__(self):
        return '%s %s %s %s' % (self.nombre,self.apellido,self.ocupacion,self.genero)   
