from typing import Any
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class DetailViewMixin(LoginRequiredMixin, DetailView):
    context_object_name = 'object'
    template_name = 'detail_measurement.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object}'
        app = self.model._meta.app_label
        model_name = self.model.__name__.lower()
        context['action'] = reverse_lazy(
            f'{app}:update{"-" + model_name if app in ['artwork', 'measurement'] else ""}',
            kwargs={'slug': self.object.slug}
            )
        return context
