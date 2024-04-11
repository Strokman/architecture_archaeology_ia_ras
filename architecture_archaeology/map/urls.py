from django.urls import path

from .views import MapView, get_data, get_user_data

from django.views.decorators.cache import cache_page
from architecture_archaeology.settings import DEFAULT_TIMEOUT

app_name = 'map'
urlpatterns = [
    path("", cache_page(DEFAULT_TIMEOUT)(MapView.as_view()), name="map"),
    path("get/", get_data, name="get"),
    path("user/", get_user_data, name="get_user")
]