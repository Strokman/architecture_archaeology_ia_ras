from django.views.generic import CreateView
from django.urls import reverse_lazy

from core.view_mixins import FormValidFilesMixin


class CreateViewMixin(FormValidFilesMixin, CreateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Добавление {self.model._meta.verbose_name_plural}'
        context['method'] = 'POST'
        context['render_kw'] = {'enctype': 'multipart/form-data'}
        app = self.model._meta.app_label
        obj_name = self.model.__name__.lower()
        context['action'] = reverse_lazy(
            f'{app}:submit{"-" + obj_name if app in ['artwork'] else ""}'
            )
        return context
