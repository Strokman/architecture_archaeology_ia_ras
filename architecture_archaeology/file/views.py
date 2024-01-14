from typing import Any
from django.http import HttpResponse

from file.services import S3FileHandler
from file.models import File
# Create your views here.


def get_file(request, filename):
    file = File.objects.get(filename=filename)
    file_from_cloud = S3FileHandler(file)
    return_value = file_from_cloud.get_file_from_s3()
    response = HttpResponse(return_value, content_type=f'application/{file.extension}')
    return response
