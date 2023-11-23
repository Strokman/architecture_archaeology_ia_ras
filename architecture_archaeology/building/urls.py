from django.urls import path

from building.views import Submit, Display

app_name = 'building'
urlpatterns = [
    path("submit/", Submit.as_view(), name="submit"),
    path("display/", Display.as_view(), name="display")
]