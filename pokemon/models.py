from django.db import models

# Create your models here.

from django.db import models

class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True, max_length=3)
    nombre = models.CharField(max_length=30)
    especie = models.CharField(max_length=30)
    nivel = models.IntegerField(max_length=2)
    habilidad = models.CharField(max_length=30)
    objeto = models.CharField(max_length=20)

    intercambiable = models.BooleanField


