from measurement.models import GasChromatographyMassSpectrometry

from core.view_mixins import DetailViewMixin


class DetailGCMSView(DetailViewMixin):
    model = GasChromatographyMassSpectrometry
    template_name = 'gc_ms/detail.html'
