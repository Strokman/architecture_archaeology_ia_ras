from django.urls import path

from arch_site.views import (SubmitSiteView,
                             ListSiteView,
                             DetailSiteView,
                             UpdateSiteView,
                             DeleteArchaeologicalSiteView)

from django.views.decorators.cache import cache_page

from architecture_archaeology.settings import DEFAULT_TIMEOUT

app_name = 'arch_site'
urlpatterns = [
    path("submit/", SubmitSiteView.as_view(), name="submit"),
    path("detail/<slug:slug>/", DetailSiteView.as_view(), name="detail"),
    path("list/", ListSiteView.as_view(), name="list"),
    path("update/<slug:slug>", UpdateSiteView.as_view(), name="update"),
    path("delete/arch-site/<slug:slug>", DeleteArchaeologicalSiteView.as_view(), name="delete"),
]
