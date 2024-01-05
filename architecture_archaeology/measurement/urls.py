from django.urls import path

from measurement.views import SubmitRFAView

app_name = 'measurement'
urlpatterns = [
    path("submit/", SubmitRFAView.as_view(), name="submit"),
]