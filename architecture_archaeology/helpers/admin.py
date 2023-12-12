from django.contrib import admin
from .models import Preservation, Color, Country, Region
# Register your models here.


admin.site.register(Preservation)
admin.site.register(Color)
admin.site.register(Country)
admin.site.register(Region)
