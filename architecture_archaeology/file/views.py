from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from file.services import S3FileHandler
from file.models import File, Foto
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.


def check_admin(user):
    return user.is_superuser


@login_required
def get_file(request, filename):
    file = File.objects.get(filename=filename)
    file_from_cloud = S3FileHandler(file)
    return_value = file_from_cloud.get_file_from_s3()
    response = HttpResponse(return_value, content_type=f'application/{file.extension}')
    return response


@login_required
def get_foto(request, filename):
    file = Foto.objects.get(filename=filename)
    file_from_cloud = S3FileHandler(file)
    return_value = file_from_cloud.get_file_from_s3()
    response = HttpResponse(return_value, content_type=f'application/{file.extension}')
    return response


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
