from typing import Any
from django.views.generic import UpdateView
from arch_site.models import ArchaeologicalSite

# from arch_site.forms import SubmitArchaeologicalSiteForm


class UpdateSiteView(UpdateView):
    model = ArchaeologicalSite
    # form_class = SubmitArchaeologicalSiteForm
    fields = ['name', 'description', 'region', 'long', 'lat', 'year_min', 'year_max', 'comment']
    template_name = 'arch_site/update.html'
    success_url = '/'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # logger.info(f'Display view of {self.object_name} accessed')
        context['title'] = f'Редактирование - {self.model}'
        # context['action'] = reverse_lazy('arch_site:update', self.get_object().slug)
        context['method'] = 'POST'
        context['value'] = 'Save'
        return context
