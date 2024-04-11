from django.urls import path

from building.views import SubmitBuildingView, BuildingDetailView, BuildingListView, UpdateBuildingView

from django.views.decorators.cache import cache_page

from architecture_archaeology.settings import DEFAULT_TIMEOUT

app_name = 'building'
urlpatterns = [
    path("submit/", SubmitBuildingView.as_view(), name="submit"),
    path("detail/<slug:slug>/", BuildingDetailView.as_view(), name="detail"),
    path("list/", BuildingListView.as_view(), name="list"),
    path("update/<slug:slug>", UpdateBuildingView.as_view(), name="update")
]