from django.db import models

# Create your models here.

class Cliente(models.Model):       
    rut = models.CharField(max_length=10, null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=100, null=False)
    edad= models.IntegerField()
    clave= models.CharField(max_length=20)