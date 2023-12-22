from typing import Any
from django.views.generic import UpdateView

from building.forms import SubmitBuildingForm
from building.models import Building

from file.services import FileHandler
from file.services import S3FileHandler


class UpdateBuildingView(UpdateView):
    model = Building
    form_class = SubmitBuildingForm
    template_name = 'building/update.html'
    success_url = '/'

    def form_valid(self, form):
        building = form.save()
        uploaded_fotos = form.cleaned_data['foto']
        for foto in uploaded_fotos:
            processed_foto = FileHandler(foto,
                                         building,
                                         'фотография')
            foto_instance = processed_foto.to_orm()
            uploader = S3FileHandler(processed_foto)
            uploader.upload_file_to_s3()
            foto_instance.save()
            building.file_set.add(foto_instance)
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование - {self.model}'
        context['method'] = 'POST'
        context['value'] = 'Save'
        context['render_kw'] = {'enctype': 'multipart/form-data'}
        return context
