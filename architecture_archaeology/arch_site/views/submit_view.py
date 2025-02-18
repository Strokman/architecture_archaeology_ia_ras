from arch_site.forms import SubmitArchaeologicalSiteForm
from arch_site.models import ArchaeologicalSite
from core.view_mixins import CreateViewMixin


class SubmitSiteView(CreateViewMixin):
    model = ArchaeologicalSite
    form_class = SubmitArchaeologicalSiteForm
