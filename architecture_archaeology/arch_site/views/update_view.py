from typing import Any
from django.views.generic import UpdateView
from arch_site.models import ArchaeologicalSite

from arch_site.forms import SubmitArchaeologicalSiteForm


from file.services import FileHandler
from file.services import S3FileHandler



class UpdateSiteView(UpdateView):
    model = ArchaeologicalSite
    # form_class = SubmitArchaeologicalSubmitArchaeologicalSiteForm
    # fields = ['name', 'description', 'region', 'long', 'lat', 'year_min', 'year_max', 'comment']
    form_class = SubmitArchaeologicalSiteForm
    template_name = 'arch_site/update.html'
    success_url = '/'

    def form_valid(self, form):
        site = form.save()
        uploaded_fotos = form.cleaned_data['foto']
        for foto in uploaded_fotos:
            processed_foto = FileHandler(foto,
                                         site,
                                         'фотография')
            foto_instance = processed_foto.to_orm()
            uploader = S3FileHandler(processed_foto)
            uploader.upload_file_to_s3()
            site.save()
            foto_instance.save()
            site.file_set.add(foto_instance)
        plan = FileHandler(form.cleaned_data['plan'],
                           site,
                           'план')
        plan_instance = plan.to_orm()
        uploader = S3FileHandler(plan)
        uploader.upload_file_to_s3()
        plan_instance.save()
        site.file_set.add(plan_instance)
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # logger.info(f'Display view of {self.object_name} accessed')
        context['title'] = f'Редактирование - {self.model}'
        # context['action'] = reverse_lazy('arch_site:update', self.get_object().slug)
        context['method'] = 'POST'
        context['value'] = 'Save'
        context['render_kw'] = {'enctype': 'multipart/form-data'}
        return context
