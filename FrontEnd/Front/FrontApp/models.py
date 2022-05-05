from django.db import models

# Create your models here.

class Prueba(models.Model):
    nombre = models.TextField()
    positivos = models.IntegerField()
    negativos = models.IntegerField()