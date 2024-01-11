from typing import Any

from django.urls import reverse_lazy
from django.views.generic import ListView


class ListViewMixin(ListView):
    context_object_name = 'objects'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name_plural
        app = self.model._meta.app_label
        model_name = self.model.__name__.lower()
        context['action'] = reverse_lazy(
            f'{app}:submit{"-" + model_name if app in ['artwork', 'measurement'] else ""}'
            )
        return context

    def get_template_names(self) -> list[str]:
        template_names = super().get_template_names()
        template_names.append('list.html')
        return template_names