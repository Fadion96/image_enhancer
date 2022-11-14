from django.urls import path, include
from .views import ImageViewSet


app_name = 'image'
urlpatterns = [
   path("", ImageViewSet.as_view({'get': 'list'}), name="index"),
   path("upload", ImageViewSet.as_view({'post': 'create'}), name="index"),
]