import django_filters
from arch_site.models import ArchaeologicalSite


class ArchSiteFilter(django_filters.FilterSet):
    # name = django_filters.ModelChoiceFilter(queryset=ArchaeologicalSite.objects.all())
    description = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = ArchaeologicalSite
        fields = ['name', 'region']
