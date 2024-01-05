from django.db import models
from core.models import TimestampMixin


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
    indoor_artwork = models.ForeignKey('artwork.IndoorArtwork', null=True, on_delete=models.CASCADE)
    lotok = models.ForeignKey('artwork.Lotok', null=True, on_delete=models.CASCADE)
    frescoe = models.ForeignKey('artwork.Frescoe', null=True, on_delete=models.CASCADE)
    artefact = models.ForeignKey('artefact.Artefact', null=True, on_delete=models.CASCADE)
    rfa = models.ForeignKey('measurement.RFA', null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.filename
