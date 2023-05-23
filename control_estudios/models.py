from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=164) #Equivalente de str
    comision = models.IntegerField() # Equivalente de int

    def __str__(self):
        return f'{self.nombre} / {self.comision}'

class Estudiante(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(blank=True)

    #Para permitir un campo en blanco, se debe agregar "blank=True", como en email y telefono, si fuera un numero, se agrega adicionalmente "null=True"
    def __str__(self):
        return f'{self.nombre}, {self.apellido}'

class Profesor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(blank=True)
    profesion = models.CharField(max_length=128)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField()
    esta_aprobado = models.BooleanField(default=False) # Equivalente a bool (True, False)