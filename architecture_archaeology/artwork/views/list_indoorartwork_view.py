from typing import Any

from django.urls import reverse_lazy
from django.views.generic import ListView
from artwork.models import IndoorArtwork


class ListIndoorArtworkView(ListView):
    template_name = 'list.html'
    model = IndoorArtwork
    context_object_name = 'objects'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изображения в постройке'
        context['action'] = reverse_lazy('artwork:submit-indoorartwork')
        return context
