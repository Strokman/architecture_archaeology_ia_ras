from django.views.generic import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.forms.forms import BaseForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from core.view_mixins.form_valid_files import FormValidFilesMixin
from helpers.models import Region, Country
from core.geocode import create_geocode_url, get_location_data

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin




# TODO: добавить проверку, что широта и долгота == записи в ДБ и не делать ничего
class UpdateViewMixin(
                    SuccessMessageMixin,
                    UserPassesTestMixin,
                    LoginRequiredMixin,
                    FormValidFilesMixin,
                    UpdateView
                    ):

    def form_valid(self, form: BaseForm) -> HttpResponse:
        if len(form.cleaned_data.get('foto')) + len(self.object.foto_set.all()) > 3:
            messages.error(self.request, 'Количество фотографий не может превышать 3')
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        if len(form.cleaned_data.get('other')) + len(self.object.file_set.all()) > 10:
            messages.error(self.request, 'Количество других файлов не может превышать 10')
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        if hasattr(self.model, 'region'):
            lat = form.cleaned_data['lat']
            long = form.cleaned_data['long']
            try:
                region_data = get_location_data(create_geocode_url(lat, long))
            except ValueError as error:
                messages.error(self.request, error)
                return super().form_invalid(form)
            try:
                country = Country.objects.get(name=region_data['country'])
            except Country.DoesNotExist:
                country = Country.objects.create(name=region_data['country'])
            try:
                region = Region.objects.get(name=region_data['region'])
            except Region.DoesNotExist:
                region = Region.objects.create(name=region_data['region'], country=country)
   
            form.instance.region = region
        self.object.editor = self.request.user
        self.object = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование {self.model._meta.verbose_name}: {self.object.name}'
        return context

    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return f'{self.model._meta.verbose_name} {self.object} успешно отредактирован'

    def get_success_url(self) -> str:
        return self.object.get_absolute_url()

    def get_template_names(self) -> list[str]:
        template_names = super().get_template_names()
        template_names.append('form_template.html')
        return template_names

    def test_func(self) -> bool | None:
        obj = self.model.objects.get(slug=self.request.resolver_match.kwargs['slug'])
        if obj.creator != self.request.user and not self.request.user.is_superuser:
            return False
        return True

    def handle_no_permission(self) -> HttpResponseRedirect:
        messages.error(self.request, 'Вы можете изменять только созданные Вами объекты')
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
