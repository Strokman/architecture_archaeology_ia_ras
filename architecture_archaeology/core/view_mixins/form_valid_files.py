from django.views import View
from django.views.generic.edit import ModelFormMixin

from django.http import HttpResponseRedirect
from file.services import FileHandler
from file.services import S3FileHandler

filetypes = {
    'foto': 'фотография',
    'plan': 'план',
    'report': 'отчет',
    'other': 'другое'
}

# TODO: сделать проверку на несуществующие ключи и сделать ошибку


class FormValidFilesMixin(ModelFormMixin):

    def form_valid(self, form):
        super().form_valid(form)
        existing_keys = set(form.cleaned_data) & set(filetypes)
        for key in existing_keys:
            files = form.cleaned_data.get(key)
            if files:
                files_list = []
                if isinstance(files, list):
                    files_list = files
                else:
                    files_list.append(files)
                for file in files_list:
                    processed_foto = FileHandler(file,
                                             self.object,
                                             filetypes.get(key))
                    file_instance = processed_foto.to_orm()
                    uploader = S3FileHandler(processed_foto)
                    uploader.upload_file_to_s3()
                    file_instance.save()
                    self.object.file_set.add(file_instance)
        return HttpResponseRedirect(self.get_success_url())