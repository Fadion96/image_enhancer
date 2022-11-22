from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import Image
import os

@receiver(post_delete, sender=Image)
def remove_image_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
