import django_filters
from arch_site.models import ArchaeologicalSite

class ArchSiteFilter(django_filters.FilterSet):

    class Meta:
        model = ArchaeologicalSite
        fields = ['name', 'region']