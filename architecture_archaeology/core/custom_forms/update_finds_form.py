from typing import Any, Mapping

from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from artefact.models import Artefact
from django import forms
from core.custom_forms import FileFormMixin, YearValidationMixin, BuildingMixin
from building.models import Building


class UpdateArtefactForm(forms.ModelForm, YearValidationMixin, FileFormMixin):



    class Meta:
        model = Artefact
        fields = ('name',
                  'description',
                  'site',
                  'building',
                  'building_part',
                  'year_min',
                  'year_max',
                  'find_date_from',
                  'find_date_to',
                  'square_number',
                  'comment',
                  'storage',
                  'museum_code',
                  'foto',
                  'other')