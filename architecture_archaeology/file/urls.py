from django.urls import path

from file import views

app_name = 'file'
urlpatterns = [
    path("get/<str:filename>", views.get_file, name="get")
]