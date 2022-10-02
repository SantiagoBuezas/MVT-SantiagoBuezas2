from django.db import models

# Create your models here.
class Familiar(models.Model):

    nombre = models.CharField()
    parentezco = models.CharField()
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()
