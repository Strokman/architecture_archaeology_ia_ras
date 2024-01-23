import django_filters
from arch_site.models import ArchaeologicalSite


class ArchSiteFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    comment = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = ArchaeologicalSite
        fields = ['region']
