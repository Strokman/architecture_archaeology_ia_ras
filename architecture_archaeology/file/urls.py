from django.urls import path

from file import views

from django.views.decorators.cache import cache_page
from architecture_archaeology.settings import DEFAULT_TIMEOUT

app_name = 'file'
urlpatterns = [
    path("file/get/<str:filename>", cache_page(DEFAULT_TIMEOUT)(views.get_file), name="get"),
    path("foto/get/<str:filename>", cache_page(DEFAULT_TIMEOUT)(views.get_foto), name="get-foto"),
    path("file/delete/<str:filename>", cache_page(DEFAULT_TIMEOUT)(views.delete_file), name="delete-file"),
    path("foto/delete/<str:filename>", cache_page(DEFAULT_TIMEOUT)(views.delete_foto), name="delete-foto"),
    path("default-image/<str:model_name>", cache_page(DEFAULT_TIMEOUT)(views.get_default_image), name="get-default-image"),
]