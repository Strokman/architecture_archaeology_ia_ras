from arch_site.forms import SubmitArchaeologicalSiteForm
from arch_site.models import ArchaeologicalSite
from django.urls import reverse_lazy

from core.view_mixins import CreateViewMixin
# Create your views here.


class SubmitSiteView(CreateViewMixin):
    template_name = 'submit.html'
    model = ArchaeologicalSite
    form_class = SubmitArchaeologicalSiteForm
    success_url = reverse_lazy('index')
