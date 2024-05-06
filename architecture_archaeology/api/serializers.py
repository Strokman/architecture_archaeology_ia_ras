from rest_framework import serializers

from arch_site.models import ArchaeologicalSite
from helpers.models import Region


class RegionSerializer(serializers.ModelSerializer):

    country = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )

    class Meta:
        model = Region
        fields = ('name', 'country')


class ArchaeologicalSiteSerializer(serializers.ModelSerializer):

    region = RegionSerializer(read_only=True)

    class Meta:
        model = ArchaeologicalSite
        fields = ('id', 'name', 'long', 'lat', 'region', 'description')
