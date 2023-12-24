from django.views.generic import CreateView
from artwork.models import Artwork
from artwork.forms import SubmitArtworkForm


class SubmitArtworkView(CreateView):
    model = Artwork
    form_class = SubmitArtworkForm
    template_name = 'artwork/submit.html'
    success_url = '/'

    # def form_valid(self, form):
    #     return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = 'POST'
        # context['action'] = reverse_lazy('arch_site:submit')
        # context['render_kw'] = {'enctype': 'multipart/form-data'}
        return context