from measurement.models import ScanningElectronMicroscopy
from core.view_mixins import ListViewMixin
from measurement.filters import ScanningMicroscopyFilter


class ListScanningMicroscopyView(ListViewMixin):
    filterset_class = ScanningMicroscopyFilter
    model = ScanningElectronMicroscopy
