from django.views.generic import CreateView
from django.urls import reverse_lazy
from file.services import FileHandler
from file.services import S3FileHandler
from django.apps import apps


class CreateViewMixin(CreateView):

    def form_valid(self, form):
        obj = super().form_valid(form)
        if 'foto' in form.cleaned_data and form.cleaned_data['foto']:
            fotos = []
            if len(form.cleaned_data['foto']) == 1:
                fotos.append(form.cleaned_data['foto'])
            elif len(form.cleaned_data['foto']) > 1:
                fotos = form.cleaned_data['foto']
            for foto in fotos:
                processed_foto = FileHandler(foto,
                                             obj,
                                             'фотография')
                foto_instance = processed_foto.to_orm()
                uploader = S3FileHandler(processed_foto)
                uploader.upload_file_to_s3()
                foto_instance.save()
                obj.file_set.add(foto_instance)
        if 'plan' in form.cleaned_data and form.cleaned_data['plan']:
            plan_file = form.cleaned_data['plan']
            plan = FileHandler(plan_file,
                               obj,
                               'план')
            plan_instance = plan.to_orm()
            uploader = S3FileHandler(plan)
            uploader.upload_file_to_s3()
            plan_instance.save()
            obj.file_set.add(plan_instance)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Добавление {self.model._meta.verbose_name_plural}'
        context['method'] = 'POST'
        context['render_kw'] = {'enctype': 'multipart/form-data'}
        app = self.model._meta.app_label
        models = apps.all_models['artwork']
        obj_name = self.model.__name__.lower()
        context['action'] = reverse_lazy(
            f'{app}:submit{"-" + obj_name if obj_name in models else ""}'
            )
        return context
