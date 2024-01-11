from measurement.models import GasChromatographyMassSpectrometry

from core.view_mixins import DetailViewMixin


class DetailGCMSView(DetailViewMixin):
    model = GasChromatographyMassSpectrometry
