from typing import Any
from django.http import HttpResponse
from django.views.generic import FormView
from building.forms import SubmitBuildingForm
from building.models import Building
from file.services import FileHandler, S3FileHandler
from django.urls import reverse_lazy
from core.view_mixins import CreateViewMixin
# Create your views here.


class SubmitBuildingView(CreateViewMixin):
    template_name = 'submit.html'
    model = Building
    form_class = SubmitBuildingForm
    success_url = reverse_lazy('index')
