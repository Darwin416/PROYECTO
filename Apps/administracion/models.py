from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

# Create your models Admin.

class Admin(models.Model):
    nombre=models.CharField(max_length=50) 
    apellido=models.CharField(max_length=50) 
    direccion=models.CharField(max_length=20) 
    email=models.CharField(max_length=20) 
    telefono=models.CharField(max_length=200) 

    def __str__(self):
        return '%s %s %s' % (self.nombre,self.apellido,self.email)

# Create your models curso.

class Curso(models.Model):

   st = (
    ("ACTIVO","ACTIVO"),
    ("DESACTIVAR","DESACTIVAR"),
    )

   codigo=models.CharField(max_length=50) 
   nombre=models.CharField(max_length=50) 
   estado=models.CharField(
        max_length=20,
        choices=st,
        default="M") 
    

   def __str__(self):
        return '%s %s %s' % (self.codigo,self.nombre,self.estado)

# Create your models Sección.

class Seccion(models.Model):

   st = (
    ("ACTIVO","ACTIVO"),
    ("DESACTIVAR","DESACTIVAR"),
    )

   añ = (
    ("2021","2021"),
    ("2022","2022"),
    )
   sc = (
    ("A","A"),
    ("B","B"),
    ("C","C"),
    )

   seccion=models.CharField(
        max_length=20,
        choices=sc,
        default="M") 
   estado=models.CharField(
        max_length=20,
        choices=st,
        default="M") 

   año=models.CharField(
        max_length=20,
        choices=añ,
        default="M") 

   def __str__(self):
        return '%s %s %s' % (self.seccion,self.estado,self.año,)  


# Create your models Salon.

class Salon(models.Model):

   

   codigo=models.CharField(max_length=50) 
   capacidad=models.CharField(max_length=50) 
    

   def __str__(self):
        return '%s %s ' % (self.codigo,self.capacidad)    

# Create your models Periodo.

class Periodo(models.Model):
   
   st = (
    ("ACTIVO","ACTIVO"),
    ("DESACTIVAR","DESACTIVAR"),
    )

   hora_de_inicio=models.DateField() 
   hora_de_final=models.DateField() 
   estado=models.CharField(
        max_length=20,
        choices=st,
        default="M") 

   def __str__(self):
        return '%s %s %s' % (self.hora_de_inicio,self.hora_de_final,self.estado) 