from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Vehiculo

@receiver(post_save, sender=User)
def asignar_permiso_visualizar_catalogo(sender, instance, created, **kwargs):
    if created:
        content_type = ContentType.objects.get_for_model(Vehiculo)
        permiso = Permission.objects.get(content_type=content_type, codename='visualizar_catalogo')
        instance.user_permissions.add(permiso)
