from rest_framework import permissions, viewsets

from api.serializers import ArchaeologicalSiteSerializer
from arch_site.models import ArchaeologicalSite


class ArchsiteViewSet(viewsets.ModelViewSet):
    """
    Заготовка для вьюхи по отдаче данных для фронтенда карты на сайте ИА РАН.
    На основе Django Rest Framework
    На данный момент не используется
    """
    queryset = ArchaeologicalSite.objects.all().order_by('-name')
    serializer_class = ArchaeologicalSiteSerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]
