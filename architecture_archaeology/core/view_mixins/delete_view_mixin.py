from django.forms import BaseForm
from django.http.response import HttpResponse
from django.views.generic import DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from file.services import S3FileHandler


class DeleteViewMixin(
                    SuccessMessageMixin,
                    UserPassesTestMixin,
                    LoginRequiredMixin,
                    DeleteView
                    ):
    """
    Миксин сделан для кастомизации generic-view Django,
    чтобы он охватывал большую часть моделей, описанных в приложении
    """
    def form_valid(self, form: BaseForm) -> HttpResponse:
        """
        Если модель предусматривает привязку файла - то
        при удаления объекта из базы данных также удаляется
        файл из S3 Яндекса
        """
        if self.object.file_set:
            for file in self.object.file_set.all():
                s3file = S3FileHandler(file)
                s3file.delete_file_from_s3()
        if self.object.foto_set.all():
            for file in self.object.foto_set.all():
                s3file = S3FileHandler(file)
                s3file.delete_file_from_s3()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data: dict[str, str]) -> str:
        return f'{self.model._meta.verbose_name} {self.object} успешно удален'

    def get_success_url(self) -> str:
        app = self.model._meta.app_label
        model_name = self.model.__name__.lower()
        url = reverse_lazy(
            f'{app}:list{"-" + model_name if app in ['artwork', 'measurement'] else ""}'
            )
        return url

    def test_func(self) -> bool | None:
        """
        Если пользователь является админом (superuser),
        то он может удалять запись. Если нет - то нет. Пока по ТЗ так было
        """
        obj = self.model.objects.get(slug=self.request.resolver_match.kwargs['slug'])
        if obj.creator != self.request.user and not self.request.user.is_superuser:
            return False
        return True
