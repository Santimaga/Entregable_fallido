from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    #nacimiento =models.DateField()
    edad = models.IntegerField()
    con_vida = models.BooleanField()