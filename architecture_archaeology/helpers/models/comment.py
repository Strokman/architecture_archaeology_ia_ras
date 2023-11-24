from django.db import models
from core.base_model import BaseModel


class Comment(BaseModel):
    text = models.TextField()

    building = models.ForeignKey('building.Building', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
