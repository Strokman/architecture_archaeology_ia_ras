from arch_site.models import ArchaeologicalSite
from core.view_mixins import ListViewMixin


class ListSiteView(ListViewMixin):
    model = ArchaeologicalSite
