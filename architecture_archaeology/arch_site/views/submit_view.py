from typing import Any
from django.http import HttpResponse
from django.views.generic import FormView
from arch_site.forms import SubmitArchaeologicalSiteForm
from arch_site.models import ArchaeologicalSite
from django.urls import reverse_lazy
from file.services import FileHandler
from file.services import S3FileHandler


# Create your views here.


class SubmitSiteView(FormView):
    template_name = 'arch_site/submit.html'
    form_class = SubmitArchaeologicalSiteForm
    success_url = reverse_lazy('index')

    def form_valid(self, form: Any) -> HttpResponse:
        arch_site_data = {k: v for k, v in form.cleaned_data.items() if hasattr(ArchaeologicalSite, k)}
        new_site = ArchaeologicalSite(**arch_site_data)
        uploaded_fotos = form.cleaned_data['foto']
        for foto in uploaded_fotos:
            processed_foto = FileHandler(foto,
                                         new_site,
                                         'фотография')
            foto_instance = processed_foto.to_orm()
            uploader = S3FileHandler(processed_foto)
            uploader.upload_file_to_s3()
            new_site.save()
            foto_instance.save()
            new_site.file_set.add(foto_instance)
        plan = FileHandler(form.cleaned_data['plan'],
                           new_site,
                            'план')
        plan_instance = plan.to_orm()
        uploader = S3FileHandler(plan)
        uploader.upload_file_to_s3()
        plan_instance.save()
        new_site.file_set.add(plan_instance)
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['method'] = 'POST'
        context['action'] = reverse_lazy('arch_site:submit')
        context['render_kw'] = {'enctype': 'multipart/form-data'}
        return context
