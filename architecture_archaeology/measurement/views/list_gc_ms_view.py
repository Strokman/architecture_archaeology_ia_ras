from measurement.models import GasChromatographyMassSpectrometry
from core.view_mixins import ListViewMixin
from measurement.filters import GCMSFilter


class ListGCMSView(ListViewMixin):
    filterset_class = GCMSFilter
    model = GasChromatographyMassSpectrometry