from django.core.exceptions import ValidationError


class FilesNumberValidationError(ValidationError):
    def __init__(self, value, *args, **kwargs):
        message = f'Количество файлов не должно превышать {value}'
        super().__init__(message=message, *args, **kwargs)
