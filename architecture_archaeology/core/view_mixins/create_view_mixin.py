from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from file.services import FileHandler
from file.services import S3FileHandler
from django.apps import apps


class CreateViewMixin(CreateView):

    def form_valid(self, form):
        super().form_valid(form)
        form_fotos = form.cleaned_data.get('foto')
        if form_fotos:
            fotos = []
            if isinstance(form_fotos, list):
                fotos = form_fotos
            else:
                fotos.append(form.cleaned_data['foto'])
            for foto in fotos:
                processed_foto = FileHandler(foto,
                                             self.object,
                                             'фотография')
                foto_instance = processed_foto.to_orm()
                uploader = S3FileHandler(processed_foto)
                uploader.upload_file_to_s3()
                foto_instance.save()
                self.object.file_set.add(foto_instance)
        plan_file = form.cleaned_data.get('plan')
        if plan_file:
            plan = FileHandler(plan_file,
                               self.object,
                               'план')
            plan_instance = plan.to_orm()
            uploader = S3FileHandler(plan)
            uploader.upload_file_to_s3()
            plan_instance.save()
            self.object.file_set.add(plan_instance)
        return HttpResponseRedirect(self.get_success_url())

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
