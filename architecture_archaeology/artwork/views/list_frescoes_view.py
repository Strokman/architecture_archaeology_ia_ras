from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from artwork.models import Frescoe
from core.view_mixins import ListViewMixin
from artwork.filters.frescoe_filter import FrescoeFilter


class ListFrescoeView(ListViewMixin):
    filterset_class = FrescoeFilter

    model = Frescoe
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if 'lotok' in self.request.path:
            context['title'] = 'Лотки'
            context['action'] = reverse_lazy('artwork:submit-lotok')
            context['base_url'] = reverse_lazy('artwork:list-lotok')
        else:
            context['title'] = 'Фрески'
            context['action'] = reverse_lazy('artwork:submit-frescoe')
            context['base_url'] = reverse_lazy('artwork:list-frescoe')
        return context


    def get_queryset(self) -> QuerySet[Any]:
        if 'lotok' in self.request.path:
            qs = Frescoe.objects.filter(kind='L')
        else:
            qs = Frescoe.objects.filter(kind='I')
        return qs
