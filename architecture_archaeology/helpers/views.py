from django.apps import apps
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required


def f(n):
    return {
        'id': n.id,
        'name': n.name
    }


# Create your views here.
@login_required
def artwork_get_building(request, model, slug):
    model_mapper = {
        'indoor': ('artwork', 'indoorartwork'),
        'frescoe': ('artwork', 'frescoe'),
        'artefact': ('artefact', 'artefact')
    }
    model_data = model_mapper[model]
    model = apps.get_model(model_data[0], model_data[1])
    obj = model.objects.get(slug=slug)
    building = obj.building
    all_other_buildings = list(map(f, [i for i in obj.site.building_set.all() if i != building]))
    rv = {
        'building': {
            'id': building.id if building else 'default',
            'name': building.name if building else '---------'
        },
        'other': all_other_buildings
    }
    rv = json.dumps(rv)
    return HttpResponse(rv, content_type='application/json')
