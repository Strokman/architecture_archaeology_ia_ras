from django.urls import path

from artwork.views import (SubmitIndoorArtworkView,
                           ListIndoorArtworkView,
                           DetailIndoorArtworkView,
                           SubmitFrescoeView,
                           ListFrescoeView,
                           DetailFrescoeView,
                           UpdateFrescoeView,
                           UpdateIndoorArtworkView,
                           ListLotokView,
                           SubmitLotokView,
                           DetailLotokView,
                           UpdateLotokView
                           )

app_name = 'artwork'
urlpatterns = [
    path("submit/indoor/", SubmitIndoorArtworkView.as_view(), name="submit-indoorartwork"),
    path("list/indoor/", ListIndoorArtworkView.as_view(), name="list-indoorartwork"),
    path("detail/indoor/<slug:slug>", DetailIndoorArtworkView.as_view(), name="detail-indoorartwork"),
    path("update/indoor/<slug:slug>", UpdateIndoorArtworkView.as_view(), name="update-indoorartwork"),
    path("submit/frescoe/", SubmitFrescoeView.as_view(), name="submit-frescoe"),
    path("list/frescoes/", ListFrescoeView.as_view(), name="list-frescoe"),
    path("detail/frescoe/<slug:slug>", DetailFrescoeView.as_view(), name="detail-frescoe"),
    path("update/frescoe/<slug:slug>", UpdateFrescoeView.as_view(), name="update-frescoe"),
    path("list/lotok/", ListLotokView.as_view(), name="list-lotok"),
    path("submit/lotok/", SubmitLotokView.as_view(), name="submit-lotok"),
    path("detail/lotok/<slug:slug>", DetailLotokView.as_view(), name="detail-lotok"),
    path("update/lotok/<slug:slug>", UpdateLotokView.as_view(), name="update-lotok"),
]
