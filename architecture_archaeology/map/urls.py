from django.urls import path

from .views import MapView, get_data

app_name = 'map'
urlpatterns = [
    path("", MapView.as_view(), name="map"),
    path("get/", get_data, name="get"),
]