from django.db import models
from core.base_model import BaseModel


class Storage(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name