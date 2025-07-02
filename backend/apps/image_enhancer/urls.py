from django.urls import include, path
from rest_framework import routers

from apps.image_enhancer.views import ImageEnhance, ImageViewSet

app_name = "image"

router = routers.DefaultRouter()
router.register(r"", ImageViewSet, basename="Image")


urlpatterns = [
    path("enhance/", ImageEnhance.as_view()),
    path("", include(router.urls)),
]
