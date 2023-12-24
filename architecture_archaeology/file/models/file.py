from django.db import models
from core.timestamp_mixin import TimestampMixin


# CHOICES = [
#     ('F', 'фотография'),
#     ('PIC', 'рисунок'),
#     ('P', 'план')
#     ]


class File(TimestampMixin):
    filename = models.CharField(max_length=255)
    extension = models.CharField(max_length=255)
    original_name = models.CharField(max_length=255)
    object_storage_key = models.CharField(max_length=255)

    type = models.ForeignKey('file.FileType', null=False, on_delete=models.PROTECT)

    site = models.ForeignKey('arch_site.ArchaeologicalSite', null=True, on_delete=models.CASCADE)
    bulding = models.ForeignKey('building.Building', null=True, on_delete=models.CASCADE)
    bulding_part = models.ForeignKey('building.BuildingPart', null=True, on_delete=models.CASCADE)
    artwork = models.ForeignKey('artwork.Artwork', null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.filename
