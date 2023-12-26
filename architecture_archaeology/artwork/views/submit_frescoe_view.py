from django.views.generic import CreateView
from django.urls import reverse_lazy
from artwork.models import Frescoe
from artwork.forms import SubmitFrescoeForm

from file.services import FileHandler, S3FileHandler


class SubmitFrescoeView(CreateView):
    model = Frescoe
    form_class = SubmitFrescoeForm
    template_name = 'submit.html'
    context_object_name = 'object'
    success_url = '/'

    def form_valid(self, form):
        frescoe = form.save()
        foto = form.cleaned_data['foto']
        processed_foto = FileHandler(foto,
                                     frescoe,
                                     'фотография')
        foto_instance = processed_foto.to_orm()
        uploader = S3FileHandler(processed_foto)
        uploader.upload_file_to_s3()
        foto_instance.save()
        frescoe.file_set.add(foto_instance)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление фрески'
        context['method'] = 'POST'
        context['action'] = reverse_lazy('artwork:submit-frescoe')
        context['render_kw'] = {'enctype': 'multipart/form-data'}
        return context