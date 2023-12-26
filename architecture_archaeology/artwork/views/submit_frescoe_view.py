from django.views.generic import CreateView
from django import forms
from artwork.models import Frescoe


class SubmitFrescoeView(CreateView):
    model = Frescoe
    fields = '__all__'
    template_name = 'frescoe/submit.html'
    success_url = '/'

    # def form_valid(self, form):
    #     return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = 'POST'
        context['title'] = 'Submit frescoe'
        # context['action'] = reverse_lazy('arch_site:submit')
        # context['render_kw'] = {'enctype': 'multipart/form-data'}
        return context
    
    # def get_form(self, form_class=None):
    #     form = super(SubmitFrescoeView, self).get_form(form_class)
    #     form.fields['name'].widget = forms.TextInput(attrs={'class': 'form-control'})
    #     return form