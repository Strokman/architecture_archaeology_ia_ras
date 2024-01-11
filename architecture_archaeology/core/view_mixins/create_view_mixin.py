from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from core.view_mixins.form_valid_files import FormValidFilesMixin


class CreateViewMixin(SuccessMessageMixin, FormValidFilesMixin, CreateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Добавление {self.model._meta.verbose_name_plural}'
        return context

    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return f'{self.model._meta.verbose_name} {self.object.name} успешно создан'

    def get_success_url(self) -> str:
        return self.object.get_absolute_url()

    def get_template_names(self) -> list[str]:
        template_names = super().get_template_names()
        template_names.append('form_template.html')
        return template_names
