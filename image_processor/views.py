from django.http import JsonResponse
import base64
import uuid
from celery.result import AsyncResult
from . import tasks
from .models import Image
from .utils import s3
from io import BytesIO

def convert_black_and_white(request, id=None):
    if request.method == 'POST':
        _file_name = request.FILES['file'].name
        file_data = request.FILES['file'].read()
        
        _task = tasks.black_and_white(file_data)

        return JsonResponse({'not_implemented': 'True'})

    if request.method == 'GET' and id:
        return JsonResponse({'not_implemented': 'True'})
