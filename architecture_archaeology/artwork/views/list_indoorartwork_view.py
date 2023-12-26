from django.views.generic import ListView
from artwork.models import IndoorArtwork


class ListIndoorArtworkView(ListView):
    template_name = 'artwork/list.html'
    model = IndoorArtwork
    context_object_name = 'artworks'
