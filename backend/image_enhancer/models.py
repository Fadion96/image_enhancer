from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
import os


def user_dir_path(instance, filename):
    return f"user_{instance.owner.id}/{filename}"


class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_dir_path)
    upload_date = models.DateTimeField(auto_now_add=True)
    is_result = models.BooleanField(default=False)

    def filename(self):
        return os.path.basename(self.image.name)
