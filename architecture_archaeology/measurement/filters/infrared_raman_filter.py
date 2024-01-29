from measurement.models import InfraredRamanMicroscopy
from measurement.filters import MeasurementBaseFilter
import django_filters


class InfraredRamanFilter(MeasurementBaseFilter):

    groups = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = InfraredRamanMicroscopy
        fields = ['method']