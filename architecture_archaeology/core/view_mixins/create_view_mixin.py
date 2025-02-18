from django.forms.forms import BaseForm
from django.http.response import HttpResponse
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from core.view_mixins.form_valid_files import FormValidFilesMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from core.geocode import create_geocode_url, get_location_data
from core.services.index_service import sequence_id
from django.contrib import messages
from helpers.models import Country, Region


class CreateViewMixin(
                    SuccessMessageMixin,
                    LoginRequiredMixin,
                    FormValidFilesMixin,
                    CreateView
                    ):
    
    """
    Миксин сделан для кастомизации generic-view Django,
    чтобы он охватывал большую часть моделей, описанных в приложении
    """

    def form_valid(self, form: BaseForm) -> HttpResponse:
        """
        Если в модели, для которой сделан view, есть поле регион - 
        то делается запрос к API яндекса и создаются записи или 
        делается привязка к уже существующим записям региона и страны.
        """
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
        form.instance.creator = form.instance.editor = self.request.user
        """
        Если у модели есть поле Шифр (code) - 
        то делается запрос в БД и берется номер из последовательности последний,
        который и присваивается в поле шифр объекта
        """
        if hasattr(form.instance, 'code'):
            form.instance.code = sequence_id()
        self.object = form.save()
        return super().form_valid(form)

    """
    Чтобы название view, которое будет отображаться в темплейте,
    не писать в контекст каждый раз, то берется множественное число
    базовой модели
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Добавление {self.model._meta.verbose_name_plural}'
        return context

    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return f'{self.model._meta.verbose_name} {self.object} успешно создан'

    def get_success_url(self) -> str:
        return self.object.get_absolute_url()

    def get_template_names(self) -> list[str]:
        template_names = super().get_template_names()
        template_names.append('form_template.html')
        return template_names
