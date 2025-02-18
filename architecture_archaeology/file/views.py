from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from file.services import S3FileHandler
from file.models import File, Foto
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.


def check_admin(user):
    return user.is_superuser


class DefaultImage:
    """
    Здесь данные дефолтных картинок для разных моделей
    """

    def __init__(self, model_name):
        self.extension = 'jpg'
        self.object_storage_key = f'defaults/{model_name}.{self.extension}'

"""
View для получения файлов из S3 из темплейтов (для preview).
В идеале нужно все переделать на pre-signed links и сжатие файлов
"""
@login_required
def get_file(request, filename):
    file = File.objects.get(filename=filename)
    file_from_cloud = S3FileHandler(file)
    return_value = file_from_cloud.get_file_from_s3()
    response = HttpResponse(return_value, content_type=f'application/{file.extension}')
    response['Content-Disposition'] = f'attachment; filename={file.original_name}'
    return response


@login_required
def get_default_image(request, model_name):
    img = DefaultImage(model_name)
    file_from_cloud = S3FileHandler(img)
    return_value = file_from_cloud.get_file_from_s3()
    response = HttpResponse(return_value, content_type=f'application/{img.extension}')
    return response


@login_required
def get_foto(request, filename):
    file = Foto.objects.get(filename=filename)
    file_from_cloud = S3FileHandler(file)
    return_value = file_from_cloud.get_file_from_s3()
    response = HttpResponse(return_value, content_type=f'application/{file.extension}')
    response['Content-Disposition'] = f'attachment; filename={file.original_name}'
    return response

"""
View для удаления файлов из S3 из темплейтов.
Добавлена проверка на то, что пользователь - админ
"""
@user_passes_test(check_admin, '/')
@login_required
def delete_file(request, filename):
    if request.method == 'POST':
        file = File.objects.get(filename=filename)
        s3file = S3FileHandler(file)
        s3file.delete_file_from_s3()
        file.delete()
        messages.success(request, 'Файл успешно удален')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@user_passes_test(check_admin, '/')
@login_required
def delete_foto(request, filename):
    if request.method == 'POST':
        file = Foto.objects.get(filename=filename)
        s3file = S3FileHandler(file)
        s3file.delete_file_from_s3()
        file.delete()
        messages.success(request, 'Файл успешно удален')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
