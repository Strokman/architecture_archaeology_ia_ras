from typing import Any
from django.forms.forms import BaseForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from core.view_mixins import UpdateViewMixin

from artwork.models import IndoorArtwork, Frescoe
from artefact.models import Artefact


class UpdateMeasurementMixin(UpdateViewMixin):

    def form_valid(self, form: BaseForm) -> HttpResponse:
        code = form.cleaned_data['code']
        if code != self.object.parent_obj.code:
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
                self.object.parent_obj = obj
            except ValueError:
                messages.error(self.request, 'Фрески или находки не существует!')
                return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        return super().form_valid(form)

    def get_initial(self) -> dict[str, Any]:
        initial = super().get_initial()
        initial['code'] = self.object.parent_obj.code
        return initial
