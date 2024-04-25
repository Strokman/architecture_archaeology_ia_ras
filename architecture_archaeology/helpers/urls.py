from django.urls import path

from helpers.views import artwork_get_building


app_name = 'helpers'
urlpatterns = [
    path("get-building-by-artwork/<str:model>/<slug:slug>", artwork_get_building, name="get-artwork-building")
]