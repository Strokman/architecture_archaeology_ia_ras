from typing import Any

from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin


class ListViewMixin(LoginRequiredMixin, FilterView):
    paginate_by = 10
    context_object_name = 'objects'
    template_name = 'list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        print('TEST TEST TEST')
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name_plural
        app = self.model._meta.app_label
        model_name = self.model.__name__.lower()
        context['action'] = reverse_lazy(
            f'{app}:submit{"-" + model_name if app in ['artwork', 'measurement'] else ""}'
            )
        context['base_url'] = reverse_lazy(
            f'{app}:list{"-" + model_name if app in ['artwork', 'measurement'] else ""}'
            )
        return context

    def get_queryset(self) -> QuerySet[Any]:
        """
        Метод переопределен, чтобы отфильтровать список объектов
        по шифрам родительских объектов (фрески, артефакты).
        Прежде всего переопределение предназначено для измерений.
        Список получается через query string, queryset Django
        фильтруется по этому списку
        """
        parent_obj_codes = self.request.GET.get('parent')
        if parent_obj_codes:

            # Если в запросе есть ключ parent - преобразовывается
            # в список интов
            parent_obj_codes = (i for i in parent_obj_codes.split(',') if i.isdigit())
            parent_obj_codes = list(map(int, parent_obj_codes))
            # делается запрос на все измерения
            qs = self.model.objects.all()

            # создаем список айдишников измерений,
            # если шифр в списке шифров родительских объектов
            list_of_ids = [
                i.pk for i in qs if i.parent_obj.code in parent_obj_codes
                ]

            # фильтруем объекты по списку айдишников
            qs = qs.filter(pk__in=list_of_ids)
            return qs

        # Если нужная query string не пришла - 
        # вызываем метод дальше по иерархии
        return super().get_queryset()
