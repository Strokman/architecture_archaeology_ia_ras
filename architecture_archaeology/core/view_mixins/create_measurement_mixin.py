from typing import Any
from django.forms.forms import BaseForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from core.view_mixins import CreateViewMixin

from artwork.models import IndoorArtwork, Frescoe
from artefact.models import Artefact


class CreateMeasurementMixin(CreateViewMixin):
    """
    Так как все изображения и находки имеют сплошную и сквозную
    нумерацию (шифр/code), то проводится проверка по коду, какая запись
    существует в БД (через блоки try-catch проходятся три модели) и по
    результату запись вносится в БД
    """

    def form_valid(self, form: BaseForm) -> HttpResponse:
        code = form.cleaned_data['code']
        obj = None
        try:
            obj = Frescoe.objects.get(code=code)
        except:
            pass
        try:
            obj = IndoorArtwork.objects.get(code=code)
        except:
            pass
        try:
            obj = Artefact.objects.get(code=code)
        except:
            pass
        try:
            form.instance.parent_obj = obj
        except ValueError:
            messages.error(self.request, 'Фрески или находки не существует!')
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        return super().form_valid(form)

    def get_initial(self) -> dict[str, Any]:
        initial = super().get_initial()
        initial['code'] = self.request.GET.get('code')
        return initial