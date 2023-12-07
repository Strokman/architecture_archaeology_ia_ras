from logging import getLogger
from django.views.generic.base import TemplateView
# from django.shortcuts import get_object_or_404
from django.shortcuts import render, HttpResponseRedirect
from django.core.handlers.wsgi import WSGIRequest as req
from django.urls import reverse

import architecture_archaeology.settings as settings
# from building.models import Building
from building.forms import SubmitBuildingForm

logger = getLogger(f'{settings.PROJECT}.{__name__}')


class Submit(TemplateView):
    template_name = 'building/submit.html'

    def get(self, request: req):
        logger.info('test')
        form = SubmitBuildingForm()
        context = {
            'title': 'Добавление постройки',
            'form': form,
            'action': reverse('building:submit'),
            'method': 'post'
        }
        return render(request, self.template_name, context)

    def post(self, request: req):
        logger.info('test')
        form = SubmitBuildingForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('building:submit'))
        else:
            return render(request, self.template_name, context)
        
