from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True, max_length=3)
    nombre = models.CharField(max_length=30)
    especie = models.CharField(max_length=30)
    nivel = models.IntegerField(max_length=2)
    habilidad = models.CharField(max_length=30)
    objeto = models.CharField(max_length=20)
    icono = models.CharField(max_length=500)
    genero = models.CharField(max_length=1)
    intercambiable = models.CharField(max_length=1)

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    web = models.URLField(blank=True)

    # Python 3
    def __str__(self):
        return self.usuario.username


@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(usuario=instance)


@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()



