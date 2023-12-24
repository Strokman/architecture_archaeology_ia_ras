from django.urls import path

from artwork.views import IndexView, SubmitArtworkView, ListArtworkView, DisplayArtworkView

app_name = 'artwork'
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("submit/", SubmitArtworkView.as_view(), name="submit"),
    path("list/", ListArtworkView.as_view(), name="list"),
    path("detail/<int:pk>", DisplayArtworkView.as_view(), name="detail"),
]