from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Persona(models.Model):
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=50)
    telefono_suplente = models.CharField(max_length=9, default='')


    def __str__(self):
        return self.nombre

class Animales(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.CharField(max_length=2)
    tipo = models.CharField(max_length=30)
    raza = models.CharField(max_length=50, default='')
    datos = models.CharField(max_length=250, default='')
    diagnostico = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='fotos/')
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=False, blank=False)
