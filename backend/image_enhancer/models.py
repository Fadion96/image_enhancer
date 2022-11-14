from django.db import models
from django.contrib.auth.models import User

def user_dir_path(instance, filename):
    return f'user_{instance.owner.id}/{filename}'

class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_dir_path)
    upload_date = models.DateTimeField(auto_now_add=True)
