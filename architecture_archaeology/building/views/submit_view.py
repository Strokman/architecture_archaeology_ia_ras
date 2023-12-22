from typing import Any
from django.http import HttpResponse
from django.views.generic import FormView
from building.forms import SubmitBuildingForm
from building.models import Building
from file.models import File
from file.services import FileHandler, S3FileHandler
from django.urls import reverse_lazy
from uuid import uuid1
# Create your views here.


class SubmitBuildingView(FormView):
    template_name = 'building/submit.html'
    form_class = SubmitBuildingForm
    success_url = reverse_lazy('index')

    def form_valid(self, form: Any) -> HttpResponse:
        building_data = {k: v for k, v in form.cleaned_data.items() if hasattr(Building, k)}
        print(building_data)
        print(form.cleaned_data)
        print(type(form.cleaned_data['plan']))
        plan = form.cleaned_data['plan']
        print(plan.__dict__)
        print(plan.file.__dict__)
        f = FileHandler(plan)
        assert f.extension == 'pdf'
        assert f.original_filename == plan.name
        # new_bld = Building(**building_data)
        # uploaded_files = form.cleaned_data['foto']
        # for file in uploaded_files:
        #     extension = file.name.rsplit('.', 1)[1]
        #     filename = uuid1()
        #     file_type = 'foto'
        #     original_name = file.name
        #     new_file = File(filename=filename, extension=extension, original_name=original_name, file_type=file_type)
        # upload_file_to_s3(plan, f'some_test/{plan.name}')
        #     new_site.save()
        #     new_file.save()
        #     new_site.file_set.add(new_file)
            
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['method'] = 'POST'
        context['action'] = reverse_lazy('building:submit')
        context['render_kw'] = {'enctype': 'multipart/form-data'}
        return context
