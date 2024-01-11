from django.urls import path

from measurement.views import (SubmitRFAView,
                               SubmitMicroscopyView,
                               SubmitGCMSView
                               )

app_name = 'measurement'
urlpatterns = [
    path("submit/rfa/", SubmitRFAView.as_view(), name="submit-rfa"),
    path("submit/microscopy/", SubmitMicroscopyView.as_view(), name="submit-scanningelectronmicroscopy"),
    path("submit/gc-ms/", SubmitGCMSView.as_view(), name="submit-gaschromatographymassspectrometry"),
]