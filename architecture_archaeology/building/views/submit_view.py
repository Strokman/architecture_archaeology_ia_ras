from logging import getLogger
from typing import Any
from django.views.generic.base import TemplateView
# from django.shortcuts import get_object_or_404
from django.shortcuts import render, HttpResponseRedirect
from django.core.handlers.wsgi import WSGIRequest as req
from django.urls import reverse

import architecture_archaeology.settings as settings
# from building.models import Building
from building.forms import SubmitBuildingForm
from file.forms.upload_form import UploadFileForm

logger = getLogger(f'{settings.PROJECT}.{__name__}')


class BuildingSubmitView(TemplateView):
    template_name = 'building/submit.html'

    def get(self, request: req):
        logger.info('test')
        form_1 = SubmitBuildingForm()
        form_2 = UploadFileForm()
        context = self.get_context_data()
        context['form_1'] = form_1
        context['form_2'] = form_2
        return render(request, self.template_name, context)

    def post(self, request: req):
        logger.info('test')
        form_1 = SubmitBuildingForm(request.POST)
        form_2 = UploadFileForm(request.POST)
        context = self.get_context_data()
        context['form_1'] = form_1
        context['form_2'] = form_2
        print(request.FILES)
        if form_2.is_valid():
            print('LOLKA')
        if form_1.is_valid() and form_2.is_valid():
            print(form_2.cleaned_data)
            return HttpResponseRedirect(reverse('building:submit'))
        else:
            return render(request, self.template_name, context)
        
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление постройки'
        context['action'] = reverse('building:submit')
        context['method'] = 'post'
        context['render_kw'] = {'enctype': 'multipart/form-data'}
        return context
        
