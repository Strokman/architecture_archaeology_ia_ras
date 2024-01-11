from django.views.generic import UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from core.view_mixins.form_valid_files import FormValidFilesMixin


class UpdateViewMixin(SuccessMessageMixin, FormValidFilesMixin, UpdateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование {self.model._meta.verbose_name}: {self.object.name}'
        return context

    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return f'{self.model._meta.verbose_name} {self.object.name} успешно отредактирован'

    def get_success_url(self) -> str:
        return self.object.get_absolute_url()

    def get_template_names(self) -> list[str]:
        template_names = super().get_template_names()
        template_names.append('form_template.html')
        return template_names
