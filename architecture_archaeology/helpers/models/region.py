from django.db import models
from core.base_model import BaseModel


class Region(BaseModel):
    name = models.CharField(max_length=200)

    country = models.ForeignKey('helpers.Country', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
