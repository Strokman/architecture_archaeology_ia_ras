from django.urls import path

from artefact.views import SubmitArtefactView, ListArtefactView, DetailArtefactView, UpdateArtefactView

app_name = 'artefact'
urlpatterns = [
    path("submit/", SubmitArtefactView.as_view(), name="submit"),
    path("list/", ListArtefactView.as_view(), name="list"),
    path("detail/<slug:slug>", DetailArtefactView.as_view(), name="detail"),
    path("update/artefact/<slug:slug>", UpdateArtefactView.as_view(), name="update")
]