from django import forms
# from file.models import File


class UploadFileForm(forms.Form):
    file = forms.FileField()
