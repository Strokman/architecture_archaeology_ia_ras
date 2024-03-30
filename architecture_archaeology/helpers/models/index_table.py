from django.db import models


class IndexTable(models.Model):

    frescoe = models.ForeignKey('artwork.Frescoe', null=True, on_delete=models.CASCADE)
    artefact = models.ForeignKey('artefact.Artefact', null=True, on_delete=models.CASCADE)
    indoor_artwork = models.ForeignKey('artwork.IndoorArtwork', null=True, on_delete=models.CASCADE)
