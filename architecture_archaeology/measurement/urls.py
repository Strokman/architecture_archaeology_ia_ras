from django.urls import path

from measurement.views import (SubmitRFAView,
                               SubmitMicroscopyView,
                               SubmitGCMSView,
                               SubmitInfraredRamanView,
                               SubmitRoentgenView,
                               SubmitPetrographyView,

                               DetailGCMSView,
                               DetailInfraredRamanView,
                               DetailRFAView,
                               DetailRoentgenView,
                               DetailScanningMiscroscopyView,
                               DetailPetrographyView,

                               UpdateGCMSView,
                               UpdateInfraredRamanView,
                               UpdateRFAView,
                               UpdateRoentgenView,
                               UpdateScanningMicroscopyView,
                               UpdatePetrographyView,

                               ListInfraredRamanView,
                               ListRoentgenView,
                               ListGCMSView,
                               ListRFAView,
                               ListScanningMicroscopyView,
                               ListPetrographyView
                               )

app_name = 'measurement'
urlpatterns = [
    path("submit/rfa/", SubmitRFAView.as_view(), name="submit-rfa"),
    path("submit/scanning-electron-microscopy/", SubmitMicroscopyView.as_view(), name="submit-scanningelectronmicroscopy"),
    path("submit/gc-ms/", SubmitGCMSView.as_view(), name="submit-gaschromatographymassspectrometry"),
    path("submit/roentgen/", SubmitRoentgenView.as_view(), name="submit-roentgen"),
    path("submit/infrared-raman/", SubmitInfraredRamanView.as_view(), name="submit-infraredramanmicroscopy"),
    path("submit/petrography/", SubmitPetrographyView.as_view(), name="submit-petrography"),

    path("detail/rfa/<slug:slug>", DetailRFAView.as_view(), name="detail-rfa"),
    path("detail/gc-ms/<slug:slug>", DetailGCMSView.as_view(), name="detail-gaschromatographymassspectrometry"),
    path("detail/infrared-raman/<slug:slug>", DetailInfraredRamanView.as_view(), name="detail-infraredramanmicroscopy"),
    path("detail/roentgen/<slug:slug>", DetailRoentgenView.as_view(), name="detail-roentgen"),
    path("detail/scanning-electron-microscopy/<slug:slug>", DetailScanningMiscroscopyView.as_view(), name="detail-scanningelectronmicroscopy"),
    path("detail/petrography/<slug:slug>", DetailPetrographyView.as_view(), name="detail-petrography"),

    path("update/gc-ms/<slug:slug>", UpdateGCMSView.as_view(), name="update-gaschromatographymassspectrometry"),
    path("update/rfa/<slug:slug>", UpdateRFAView.as_view(), name="update-rfa"),
    path("update/infrared-raman/<slug:slug>", UpdateInfraredRamanView.as_view(), name="update-infraredramanmicroscopy"),
    path("update/roentgen/<slug:slug>", UpdateRoentgenView.as_view(), name="update-roentgen"),
    path("update/scanning-electron-microscopy/<slug:slug>", UpdateScanningMicroscopyView.as_view(), name="update-scanningelectronmicroscopy"),
    path("update/petrography/<slug:slug>", UpdatePetrographyView.as_view(), name="update-petrography"),

    path("list/infrared-raman/", ListInfraredRamanView.as_view(), name="list-infraredramanmicroscopy"),
    path("list/gc-ms/", ListGCMSView.as_view(), name="list-gaschromatographymassspectrometry"),
    path("list/roentgen/", ListRoentgenView.as_view(), name="list-roentgen"),
    path("list/rfa/", ListRFAView.as_view(), name="list-rfa"),
    path("list/scanning-electron-microscopy/", ListScanningMicroscopyView.as_view(), name="list-scanningelectronmicroscopy"),
    path("list/petrography/", ListPetrographyView.as_view(), name="list-petrography"),
]