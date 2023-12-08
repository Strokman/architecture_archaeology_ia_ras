from django.urls import path

from file.views import UploadFileView

app_name = 'file'
urlpatterns = [
    path("upload/", UploadFileView.as_view(), name="upload")
]