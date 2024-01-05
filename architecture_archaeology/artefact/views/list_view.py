from typing import Any

from django.urls import reverse_lazy
from django.views.generic import ListView
from artefact.models import Artefact


class ListArtefactView(ListView):
    template_name = 'list.html'
    model = Artefact
    context_object_name = 'objects'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Находки'
        context['action'] = reverse_lazy('artefact:submit')
        return context