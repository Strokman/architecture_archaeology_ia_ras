from django.forms.forms import BaseForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from core.view_mixins import CreateViewMixin

from artwork.models import IndoorArtwork, Frescoe
from artefact.models import Artefact


class CreateMeasurementMixin(CreateViewMixin):

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
