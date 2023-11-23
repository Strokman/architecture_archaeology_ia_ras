from django.db import models
from core.base_model import BaseModel


class Comment(BaseModel):
    text = models.TextField()

    def __str__(self):
        return self.text
