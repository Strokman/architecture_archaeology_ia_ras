from measurement.models import Roentgen
from measurement.filters import MeasurementBaseFilter
import django_filters


class RoentgenFilter(MeasurementBaseFilter):

    groups = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Roentgen
        fields = ()