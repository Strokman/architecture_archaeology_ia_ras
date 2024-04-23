from artefact.models import Artefact
from core.custom_forms import FileFormMixin, YearValidationMixin, BuildingMixin


class SubmitArtefactForm(YearValidationMixin, BuildingMixin, FileFormMixin):

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
