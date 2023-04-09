from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision =  models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.comision}"
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)  
    apellido = models.CharField(max_length=50) 
    #dni =  models.IntegerField()
    email = models.EmailField() # unique LO USAMOS PARA NO REPETIR LOS DATOS DEL USUARIO, PARA QUE SEA CARGADO UNA SOLA VEZ

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    #dni =  models.IntegerField()
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_entrega = models.DateField()
    entregado =  models.BooleanField()
    
    
