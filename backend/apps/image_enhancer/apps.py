from django.apps import AppConfig


class ImageEnhancerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.image_enhancer"

    def ready(self) -> None:
        import apps.image_enhancer.signals
