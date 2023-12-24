from django.views.generic import ListView
from artwork.models import Artwork


class ListArtworkView(ListView):
    template_name = 'artwork/list.html'
    model = Artwork
    context_object_name = 'artworks'