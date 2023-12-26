from django.views.generic import CreateView
from django.urls import reverse_lazy
from artwork.models import IndoorArtwork
from artwork.forms import SubmitIndoorArtworkForm
from file.services import FileHandler
from file.services import S3FileHandler


class SubmitIndoorArtworkView(CreateView):
    model = IndoorArtwork
    form_class = SubmitIndoorArtworkForm
    template_name = 'submit.html'
    success_url = '/'

    def form_valid(self, form):
        # artwork_data = {k: v for k, v in form.cleaned_data.items() if hasattr(IndoorArtwork, k)}
        # artwork = IndoorArtwork(**artwork_data)
        # artwork.save()
        artwork = form.save()
        foto = form.cleaned_data['foto']
        processed_foto = FileHandler(foto,
                                     artwork,
                                     'фотография')
        foto_instance = processed_foto.to_orm()
        uploader = S3FileHandler(processed_foto)
        uploader.upload_file_to_s3()
        artwork.save()
        foto_instance.save()
        artwork.file_set.add(foto_instance)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление изображения'
        context['method'] = 'POST'
        context['action'] = reverse_lazy('artwork:submit-indoor')
        context['render_kw'] = {'enctype': 'multipart/form-data'}
        return context