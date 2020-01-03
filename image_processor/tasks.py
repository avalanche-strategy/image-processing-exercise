from celery import shared_task, current_task
from PIL import Image
from io import BytesIO
import uuid
from .utils import s3
from .models import Image as ImageModel

@shared_task
def black_and_white(image_data):
    return None
