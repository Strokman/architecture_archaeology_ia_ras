from measurement.models import ScanningElectronMicroscopy
from measurement.filters import MeasurementBaseFilter
import django_filters


class ScanningMicroscopyFilter(MeasurementBaseFilter):

    elements = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ScanningElectronMicroscopy
        fields = []