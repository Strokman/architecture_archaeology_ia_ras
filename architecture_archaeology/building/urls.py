from django.urls import path

from building.views import Submit, Display, ListBuildingView

app_name = 'building'
urlpatterns = [
    path("submit/", Submit.as_view(), name="submit"),
    path("display/", Display.as_view(), name="display"),
    path("list/", ListBuildingView.as_view(), name="list")
]