from measurement.models import ScanningElectronMicroscopy

from core.view_mixins import DetailViewMixin


class DetailScanningMiscroscopyView(DetailViewMixin):
    model = ScanningElectronMicroscopy