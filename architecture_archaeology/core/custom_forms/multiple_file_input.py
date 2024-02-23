from django import forms
from core.exceptions import FilesNumberValidationError


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, value, *args, **kwargs):
        self.allowed_number_of_files = value
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        if len(data) > self.allowed_number_of_files:
            raise FilesNumberValidationError(self.allowed_number_of_files)
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
