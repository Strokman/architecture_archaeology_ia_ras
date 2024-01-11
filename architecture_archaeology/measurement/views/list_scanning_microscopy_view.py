from measurement.models import ScanningElectronMicroscopy
from core.view_mixins import ListViewMixin


class ListScanningMicroscopyView(ListViewMixin):
    model = ScanningElectronMicroscopy
