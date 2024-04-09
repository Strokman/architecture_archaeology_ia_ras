from typing import Any

from django.urls import reverse_lazy
# from django.views.generic import ListView
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin


class ListViewMixin(LoginRequiredMixin, FilterView):
    paginate_by = 10
    context_object_name = 'objects'
    template_name = 'list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name_plural
        app = self.model._meta.app_label
        model_name = self.model.__name__.lower()
        context['action'] = reverse_lazy(
            f'{app}:submit{"-" + model_name if app in ['artwork', 'measurement'] else ""}'
            )
        context['base_url'] = reverse_lazy(
            f'{app}:list{"-" + model_name if app in ['artwork', 'measurement'] else ""}'
            )
        return context
