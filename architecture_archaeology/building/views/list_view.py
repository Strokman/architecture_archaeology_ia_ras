from typing import Any
from django.views.generic import ListView
from django.urls import reverse_lazy
from building.models import Building


class BuildingListView(ListView):
    template_name = 'building/list.html'
    model = Building
    context_object_name = 'buildings'


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Постройки'
        context['action'] = reverse_lazy('building:submit')
        return context
