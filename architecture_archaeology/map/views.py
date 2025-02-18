from django.views.generic import TemplateView

from django.http import HttpResponse

import json
from django.core import serializers
from arch_site.models import ArchaeologicalSite

# Create your views here.


"""
View для отображения карты и объектов на ней.
"""
class MapView(TemplateView):
    template_name = 'map/map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Карта памятников'
        return context


def get_data(request):
    sites = ArchaeologicalSite.objects.all()
    serialized_objs = serializers.serialize('json', sites)
    return HttpResponse(serialized_objs, content_type='application/json')


def get_user_data(request):
    """
    Функция, которая отдает данные зарегистрирован ли я юзер в темплейт.
    В зависимости от этого памятники отображаются или нет в крупном
    масштабе - см js скрипт
    """
    is_authenticated = json.dumps(
        {'is_authenticated':
         request.user.is_authenticated}
         )
    return HttpResponse(is_authenticated, content_type='application/json')
