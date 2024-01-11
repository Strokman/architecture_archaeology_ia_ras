from measurement.models import GasChromatographyMassSpectrometry
from core.view_mixins import ListViewMixin


class ListGCMSView(ListViewMixin):
    model = GasChromatographyMassSpectrometry