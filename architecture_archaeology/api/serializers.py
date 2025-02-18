from rest_framework import serializers

from arch_site.models import ArchaeologicalSite
from building.models import Building
from helpers.models import Region


class RegionSerializer(serializers.ModelSerializer):
    """
    Сериализация данных по памятникам и постройкам,
    используется стандартный класс DRF для моделей Django ORM
    """

    country = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )

    class Meta:
        model = Region
        fields = ('name', 'country')


class BuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = ('id', 'name', 'lat', 'long', 'description')


class ArchaeologicalSiteSerializer(serializers.ModelSerializer):

    region = RegionSerializer(read_only=True)
    buildings = BuildingSerializer(source='building_set', many=True, read_only=True)

    class Meta:
        model = ArchaeologicalSite
        fields = ('id', 'name', 'long', 'lat', 'region', 'description', 'buildings')
