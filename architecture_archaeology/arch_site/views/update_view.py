from arch_site.models import ArchaeologicalSite
from arch_site.forms import SubmitArchaeologicalSiteForm

from core.view_mixins import UpdateViewMixin


class UpdateSiteView(UpdateViewMixin):
    model = ArchaeologicalSite
    form_class = SubmitArchaeologicalSiteForm
