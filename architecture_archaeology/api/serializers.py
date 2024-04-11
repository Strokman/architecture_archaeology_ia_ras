from rest_framework import serializers

from arch_site.models import ArchaeologicalSite


class ArchaeologicalSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchaeologicalSite
        fields = ('id','name', 'long', 'lat', 'description')
