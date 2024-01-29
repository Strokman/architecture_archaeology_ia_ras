import django_filters
from arch_site.models import ArchaeologicalSite
from building.models import Building
from core.filters import RangeDatesFilterBase


class BuildingFilter(django_filters.FilterSet, RangeDatesFilterBase):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    year = django_filters.RangeFilter(label='Датировка', method='filter_dating')
    comment = django_filters.CharFilter(lookup_expr='icontains')
    site = django_filters.ModelMultipleChoiceFilter(queryset=ArchaeologicalSite.objects.all())

    class Meta:
        model = Building
        fields = []
