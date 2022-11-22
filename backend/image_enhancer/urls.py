from django.urls import path, include
from .views import ImageViewSet, ImageEnhance
from rest_framework import routers

app_name = 'image'

router = routers.DefaultRouter()
router.register(r'', ImageViewSet, basename='Image')


urlpatterns = [
   path("enhance/", ImageEnhance.as_view()),
   path("", include(router.urls)),
]