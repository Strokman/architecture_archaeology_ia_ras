from django.shortcuts import render
from arch_site.models import ArchaeologicalSite
from django.core import serializers
from django.http import HttpResponse


# Create your views here.
def get_bulding(request, pk):
    site = ArchaeologicalSite.objects.get(pk=pk)
    buildings = site.building_set.all()
    buildingArray: list[dict[int, str]] = serializers.serialize('json', buildings)
    return HttpResponse(buildingArray, content_type='application/json')