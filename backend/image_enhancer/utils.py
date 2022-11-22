from PIL import Image as PImage
from PIL.ImageOps import grayscale
from io import BytesIO
from django.core.files.base import ContentFile


def enhance(image):
    img = PImage.open(image.image.path)

    enhanced_img = grayscale(img)
    enhanced_img_bytes = BytesIO()
    enhanced_img.save(enhanced_img_bytes, format="JPEG")
    img_file = ContentFile(enhanced_img_bytes.getvalue(), f'edited_{image.filename()}')
    return img_file
