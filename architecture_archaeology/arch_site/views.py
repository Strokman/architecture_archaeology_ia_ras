from typing import Any
from django.http import HttpResponse
from django.views.generic import FormView, ListView, DetailView, UpdateView
from arch_site.forms import SubmitArchaeologicalSiteForm
from arch_site.models import ArchaeologicalSite
from django.urls import reverse_lazy

# Create your views here.


class SubmitSiteView(FormView):
    template_name = 'arch_site/submit.html'
    form_class = SubmitArchaeologicalSiteForm
    success_url = reverse_lazy('index')

    def form_valid(self, form: Any) -> HttpResponse:
        print(form.cleaned_data)
        arch_site_data = {k: v for k, v in form.cleaned_data.items() if hasattr(ArchaeologicalSite, k)}
        site = ArchaeologicalSite.objects.create(**arch_site_data)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['method'] = 'POST'
        context['action'] = reverse_lazy('arch_site:submit')
        context['render_kw'] = {'enctype': 'multipart/form-data'}
        return context


class ListSiteView(ListView):
    template_name = 'arch_site/list.html'
    model = ArchaeologicalSite
    context_object_name = 'sites'


class DisplaySiteView(DetailView):
    model = ArchaeologicalSite
    template_name = 'arch_site/detail.html'

    def get_object(self, queryset=None):
        rv = super().get_object(queryset)
        self.object_name = rv.name
        return rv

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # logger.info(f'Display view of {self.object_name} accessed')
        context['title'] = f'{self.object_name}'
        return context


class UpdateSiteView(UpdateView):
    model = ArchaeologicalSite
    fields = ['name', 'description', 'region', 'long', 'lat', 'year_min', 'year_max', 'comment']
    template_name = 'arch_site/update.html'
    success_url = '/'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # logger.info(f'Display view of {self.object_name} accessed')
        context['title'] = f'Редактирование - {self.model}'
        # context['action'] = reverse_lazy('arch_site:update', self.get_object().slug)
        context['method'] = 'POST'
        context['value'] = 'Save'
        return context
