from django.db import models
from core.base_model import BaseModel


class Comment(BaseModel):
    text = models.TextField()

    building = models.ForeignKey('building.Building', null=True, blank=True, on_delete=models.CASCADE)
    site = models.ForeignKey('arch_site.ArchaeologicalSite', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
