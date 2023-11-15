from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/<int:id>/", views.add_artwork, name="add_artwork"),
]