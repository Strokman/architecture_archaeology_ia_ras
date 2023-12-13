from django.views.generic import ListView
from arch_site.models import ArchaeologicalSite


class ListSiteView(ListView):
    template_name = 'arch_site/list.html'
    model = ArchaeologicalSite
    context_object_name = 'sites'
