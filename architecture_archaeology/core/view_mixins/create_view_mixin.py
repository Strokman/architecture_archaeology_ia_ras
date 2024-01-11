from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from core.view_mixins.form_valid_files import FormValidFilesMixin


class CreateViewMixin(SuccessMessageMixin, FormValidFilesMixin, CreateView):
    # template_name = 'form_template.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Добавление {self.model._meta.verbose_name_plural}'
        # context['method'] = 'POST'
        # context['render_kw'] = {'enctype': 'multipart/form-data'}
        # app = self.model._meta.app_label
        # obj_name = self.model.__name__.lower()
        # context['action'] = reverse_lazy(
        #     f'{app}:submit{"-" + obj_name if app in ['artwork', 'measurement'] else ""}'
        #     )
        return context
    
    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return f'{self.model._meta.verbose_name} {self.object.name} успешно создан'
    
    def get_success_url(self) -> str:
        return self.object.get_absolute_url()
