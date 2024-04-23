"""
URL configuration for architecture_archaeology project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api import api_view as view

router = routers.DefaultRouter()
router.register(r'arch-sites', view.ArchsiteViewSet)

admin.site.site_header = "Архитектурная Археология"
admin.site.index_title = "Административная панель"

urlpatterns = [
    path(
        "accounts/password_change/",
        auth_views.PasswordChangeView.as_view(template_name="registration/change-password.html"),
    ),
    path(
        "accounts/password_reset/",
        auth_views.PasswordResetView.as_view(template_name="registration/change-password.html"),
    ),
    path(
        "accounts/password_change/done/",
        auth_views.PasswordResetView.as_view(template_name="registration/change-password-done.html"),
    ),
    path(
        "accounts/reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="registration/change-password.html"),
    ),
    path(
        "accounts/password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="registration/reset-password-done.html"),
    ),
    path(
        "accounts/reset/done/",
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/change-password-done.html"),
    ),
    path("", include("index.urls")),
    path("artwork/", include("artwork.urls")),
    path("arch-site/", include("arch_site.urls")),
    path("building/", include("building.urls")),
    path("file/", include("file.urls")),
    path("artefact/", include("artefact.urls")),
    path("measurement/", include("measurement.urls")),
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("map/", include("map.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path(
        "accounts/password_change/",
        auth_views.PasswordChangeView.as_view(template_name="change-password.html"),
    ),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
