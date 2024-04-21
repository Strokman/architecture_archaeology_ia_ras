from django.contrib import admin
from .models import (
    Preservation,
    Color,
    Storage,
    Pigment,
    Material,
    Mineral,
    Filler,
    Element
)


admin.site.register(Preservation)
admin.site.register(Color)
admin.site.register(Storage)
admin.site.register(Pigment)
admin.site.register(Material)
admin.site.register(Mineral)
admin.site.register(Filler)
admin.site.register(Element)
