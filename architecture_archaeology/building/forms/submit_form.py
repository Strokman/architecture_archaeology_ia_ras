from django.forms import ModelForm
from building.models import Building


class SubmitBuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = ['name', 'description', 'long', 'lat', 'region']
