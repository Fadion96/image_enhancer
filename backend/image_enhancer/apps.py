from django.apps import AppConfig


class ImageEnhancerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'image_enhancer'

    def ready(self):
        from . import signals
