from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Image
from .serializers import ImageSerializer
from rest_framework.parsers import FormParser, MultiPartParser


class ImageViewSet(ModelViewSet):

    serializer_class = ImageSerializer
    parser_classes = [FormParser, MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Image.objects.filter(owner=self.request.user)
        
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)