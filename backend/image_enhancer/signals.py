from typing import Any
from django.dispatch import receiver
from django.db.models.signals import post_delete
from image_enhancer.models import Image
import os


@receiver(post_delete, sender=Image)
def remove_image_file_on_delete(
    sender: Image, instance: Image, **kwargs: Any
) -> None:
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
