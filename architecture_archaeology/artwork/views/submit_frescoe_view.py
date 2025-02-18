from django.forms import BaseForm
from django.http.response import HttpResponse
from artwork.models import Frescoe
from artwork.forms import SubmitFrescoeForm
from core.view_mixins import CreateViewMixin


class SubmitFrescoeView(CreateViewMixin):
    """
    В соотв. с ТЗ фрекси могут быть индивидуальными или
    фрагментированными в лотке. Здесь то же самое, чтобы не повторять код - 
    проверяется, какой пришел запрос. Также в контекст темплейта передается
    различное название, в зависимости от запроса.
    """
    model = Frescoe
    form_class = SubmitFrescoeForm

    def form_valid(self, form: BaseForm) -> HttpResponse:
        if 'lotok' in self.request.path:
            form.instance.kind = 'L'
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'lotok' in self.request.path:
            context['title'] = 'Добавление лотка'
        else:
            context['title'] = 'Добавление фрески'
        return context
