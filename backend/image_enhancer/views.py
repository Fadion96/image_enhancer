from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from .models import Image
from .utils import enhance
from .serializers import ImageSerializer

class ImageViewSet(ModelViewSet):

    serializer_class = ImageSerializer
    parser_classes = [FormParser, MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Image.objects.filter(owner=self.request.user)
        
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ImageEnhance(APIView):

    # serializer_class = EnhanceSerializer
    parser_classes = [JSONParser]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        content_image_id = request.data['content_image_id']
        style_image_id = request.data['style_image_id']
        queryset= Image.objects.filter(owner=request.user)
        content_image = get_object_or_404(queryset, pk=content_image_id)
        style_image = get_object_or_404(queryset, pk=style_image_id)

        enhanced_img_file = enhance(content_image, style_image)
        enhanced_img = Image(owner=request.user, image=enhanced_img_file)
        enhanced_img.save()
        enhanced_img_serialized = ImageSerializer(enhanced_img).data
        
        return Response(enhanced_img_serialized, status=status.HTTP_201_CREATED)
        