from arch_site.models import ArchaeologicalSite
from core.view_mixins import DeleteViewMixin


class DeleteArchaeologicalSiteView(DeleteViewMixin):
    model = ArchaeologicalSite
