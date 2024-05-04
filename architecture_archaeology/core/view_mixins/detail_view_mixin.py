from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class DetailViewMixin(LoginRequiredMixin, DetailView):
    context_object_name = 'object'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object}'
        app = self.model._meta.app_label
        model_name = self.model.__name__.lower()
        context['action'] = reverse_lazy(
            f'{app}:update{"-" + model_name if app in ['artwork', 'measurement'] else ""}',
            kwargs={'slug': self.object.slug}
            )
        context['delete_action'] = reverse_lazy(
            f'{app}:delete{"-" + model_name if app in ['artwork', 'measurement'] else ""}',
            kwargs={'slug': self.object.slug}
            )
        return context
