from django.db import models

# Create your models here.

class Prueba(models.Model):
    nombre = models.TextField()
    positivos = models.IntegerField()
    negativos = models.IntegerField()


class SentimientosEmpresa(models.Model):
    nombre = models.TextField()
    totalMensajes = models.IntegerField()
    positivos = models.IntegerField()
    negativos = models.IntegerField()
    neutrales = models.IntegerField()