from core.utils import slugify
from django.db import models
from core.base_model import BaseModel


class SlugMixin(BaseModel):

    slug = models.SlugField(null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name if hasattr(self, 'name') else self.description, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:

        abstract = True
