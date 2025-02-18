import django_filters
from django import forms
from arch_site.models import ArchaeologicalSite
from building.models import Building
from helpers.models import Color, Preservation
from core.filters import RangeDatesFilterBase

# from django.contrib.auth.models import User


class ArtworkBaseFilter(django_filters.FilterSet, RangeDatesFilterBase):
    """
    Используется библиотека django_filters, в полях датировка и год находки
    спользуется самописный метод filter_dating, см. описание в миксине
    """
    name = django_filters.CharFilter(lookup_expr='icontains')
    code = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    dating = django_filters.RangeFilter(
        label='Датировка',
        method='filter_dating')
    find_date = django_filters.RangeFilter(
        label='Год находки',
        method='filter_dating'
        )
    comment = django_filters.CharFilter(lookup_expr='icontains')
    site = django_filters.ModelMultipleChoiceFilter(
        queryset=ArchaeologicalSite.objects.all()
        )
    building = django_filters.ModelMultipleChoiceFilter(
        queryset=Building.objects.all()
        )
    color = django_filters.ModelMultipleChoiceFilter(
        queryset=Color.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={'size': 10})
        )
    preservation = django_filters.ModelMultipleChoiceFilter(
        queryset=Preservation.objects.all()
        )
    
    # TODO: сделать фильтрацию по авторам записи, переопредилить __str__ для юзера
    # creator = django_filters.ModelMultipleChoiceFilter(
    #     queryset=User.objects.all(),
    #     widget=forms.widgets.SelectMultiple(attrs={'size': 6})
    #     )