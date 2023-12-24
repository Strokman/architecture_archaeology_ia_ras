from django import forms
from artwork.models import Artwork


class SubmitArtworkForm(forms.ModelForm):

    class Meta:
        model = Artwork
        fields = '__all__'
