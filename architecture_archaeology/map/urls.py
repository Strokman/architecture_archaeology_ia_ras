from django.urls import path

from .views import MapView, get_data, get_user_data

app_name = 'map'
urlpatterns = [
    path("", MapView.as_view(), name="map"),
    path("get/", get_data, name="get"),
    path("user/", get_user_data, name="get_user")
]