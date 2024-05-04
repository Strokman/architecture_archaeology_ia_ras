from measurement.models import ScanningElectronMicroscopy
from core.view_mixins import DeleteViewMixin


class DeleteScanningMicroscopyView(DeleteViewMixin):
    model = ScanningElectronMicroscopy