from django.urls import path

from artwork.views import (SubmitIndoorArtworkView,
                           ListIndoorArtworkView,
                           DetailIndoorArtworkView,
                           SubmitFrescoeView)

app_name = 'artwork'
urlpatterns = [
    path("submit/indoor/", SubmitIndoorArtworkView.as_view(), name="submit-indoor"),
    path("list/indoor/", ListIndoorArtworkView.as_view(), name="list-indoor"),
    path("detail/indoor/<slug:slug>", DetailIndoorArtworkView.as_view(), name="detail-indoor"),
    path("submit/frescoe/", SubmitFrescoeView.as_view(), name="submit-frescoe")
]
