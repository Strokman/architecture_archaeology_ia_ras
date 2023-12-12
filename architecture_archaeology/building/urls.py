from django.urls import path

from building.views import BuildingSubmitView, BuildingDetailView, BuildingListView

app_name = 'building'
urlpatterns = [
    path("submit/", BuildingSubmitView.as_view(), name="submit"),
    path("display/<slug:slug>/", BuildingDetailView.as_view(), name="display"),
    path("list/", BuildingListView.as_view(), name="list")
]