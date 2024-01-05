from django.urls import path

from artefact.views import SubmitArtefactView, ListArtefactView, DetailArtefactView

app_name = 'artefact'
urlpatterns = [
    path("submit/", SubmitArtefactView.as_view(), name="submit"),
    path("list/", ListArtefactView.as_view(), name="list"),
    path("detail/<slug:slug>", DetailArtefactView.as_view(), name="detail"),
]