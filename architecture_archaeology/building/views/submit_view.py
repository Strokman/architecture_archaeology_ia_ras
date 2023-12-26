from typing import Any
from django.http import HttpResponse
from django.views.generic import FormView
from building.forms import SubmitBuildingForm
from building.models import Building
from file.services import FileHandler, S3FileHandler
from django.urls import reverse_lazy
# Create your views here.


class SubmitBuildingView(FormView):
    template_name = 'submit.html'
    form_class = SubmitBuildingForm
    success_url = reverse_lazy('index')

    def form_valid(self, form: Any) -> HttpResponse:
        building_data = {k: v for k, v in form.cleaned_data.items() if hasattr(Building, k)}
        new_building = Building(**building_data)
        new_building.save()
        uploaded_fotos = form.cleaned_data['foto']
        for foto in uploaded_fotos:
            processed_foto = FileHandler(foto,
                                         new_building,
                                         'фотография')
            foto_instance = processed_foto.to_orm()
            uploader = S3FileHandler(processed_foto)
            uploader.upload_file_to_s3()
            
            foto_instance.save()
            new_building.file_set.add(foto_instance)
            
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['method'] = 'POST'
        context['action'] = reverse_lazy('building:submit')
        context['render_kw'] = {'enctype': 'multipart/form-data'}
        return context
