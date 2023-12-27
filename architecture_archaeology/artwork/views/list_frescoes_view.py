from typing import Any

from django.urls import reverse_lazy
from django.views.generic import ListView
from artwork.models import Frescoe


class ListFrescoeView(ListView):
    template_name = 'list.html'
    model = Frescoe
    context_object_name = 'objects'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Фрески'
        context['action'] = reverse_lazy('artwork:submit-frescoe')
        return context
