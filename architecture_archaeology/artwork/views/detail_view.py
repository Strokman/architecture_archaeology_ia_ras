from typing import Any
from django.views.generic import DetailView
from artwork.models import Artwork


class DisplayArtworkView(DetailView):
    model = Artwork
    template_name = 'artwork/detail.html'

    def get_object(self, queryset=None):
        rv = super().get_object(queryset)
        self.object_name = rv.code
        return rv

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # logger.info(f'Display view of {self.object_name} accessed')
        context['title'] = f'{self.object_name}'
        return context
