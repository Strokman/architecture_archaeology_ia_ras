import django_filters
from building.models import Building


class BuildingFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    comment = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Building
        fields = ['name', 'site']
