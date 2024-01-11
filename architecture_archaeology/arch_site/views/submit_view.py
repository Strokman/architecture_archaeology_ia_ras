from arch_site.forms import SubmitArchaeologicalSiteForm
from arch_site.models import ArchaeologicalSite


from core.view_mixins import CreateViewMixin
# Create your views here.


class SubmitSiteView(CreateViewMixin):

    template_name = 'form_template.html'
    model = ArchaeologicalSite
    form_class = SubmitArchaeologicalSiteForm
