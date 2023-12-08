from typing import Any
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import FormView
from file.forms.upload_form import UploadFileForm


class UploadFileView(FormView):
    template_name = 'file/file_form.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('building:submit')

    def post(self, request, *args, **kwargs):
        print(request)
        print(request.FILES['file'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        rv = super().get_context_data(**kwargs)
        rv['method'] = 'post'
        rv['action'] = reverse_lazy('file:upload')
        rv['render_kw'] = {'enctype': 'multipart/form-data'}
        return rv
