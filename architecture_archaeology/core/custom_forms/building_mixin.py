from django import forms
from building.models import Building


class BuildingMixin(forms.ModelForm):
    """
    Миксин для форм, где используется поле привязки к постройке.
    """

    building = forms.CharField(
        label='Постройка',
        required=False,
        widget=forms.Select,
        help_text='Сначала выберите памятник, затем - постройку'
        )

    def clean_building(self):
        """
        В формах и JS скрипте возможно, что прилетит пустое поле
        или default - поэтому сделана такая проверка
        """
        building_id = self.cleaned_data.get('building')
        if building_id != 'default' and building_id:
            building = Building.objects.get(id=building_id)
            return building
        return None
