from django.views.generic.edit import ModelFormMixin

from django.http import HttpResponseRedirect
from file.services import FileHandler

filetypes = {
    'foto': 'foto',
    'plan': 'план',
    'report': 'отчет',
    'other': 'file'
}

# TODO: сделать проверку на несуществующие ключи и сделать ошибку


class FormValidFilesMixin(ModelFormMixin):
    """
    Если к объекту привязываются файлы - то переданные файлы обрабатываются,
    создаются записи в баз данных. Сами файлы загружаются в S3
    """
    
    def form_valid(self, form):
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
                    processed_foto.to_orm()
        return HttpResponseRedirect(self.get_success_url())
