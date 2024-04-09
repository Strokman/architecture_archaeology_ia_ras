from django.views.generic import TemplateView

from django.http import HttpResponse

import json
from django.core import serializers
from arch_site.models import ArchaeologicalSite

# Create your views here.


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
    is_authenticated = json.dumps(
        {'is_authenticated':
         request.user.is_authenticated}
         )
    return HttpResponse(is_authenticated, content_type='application/json')
