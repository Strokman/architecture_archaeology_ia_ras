from django.views.generic import ListView
from building.models import Building


class ListBuildingView(ListView):
    template_name = 'building/list.html'
    model = Building
    context_object_name = 'buildings'
