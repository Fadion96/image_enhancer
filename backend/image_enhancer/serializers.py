from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    image = serializers.ImageField(required=True)

    class Meta:
        model = Image
        fields = ['id', 'owner', 'owner_id', 'image', 'upload_date']