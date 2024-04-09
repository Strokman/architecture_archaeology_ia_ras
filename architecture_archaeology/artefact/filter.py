import django_filters
from artefact.models import Artefact
from arch_site.models import ArchaeologicalSite
from helpers.models import Storage
from core.filters import RangeDatesFilterBase


class ArtefactFilter(django_filters.FilterSet, RangeDatesFilterBase):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    code = django_filters.CharFilter(lookup_expr='icontains')
    dating = django_filters.RangeFilter(label='Датировка', method='filter_dating')
    find_date = django_filters.RangeFilter(label='Год находки', method='filter_dating')
    site = django_filters.ModelMultipleChoiceFilter(queryset=ArchaeologicalSite.objects.all())
    storage = django_filters.ModelMultipleChoiceFilter(queryset=Storage.objects.all())
    comment = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Artefact
        fields = (
            'name',
            'code',
            'site',
            'dating',
            'find_date',
            'storage',
            'square_number',
            'museum_code',
            'description',
            'comment'
        )
