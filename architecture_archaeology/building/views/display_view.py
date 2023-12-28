from logging import getLogger
from typing import Any
from django.views.generic import DetailView
import architecture_archaeology.settings as settings
from building.models import Building

logger = getLogger(f'{settings.PROJECT}.{__name__}')


class BuildingDetailView(DetailView):
    model = Building
    template_name = 'building/detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        logger.info(f'Display view of {self.object} accessed')
        context['title'] = f'Постройка {self.object}'
        return context
