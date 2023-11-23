from django.urls import path

from artwork.views import IndexView

app_name = 'artwork'
urlpatterns = [
    path("", IndexView.as_view(), name="index")
]