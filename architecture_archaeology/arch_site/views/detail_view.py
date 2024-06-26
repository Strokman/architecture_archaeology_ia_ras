from arch_site.models import ArchaeologicalSite
from core.view_mixins import DetailViewMixin


class DetailSiteView(DetailViewMixin):
    model = ArchaeologicalSite
    template_name = 'detail_arch_object.html'
