from datetime import datetime
from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image as PImage

from apps.image_enhancer.models import Image as ImageModel
from apps.image_enhancer.network.predict import predict


def enhance(content_image: ImageModel, style_image: ImageModel) -> ContentFile:
    content_img = PImage.open(content_image.image.path)
    style_img = PImage.open(style_image.image.path)

    enhanced_img = predict(content_img, style_img)
    enhanced_img_bytes = BytesIO()
    enhanced_img.save(enhanced_img_bytes, format="JPEG")
    img_file = ContentFile(
        enhanced_img_bytes.getvalue(),
        f'edited_{datetime.now().strftime("%Y%m%d-%H%M%S")}_{content_image.filename}',
    )

    return img_file
