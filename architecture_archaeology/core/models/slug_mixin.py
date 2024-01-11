from core.utils import slugify
from django.db import models
from core.models.base_model import BaseModel
from uuid import uuid1


class SlugMixin(BaseModel):

    slug = models.SlugField(max_length=500, unique=True, null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True) + '-' + str(uuid1())
        super().save(*args, **kwargs)

    class Meta:

        abstract = True
