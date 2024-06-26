from rest_framework import permissions, viewsets

from api.serializers import ArchaeologicalSiteSerializer
from arch_site.models import ArchaeologicalSite


class ArchsiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ArchaeologicalSite.objects.all().order_by('-name')
    serializer_class = ArchaeologicalSiteSerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]
