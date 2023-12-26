from django.urls import path

from arch_site.views import SubmitSiteView, ListSiteView, DisplaySiteView, UpdateSiteView

app_name = 'arch_site'
urlpatterns = [
    path("submit/", SubmitSiteView.as_view(), name="submit"),
    path("display/<slug:slug>/", DisplaySiteView.as_view(), name="detail"),
    path("list/", ListSiteView.as_view(), name="list"),
    path("update/<slug:slug>", UpdateSiteView.as_view(), name="update")
]