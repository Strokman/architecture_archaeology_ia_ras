from django.apps import apps


class FileFactory:

    def __init__(self, obj, file_data) -> None:
        self.obj = obj
        self.file_data = file_data

    @classmethod
    def create_file(cls, model_name, file_data):
        model = apps.get_model('file', model_name)
        return model.objects.create(**file_data)
