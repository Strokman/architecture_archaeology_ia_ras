from django.db import models


class Element(models.Model):

    atomic_number = models.IntegerField()
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=2)

    def __str__(self) -> str:
        return f'{self.symbol} - {self.name}'

    class Meta:
        ordering = ('name', )