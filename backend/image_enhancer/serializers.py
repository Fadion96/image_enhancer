from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    owner_id = serializers.ReadOnlyField(source="owner.id")
    image = serializers.ImageField(required=True)
    # is_result = serializers.BooleanField(required=False)

    class Meta:
        model = Image
        fields = [
            "id",
            "owner",
            "owner_id",
            "image",
            "upload_date",
            "is_result",
        ]
        read_only_fields = ["is_result"]
