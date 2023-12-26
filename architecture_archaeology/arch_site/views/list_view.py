from typing import Any

from django.urls import reverse_lazy
from django.views.generic import ListView
from arch_site.models import ArchaeologicalSite


class ListSiteView(ListView):
    template_name = 'list.html'
    model = ArchaeologicalSite
    context_object_name = 'objects'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Археологические памятники'
        context['action'] = reverse_lazy('arch_site:submit')
        return context
