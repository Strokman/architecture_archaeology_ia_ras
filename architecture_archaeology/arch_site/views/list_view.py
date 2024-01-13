from arch_site.models import ArchaeologicalSite
from core.view_mixins import ListViewMixin
from arch_site.filter import ArchSiteFilter


class ListSiteView(ListViewMixin):
    model = ArchaeologicalSite
    filterset_class = ArchSiteFilter
