from django.db import models


class ArchSiteFoto(models.Model):

    site = models.ForeignKey('arch_site.ArchaeologicalSite',
                             null=False,
                             on_delete=models.CASCADE
                             )
    foto = models.ForeignKey('file.Foto',
                               null=False,
                               on_delete=models.CASCADE
                               )
