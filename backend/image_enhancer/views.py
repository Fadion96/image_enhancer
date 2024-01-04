from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from image_enhancer.models import Image
from image_enhancer.utils import enhance
from image_enhancer.serializers import ImageSerializer


class ImageViewSet(ModelViewSet):
    serializer_class = ImageSerializer
    parser_classes = [FormParser, MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self) -> list[Image]:
        return Image.objects.filter(owner=self.request.user)

    def perform_create(self, serializer: ImageSerializer) -> None:
        serializer.save(owner=self.request.user)


class ImageEnhance(APIView):
    # serializer_class = EnhanceSerializer
    parser_classes = [JSONParser]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: Request) -> Response:
        content_image_id = request.data["content_image"]
        style_image_id = request.data["style_image"]
        queryset = Image.objects.filter(owner=request.user)
        content_image = get_object_or_404(queryset, pk=content_image_id)
        style_image = get_object_or_404(queryset, pk=style_image_id)

        enhanced_img_file = enhance(content_image, style_image)
        enhanced_img = Image(
            owner=request.user, image=enhanced_img_file, is_result=True
        )
        enhanced_img.save()
        enhanced_img_serialized = ImageSerializer(enhanced_img).data

        return Response(
            enhanced_img_serialized, status=status.HTTP_201_CREATED
        )
