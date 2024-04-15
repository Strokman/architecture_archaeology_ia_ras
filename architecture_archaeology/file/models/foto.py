from django.db import models
from core.models import TimestampMixin


class Foto(TimestampMixin):
    filename = models.CharField(max_length=255)
    extension = models.CharField(max_length=255)
    original_name = models.CharField(max_length=255)
    object_storage_key = models.CharField(max_length=255)

    site = models.ForeignKey('arch_site.ArchaeologicalSite', null=True, on_delete=models.CASCADE)
    bulding = models.ForeignKey('building.Building', null=True, on_delete=models.CASCADE)
    bulding_part = models.ForeignKey('building.BuildingPart', null=True, on_delete=models.CASCADE)
    indoor_artwork = models.ForeignKey('artwork.IndoorArtwork', null=True, on_delete=models.CASCADE)
    frescoe = models.ForeignKey('artwork.Frescoe', null=True, on_delete=models.CASCADE)
    artefact = models.ForeignKey('artefact.Artefact', null=True, on_delete=models.CASCADE)
    rfa = models.ForeignKey('measurement.RFA', null=True, on_delete=models.CASCADE)
    scanning_microscopy = models.ForeignKey('measurement.ScanningElectronMicroscopy', null=True, on_delete=models.CASCADE)
    gc_ms = models.ForeignKey('measurement.GasChromatographyMassSpectrometry', null=True, on_delete=models.CASCADE)
    roentgen = models.ForeignKey('measurement.Roentgen', null=True, on_delete=models.CASCADE)
    infrared_ramanov = models.ForeignKey('measurement.InfraredRamanMicroscopy', null=True, on_delete=models.CASCADE)
    petrography = models.ForeignKey('measurement.Petrography', null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.filename

    class Meta:

        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ('id', )