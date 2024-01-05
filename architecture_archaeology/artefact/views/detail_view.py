from logging import getLogger
from typing import Any
from django.views.generic import DetailView
import architecture_archaeology.settings as settings
from artefact.models import Artefact

logger = getLogger(f'{settings.PROJECT}.{__name__}')


class DetailArtefactView(DetailView):
    model = Artefact
    template_name = 'artefact/detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        logger.info(f'Display view of {self.object} accessed')
        context['title'] = f'Находка {self.object}'
        return context