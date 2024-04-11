from django.urls import path

from file import views

from django.views.decorators.cache import cache_page
from architecture_archaeology.settings import DEFAULT_TIMEOUT

app_name = 'file'
urlpatterns = [
    path("get/<str:filename>", cache_page(DEFAULT_TIMEOUT)(views.get_file), name="get")
]